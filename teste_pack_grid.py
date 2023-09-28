import tkinter as tk

# Funções para botões dos frames 1 e 2
def botao1_clicado():
    label1.config(text="Botão 1 Clicado!")

def botao2_clicado():
    label1.config(text="Botão 2 Clicado!")

# Função para botão do frame 3
def botao3_clicado():
    texto = ""
    for entry in entries:
        texto += entry.get() + "\n"
    label3.config(text=texto)

# Cria uma instância da janela principal
janela = tk.Tk()
janela.title("Janela com Frames")

#label posicionado com pack() antes dos frames
label1 = tk.Label(janela, text="Passo 1: Tentativa de posicionar com Pack")
label1.pack()

# Cria o primeiro frame com 2 botões usando grid
frame1 = tk.Frame(janela)
frame1.pack()

botao_frame1_1 = tk.Button(frame1, text="Botão 1", command=botao1_clicado)
botao_frame1_1.grid(row=0, column=0, padx=5, pady=5)

botao_frame1_2 = tk.Button(frame1, text="Botão 2", command=botao2_clicado)
botao_frame1_2.grid(row=1, column=0, padx=5, pady=5)

label1 = tk.Label(frame1, text="")
label1.grid(row=2, column=0)

# Cria o segundo frame com 2 botões usando pack
frame2 = tk.Frame(janela)
frame2.pack()

botao_frame2_1 = tk.Button(frame2, text="Botão 3", command=botao1_clicado)
botao_frame2_1.pack(padx=5, pady=5)

botao_frame2_2 = tk.Button(frame2, text="Botão 4", command=botao2_clicado)
botao_frame2_2.pack(padx=5, pady=5)

label2 = tk.Label(frame2, text="")
label2.pack()

# Cria o terceiro frame com 5 campos de entrada usando grid
frame3 = tk.Frame(janela)
frame3.pack()

entries = []
for i in range(5):
    label_entry = tk.Label(frame3, text=f"Campo {i+1}:")
    label_entry.grid(row=i, column=0, padx=5, pady=5)

    entry = tk.Entry(frame3)
    entry.grid(row=i, column=1, padx=5, pady=5)
    entries.append(entry)

botao_frame3 = tk.Button(frame3, text="Mostrar Texto", command=botao3_clicado)
botao_frame3.grid(row=5, column=0, columnspan=2, padx=5, pady=10)

label3 = tk.Label(frame3, text="")
label3.grid(row=6, column=0, columnspan=2)

# Inicia o loop principal da janela
janela.mainloop()
