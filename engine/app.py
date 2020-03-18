import os
from tkinter import *
from tkinter import ttk, messagebox
from functools import partial

from engine.database.database import DB
from engine.carnets.popups import NewCarnet, SearchPopup, EditCarnet

BASE_DIR = os.getcwd()
DBFILE = BASE_DIR + "/engine/database/sciankadatabase.db"

class App:

    def __init__(self):
        self.database = DB(DBFILE)
        #init TKfrom functools import partialfrom functools import partial
        self.root = Tk()
        #self.root.iconbitmap("/img/logo.ico")
        self.root.geometry("1100x300")
        self.root.resizable(False, False)
        self.root.title("Karnety")
        
        self.bottom_frame = Frame(self.root)
        self.bottom_frame.pack(side=BOTTOM)

        #set Tree
        self.set_tree()
        self.fill_tree()

        self.tree.bind("<Button-3>", self.preClick)
        self.tree.bind("<Button-1>", self.onLeft)
    
        #add buttons
        self.add_buttons()
        

    def set_tree(self):
        
        self.tree = ttk.Treeview(self.root)
        
        #treeScroll = ttk.Scrollbar(self.tree, orient="vertical", command=self.tree.yview)
        
        #self.tree.configure(yscrollcommand=treeScroll.set)

        self.tree["columns"] = ("first_name", "last_name", "date_created", "date_valid", "carnet_id")
        self.tree["show"] = "headings"

        self.tree.heading("first_name", text="Imie")
        self.tree.heading("last_name", text="Nazwisko")
        self.tree.heading("date_created", text="Data wystawienia")
        self.tree.heading("date_valid", text="Data ważności")
        self.tree.heading("carnet_id", text="ID karnetu")

        self.tree.pack(side=TOP,fill=X)
        #treeScroll.pack(side="right", fill=Y)
        
    def fill_tree(self):
       
       data = self.database.get_all_carnets()
       for d in data:
           self.tree.insert("", "end", values=(d[1],d[2],d[3],d[4],d[5]))

    def onRight(self):
        cursorx = int(self.root.winfo_pointerx() - self.root.winfo_rootx())
        cursory = int(self.root.winfo_pointery() - self.root.winfo_rooty())

        #menu
        self.small_menu = Canvas(self.root, width=150, height=65, highlightbackground="gray", highlightthickness=1)
        self.small_menu.place(x=cursorx, y=cursory)
        self.small_menu.pack_propagate(0)

        #labels
        updateLabel = Label(self.small_menu, text="Edytuj", cursor="hand2", anchor="w")
        updateLabel.pack(side="top", padx=1, pady=1, fill="x")

        printLabel = Label(self.small_menu, text="Drukuj", cursor="hand2", anchor="w")
        printLabel.pack(padx=1, pady=1, fill="x")

        delLabel = Label(self.small_menu, text="Usuń", cursor="hand2", anchor="w")
        delLabel.pack(side="bottom", padx=1, pady=1, fill="x")

        updateLabel.bind("<Button-1>", self.update_carnet)
        delLabel.bind("<Button-1>", self.delete_carnet)
        printLabel.bind("<Button-1>",self.print_carnet)

    def destroy_small_menu(self):
        self.small_menu.place_forget()

    def update_carnet(self, *args):
        self.destroy_small_menu()
        selection = self.tree.selection()
        data = self.tree.item(selection)["values"]
        e = EditCarnet(self.tree, self.database, "update",id=data[4])

    def delete_carnet(self, *args):
        self.destroy_small_menu()
        if messagebox.askyesnocancel("","Czy na pewno chcesz usunąć?"):
            selection = self.tree.selection()
            data = self.tree.item(selection)["values"]
            self.database.delete_carnet(data[4])
            self.tree.delete(selection)

            messagebox.showinfo("", "Usunięto")
        
    def print_carnet(self, *args):
        self.destroy_small_menu()
        selection = self.tree.selection()
        id = str(selection[0]).strip("I00")
        #
        #   print function
        #
        
    def preClick(self, *args):
        try:
            self.small_menu.place_forget()
            self.onRight()
        except Exception:
            self.onRight()

    def onLeft(self, *args):
        try:
            self.small_menu.place_forget()
        except Exception:
            pass

    def add_buttons(self):
        
        add_carnet = Button(self.bottom_frame, text="Dodaj Karnet", command=self.add_carnet)
        add_carnet.pack(side=LEFT, padx=20, pady=30)

        search_carnet = Button(self.bottom_frame, text="Szukaj", command=self.search)
        search_carnet.pack(side=RIGHT, padx=20, pady=30)
        
    def add_carnet(self):
        carnet_popup = NewCarnet(self.database, self.tree)
    
    def search(self):
        search_popup = SearchPopup(self.tree, self.database)

    def run(self):
        #run TK
        self.root.mainloop()


