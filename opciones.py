from tkinter import Tk, Label, Button
from dificultades import Dificultades
from tablero import Tablero

bg_color = "#c2e7ff"
fg_color = "#000000"
font_family = "Ubuntu"

class Opciones:
    def __init__(self):
        self.display_opciones()

    def toTablero(self):
        self.root.destroy()
        Tablero()

    def toDificultades(self):
        self.root.destroy()
        Dificultades()

    def display_opciones(self):
        self.root = Tk()
        self.root.title("Opciones Tic Tac Toe")
        self.root.geometry("400x400")
        self.root.resizable(False, False)
        self.root.eval('tk::PlaceWindow . center')
        self.root.configure(bg=bg_color)
        title = Label(self.root, text="Elije una opcion", font=(font_family, 30), bg=bg_color, fg=fg_color)
        title.pack(pady=20)
        button = Button(self.root, text="Jugador vs Jugador", font=(font_family, 20), bg=bg_color, fg=fg_color, command=lambda: self.toTablero())
        button.pack(pady=20)
        button = Button(self.root, text="Jugador vs CPU", font=(font_family, 20), bg=bg_color, fg=fg_color, command=lambda: self.toDificultades())
        button.pack(pady=20)
        self.root.mainloop()
    
   
        