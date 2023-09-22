#Aprimorando, usando PACK :(

import tkinter as tk
from tkinter import ttk

class Janela:
    def __init__(self, root):
        self.root = root
        self.root.title("Cadastro de Clientes")

        #Frame
        self.frame_tabela = tk.Frame(self.root)
        
        
        # Configuração do Treeview
        self.tree = ttk.Treeview(self.frame_tabela, columns=[f'col{i}' for i in range(15)])
        self.tree.heading("#0", text="ID")
        self.tree.column("#0", width=50)
        for i in range(15):
            self.tree.heading(f'col{i}', text=f"Coluna {i+1}")
            self.tree.column(f'col{i}', width=100, stretch=False)  # Impede o estiramento das colunas

        # Configuração da Scrollbar horizontal
        self.horizontal_scrollbar = ttk.Scrollbar(self.frame_tabela, orient="horizontal", command=self.tree.xview)
        self.tree.configure(xscrollcommand=self.horizontal_scrollbar.set)

        # Entradas
        self.entry1 = tk.Entry(self.root, width=50)
        self.entry2 = tk.Entry(self.root, width=50)

        # Botão de Adicionar Cliente
        self.add_button = tk.Button(self.root, text="Adicionar Cliente", command=self.adicionar_cliente)

        # Posicionamento dos widgets
        self.entry1.pack()
        self.entry2.pack()
        self.add_button.pack()
        
        self.frame_tabela.pack()
        
        self.tree.pack()
        self.horizontal_scrollbar.pack(side='top',fill="x")

    def adicionar_cliente(self):
        # Simplesmente adiciona uma nova linha com dados fictícios ao Treeview
        data = [f"Dado{i+1}" for i in range(15)]
        self.tree.insert("", "end", text="Cliente Novo", values=data)

if __name__ == "__main__":
    root = tk.Tk()
    app = Janela(root)
    root.mainloop()
