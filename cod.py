import re
from tkinter import *
from PIL import ImageTk, Image 
from autocompl import AutocompleteEntry


lista_paises = ["Argentina","Brasil","Canada","Dubai","Espanha","França","Grecia"]

usuario = ""

    
#################
#Definição da UI

#Janela
root = Tk()
root.title('CoRi Tool v0.1')
root.geometry("350x600")
root.resizable(0, 0)

#Grid
root.columnconfigure(0, weight=1) #Coluna vazia

#################
#Funções 
def Att_Comites():
    print("att")
    
def Att_Comites():
    print("att")
    
def Att_Comites():
    print("att")
    
def Att_Comites():
    print("att")
    
def Att_Comites():
    print("att")


##################
#Controles Tool

#Icone da janela
ico = PhotoImage(file = 'resources/globo_ico_raw.png')
root.iconphoto(False, ico)

#Imagem 
logo = ImageTk.PhotoImage(Image.open('resources/globo_ico_raw.png'))
#The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = Label(root, image = logo)
#The Pack geometry manager packs widgets in rows or columns.
#panel.pack(side = "bottom", fill = "both", expand = "yes")
panel.grid(row=0, column=0)

#Label Usuário
label_usuario_txt = "Usuário: " + usuario
label_usuario = Label(root,text=label_usuario_txt,font=('Helvetica bold', 14),fg="black")
label_usuario.grid(row=1, column=0, sticky="NW")

#Botão Atualizar Comite
button_att_comite = Button(root, text ="Atualizar Comitês", command = Att_Comites)
button_att_comite.grid(row=2, column=0, sticky="NEW")

#Botão Atualizar Comite
button_cad_flex = Button(root, text ="Cadastrar Flexibilização", command = Att_Comites)
button_cad_flex.grid(row=4, column=0, sticky="NEW")

#Botão Atualizar Comite
button_cad_rem = Button(root, text ="Cadastrar Remanejamento", command = Att_Comites)
button_cad_rem.grid(row=3, column=0, sticky="NEW")

#Botão Atualizar Comite
button_cad_comite = Button(root, text ="Cadastrar Resultado Comitê", command = Att_Comites)
button_cad_comite.grid(row=5, column=0, sticky="NEW")

#Botão Atualizar Comite
button_apre_comite = Button(root, text ="Montar Apresentação Comitê", command = Att_Comites)
button_apre_comite.grid(row=6, column=0, sticky="NEW")

root.mainloop()
