import tkinter as tk
from tkinter import *


zprava = tk.Tk()
zprava.geometry("600x400")
zprava.title("Výstup")


##trying out tk.Entry command for unlimited text-insertion space
textove_pole = tk.Entry(zprava, width=600)
textove_pole.grid(row=0, column=1)

labelPrijeti = tk.Label(zprava, text = "Důvod k přijetí nebo ošetření:")
labelPrijeti.grid(row=0, column=0)

labelSocialni = tk.Label(zprava, text = "Sociální anamnéza:")
labelSocialni.grid(row=2, column=0)

socialni_pole = tk.Entry(zprava, width=600)
socialni_pole.grid(row=2, column=1)



def fceambu():
    textove_pole.insert(END, "Pacient přichází do ambulance ")

def fcehospi():
    textove_pole.insert(END, "Pacient je hospitalizován ")



def back_tlacitko1():
    ambulantni_text = "Pacient přichází do ambulance "
    hospitalizovany_text = "Pacient je hospitalizován "
    celytext = textove_pole.get()



    if celytext.find(ambulantni_text) >= 0:
        textove_pole.delete(celytext.find(ambulantni_text), celytext.find(ambulantni_text) + len(ambulantni_text))
    if celytext.find(hospitalizovany_text) >= 0:
        textove_pole.delete(celytext.find(hospitalizovany_text), celytext.find(hospitalizovany_text) + len(hospitalizovany_text))

#creating class enabling switching between pages
class inter(tk.Tk):
   def __init__(self, *args, **kwargs):
       tk.Tk.__init__(self, *args, **kwargs)
       self.geometry("600x400")


       container = tk.Frame(self)
       container.pack(side="top", fill="both", expand= True)

       container.grid_rowconfigure(0, weight=1)
       container.grid_columnconfigure(0, weight=1)


       self.frames = {}

       for F in (Page1, Page2, Page3, PageSoc1):

           frame = F(container, self)

           self.frames[F] = frame

           frame.grid(row=0, column=0, sticky="nsew")

       self.show_frame(Page1)

   def show_frame(self, cont):
       frame = self.frames[cont]
       frame.tkraise()








##row1 label


##row1 buttons




class Page1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        row1 = tk.Label(self, text="Je pacient ambulatní nebo je hospitalizován? ", wraplength=300)
        row1.grid(column=0, row=0)

        btnBack = tk.Button(self, text="Ambulantni",
                            command=lambda: controller.show_frame(Page2) + fceambu())
        btnBack.grid(row=1, column=3)

        btn_hospitalizovany = tk.Button(self, height=1, width=12, text="Hospitalizovaný",
                                        command= lambda: controller.show_frame(Page2) + fcehospi())
        btn_hospitalizovany.grid(column=4, row=1)


class Page3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Vyberte potíže, které pacienta přivedly a klikněte na tlačítko OK")
        label.grid(row=0, column=0)





        btn_bolest = tk.Menubutton(self, height=1, width=10, text="Bolest ", relief=RAISED)
        btn_bolest.grid(column=1, row=1)
        bolest_menu = tk.Menu(btn_bolest, tearoff=0)
        btn_bolest["menu"] = bolest_menu

        DKK = StringVar(self)
        HKK = StringVar(self)

        bolest_menu.add_checkbutton(label="DK", variable=DKK,
                                    onvalue="bolesti v oblasti HKK", offvalue="")
        bolest_menu.add_checkbutton(label="HK", variable=HKK,
                                    onvalue="bolesti v oblasti DKK", offvalue="")

        btn_ok = tk.Button(self, text="OK",
                           command= lambda: controller.show_frame(PageSoc1) + textove_pole.insert(END, HKK.get() + DKK.get()))
                            #zde by bylo lepší mít funkci s if-statementem - if both are onvalue - then HKK.get() + " a " + DKK.get(), jinak HKK + DKK
        btn_ok.grid(row=2, column=2)




class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="O jaké stádium potíží se jedná?")
        label.grid(row=0, column=0)

        btnBack = tk.Button(self, text="Zpět", command=lambda: controller.show_frame(Page1) + back_tlacitko1())
        btnBack.grid(row=1, column=4)

        btnAkut = tk.Button(self, text = "Akutní",
                            command=lambda : controller.show_frame(Page3) + textove_pole.insert(END, "pro náhle vzniklé "))
        btnAkut.grid(row=1, column=1)
        btnChronic = tk.Button(self, text = "Chronické", command=lambda : controller.show_frame(Page3) + textove_pole.insert(END, "pro dlouhotrvající "))
        btnChronic.grid(row=1, column=2)
        btnRelaps = tk.Button(self, text = "Relaps", command=lambda : controller.show_frame(Page3) + textove_pole.insert(END, "pro zhoršení "))
        btnRelaps.grid(row=1, column=3)

class PageSoc1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Rodinné poměry:")
        label.grid(row=0, column=0)

        Marital = StringVar(self)
        btnMarital = tk.Checkbutton(self, text = "Ženatý", variable=Marital, onvalue="karel")
        btnMarital.grid(row=1, column=1)

        #btnBack = tk.Button(self, text="Zpět", command=lambda: controller.show_frame(Page1) + back_tlacitko1())
        #btnBack.grid(row=1, column=4)

app = inter()
app.mainloop()
zprava.mainloop()