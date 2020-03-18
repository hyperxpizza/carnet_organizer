from tkinter import *
from tkinter import messagebox

from .generator import generate_qr

import random
from datetime import datetime
import uuid

class NewCarnet(Toplevel):

    def __init__(self, database, master):
        self.tree = master
        Toplevel.__init__(self)
        
        self.topframe = Frame(self)
        self.title("Dodaj Karnet")
        self.geometry("350x250")
        self.resizable(False, False)
        self.topframe.pack()
        self.set_widgets()

        self.database = database

    def set_widgets(self):
        self.first_name_var = StringVar()
        self.last_name_var = StringVar()
        self.date_created_var = StringVar()
        self.date_created_var.set(datetime.date(datetime.now()))
        self.date_valid_var = StringVar()

        first_name = Label(self.topframe, text="Imie:").grid(row=0, column=0, pady=10, padx=10)
        last_name = Label(self.topframe, text="Nazwisko:").grid(row=1, column=0, pady=10, padx=10)
        date_created = Label(self.topframe, text="Data wystawienia:").grid(row=2, column=0, pady=10, padx=10)
        date_valid = Label(self.topframe, text="Data ważności:").grid(row=3, column=0, pady=10, padx=10)

        self.e_first_name = Entry(self.topframe, textvariable=self.first_name_var)
        self.e_first_name.grid(row=0, column=1, padx=10)

        self.e_last_name = Entry(self.topframe, textvariable=self.last_name_var)
        self.e_last_name.grid(row=1, column=1, padx=10)

        self.e_date_created = Entry(self.topframe, textvariable=self.date_created_var)
        self.e_date_created.grid(row=2, column=1, padx=10)

        self.e_date_valid = Entry(self.topframe, textvariable=self.date_valid_var)
        self.e_date_valid.grid(row=3, column=1, padx=10)

        add_button = Button(self.topframe, text="Dodaj", command=self.add_to_db)
        add_button.grid(column=1, pady=20)

        

    def check_if_valid(self):
        
        if len(self.first_name_var.get()) == 0:
            self.e_first_name.config(highlightbackground="red")

            return False

        if len(self.last_name_var.get()) == 0:
            self.e_last_name.config(highlightbackground="red")

            return False

        if len(self.date_created_var.get()) == 0:
            self.e_last_name.config(highlightbackground="red")

            return False

        if len(self.date_valid_var.get()) == 0:
            self.e_last_name.config(highlightbackground="red")

            return False

        return True

    def add_to_db(self):
        res = self.check_if_valid()

        if res == True:
            carnet_id = random.randrange(1000000,100000000)
            print(carnet_id)

            res2 = self.database.add_carnet(self.first_name_var.get(), self.last_name_var.get(), self.date_created_var.get(), self.date_valid_var.get(), carnet_id)

            if res2 == True:
                generate_qr(carnet_id)
                self.tree.insert("", "end",values=(self.first_name_var.get(), self.last_name_var.get(), self.date_created_var.get(), self.date_valid_var.get(), carnet_id))
                messagebox.showinfo("", "Dodano Karnet")
                self.destroy()
            else:
                messagebox.showerror("", "Błąd przy dodawaniu")


class EditCarnet(Toplevel):

    def __init__(self, master, database, mission, first_name=None, last_name=None, date_created=None, date_valid=None, id=None):
        self.tree = master
        Toplevel.__init__(self)
        self.database = database
        self.topframe = Frame(self)
        self.title("Karnet")
        self.geometry("350x250")
        self.resizable(False, False)
        self.topframe.pack()

        self.first_name_var = StringVar()
        self.last_name_var = StringVar()
        self.date_created_var = StringVar()
        self.date_valid_var = StringVar()

        self.mission = mission
        if first_name != None:
            self.first_name_var.set(first_name)

        if last_name != None:
            self.last_name_var.set(last_name)

        if date_created != None:
            self.date_created_var.set(date_created)

        if date_valid != None:
            self.date_valid_var.set(date_valid)

        if id != None:
            self.get_carnet(id)

        self.set_widgets()

    def get_carnet(self, id):
        carnet = self.database.get_by_carnet_id(id)
        print(carnet)

        self.first_name_var.set(carnet[0])
        self.last_name_var.set(carnet[1])
        self.date_created_var.set(carnet[2])
        self.date_valid_var.set(carnet[3])
        self.carnet_id = id

    def set_widgets(self):
        
        first_name = Label(self.topframe, text="Imie:").grid(row=0, column=0, pady=10, padx=10)
        last_name = Label(self.topframe, text="Nazwisko:").grid(row=1, column=0, pady=10, padx=10)
        date_created = Label(self.topframe, text="Data wystawienia:").grid(row=2, column=0, pady=10, padx=10)
        date_valid = Label(self.topframe, text="Data ważności:").grid(row=3, column=0, pady=10, padx=10)

        self.e_first_name = Entry(self.topframe, textvariable=self.first_name_var)
        self.e_first_name.grid(row=0, column=1, padx=10)

        self.e_last_name = Entry(self.topframe, textvariable=self.last_name_var)
        self.e_last_name.grid(row=1, column=1, padx=10)

        self.e_date_created = Entry(self.topframe, textvariable=self.date_created_var)
        self.e_date_created.grid(row=2, column=1, padx=10)

        self.e_date_valid = Entry(self.topframe, textvariable=self.date_valid_var)
        self.e_date_valid.grid(row=3, column=1, padx=10)

        if self.mission == "lookup":
            add_button = Button(self.topframe, text="Ok", command=self.ok)

        else:
            add_button = Button(self.topframe, text="Edit", command=self.update_in_db)
        add_button.grid(column=1, pady=20)

    def ok(self):
        self.destroy()

    def check_if_valid(self):
        
        if len(self.first_name_var.get()) == 0:
            self.e_first_name.config(highlightbackground="red")

            return False

        if len(self.last_name_var.get()) == 0:
            self.e_last_name.config(highlightbackground="red")

            return False

        if len(self.date_created_var.get()) == 0:
            self.e_last_name.config(highlightbackground="red")

            return False

        if len(self.date_valid_var.get()) == 0:
            self.e_last_name.config(highlightbackground="red")

            return False

        return True

    def update_in_db(self):
        valid = self.check_if_valid()
        if valid:
            res = self.database.update_carnet(self.first_name_var.get(), self.last_name_var.get(), self.date_created_var.get(), self.date_valid_var.get(), self.carnet_id)

            if res:
                messagebox.showinfo("", "Zaktualizowano")
                self.ok()
            else:
                messagebox.showerror("", "Błąd")

class SearchPopup(Toplevel):

    def __init__(self, master, database):
        self.tree = master
        Toplevel.__init__(self)
        self.database = database
        self.frame = Frame(self)
        self.title("Szukaj")
        self.geometry("300x130")
        self.resizable(False, False)
        self.frame.pack()

        self.set_widgets()

    def set_widgets(self):
        self.carnet_id_var = StringVar()

        carnet_id_label = Label(self.frame, text="ID karnetu: ").grid(row=0, column=0, pady=20, padx=10)
        carnet_id_entry = Entry(self.frame, textvariable=self.carnet_id_var).grid(row=0, column=1, pady=20, padx=10)

        add_button = Button(self.frame, text="Szukaj", command=self.search)
        add_button.grid(column=1, pady=10)

    def check_if_valid(self):
        
        if len(self.carnet_id_var.get()) == 0:
            self.carnet_id_entry.config(highlightbackground="red")

            return False

        return True

    def search(self):
        valid = self.check_if_valid()
        if valid:
            data = self.database.get_by_carnet_id(int(self.carnet_id_var.get()))
            
            if data:
                e = EditCarnet(self.tree, self.database, "lookup", data[0], data[1], data[2], data[3], id=None)
                self.destroy()

            else:
                messagebox.showerror("", "Nie znaleziono karnetu o podanym id.")

            