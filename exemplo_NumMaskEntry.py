import locale

root = tk.Tk()

a = tk.StringVar()
b = tk.Entry(root, textvariable = a, justify = tk.RIGHT)
b.pack()

def secod(*events):
    numero = a.get()
    if numero == "": return
    numero_formatado = numero.replace(".",'')
    numero_formatado = int(numero_formatado)
    try:
        numero_formatado = format(numero_formatado,",")
    except:
        print("b")
        
    numero_formatado = numero_formatado.replace(',', '.')
    # Overwrite the Entrybox content using the widget's own methods
    b.delete(0, tk.END)
    b.insert(0, numero_formatado)

a.trace('w',secod)
root.mainloop()
