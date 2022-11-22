import tkinter as tk
from tkinter import Tk, Label, Button
from opciones import Opciones

bg_color = "#c2e7ff"
fg_color = "#000000"
font_family = "Ubuntu"

class Menu:
    def __init__(self):
        self.display_menu()

    def toOpciones(self):
        self.root.destroy()
        Opciones()

    def display_menu(self):
        self.root = Tk()
        self.root.title("Menu Tic Tac Toe")
        self.root.geometry("400x350")
        self.root.resizable(False, False)
        self.root.configure(bg=bg_color)
        self.root.eval('tk::PlaceWindow . center')
        title = Label(self.root, text="Tic Tac Toe", font=(font_family, 30), bg=bg_color, fg=fg_color)
        title.pack(pady=20)
        button = Button(self.root, text="Iniciar Juego", font=(font_family, 20), bg=bg_color, fg=fg_color, command=lambda: self.toOpciones())
        button.pack(pady=20)
        button = Button(self.root, text="Salir", font=(font_family, 20), bg=bg_color, fg=fg_color, command=self.root.destroy)
        button.pack(pady=20)
        footer = Label(self.root, text="By: @kendalqb1, @Alejandro-10bv, @wendyaraya", font=(font_family, 10), bg=bg_color, fg=fg_color)
        footer.pack(pady=10)
        footer = Label(self.root, text="Proyecto 2 Estructuras de Datos", font=(font_family, 10), bg=bg_color, fg=fg_color)
        footer.pack(pady=1)
        self.root.mainloop()
        