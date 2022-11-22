from tkinter import Tk, Label, Button, messagebox, simpledialog
from dificultades import Dificultades


bg_color = "#c2e7ff"
fg_color = "#000000"
font_family = "Ubuntu"

class Tablero:
    def __init__(self):
        self.display_tablero()

    def cambiar(self, value):
        if self.turno == 1:
            self.listBotones[value].config(text="X")
            self.tablero[value] = "X"
            self.turno = 2
            self.laberJugador.config(text="Turno de " + self.jugador2)
        else:
            self.listBotones[value].config(text="O")
            self.tablero[value] = "O"
            self.turno = 1
            self.laberJugador.config(text="Turno de " + self.jugador1)
        self.listBotones[value].config(state="disabled")
        self.verificar()

    def verificar(self):
        if self.tablero[0] == self.tablero[1] == self.tablero[2] != " ":
            self.ganador()
        elif self.tablero[3] == self.tablero[4] == self.tablero[5] != " ":
            self.ganador()
        elif self.tablero[6] == self.tablero[7] == self.tablero[8] != " ":
            self.ganador()
        elif self.tablero[0] == self.tablero[3] == self.tablero[6] != " ":
            self.ganador()
        elif self.tablero[1] == self.tablero[4] == self.tablero[7] != " ":
            self.ganador()
        elif self.tablero[2] == self.tablero[5] == self.tablero[8] != " ":
            self.ganador()
        elif self.tablero[0] == self.tablero[4] == self.tablero[8] != " ":
            self.ganador()
        elif self.tablero[2] == self.tablero[4] == self.tablero[6] != " ":
            self.ganador()
        elif " " not in self.tablero:
            messagebox.showinfo("Empate", "No hay ganador")
            self.root.destroy()
            Dificultades()
    
    def ganador(self):
        self.laberJugador.config(text="Termino")
        if self.turno == 1:
            messagebox.showinfo("Ganador", "El ganador es " + self.jugador2)
        else:
            messagebox.showinfo("Ganador", "El ganador es " + self.jugador1)
        self.root.destroy()
        Dificultades()


    def display_tablero(self):
        self.root = Tk()
        self.root.title("Tic Tac Toe")
        self.root.geometry("400x400")
        self.root.resizable(False, False)
        self.root.eval('tk::PlaceWindow . center')
        self.root.configure(bg=bg_color)
        self.jugador1 = simpledialog.askstring("Jugador 1", "Ingresa tu nombre")
        self.jugador2 = simpledialog.askstring("Jugador 2", "Ingresa tu nombre")
        self.turno = 1
        self.listBotones = []
        self.tablero = [" "] * 9
        self.laberJugador = Label(self.root, text="Turno de: " + self.jugador1, font=(font_family, 20), bg=bg_color, fg=fg_color)
        self.laberJugador.pack(pady=20)
        boton0 = Button(self.root, text=" ", width=10, height=5, bg=bg_color, fg=fg_color, command=lambda: self.cambiar(0))
        boton0.place(x=50, y=50)
        self.listBotones.append(boton0)
        boton1 = Button(self.root, text=" ", width=10, height=5, bg=bg_color, fg=fg_color, command=lambda: self.cambiar(1))
        boton1.place(x=150, y=50)
        self.listBotones.append(boton1)
        boton2 = Button(self.root, text=" ", width=10, height=5, bg=bg_color, fg=fg_color, command=lambda: self.cambiar(2))
        boton2.place(x=250, y=50)
        self.listBotones.append(boton2)
        boton3 = Button(self.root, text=" ", width=10, height=5, bg=bg_color, fg=fg_color, command=lambda: self.cambiar(3))
        boton3.place(x=50, y=150)
        self.listBotones.append(boton3)
        boton4 = Button(self.root, text=" ", width=10, height=5, bg=bg_color, fg=fg_color, command=lambda: self.cambiar(4))
        boton4.place(x=150, y=150)
        self.listBotones.append(boton4)
        boton5 = Button(self.root, text=" ", width=10, height=5, bg=bg_color, fg=fg_color, command=lambda: self.cambiar(5))
        boton5.place(x=250, y=150)
        self.listBotones.append(boton5)
        boton6 = Button(self.root, text=" ", width=10, height=5, bg=bg_color, fg=fg_color, command=lambda: self.cambiar(6))
        boton6.place(x=50, y=250)
        self.listBotones.append(boton6)
        boton7 = Button(self.root, text=" ", width=10, height=5, bg=bg_color, fg=fg_color, command=lambda: self.cambiar(7))
        boton7.place(x=150, y=250)
        self.listBotones.append(boton7)
        boton8 = Button(self.root, text=" ", width=10, height=5, bg=bg_color, fg=fg_color, command=lambda: self.cambiar(8))
        boton8 .place(x=250, y=250)
        self.listBotones.append(boton8)
        self.root.mainloop()

    
