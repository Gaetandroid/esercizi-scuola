from tkinter import *
from tkinter import ttk
import os

def open_quadrato():
    os.system('"%s"' %"areaquadrato.py")

def open_rettangolo():
    os.system('"%s"' %"arearettangolo.py")

def open_cerchio():
    os.system('"%s"' %"pigreco.py")

def open_triangolo():
    os.system('"%s"' %"Areatrriangolo.py")

root=Tk()
root.title("Calcolatrice Area Poligoni")
root.geometry("500x100")
mainframe = ttk.Frame(root)
mainframe.place(height=0, x=0, y=0)

Button(root, text="AREA TRIANGOLO", command=open_triangolo, font=('verdana', 15)).place(height=25, x=5, y=20)
Button(root, text="AREA QUADRATO", command=open_quadrato, font=('verdana', 15)).place(height=25, x=250, y=20)
Button(root, text="AREA RETTANGOLO", command=open_rettangolo, font=('verdana', 15)).place(height=25, x=5, y=60)
Button(root, text="AREA CERCHIO", command=open_cerchio, font=('verdana', 15)).place(height=25, x=250, y=60)

root.mainloop()