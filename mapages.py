
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

        for F in (PageOne, PageTwo, PageThree):

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

        btnAkut = tk.Button(self, text = "Akutní", command=lambda : controller.show_frame(PageTwo) + controller.inzerce("end", "pro náhle vzniklé "))
        btnAkut.grid(row=1, column=1)
        btnChronic = tk.Button(self, text = "Chronické", command=lambda : controller.show_frame(PageTwo) + controller.inzerce("end", "pro dlouhotrvající "))
        btnChronic.grid(row=1, column=2)
        btnRelaps = tk.Button(self, text = "Relaps", command=lambda : controller.show_frame(PageTwo) + controller.inzerce("end", "pro zhoršení "))
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

class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        canvas = tk.Canvas(self, width = 600, height = 500)
        canvas.grid(column=0, row=1)


        #creating background
        bgImage = ImageTk.PhotoImage(Image.open("silueta_zpredu_2.png"))
        bg = canvas.create_image(20, 0, image=bgImage, anchor="nw")


        class teloButton():
            def __init__(self, x, y, file, cvs):
                self.x = x #shift on horizontal axis (left=0)
                self.y = y #shift on vertical axis (top=zero)
                self.file = file #stands for future-image-button file
                self.cvs = cvs #stands for canvas


                self.foto = ImageTk.PhotoImage(Image.open(self.file))
                self.image = self.cvs.create_image(self.x, self.y, image=self.foto)


                self.button = self.cvs.tag_bind(self.image, "<Button-1>", lambda e: self.cvs.tag_lower(self.image) + self.cvs.tag_lower(bg))

        #Hlava
        R_scalp = teloButton(132, 11, "mapa_tela/R_scalp.png", canvas)
        G_scalp = teloButton(132, 11, "mapa_tela/G_scalp.png", canvas)

        RR_scalp = teloButton(153, 11, "mapa_tela/RR_scalp.png", canvas)
        GG_scalp = teloButton(153, 11, "mapa_tela/GG_scalp.png", canvas)

        R_orbit = teloButton(132, 31, "mapa_tela/R_orbita.png", canvas)
        G_orbit = teloButton(132, 31, "mapa_tela/G_orbita.png", canvas)

        RR_orbita = teloButton(152, 31, "mapa_tela/RR_orbita.png", canvas)
        GG_orbita = teloButton(152, 31, "mapa_tela/GG_orbita.png", canvas)

        R_maxilla = teloButton(131, 37, "mapa_tela/R_maxilla.png", canvas)
        G_maxilla = teloButton(131, 37, "mapa_tela/G_maxilla.png", canvas)

        RR_maxilla = teloButton(154, 35, "mapa_tela/RR_maxilla.png", canvas)
        GG_maxilla = teloButton(154, 35, "mapa_tela/GG_maxilla.png", canvas)

        R_mandibula = teloButton(132, 52, "mapa_tela/R_mandibula.png", canvas)
        G_mandibula = teloButton(132, 52, "mapa_tela/G_mandibula.png", canvas)

        RR_mandibula = teloButton(152, 55, "mapa_tela/RR_mandibula.png", canvas)
        GG_mandibula = teloButton(152, 55, "mapa_tela/GG_mandibula.png", canvas)
        #Trup vpravo
        R_trapez = teloButton(105, 83, "mapa_tela/R_trapez.png", canvas)
        G_trapez = teloButton(105, 83, "mapa_tela/G_trapez.png", canvas)

        R_clavicle = teloButton(108, 91, "mapa_tela/R_clavicle.png", canvas)
        G_clavicle = teloButton(108, 91, "mapa_tela/G_clavicle.png", canvas)

        R_upper_pec = teloButton(108, 112, "mapa_tela/R_upper_pec.png", canvas)
        G_upper_pec = teloButton(108, 112, "mapa_tela/G_upper_pec.png", canvas)

        R_lower_pec = teloButton(110, 133, "mapa_tela/R_lower_pec.png", canvas)
        G_lower_pec = teloButton(110, 133, "mapa_tela/G_lower_pec.png", canvas)

        R_thorax = teloButton(119, 161, "mapa_tela/R_thorax.png", canvas)
        G_thorax = teloButton(119, 161, "mapa_tela/G_thorax.png", canvas)

        R_epigastrium = teloButton(122, 180, "mapa_tela/R_epigastrium.png", canvas)
        G_epigastrium = teloButton(122, 180, "mapa_tela/G_epigastrium.png", canvas)

        R_hypogastrium = teloButton(121, 216, "mapa_tela/R_hypogastrium.png", canvas)
        G_hypogastrium = teloButton(121, 216, "mapa_tela/G_hypogastrium.png", canvas)

        R_inguina = teloButton(122, 248, "mapa_tela/R_inguina.png", canvas)
        G_inguina = teloButton(122, 248, "mapa_tela/G_inguina.png", canvas)
        #Trup vlevo
        RR_trapez = teloButton(177, 80, "mapa_tela/RR_trapez.png", canvas)
        GG_trapez = teloButton(177, 80, "mapa_tela/GG_trapez.png", canvas)

        RR_clavicle = teloButton(174, 91, "mapa_tela/RR_clavicle.png", canvas)
        GG_clavicle = teloButton(174, 91, "mapa_tela/GG_clavicle.png", canvas)

        RR_upper_pec = teloButton(175, 112, "mapa_tela/RR_upper_pec.png", canvas)
        GG_upper_pec = teloButton(175, 112, "mapa_tela/GG_upper_pec.png", canvas)

        RR_lower_pec = teloButton(172, 134, "mapa_tela/RR_lower_pec.png", canvas)
        GG_lower_pec = teloButton(172, 134, "mapa_tela/GG_lower_pec.png", canvas)

        RR_thorax = teloButton(164, 161, "mapa_tela/RR_thorax.png", canvas)
        GG_thorax = teloButton(164, 161, "mapa_tela/GG_thorax.png", canvas)

        RR_epigastrium = teloButton(160, 180, "mapa_tela/RR_epigastrium.png", canvas)
        GG_epigastrium = teloButton(160, 180, "mapa_tela/GG_epigastrium.png", canvas)

        RR_hypogastrium = teloButton(161, 216, "mapa_tela/RR_hypogastrium.png", canvas)
        GG_hypogastrium = teloButton(161, 216, "mapa_tela/GG_hypogastrium.png", canvas)

        RR_inguina = teloButton(159, 248, "mapa_tela/RR_inguina.png", canvas)
        GG_inguina = teloButton(159, 248, "mapa_tela/GG_inguina.png", canvas)
        #Trup ve středu
        R_sternum = teloButton(142, 134, "mapa_tela/R_sternum.png", canvas)
        G_sternum = teloButton(142, 134, "mapa_tela/G_sternum.png", canvas)

        R_manubrium = teloButton(142, 98, "mapa_tela/R_manubrium.png", canvas)
        G_manubrium = teloButton(142, 98, "mapa_tela/G_manubrium.png", canvas)

        R_cervix = teloButton(140, 75, "mapa_tela/R_cervix.png", canvas)
        G_cervix = teloButton(140, 75, "mapa_tela/G_cervix.png", canvas)
        #P dolní končetina

        R_hip = teloButton(99, 239, "mapa_tela/R_hip.png", canvas)
        G_hip = teloButton(99, 239, "mapa_tela/G_hip.png", canvas)

        R_upper_thigh = teloButton(112, 267, "mapa_tela/R_upper_thigh.png", canvas)
        G_upper_thigh = teloButton(112, 267, "mapa_tela/G_upper_thigh.png", canvas)

        R_mid_thigh = teloButton(115, 300, "mapa_tela/R_mid_thigh.png", canvas)
        G_mid_thigh = teloButton(115, 300, "mapa_tela/G_mid_thigh.png", canvas)

        R_lower_thigh = teloButton(121, 337, "mapa_tela/R_lower_thigh.png", canvas)
        G_lower_thigh = teloButton(121, 337, "mapa_tela/G_lower_thigh.png", canvas)

        R_gracilis = teloButton(136, 316, "mapa_tela/R_gracilis.png", canvas)
        G_gracilis = teloButton(136, 316, "mapa_tela/G_gracilis.png", canvas)

        R_genus = teloButton(123, 375, "mapa_tela/R_genus.png", canvas)
        G_genus = teloButton(123, 375, "mapa_tela/G_genus.png", canvas)

        R_caput_fibulae = teloButton(111, 377, "mapa_tela/R_caput_fibulae.png", canvas)
        G_caput_fibulae = teloButton(111, 377, "mapa_tela/G_caput_fibulae.png", canvas)

        R_crux_lateralis = teloButton(117, 425, "mapa_tela/R_crux_lateralis.png", canvas)
        G_crux_lateralis = teloButton(117, 425, "mapa_tela/G_crux_lateralis.png", canvas)

        R_crux_medialis = teloButton(129, 435, "mapa_tela/R_crux_medialis.png", canvas)
        G_crux_medialis = teloButton(129, 435, "mapa_tela/G_crux_medialis.png", canvas)

        R_pes = teloButton(125, 477, "mapa_tela/R_pes.png", canvas)
        G_pes = teloButton(125, 477, "mapa_tela/G_pes.png", canvas)

        R_digitus_minimus = teloButton(114, 475, "mapa_tela/R_digitus_minimus.png", canvas)
        G_digitus_minimus = teloButton(114, 475, "mapa_tela/G_digitus_minimus.png", canvas)
        #L dolní končetina

        RR_hip = teloButton(182, 242, "mapa_tela/RR_hip.png", canvas)
        GG_hip = teloButton(182, 242, "mapa_tela/GG_hip.png", canvas)

        RR_upper_thigh = teloButton(170, 266, "mapa_tela/RR_upper_thigh.png", canvas)
        GG_upper_thigh = teloButton(170, 266, "mapa_tela/GG_upper_thigh.png", canvas)

        RR_mid_thigh = teloButton(167, 300, "mapa_tela/RR_mid_thigh.png", canvas)
        GG_mid_thigh = teloButton(167, 300, "mapa_tela/GG_mid_thigh.png", canvas)

        RR_lower_thigh = teloButton(161, 337, "mapa_tela/RR_lower_thigh.png", canvas)
        GG_lower_thigh = teloButton(161, 337, "mapa_tela/GG_lower_thigh.png", canvas)

        RR_gracilis = teloButton(147, 316, "mapa_tela/RR_gracilis.png", canvas)
        GG_gracilis = teloButton(147, 316, "mapa_tela/GG_gracilis.png", canvas)

        RR_genus = teloButton(156, 376, "mapa_tela/RR_genus.png", canvas)
        GG_genus = teloButton(156, 376, "mapa_tela/GG_genus.png", canvas)

        RR_caput_fibulae = teloButton(166, 375, "mapa_tela/RR_caput_fibulae.png", canvas)
        GG_caput_fibulae = teloButton(166, 375, "mapa_tela/GG_caput_fibulae.png", canvas)

        RR_crux_lateralis = teloButton(162, 426, "mapa_tela/RR_crux_lateralis.png", canvas)
        GG_crux_lateralis = teloButton(162, 426, "mapa_tela/GG_crux_lateralis.png", canvas)

        RR_crux_medialis = teloButton(150, 435, "mapa_tela/RR_crux_medialis.png", canvas)
        GG_crux_medialis = teloButton(150, 435, "mapa_tela/GG_crux_medialis.png", canvas)

        RR_pes = teloButton(152, 478, "mapa_tela/RR_pes.png", canvas)
        GG_pes = teloButton(152, 478, "mapa_tela/GG_pes.png", canvas)

        RR_digitus_minimus = teloButton(163, 474, "mapa_tela/RR_digitus_minimus.png", canvas)
        GG_digitus_minimus = teloButton(163, 474, "mapa_tela/GG_digitus_minimus.png", canvas)
        #Pravá paže a ruka
        R_omus = teloButton(79, 115, "mapa_tela/R_omus.png", canvas)
        G_omus = teloButton(79, 115, "mapa_tela/G_omus.png", canvas)

        R_brach_lat = teloButton(78, 157, "mapa_tela/R_brachii_lateralis.png", canvas)
        G_brach_lat = teloButton(78, 157, "mapa_tela/G_brachii_lateralis.png", canvas)

        R_brach_med = teloButton(88, 153, "mapa_tela/R_brachii_medialis.png", canvas)
        G_brach_med = teloButton(88, 153, "mapa_tela/G_brachii_medialis.png", canvas)

        R_ante_lat = teloButton(63, 207, "mapa_tela/R_antebrachii_lateralis.png", canvas)
        G_ante_lat = teloButton(63, 207, "mapa_tela/G_antebrachii_lateralis.png", canvas)

        R_ante_med = teloButton(75, 211, "mapa_tela/R_antebrachii_medialis.png", canvas)
        G_ante_med = teloButton(75, 211, "mapa_tela/G_antebrachii_medialis.png", canvas)

        R_manus_lat = teloButton(38, 274, "mapa_tela/R_manus_lateralis.png", canvas)
        G_manus_lat = teloButton(38, 274, "mapa_tela/G_manus_lateralis.png", canvas)

        R_manus_med = teloButton(53, 274, "mapa_tela/R_manus_medialis.png", canvas)
        G_manus_med = teloButton(53, 274, "mapa_tela/G_manus_medialis.png", canvas)
        #Levá paže a ruka
        RR_omus = teloButton(203, 115, "mapa_tela/RR_omus.png", canvas)
        GG_omus = teloButton(203, 115, "mapa_tela/GG_omus.png", canvas)

        RR_brach_lat = teloButton(204, 157, "mapa_tela/RR_brachii_lateralis.png", canvas)
        GG_brach_lat = teloButton(204, 157, "mapa_tela/GG_brachii_lateralis.png", canvas)

        RR_brach_med = teloButton(193, 154, "mapa_tela/RR_brachii_medialis.png", canvas)
        GG_brach_med = teloButton(193, 154, "mapa_tela/GG_brachii_medialis.png", canvas)

        RR_ante_lat = teloButton(219, 209, "mapa_tela/RR_antebrachii_lateralis.png", canvas)
        GG_ante_lat = teloButton(219, 209, "mapa_tela/GG_antebrachii_lateralis.png", canvas)

        RR_ante_med = teloButton(206, 214, "mapa_tela/RR_antebrachii_medialis.png", canvas)
        GG_ante_med = teloButton(206, 214, "mapa_tela/GG_antebrachii_medialis.png", canvas)

        RR_manus_lat = teloButton(242, 277, "mapa_tela/RR_manus_lateralis.png", canvas)
        GG_manus_lat = teloButton(242, 277, "mapa_tela/GG_manus_lateralis.png", canvas)

        RR_manus_med = teloButton(228, 277, "mapa_tela/RR_manus_medialis.png", canvas)
        GG_manus_med = teloButton(228, 277, "mapa_tela/GG_manus_medialis.png", canvas)




app = window()
app.mainloop()
