from tkinter import Tk, Label, Button

bg_color = "#c2e7ff"
fg_color = "#000000"
font_family = "Ubuntu"

class Dificultades:
    def __init__(self):
        self.display_dificultades()

    def display_dificultades(self):
        self.root = Tk()
        self.root.title("Dificultades Tic Tac Toe")
        self.root.geometry("400x400")
        self.root.resizable(False, False)
        self.root.eval('tk::PlaceWindow . center')
        self.root.configure(bg=bg_color)
        title = Label(self.root, text="Elije la dificultad", font=(font_family, 30), bg=bg_color, fg=fg_color)
        title.pack(pady=20)
        button = Button(self.root, text="Facil", font=(font_family, 20), bg=bg_color, fg=fg_color, command=lambda: print("Facil"))
        button.pack(pady=20)
        button = Button(self.root, text="Medio", font=(font_family, 20), bg=bg_color, fg=fg_color, command=lambda: print("Medio"))
        button.pack(pady=20)
        button = Button(self.root, text="Dificil", font=(font_family, 20), bg=bg_color, fg=fg_color, command=lambda: print("Dificil"))
        button.pack(pady=20)
        self.root.mainloop()
        