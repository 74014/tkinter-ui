from tkinter import *
import re

class AutocompleteEntry(Entry):
    def __init__(self, autocompleteList, *args, **kwargs):
        # Listbox length
        if 'listboxLength' in kwargs:
            self.listboxLength = kwargs['listboxLength']
            del kwargs['listboxLength']
        else:
            self.listboxLength = 8

        # Custom matches function
        if 'matchesFunction' in kwargs:
            self.matchesFunction = kwargs['matchesFunction']
            del kwargs['matchesFunction']
        else:
            def matches(fieldValue, acListEntry):
                pattern = re.compile('.*' + re.escape(fieldValue) + '.*', re.IGNORECASE)
                return re.match(pattern, acListEntry)

            self.matchesFunction = matches

        Entry.__init__(self, *args, **kwargs)
        self.focus()      

        self.autocompleteList = autocompleteList

        self.var = self["textvariable"]
        if self.var == '':
            self.var = self["textvariable"] = StringVar()

        self.var.trace('w', self.changed)
        self.bind("<Right>", self.selection)
        self.bind("<Up>", self.moveUp)
        self.bind("<Down>", self.moveDown)

        self.listboxUp = False
        
    def changed(self, name, index, mode):
        if self.var.get() == '':
            if self.listboxUp:
                self.listbox.destroy()
                self.listboxUp = False
        else:
            words = self.comparison()
            if words:
                if not self.listboxUp:
                    self.listbox = Listbox(width=self["width"], height=self.listboxLength)
                    self.listbox.bind("<ButtonRelease-1>", self.selection)
                    self.listbox.bind("<Right>", self.selection)
                    #self.listbox.bind("<Return>", self.selection)
                    self.listbox.place(x=self.winfo_x(), y=self.winfo_y() + self.winfo_height())
                    self.listboxUp = True

                self.listbox.delete(0, END)
                for w in words:
                    self.listbox.insert(END, w)
                    self.listbox.select_set(0)
            else:
                if self.listboxUp:
                    self.listbox.destroy()
                    self.listboxUp = False
                    
    def selection(self, event):
        if self.listboxUp:
            self.var.set(self.listbox.get(self.listbox.curselection()[0]))
            self.listbox.destroy()
            self.listboxUp = False
            self.icursor(END)
            
    def moveUp(self, event):
        if self.listboxUp:
            if self.listbox.curselection() == []:
                self.listbox.select_set(0)
                return
                
            else:
                index = int(self.listbox.curselection()[0])

            if index != 0:
                self.listbox.selection_clear(first=str(index))
                index = int(index) - 1

                self.listbox.see(str(index))  # Scroll!
                self.listbox.selection_set(first=str(index))
                self.listbox.activate(str(index))     
                
    def moveDown(self, event):
        if self.listboxUp:
            if self.listbox.curselection() == []:
                self.listbox.select_set(0)
                return
            
            else:
                index = int(self.listbox.curselection()[0])

            if index != (int(self.listbox.index("end"))-1):
                self.listbox.selection_clear(first=str(index))
                index = int(index) + 1

                self.listbox.see(str(index))  # Scroll!
                self.listbox.selection_set(first=str(index))
                self.listbox.activate(str(index))
                
    def comparison(self):
        return [w for w in self.autocompleteList if self.matchesFunction(self.var.get(), w)]
