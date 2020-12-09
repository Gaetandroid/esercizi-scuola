from tkinter import *
from tkinter import ttk


def calcoloarea(*args):
 try:
     lato=float(l.get())
     risultato.set(lato**2)


 except ValueError:
     risultato.set("ERRORE")
     pass


def reset(*args):
 clear = ""
 l.set(clear)
 risultato.set(clear)


root=Tk()
root.title("Calcolatrice Area Quadrato")
root.geometry("600x270")
mainframe = ttk.Frame(root)
mainframe.place(height=0, x=0, y=0)


l=StringVar()
risultato=StringVar()
risultato2=StringVar()


l_entry=Entry(root, width=3, textvariable=l, font=('verdana', 50))
l_entry.place(height=100, x=5, y=100)


Label(root, text="RISULTATO AREA:", font=('verdana', 15)).place(height=20, x=5, y=240)
Label(root, text="Calcolo Area del quadrato", font=('verdana', 20)).pack(anchor=N)

Label(root, text="Lato:", font=('verdana', 20)).place(height=50, x=5, y=50)

Label(root, textvariable=risultato, font=('verdana', 15)).place(height=20, x=200, y=240)
Button(root, text="CALCOLA AREA", command=calcoloarea, font=('verdana', 15)).place(height=25, x=5, y=210)
Button(root, text="RESET", command=reset, font=('verdana', 15)).place(height=25, x=505, y=240)

root.bind('<Return>', calcoloarea)
root.bind('<Return>', reset)

root.mainloop()
