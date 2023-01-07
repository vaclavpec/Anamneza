import textwrap
import tkinter as tk
from tkinter import *
from tkinter import Entry

##setting two windows with tkinter - inter for button-filled inteface and zprava for text (and possibly image) outputs##
zprava = tk.Tk()
zprava.geometry("600x400")
zprava.title("Výstup")

inter = tk.Tk()
inter.title("Anamnéza")
inter.geometry("600x400")

##trying out tk.Entry command for unlimited text-insertion space
textove_pole = tk.Entry(zprava, width=600)
textove_pole.grid(column=0, row=0)

##row1

##row1 label
row1 = tk.Label(inter, text="Je pacient ambulatní nebo je hospitalizován? ", wraplength=100)
row1.grid(column=0, row=0)

##row1 button functions
def uvodni_slovo_ambulantni():
    ##textove_pole.delete(0,"end")
    textove_pole.insert(0, "Pacient přichází do ambulance pro ")


def uvodni_slovo_hospitalizovany():
    ##textove_pole.delete(0,"end")
    textove_pole.insert(0, "Pacient je hospitalizován pro ")

##row1 buttons
btn_ambulantni = tk.Button(inter, height=1, width=10, text="Ambulantní", command =uvodni_slovo_ambulantni)
btn_ambulantni.grid(column=1,row=0)

btn_hospitalizovany = tk.Button(inter, height=1, width=12, text="Hospitalizovaný", command =uvodni_slovo_hospitalizovany)
btn_hospitalizovany.grid(column=2,row=0)


##2nd row
##row2 button functions
def DKK():
    textove_pole.insert("end", "bolesti DKK ")

def HKK():
    textove_pole.insert("end", "bolesti HKK ")




##row2label
row2= tk.Label(inter, text="Jaká potíž pacienta přivádí ", wraplength=100)
row2.grid(column=0, row=1)

##row2buttons
btn_bolest = tk.Menubutton(inter, height=1, width=10, text="Bolest ", relief=RAISED)
btn_bolest.grid(column=1,row=1)
bolest_menu = tk.Menu(btn_bolest, tearoff=0)
btn_bolest["menu"] = bolest_menu

bolest_menu.add_command(label="DKK", command=DKK)
bolest_menu.add_command(label="HKK", command=HKK)








##aby se to rozjelo
inter.mainloop()
zprava.mainloop()