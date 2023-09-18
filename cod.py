##############
import re
import tkinter as tk
from PIL import ImageTk, Image 
from autocompl import AutocompleteEntry
import threading

import xlwings as xw
import pandas as pd
import pythoncom #Permitir que o pacote xlwings funcione com threading
############

#############
lista_paises = ["Argentina","Brasil","Canada","Dubai","Espanha","França","Grecia"]
lista_gestor = ["Corpbanca","Corporate"]
lista_unid = ["Argentina","Brasil"]
lista_prod = ["Risco Direto","Offshore","Via Garantias"]

usuario = "JUNIMIL"

def LerBase():
    print('Lendo Base')
    pythoncom.CoInitialize()
    excel_app = xw.App(visible=False)
    caminho = 'base.xlsx'
    
    base_rp = excel_app.books.open(caminho)
    
    df = base_rp.sheets[0].used_range.value
    df = pd.DataFrame(df)
    
    base_rp.close()
    excel_app.quit()

    return df
    
def Att_Func():
    print('Começando Att_Func')
    df = LerBase()
    display(df)
    print('Att_Func conseguiu finalizar!')
    display(df)
    return
    
###################

###################
#Dados do Programa
autocompleteList = lista_paises #Lista de todos os campeões da season

#Função do Autocomplete
def pais_matches(fieldValue, acListEntry):
    pattern = re.compile(re.escape(fieldValue) + '.*', re.IGNORECASE)
    return re.match(pattern, acListEntry)

#Função para adicionar o campeao ao meu time pelo Entry
def Add_Champ_Time(event):
    if entry.get() in list(dict_champs.keys()): #Se é um nome de campeão válido
        if entry.get() not in lista_meu_time: #Se ainda não estiver no meu time
            lista_meu_time.append(entry.get()) #Adiciono
            box_lista_atual.insert(END, entry.get()) #Atualizo a textbox do time
            
    Call_Sugestao()
    Get_MeusTraits()
    box_lista_sugestao_sinergia.delete(0,END)
            
#Função para adicionar o campeao ao meu time pela Box de Sugestões
def Add_Champ_Time_Box():
    print(box_lista_sugestao.curselection())
    print(len(box_lista_sugestao.curselection()))
    if len(box_lista_sugestao.curselection()) == 1:
        champ = box_lista_sugestao.get(box_lista_sugestao.curselection())
        lista_meu_time.append(champ)
        box_lista_atual.insert(END, champ)
    Call_Sugestao()
    Get_MeusTraits()
    box_lista_sugestao_sinergia.delete(0,END)
        
#Função para remover um campeao selecionado da lista clicando no botão
def Del_Champ_Time():
    del_champ = box_lista_atual.get(box_lista_atual.curselection())
    if del_champ in lista_meu_time:
        lista_meu_time.remove(del_champ)
        box_lista_atual.delete(ACTIVE)
    if(len(lista_meu_time)) > 0:
        Call_Sugestao()
        Get_MeusTraits()
    else:
        box_lista_sugestao.delete(0,END)
    box_lista_sugestao_sinergia.delete(0,END)
    Get_MeusTraits()
    
#Função para remover um campeao selecionado da lista pressionando DEL
def Del_Champ_Time_bind(event):
    del_champ = box_lista_atual.get(box_lista_atual.curselection())
    if del_champ in lista_meu_time:
        lista_meu_time.remove(del_champ)
        box_lista_atual.delete(ACTIVE)
    if(len(lista_meu_time)) > 0:
        Call_Sugestao()
        Get_MeusTraits()
    else:
        box_lista_sugestao.delete(0,END)
    box_lista_sugestao_sinergia.delete(0,END)
    Get_MeusTraits()
    
#Função para chamar as funções que calculam os melhores champs, dada meu time atual
def Get_MeusTraits():
    box_lista_atual_sinergia.delete(0,END)
    if (len(lista_meu_time) == 0):
        return
    nomes_ordenado,qntd_ordenado,tiers_ordenado = GetTeamTraits(lista_meu_time)
    print(nomes_ordenado)
    print(tiers_ordenado)
    print('')
    for i in range(len(nomes_ordenado)):
        print(nomes_ordenado[i])
        box_lista_atual_sinergia.insert(END, str(tiers_ordenado[i] + ' - ' + nomes_ordenado[i]))
    
#Função para chamar as funções que calculam os melhores champs, dada meu time atual
def Call_Sugestao():
    #Chamo as funções
    #Atualizo os controles
    box_lista_sugestao.delete(0,END)
    lista_sugestoes = AutoCompleteTeam(lista_meu_time)
    print(lista_sugestoes)
    for champ in lista_sugestoes:
        print(champ)
        box_lista_sugestao.insert(END, champ)
    
#Função para exibir a sinergia do champ selecionado
def Sugestao_Traits(event):
    box_lista_sugestao_sinergia.delete(0,END)
    lista_teste_sin = lista_meu_time.copy()
    lista_teste_sin.append(box_lista_sugestao.get(ACTIVE))
    nomes_ordenado,qntd_ordenado,tiers_ordenado = GetTeamTraits(lista_teste_sin)
    print(nomes_ordenado)
    print(tiers_ordenado)
    print('')
    for i in range(len(nomes_ordenado)):
        print(nomes_ordenado[i])
        box_lista_sugestao_sinergia.insert(END, str(tiers_ordenado[i] + ' - ' + nomes_ordenado[i]))
    
    
#################
#Definição da UI

#Janela
root = tk.Tk()
root.title('CoRi Tool v0.1')
root.geometry("350x600")
root.resizable(0, 0)

#Grid
root.columnconfigure(0, weight=1) #Coluna vazia
#root.columnconfigure(1, weight=3) #Coluna dos controles de Campeoes
#root.columnconfigure(2, weight=3) #Coluna dos controles de Traits
#root.columnconfigure(3, weight=1) #Coluna vazia

#BindKeys
#root.bind('<Return>', Add_Champ_Time)
#root.bind('<Delete>', Del_Champ_Time_bind)


#Controles
#entry = AutocompleteEntry(autocompleteList,root,listboxLength=6, width=32, matchesFunction=matches)
#entry.grid(row=1, column=1)
#entry.pack()

#label_time_atual = Label(root,text="Meu Time:",font=('Helvetica bold', 20),fg="black")
#label_time_atual.grid(row=2, column=1)
#label_time_atual.pack()

#box_lista_atual = Listbox(root, height=10,width=40)
#box_lista_atual.grid(row=3, column=1)

#box_lista_atual_sinergia = Listbox(root, height=10,width=40)
#box_lista_atual_sinergia.grid(row=3, column=2)

#button_del = Button(root, text ="Deletar", command = Del_Champ_Time)
#button_del.grid(row=4, column=1)

#label_sugestao = Label(root,text="Sugestões:",font=('Helvetica bold', 20),fg="black")
#label_sugestao.grid(row=5, column=1)

#box_lista_sugestao = Listbox(root, height=10,width=40)
#box_lista_sugestao.grid(row=6, column=1)

#box_lista_sugestao_sinergia = Listbox(root, height=10,width=40)
#box_lista_sugestao_sinergia.grid(row=6, column=2)

#button_add = Button(root, text ="Adicionar", command = Add_Champ_Time_Box)
#button_add.grid(row=7, column=1)

#BindEvents
#box_lista_sugestao.bind("<<ListboxSelect>>", Sugestao_Traits)

##################
#Controles Tool

#Icone da janela
#ico = tk.PhotoImage(file = 'resources/globo_ico_raw.png')
#root.iconphoto(False, ico)

#Imagem 
#logo = tk.PhotoImage(Image.open('resources/globo_ico_raw.png'))
#The Label widget is a standard Tkinter widget used to display a text or image on the screen.
#panel = tk.Label(root, image = logo)
#The Pack geometry manager packs widgets in rows or columns.
#panel.pack(side = "bottom", fill = "both", expand = "yes")
#panel.grid(row=0, column=0)

#Label Usuário
label_usuario_txt = "Usuário: " + usuario
label_usuario = tk.Label(root,text=label_usuario_txt,font=('Helvetica bold', 14),fg="black")
label_usuario.grid(row=1, column=0, sticky="NW")

#Botão Atualizar Comite
def butt_att():
    t1=threading.Thread(target=Att_Func)
    t1.start()

button_att_comite = tk.Button(root, text ="Atualizar Comitês", command = butt_att)
button_att_comite.grid(row=2, column=0, sticky="NEW")

#Botão Cadastrar Flex
def Cad_Flex():
    print('Abrindo nova janela')
    JanelaCadastro_Flex()

button_cad_flex = tk.Button(root, text ="Cadastrar Flexibilização", command =  Cad_Flex)
button_cad_flex.grid(row=4, column=0, sticky="NEW")

#Botão Cadastrar Rem
def Cad_Rem():
    print('Abrindo nova janela')
    JanelaCadastro_Rem()

button_cad_flex = tk.Button(root, text ="Cadastrar Remanejamento", command =  Cad_Rem)
button_cad_flex.grid(row=4, column=0, sticky="NEW")


#Funções para Funcionamento das telas de cadastro:
def Cadastro_BindEnter():
    print()
    
    
def JanelaCadastro_Flex():
    janela_cadastro_flex = tk.Toplevel(root)
    janela_cadastro_flex.title("Nova Flexibilização de Limite")
    janela_cadastro_flex.geometry("350x600")
    janela_cadastro_flex.resizable(0, 0)
    
    janela_cadastro_flex.bind('<Return>', Cadastro_BindEnter)
    
    #Campos necessários
    #Pais_1
    #Gestor_1
    #Produto_1
    #Unidade_1
    #Limite_Liq_1
    
    label_pais = tk.Label(janela_cadastro_flex, text="País:")
    label_pais.pack()
    entry_pais = tk.Entry(janela_cadastro_flex)
    entry_pais.pack()
    
def JanelaCadastro_Rem():
    janela_cadastro_rem = tk.Toplevel(root)
    janela_cadastro_rem.title("Novo Remanejamento de Limites")
    janela_cadastro_rem.geometry("350x600")
    janela_cadastro_rem.resizable(0, 0)
    
    #janela_cadastro_rem.bind('<Return>', Cadastro_BindEnter)
    
    #Campos necessários
    #Pais_1
    #Gestor_1
    #Produto_1
    #Unidade_1
    
    #Pais_2
    #Gestor_2
    #Produto_2
    #Unidade_2
    
    #Total a ser transferido:
    #Limite_Liq
    #Limite_1Y
    #(...)
    #Limite_>30
    
    label_1 = tk.Label(janela_cadastro_rem, text="Limite Origem:")
    label_1.grid(row=0, column=0, padx=10, pady=5, sticky="w")
    
    label_pais_1 = tk.Label(janela_cadastro_rem, text="País:")
    label_pais_1.grid(row=1, column=0, padx=10, pady=5, sticky="w")
    #entry_pais_1 = tk.Entry(janela_cadastro_rem)
    entry_pais_1 = AutocompleteEntry(janela_cadastro_rem,lista_paises,janela_cadastro_rem,listboxLength=5, width=18, font=('Helvetica bold',12), matchesFunction=pais_matches)
    entry_pais_1.grid(row=1, column=1, columnspan=2, padx=10, pady=5)
    
    label_gestor_1 = tk.Label(janela_cadastro_rem, text="Gestor:")
    label_gestor_1.grid(row=2, column=0, padx=10, pady=5, sticky="w")
    #entry_gestor_1 = tk.Entry(janela_cadastro_rem)
    entry_gestor_1 = AutocompleteEntry(janela_cadastro_rem,lista_gestor,janela_cadastro_rem,listboxLength=5, width=18, font=('Helvetica bold',12), matchesFunction=pais_matches)
    entry_gestor_1.grid(row=2, column=1, columnspan=2, padx=10, pady=5)
    
    label_unid_1 = tk.Label(janela_cadastro_rem, text="Unidade:")
    label_unid_1.grid(row=3, column=0, padx=10, pady=5, sticky="w")
    entry_unid_1 = tk.Entry(janela_cadastro_rem)
    entry_unid_1.grid(row=3, column=1, columnspan=2, padx=10, pady=5)
    
    label_prod_1 = tk.Label(janela_cadastro_rem, text="Produto:")
    label_prod_1.grid(row=4, column=0, padx=10, pady=5, sticky="w")
    entry_prod_1 = tk.Entry(janela_cadastro_rem)
    entry_prod_1.grid(row=4, column=1, columnspan=2, padx=10, pady=5)
    
    label_2 = tk.Label(janela_cadastro_rem, text="Limite Destino:")
    label_2.grid(row=5, column=0, padx=10, pady=5, sticky="w")
    
    label_pais_2 = tk.Label(janela_cadastro_rem, text="País:")
    label_pais_2.grid(row=6, column=0, padx=10, pady=5, sticky="w")
    entry_pais_2 = tk.Entry(janela_cadastro_rem)
    entry_pais_2.grid(row=6, column=1, columnspan=2, padx=10, pady=5)
    
    label_gestor_2 = tk.Label(janela_cadastro_rem, text="Gestor:")
    label_gestor_2.grid(row=7, column=0, padx=10, pady=5, sticky="w")
    entry_gestor_2 = tk.Entry(janela_cadastro_rem)
    entry_gestor_2.grid(row=7, column=1, columnspan=2, padx=10, pady=5)
    
    label_unid_2 = tk.Label(janela_cadastro_rem, text="Unidade:")
    label_unid_2.grid(row=8, column=0, padx=10, pady=5, sticky="w")
    entry_unid_2 = tk.Entry(janela_cadastro_rem)
    entry_unid_2.grid(row=8, column=1, columnspan=2, padx=10, pady=5)
    
    label_prod_2 = tk.Label(janela_cadastro_rem, text="Produto:")
    label_prod_2.grid(row=9, column=0, padx=10, pady=5, sticky="w")
    entry_prod_2 = tk.Entry(janela_cadastro_rem)
    entry_prod_2.grid(row=9, column=1, columnspan=2, padx=10, pady=5)
    
    botao_enviar_segunda_janela = tk.Button(janela_cadastro_rem, text="Cancelar", command=lambda: Cancelar_Rem(janela_cadastro_rem))
    botao_enviar_segunda_janela.grid(row=10, column=0, pady=10)
    botao_enviar_segunda_janela = tk.Button(janela_cadastro_rem, text="Avançar", command=Avancar_Rem)
    botao_enviar_segunda_janela.grid(row=10, column=2, pady=10)
    
def Avancar_Rem():
    print('Avançar Rem')
    
def Cancelar_Rem(janela):
    print('Cancelar Rem')
    janela.destroy()
    

#Botão Atualizar Comite
#button_cad_rem = Button(root, text ="Cadastrar Remanejamento", command = Att_Comites)
#button_cad_rem.grid(row=3, column=0, sticky="NEW")

#Botão Atualizar Comite
#button_cad_comite = Button(root, text ="Cadastrar Resultado Comitê", command = Att_Comites)
#button_cad_comite.grid(row=5, column=0, sticky="NEW")

#Botão Atualizar Comite
#button_apre_comite = Button(root, text ="Montar Apresentação Comitê", command = Att_Comites)
#button_apre_comite.grid(row=6, column=0, sticky="NEW")

root.mainloop()

################
