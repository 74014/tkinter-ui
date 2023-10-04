import tkinter as tk
from tkinter import ttk

class TreeviewEdit(ttk.Treeview):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        
        self.bind("<Double-1>", self.on_double_click)
        
    def on_double_click(self,event):
        region_clicked = self.identify_region(event.x,event.y)
        #print(region_clicked)
        
        if region_clicked not in ("tree","cell"):
            return
        
        column = self.identify_column(event.x)
        column_index = int(column[1:]) - 1
        
        selected_id = self.focus()
        selected_values = self.item(selected_id)
        
        if column == "#0":
            selected_text = selected_values.get("text")
        else:
            selected_text = selected_values.get("values")[column_index]
            
        column_box = self.bbox(selected_id, column)
        
        entry_edit = ttk.Entry(root)
        entry_edit.editing_column_index = column_index
        entry_edit.editing_item_id = selected_id
        entry_edit.insert(0, selected_text)
        entry_edit.select_range(0, tk.END)
        
        entry_edit.focus()
        
        entry_edit.bind("<FocusOut>",self.on_focus_out)
        entry_edit.bind("<Return>",self.on_return)
        
        entry_edit.place(x=column_box[0],y=column_box[1],w=column_box[2],h=column_box[3])
        
    def on_focus_out(self, event):
        event.widget.destroy()
        
    def on_return(self, event):
        new_text = event.widget.get()
        
        selected_id = event.widget.editing_item_id
        column_index = event.widget.editing_column_index
        
        if column_index == -1:
            self.item(selected_id, text=new_text)
        else:
            current_values = self.item(selected_id).get("values")
            current_values[column_index] = new_text
            self.item(selected_id, values=current_values)
            
        event.widget.destroy()
            
    

if __name__ == "__main__":
    root = tk.Tk()
    
    column_names = ("nome","ano","cor")
    
    treeview = TreeviewEdit(root, columns = column_names)
    
    treeview.heading("#0", text="Tipo")
    treeview.heading("nome", text="Nome")
    treeview.heading("ano", text="Ano")
    treeview.heading("cor", text="Cor")
    
    treeview.insert(parent="",index=tk.END,values=("Civic","1999","Prata",))
    treeview.insert("",index=tk.END,values=("Civic","1999","Prata"))
    treeview.insert("",index=tk.END,values=("Civic","1999","Prata"))
    
    treeview.pack(fill=tk.BOTH, expand=True)
    
    root.mainloop()
