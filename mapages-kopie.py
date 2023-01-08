import tkinter as tk
from PIL import Image, ImageTk





class window(tk.Tk):
     def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        zprava = tk.Toplevel(self)
        self.textove_pole = tk.Text(zprava, width=100)
        self.textove_pole.pack()



        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (PageOne, PageTwo, PageThree, PageFour):

            frame = F(container, self)
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(PageOne)
     def show_frame(self, ignac):
            frame = self.frames[ignac]
            frame.tkraise()

     def inzerce(self, index, string):
         self.textove_pole.insert(index, string)

     def hledej(self, string):
         return self.textove_pole.get("1.0", "end-1c").find(string)

     def smaz(self, first, last):
         self.textove_pole.delete(first, last)


class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        row1 = tk.Label(self, text="Je pacient ambulatní nebo je hospitalizován? ", wraplength=300)
        row1.grid(column=0, row=0)

        btnBack = tk.Button(self, text="Ambulantni",
                            command=lambda: controller.show_frame(PageThree) + controller.inzerce("end", "Pacient přichází do ambulance "))
        btnBack.grid(row=1, column=3)

        btn_hospitalizovany = tk.Button(self, height=1, width=12, text="Hospitalizovaný", command= lambda: controller.show_frame(PageThree) + controller.inzerce("end", "Pacient je hospitalizován ") )
        btn_hospitalizovany.grid(column=4, row=1)

class PageThree(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


        label = tk.Label(self, text="O jaké stádium potíží se jedná?")
        label.grid(row=0, column=0)

        btnBack = tk.Button(self, text="Zpět", command=lambda: controller.show_frame(PageOne) + back_tlacitko1())
        btnBack.grid(row=1, column=4)

        btnAkut = tk.Button(self, text = "Akutní", command=lambda : controller.show_frame(PageFour) + controller.inzerce("end", "pro náhle vzniklé "))
        btnAkut.grid(row=1, column=1)
        btnChronic = tk.Button(self, text = "Chronické", command=lambda : controller.show_frame(PageFour) + controller.inzerce("end", "pro dlouhotrvající "))
        btnChronic.grid(row=1, column=2)
        btnRelaps = tk.Button(self, text = "Relaps", command=lambda : controller.show_frame(PageFour) + controller.inzerce("end", "pro zhoršení "))
        btnRelaps.grid(row=1, column=3)

        #def back_tlacitko2():
            #ambulantni_text = controller.textove_pole.tag_add()
            #hospitalizovaný_text

        def back_tlacitko1():
            ambulantni_text = "Pacient přichází do ambulance "
            hospitalizovany_text = "Pacient je hospitalizován "

            print(controller.hledej(ambulantni_text))

            if controller.hledej(ambulantni_text) >= 0:
                controller.smaz("1." + str(controller.hledej(ambulantni_text)), "1." + str(controller.hledej(ambulantni_text) + len(ambulantni_text)))
            if controller.hledej(hospitalizovany_text) >= 0:
               controller.smaz("1." + str(controller.hledej(hospitalizovany_text)), "1." + str(controller.hledej(hospitalizovany_text) + len(hospitalizovany_text)))

class PageFour(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Vyberte potíže, které pacienta přivedly.")
        label.grid(row=0, column=0)

        btn_bolest = tk.Button(self, text = "Bolest", command=lambda : controller.show_frame(PageTwo) + controller.inzerce("end", "bolesti "))
        btn_bolest.grid(row=1, column=0)


class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "Kliknutím označte oblast/oblasti na těle, které Vás bolí.")
        label.grid(column=0, row=0)


        canvas = tk.Canvas(self, width = 500, height = 500)
        canvas.grid(column=0, row=1, rowspan=3)

        btn_bolest = tk.Menubutton(self, height=1, width=10, text="Bolest ", relief="raised")
        btn_bolest.grid(column=1, row=1)
        bolest_menu = tk.Menu(btn_bolest, tearoff=0)
        btn_bolest["menu"] = bolest_menu





  #Variables
        var1 = tk.IntVar()
        var2 = tk.IntVar()
        var3 = tk.IntVar()
        var4 = tk.IntVar()
        var5 = tk.IntVar()
        var6 = tk.IntVar()
        var7 = tk.IntVar()
        var8 = tk.IntVar()
        var9 = tk.IntVar()
        var10 = tk.IntVar()
        var11 = tk.IntVar()
        var12 = tk.IntVar()
        var13 = tk.IntVar()
        var14 = tk.IntVar()
        var15 = tk.IntVar()
        var16 = tk.IntVar()
        var17 = tk.IntVar()
        var18 = tk.IntVar()
        var19 = tk.IntVar()
        var20 = tk.IntVar()
        var21 = tk.IntVar()
        var22 = tk.IntVar()
        var23 = tk.IntVar()
        var24 = tk.IntVar()
        var25 = tk.IntVar()
        var26 = tk.IntVar()
        var27 = tk.IntVar()
        var28 = tk.IntVar()
        var29 = tk.IntVar()
        var30 = tk.IntVar()
        var31 = tk.IntVar()
        var32 = tk.IntVar()
        var33 = tk.IntVar()
        var34 = tk.IntVar()
        var35 = tk.IntVar()
        var36 = tk.IntVar()
        var37 = tk.IntVar()
        var38 = tk.IntVar()
        var39 = tk.IntVar()
        var40 = tk.IntVar()
        var41 = tk.IntVar()
        var42 = tk.IntVar()
        var43 = tk.IntVar()
        var44 = tk.IntVar()
        var45 = tk.IntVar()
        var46 = tk.IntVar()
        var47 = tk.IntVar()
        var48 = tk.IntVar()
        var49 = tk.IntVar()
        var50 = tk.IntVar()
        var51 = tk.IntVar()
        var52 = tk.IntVar()
        var53 = tk.IntVar()
        var54 = tk.IntVar()
        var55 = tk.IntVar()
        var56 = tk.IntVar()
        var57 = tk.IntVar()
        var58 = tk.IntVar()
        var59 = tk.IntVar()
        var60 = tk.IntVar()
        var61 = tk.IntVar()
        var62 = tk.IntVar()


        seznamVar = [var1, var2, var3, var4, var5, var6, var7, var8, var9, var10, var11, var12, var13, var14, var15, var16, var17, var18, var19, var20, var21, var22, var23, var24, var25, var26, var27, var28, var29, var30, var31, var32, var33, var34, var35, var36, var37, var38, var39, var40, var41, var42, var43, var44, var45, var46, var47, var48, var49, var50, var51, var52, var53, var54, var55, var56, var57, var58, var59, var60, var61, var62]

        def OK_button():
            seznam = []
            oblast = []
            for i in range(len(seznamVar)):
                seznam.append(seznamVar[i].get())

            oblast.append(sum(seznam[0:8:])) # [0] hlava
            oblast.append(seznam[26] + sum(seznam[16:18:]) + sum(seznam[8:10:])) # [1] krk
            oblast.append(sum(seznam[10:13:]) + sum(seznam[18:21:]) + sum(seznam[24:26:])) # [2] hrudník
            oblast.append(sum(seznam[13:16:]) + sum(seznam[21:25:])) #[3] břicho
            oblast.append(sum(seznam[57:63:])) #[4] PHK
            oblast.append(sum(seznam[49:57:])) #[5] LHK
            oblast.append(sum(seznam[27:38:])) #[6] LDK
            oblast.append(sum(seznam[38:49:])) #[7] PDK
            print(oblast)

            if oblast[0] >= 1 and sum(oblast[1:8:]) ==0:
                controller.inzerce("end", "v oblasti hlavy.")
            if oblast[1] >= 1 and sum(oblast[2:8:]) == 0 and oblast[0] == 0:
                controller.inzerce("end", "v oblasti krku.")
            if oblast[2] >= 1 and sum(oblast[3:8:]) == 0 and sum(oblast[0:2:]) == 0:
                controller.inzerce("end", "v oblasti hrudníku.")
            if oblast[3] >= 1 and sum(oblast[4:8:]) == 0 and sum(oblast[0:3:]) == 0:
                controller.inzerce("end", "v oblasti břicha.")
            if oblast[4] >= 1 and sum(oblast[5:8:]) == 0 and sum(oblast[0:4:]) == 0:
                controller.inzerce("end", "v oblasti LHK.")
            if oblast[5] >= 1 and sum(oblast[6:8:]) == 0 and sum(oblast[0:5:]) == 0:
                controller.inzerce("end", "v oblasti PHK.")
            if oblast[6] >= 1 and sum(oblast[0:6:]) == 0 and oblast[7] == 0:
                controller.inzerce("end", "v oblasti PDK.")
            if oblast[7] >= 1 and sum(oblast[0:7:]) ==0:
                controller.inzerce("end", "v oblasti LDK.")

        #    if sum(seznam[0:8:]) >=1:
        #        controller.inzerce("end", "v oblasti hlavy")
         #   if  (sum(seznam[0:8:]) >=1) and (seznam[26] >=1 or sum(seznam[16:18:]) >=1 or sum(seznam[8:10:]) >=1):
          #      controller.inzerce("end", ", krku")
           # elif seznam[26] >=1 or sum(seznam[16:18:]) >=1 or sum(seznam[8:10:]) >=1:
          #       controller.inzerce("end", "v oblasti krku")
           # if sum(seznam[10:13:]) >=1 or sum(seznam[18:21:]) >=1 or sum(seznam[24:26:]) >=1:
            #    controller.inzerce("end", "v oblasti hrudníku ")
          #  if sum(seznam[13:16:]) >= 1 or sum(seznam[21:25:]) >=1:
           #     controller.inzerce("end", "v oblasti břicha ")
            #if sum(seznam[57:63:]) >= 1:
             #   controller.inzerce("end", "v oblasti LHK ")
            #if sum(seznam[49:57:]) >= 1:
            #    controller.inzerce("end", "v oblasti PHK ")
            #if sum(seznam[27:38:]) >= 1:
             #   controller.inzerce("end", "v oblasti PDK ")
            #if sum(seznam[38:49:]) >= 1:
             #   controller.inzerce("end", "v oblasti LDK ")





        btn_ok = tk.Button(self, text="OK", command=OK_button)
        btn_ok.grid(column=1, row=2)
        btn_zpet = tk.Button(self, text="Zpět")
        btn_zpet.grid(column=1, row=3)


  #Buttons
        btn1 = bolest_menu.add_checkbutton(label=str(seznamVar[0]), variable=seznamVar[0], onvalue=1, offvalue=0)
        btn2 = bolest_menu.add_checkbutton(label=str(seznamVar[1]), variable=seznamVar[1], onvalue=1, offvalue=0)
        btn3 = bolest_menu.add_checkbutton(label=str(seznamVar[2]), variable=seznamVar[2], onvalue=1, offvalue=0)
        btn4 = bolest_menu.add_checkbutton(label=str(seznamVar[3]), variable=seznamVar[3], onvalue=1, offvalue=0)
        btn5 = bolest_menu.add_checkbutton(label=str(seznamVar[4]), variable=seznamVar[4], onvalue=1, offvalue=0)
        btn6 = bolest_menu.add_checkbutton(label=str(seznamVar[5]), variable=seznamVar[5], onvalue=1, offvalue=0)
        btn7 = bolest_menu.add_checkbutton(label=str(seznamVar[6]), variable=seznamVar[6], onvalue=1, offvalue=0)
        btn8 = bolest_menu.add_checkbutton(label=str(seznamVar[7]), variable=seznamVar[7], onvalue=1, offvalue=0)
        btn9 = bolest_menu.add_checkbutton(label=str(seznamVar[8]), variable=seznamVar[8], onvalue=1, offvalue=0)
        btn10 = bolest_menu.add_checkbutton(label=str(seznamVar[9]), variable=seznamVar[9], onvalue=1, offvalue=0)
        btn11 = bolest_menu.add_checkbutton(label=str(seznamVar[10]), variable=seznamVar[10], onvalue=1, offvalue=0)
        btn12 = bolest_menu.add_checkbutton(label=str(seznamVar[11]), variable=seznamVar[11], onvalue=1, offvalue=0)
        btn13 = bolest_menu.add_checkbutton(label=str(seznamVar[12]), variable=seznamVar[12], onvalue=1, offvalue=0)
        btn14 = bolest_menu.add_checkbutton(label=str(seznamVar[13]), variable=seznamVar[13], onvalue=1, offvalue=0)
        btn15 = bolest_menu.add_checkbutton(label=str(seznamVar[14]), variable=seznamVar[14], onvalue=1, offvalue=0)
        btn16 = bolest_menu.add_checkbutton(label=str(seznamVar[15]), variable=seznamVar[15], onvalue=1, offvalue=0)
        btn17 = bolest_menu.add_checkbutton(label=str(seznamVar[16]), variable=seznamVar[16], onvalue=1, offvalue=0)
        btn18 = bolest_menu.add_checkbutton(label=str(seznamVar[17]), variable=seznamVar[17], onvalue=1, offvalue=0)
        btn19 = bolest_menu.add_checkbutton(label=str(seznamVar[18]), variable=seznamVar[18], onvalue=1, offvalue=0)
        btn20 = bolest_menu.add_checkbutton(label=str(seznamVar[19]), variable=seznamVar[19], onvalue=1, offvalue=0)
        btn21 = bolest_menu.add_checkbutton(label=str(seznamVar[20]), variable=seznamVar[20], onvalue=1, offvalue=0)
        btn22 = bolest_menu.add_checkbutton(label=str(seznamVar[21]), variable=seznamVar[21], onvalue=1, offvalue=0)
        btn23 = bolest_menu.add_checkbutton(label=str(seznamVar[22]), variable=seznamVar[22], onvalue=1, offvalue=0)
        btn24 = bolest_menu.add_checkbutton(label=str(seznamVar[23]), variable=seznamVar[23], onvalue=1, offvalue=0)
        btn25 = bolest_menu.add_checkbutton(label=str(seznamVar[24]), variable=seznamVar[24], onvalue=1, offvalue=0)
        btn26 = bolest_menu.add_checkbutton(label=str(seznamVar[25]), variable=seznamVar[25], onvalue=1, offvalue=0)
        btn27 = bolest_menu.add_checkbutton(label=str(seznamVar[26]), variable=seznamVar[26], onvalue=1, offvalue=0)
        btn28 = bolest_menu.add_checkbutton(label=str(seznamVar[27]), variable=seznamVar[27], onvalue=1, offvalue=0)
        btn29 = bolest_menu.add_checkbutton(label=str(seznamVar[28]), variable=seznamVar[28], onvalue=1, offvalue=0)
        btn30 = bolest_menu.add_checkbutton(label=str(seznamVar[29]), variable=seznamVar[29], onvalue=1, offvalue=0)
        btn31 = bolest_menu.add_checkbutton(label=str(seznamVar[30]), variable=seznamVar[30], onvalue=1, offvalue=0)
        btn32 = bolest_menu.add_checkbutton(label=str(seznamVar[31]), variable=seznamVar[31], onvalue=1, offvalue=0)
        btn33 = bolest_menu.add_checkbutton(label=str(seznamVar[32]), variable=seznamVar[32], onvalue=1, offvalue=0)
        btn34 = bolest_menu.add_checkbutton(label=str(seznamVar[33]), variable=seznamVar[33], onvalue=1, offvalue=0)
        btn35 = bolest_menu.add_checkbutton(label=str(seznamVar[34]), variable=seznamVar[34], onvalue=1, offvalue=0)
        btn36 = bolest_menu.add_checkbutton(label=str(seznamVar[35]), variable=seznamVar[35], onvalue=1, offvalue=0)
        btn37 = bolest_menu.add_checkbutton(label=str(seznamVar[36]), variable=seznamVar[36], onvalue=1, offvalue=0)
        btn38 = bolest_menu.add_checkbutton(label=str(seznamVar[37]), variable=seznamVar[37], onvalue=1, offvalue=0)
        btn39 = bolest_menu.add_checkbutton(label=str(seznamVar[38]), variable=seznamVar[38], onvalue=1, offvalue=0)
        btn40 = bolest_menu.add_checkbutton(label=str(seznamVar[39]), variable=seznamVar[39], onvalue=1, offvalue=0)
        btn41 = bolest_menu.add_checkbutton(label=str(seznamVar[40]), variable=seznamVar[40], onvalue=1, offvalue=0)
        btn42 = bolest_menu.add_checkbutton(label=str(seznamVar[41]), variable=seznamVar[41], onvalue=1, offvalue=0)
        btn43 = bolest_menu.add_checkbutton(label=str(seznamVar[42]), variable=seznamVar[42], onvalue=1, offvalue=0)
        btn44 = bolest_menu.add_checkbutton(label=str(seznamVar[43]), variable=seznamVar[43], onvalue=1, offvalue=0)
        btn45 = bolest_menu.add_checkbutton(label=str(seznamVar[44]), variable=seznamVar[44], onvalue=1, offvalue=0)
        btn46 = bolest_menu.add_checkbutton(label=str(seznamVar[45]), variable=seznamVar[45], onvalue=1, offvalue=0)
        btn47 = bolest_menu.add_checkbutton(label=str(seznamVar[46]), variable=seznamVar[46], onvalue=1, offvalue=0)
        btn48 = bolest_menu.add_checkbutton(label=str(seznamVar[47]), variable=seznamVar[47], onvalue=1, offvalue=0)
        btn49 = bolest_menu.add_checkbutton(label=str(seznamVar[48]), variable=seznamVar[48], onvalue=1, offvalue=0)
        btn50 = bolest_menu.add_checkbutton(label=str(seznamVar[49]), variable=seznamVar[49], onvalue=1, offvalue=0)
        btn51 = bolest_menu.add_checkbutton(label=str(seznamVar[50]), variable=seznamVar[50], onvalue=1, offvalue=0)
        btn52 = bolest_menu.add_checkbutton(label=str(seznamVar[51]), variable=seznamVar[51], onvalue=1, offvalue=0)
        btn53 = bolest_menu.add_checkbutton(label=str(seznamVar[52]), variable=seznamVar[52], onvalue=1, offvalue=0)
        btn54 = bolest_menu.add_checkbutton(label=str(seznamVar[53]), variable=seznamVar[53], onvalue=1, offvalue=0)
        btn55 = bolest_menu.add_checkbutton(label=str(seznamVar[54]), variable=seznamVar[54], onvalue=1, offvalue=0)
        btn56 = bolest_menu.add_checkbutton(label=str(seznamVar[55]), variable=seznamVar[55], onvalue=1, offvalue=0)
        btn57 = bolest_menu.add_checkbutton(label=str(seznamVar[57]), variable=seznamVar[57], onvalue=1, offvalue=0)
        btn58 = bolest_menu.add_checkbutton(label=str(seznamVar[58]), variable=seznamVar[58], onvalue=1, offvalue=0)
        btn59 = bolest_menu.add_checkbutton(label=str(seznamVar[59]), variable=seznamVar[59], onvalue=1, offvalue=0)
        btn60 = bolest_menu.add_checkbutton(label=str(seznamVar[60]), variable=seznamVar[60], onvalue=1, offvalue=0)
        btn61 = bolest_menu.add_checkbutton(label=str(seznamVar[61]), variable=seznamVar[61], onvalue=1, offvalue=0)


        #creating background
        bgImage = ImageTk.PhotoImage(Image.open("silueta_zpredu_2.png"))
        bg = canvas.create_image(20, 0, image=bgImage)




        class teloButton():
            def __init__(self, x, y, file, cvs, boxnumber):
                self.x = x #shift on horizontal axis (left=0)
                self.y = y #shift on vertical axis (top=zero)
                self.file = file #stands for future-image-button file
                self.cvs = cvs #stands for canvas
                self.boxnumber = boxnumber


                self.foto = ImageTk.PhotoImage(Image.open(self.file))
                self.image = self.cvs.create_image(self.x, self.y, image=self.foto)
                #self.checkbox = toggle(seznamVar[boxnumber])


                self.button = self.cvs.tag_bind(self.image, "<Button-1>", lambda e: morel())

                def morel():
                    self.cvs.tag_lower(self.image)
                    self.cvs.tag_lower(bg)
                    bolest_menu.invoke(int(self.boxnumber) - 1)




        #Hlava
        R_scalp = teloButton(132, 11, "mapa_tela/R_scalp.png", canvas, 1)
        G_scalp = teloButton(132, 11, "mapa_tela/G_scalp.png", canvas, 1)

        RR_scalp = teloButton(153, 11, "mapa_tela/RR_scalp.png", canvas, 2)
        GG_scalp = teloButton(153, 11, "mapa_tela/GG_scalp.png", canvas, 2)

        R_orbit = teloButton(132, 31, "mapa_tela/R_orbita.png", canvas, 3)
        G_orbit = teloButton(132, 31, "mapa_tela/G_orbita.png", canvas, 3)

        RR_orbita = teloButton(152, 31, "mapa_tela/RR_orbita.png", canvas, 4)
        GG_orbita = teloButton(152, 31, "mapa_tela/GG_orbita.png", canvas, 4)

        R_maxilla = teloButton(131, 37, "mapa_tela/R_maxilla.png", canvas, 5)
        G_maxilla = teloButton(131, 37, "mapa_tela/G_maxilla.png", canvas, 5)

        RR_maxilla = teloButton(154, 35, "mapa_tela/RR_maxilla.png", canvas, 6)
        GG_maxilla = teloButton(154, 35, "mapa_tela/GG_maxilla.png", canvas, 6)

        R_mandibula = teloButton(132, 52, "mapa_tela/R_mandibula.png", canvas, 7)
        G_mandibula = teloButton(132, 52, "mapa_tela/G_mandibula.png", canvas, 7)

        RR_mandibula = teloButton(152, 55, "mapa_tela/RR_mandibula.png", canvas, 8)
        GG_mandibula = teloButton(152, 55, "mapa_tela/GG_mandibula.png", canvas, 8)
        #Trup vpravo
        R_trapez = teloButton(105, 83, "mapa_tela/R_trapez.png", canvas, 9)
        G_trapez = teloButton(105, 83, "mapa_tela/G_trapez.png", canvas, 9)

        R_clavicle = teloButton(108, 91, "mapa_tela/R_clavicle.png", canvas, 10)
        G_clavicle = teloButton(108, 91, "mapa_tela/G_clavicle.png", canvas, 10)

        R_upper_pec = teloButton(108, 112, "mapa_tela/R_upper_pec.png", canvas, 11)
        G_upper_pec = teloButton(108, 112, "mapa_tela/G_upper_pec.png", canvas, 11)

        R_lower_pec = teloButton(110, 133, "mapa_tela/R_lower_pec.png", canvas, 12)
        G_lower_pec = teloButton(110, 133, "mapa_tela/G_lower_pec.png", canvas, 12)

        R_thorax = teloButton(119, 161, "mapa_tela/R_thorax.png", canvas, 13)
        G_thorax = teloButton(119, 161, "mapa_tela/G_thorax.png", canvas, 13)

        R_epigastrium = teloButton(122, 180, "mapa_tela/R_epigastrium.png", canvas, 14)
        G_epigastrium = teloButton(122, 180, "mapa_tela/G_epigastrium.png", canvas, 14)

        R_hypogastrium = teloButton(121, 216, "mapa_tela/R_hypogastrium.png", canvas, 15)
        G_hypogastrium = teloButton(121, 216, "mapa_tela/G_hypogastrium.png", canvas, 15)

        R_inguina = teloButton(122, 248, "mapa_tela/R_inguina.png", canvas, 16)
        G_inguina = teloButton(122, 248, "mapa_tela/G_inguina.png", canvas, 16)
        #Trup vlevo
        RR_trapez = teloButton(177, 80, "mapa_tela/RR_trapez.png", canvas, 17)
        GG_trapez = teloButton(177, 80, "mapa_tela/GG_trapez.png", canvas, 17)

        RR_clavicle = teloButton(174, 91, "mapa_tela/RR_clavicle.png", canvas, 18)
        GG_clavicle = teloButton(174, 91, "mapa_tela/GG_clavicle.png", canvas, 18)

        RR_upper_pec = teloButton(175, 112, "mapa_tela/RR_upper_pec.png", canvas, 19)
        GG_upper_pec = teloButton(175, 112, "mapa_tela/GG_upper_pec.png", canvas, 19)

        RR_lower_pec = teloButton(172, 134, "mapa_tela/RR_lower_pec.png", canvas, 20)
        GG_lower_pec = teloButton(172, 134, "mapa_tela/GG_lower_pec.png", canvas, 20)

        RR_thorax = teloButton(164, 161, "mapa_tela/RR_thorax.png", canvas, 21)
        GG_thorax = teloButton(164, 161, "mapa_tela/GG_thorax.png", canvas, 21)

        RR_epigastrium = teloButton(160, 180, "mapa_tela/RR_epigastrium.png", canvas, 22)
        GG_epigastrium = teloButton(160, 180, "mapa_tela/GG_epigastrium.png", canvas, 22)

        RR_hypogastrium = teloButton(161, 216, "mapa_tela/RR_hypogastrium.png", canvas, 23)
        GG_hypogastrium = teloButton(161, 216, "mapa_tela/GG_hypogastrium.png", canvas, 23)

        RR_inguina = teloButton(159, 248, "mapa_tela/RR_inguina.png", canvas, 24)
        GG_inguina = teloButton(159, 248, "mapa_tela/GG_inguina.png", canvas, 24)
        #Trup ve středu
        R_sternum = teloButton(142, 134, "mapa_tela/R_sternum.png", canvas, 25)
        G_sternum = teloButton(142, 134, "mapa_tela/G_sternum.png", canvas, 25)

        R_manubrium = teloButton(142, 98, "mapa_tela/R_manubrium.png", canvas, 26)
        G_manubrium = teloButton(142, 98, "mapa_tela/G_manubrium.png", canvas, 26)

        R_cervix = teloButton(140, 75, "mapa_tela/R_cervix.png", canvas, 27)
        G_cervix = teloButton(140, 75, "mapa_tela/G_cervix.png", canvas, 27)
        #P dolní končetina

        R_hip = teloButton(99, 239, "mapa_tela/R_hip.png", canvas, 28)
        G_hip = teloButton(99, 239, "mapa_tela/G_hip.png", canvas, 28)

        R_upper_thigh = teloButton(112, 267, "mapa_tela/R_upper_thigh.png", canvas, 29)
        G_upper_thigh = teloButton(112, 267, "mapa_tela/G_upper_thigh.png", canvas, 29)

        R_mid_thigh = teloButton(115, 300, "mapa_tela/R_mid_thigh.png", canvas, 30)
        G_mid_thigh = teloButton(115, 300, "mapa_tela/G_mid_thigh.png", canvas, 30)

        R_lower_thigh = teloButton(121, 337, "mapa_tela/R_lower_thigh.png", canvas, 31)
        G_lower_thigh = teloButton(121, 337, "mapa_tela/G_lower_thigh.png", canvas, 31)

        R_gracilis = teloButton(136, 316, "mapa_tela/R_gracilis.png", canvas, 32)
        G_gracilis = teloButton(136, 316, "mapa_tela/G_gracilis.png", canvas, 32)

        R_genus = teloButton(123, 375, "mapa_tela/R_genus.png", canvas, 33)
        G_genus = teloButton(123, 375, "mapa_tela/G_genus.png", canvas, 33)

        R_caput_fibulae = teloButton(111, 377, "mapa_tela/R_caput_fibulae.png", canvas, 34)
        G_caput_fibulae = teloButton(111, 377, "mapa_tela/G_caput_fibulae.png", canvas, 34)

        R_crux_lateralis = teloButton(117, 425, "mapa_tela/R_crux_lateralis.png", canvas, 35)
        G_crux_lateralis = teloButton(117, 425, "mapa_tela/G_crux_lateralis.png", canvas, 35)

        R_crux_medialis = teloButton(129, 435, "mapa_tela/R_crux_medialis.png", canvas, 36)
        G_crux_medialis = teloButton(129, 435, "mapa_tela/G_crux_medialis.png", canvas, 36)

        R_pes = teloButton(125, 477, "mapa_tela/R_pes.png", canvas, 37)
        G_pes = teloButton(125, 477, "mapa_tela/G_pes.png", canvas, 37)

        R_digitus_minimus = teloButton(114, 475, "mapa_tela/R_digitus_minimus.png", canvas, 38)
        G_digitus_minimus = teloButton(114, 475, "mapa_tela/G_digitus_minimus.png", canvas, 38)
        #L dolní končetina

        RR_hip = teloButton(182, 242, "mapa_tela/RR_hip.png", canvas, 39)
        GG_hip = teloButton(182, 242, "mapa_tela/GG_hip.png", canvas, 39)

        RR_upper_thigh = teloButton(170, 266, "mapa_tela/RR_upper_thigh.png", canvas, 40)
        GG_upper_thigh = teloButton(170, 266, "mapa_tela/GG_upper_thigh.png", canvas, 40)

        RR_mid_thigh = teloButton(167, 300, "mapa_tela/RR_mid_thigh.png", canvas, 41)
        GG_mid_thigh = teloButton(167, 300, "mapa_tela/GG_mid_thigh.png", canvas, 41)

        RR_lower_thigh = teloButton(161, 337, "mapa_tela/RR_lower_thigh.png", canvas, 42)
        GG_lower_thigh = teloButton(161, 337, "mapa_tela/GG_lower_thigh.png", canvas, 42)

        RR_gracilis = teloButton(147, 316, "mapa_tela/RR_gracilis.png", canvas, 43)
        GG_gracilis = teloButton(147, 316, "mapa_tela/GG_gracilis.png", canvas, 43)

        RR_genus = teloButton(156, 376, "mapa_tela/RR_genus.png", canvas, 44)
        GG_genus = teloButton(156, 376, "mapa_tela/GG_genus.png", canvas, 44)

        RR_caput_fibulae = teloButton(166, 375, "mapa_tela/RR_caput_fibulae.png", canvas, 45)
        GG_caput_fibulae = teloButton(166, 375, "mapa_tela/GG_caput_fibulae.png", canvas, 45)

        RR_crux_lateralis = teloButton(162, 426, "mapa_tela/RR_crux_lateralis.png", canvas, 46)
        GG_crux_lateralis = teloButton(162, 426, "mapa_tela/GG_crux_lateralis.png", canvas, 46)

        RR_crux_medialis = teloButton(150, 435, "mapa_tela/RR_crux_medialis.png", canvas, 47)
        GG_crux_medialis = teloButton(150, 435, "mapa_tela/GG_crux_medialis.png", canvas, 47)

        RR_pes = teloButton(152, 478, "mapa_tela/RR_pes.png", canvas, 48)
        GG_pes = teloButton(152, 478, "mapa_tela/GG_pes.png", canvas, 48)

        RR_digitus_minimus = teloButton(163, 474, "mapa_tela/RR_digitus_minimus.png", canvas, 49)
        GG_digitus_minimus = teloButton(163, 474, "mapa_tela/GG_digitus_minimus.png", canvas, 49)
        #Pravá paže a ruka
        R_omus = teloButton(79, 115, "mapa_tela/R_omus.png", canvas, 50)
        G_omus = teloButton(79, 115, "mapa_tela/G_omus.png", canvas, 50)

        R_brach_lat = teloButton(78, 157, "mapa_tela/R_brachii_lateralis.png", canvas, 51)
        G_brach_lat = teloButton(78, 157, "mapa_tela/G_brachii_lateralis.png", canvas, 51)

        R_brach_med = teloButton(88, 153, "mapa_tela/R_brachii_medialis.png", canvas, 52)
        G_brach_med = teloButton(88, 153, "mapa_tela/G_brachii_medialis.png", canvas, 52)

        R_ante_lat = teloButton(63, 207, "mapa_tela/R_antebrachii_lateralis.png", canvas, 53)
        G_ante_lat = teloButton(63, 207, "mapa_tela/G_antebrachii_lateralis.png", canvas, 53)

        R_ante_med = teloButton(75, 211, "mapa_tela/R_antebrachii_medialis.png", canvas, 54)
        G_ante_med = teloButton(75, 211, "mapa_tela/G_antebrachii_medialis.png", canvas, 54)

        R_manus_lat = teloButton(38, 274, "mapa_tela/R_manus_lateralis.png", canvas, 55)
        G_manus_lat = teloButton(38, 274, "mapa_tela/G_manus_lateralis.png", canvas, 55)

        R_manus_med = teloButton(53, 274, "mapa_tela/R_manus_medialis.png", canvas, 56)
        G_manus_med = teloButton(53, 274, "mapa_tela/G_manus_medialis.png", canvas, 56)
        #Levá paže a ruka
        RR_omus = teloButton(203, 115, "mapa_tela/RR_omus.png", canvas, 57)
        GG_omus = teloButton(203, 115, "mapa_tela/GG_omus.png", canvas, 57)

        RR_brach_lat = teloButton(204, 157, "mapa_tela/RR_brachii_lateralis.png", canvas, 58)
        GG_brach_lat = teloButton(204, 157, "mapa_tela/GG_brachii_lateralis.png", canvas, 58)

        RR_brach_med = teloButton(193, 154, "mapa_tela/RR_brachii_medialis.png", canvas, 59)
        GG_brach_med = teloButton(193, 154, "mapa_tela/GG_brachii_medialis.png", canvas, 59)

        RR_ante_lat = teloButton(219, 209, "mapa_tela/RR_antebrachii_lateralis.png", canvas, 60)
        GG_ante_lat = teloButton(219, 209, "mapa_tela/GG_antebrachii_lateralis.png", canvas, 60)

        RR_ante_med = teloButton(206, 214, "mapa_tela/RR_antebrachii_medialis.png", canvas, 61)
        GG_ante_med = teloButton(206, 214, "mapa_tela/GG_antebrachii_medialis.png", canvas, 61)

        RR_manus_lat = teloButton(242, 277, "mapa_tela/RR_manus_lateralis.png", canvas, 62)
        GG_manus_lat = teloButton(242, 277, "mapa_tela/GG_manus_lateralis.png", canvas, 62)

        RR_manus_med = teloButton(228, 277, "mapa_tela/RR_manus_medialis.png", canvas, 63)
        GG_manus_med = teloButton(228, 277, "mapa_tela/GG_manus_medialis.png", canvas, 63)




app = window()
app.mainloop()
