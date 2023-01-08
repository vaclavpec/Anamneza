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
        label = tk.Label(self, text = "Kliknutím označte oblast/oblasti na těle, které Vás bolí.")
        label.grid(column=0, row=0)


        canvas = tk.Canvas(self, width = 500, height = 500)
        canvas.grid(column=0, row=1)

        btn_bolest = tk.Menubutton(self, height=1, width=10, text="Bolest ", relief="raised")
        btn_bolest.grid(column=1, row=1)
        bolest_menu = tk.Menu(btn_bolest, tearoff=0)
        btn_bolest["menu"] = bolest_menu



        # hlava
        var_R_scalp = tk.IntVar()
        var_G_scalp = tk.IntVar()
        var_RR_scalp = tk.IntVar()
        var_GG_scalp = tk.IntVar()
        var_R_orbit = tk.IntVar()
        var_G_orbit = tk.IntVar()
        var_RR_orbita = tk.IntVar()
        var_GG_orbita = tk.IntVar()
        var_R_maxilla = tk.IntVar()
        var_G_maxilla = tk.IntVar()
        var_RR_maxilla = tk.IntVar()
        var_GG_maxilla = tk.IntVar()
        var_R_mandibula = tk.IntVar()
        var_G_mandibula = tk.IntVar()
        var_RR_mandibula = tk.IntVar()
        var_GG_mandibula = tk.IntVar()

        # Trup vpravo
        var_R_trapez = tk.IntVar()
        var_G_trapez = tk.IntVar()
        var_R_clavicle = tk.IntVar()
        var_G_clavicle = tk.IntVar()
        var_R_upper_pec = tk.IntVar()
        var_G_upper_pec = tk.IntVar()
        var_R_lower_pec = tk.IntVar()
        var_G_lower_pec = tk.IntVar()
        var_R_thorax = tk.IntVar()
        var_G_thorax = tk.IntVar()
        var_R_epigastrium = tk.IntVar()
        var_G_epigastrium = tk.IntVar()
        var_R_hypogastrium = tk.IntVar()
        var_G_hypogastrium = tk.IntVar()
        var_R_inguina = tk.IntVar()
        var_G_inguina = tk.IntVar()

        # Trup vlevo
        var_RR_trapez = tk.IntVar()
        var_GG_trapez = tk.IntVar()
        var_RR_clavicle = tk.IntVar()
        var_GG_clavicle = tk.IntVar()
        var_RR_upper_pec = tk.IntVar()
        var_GG_upper_pec = tk.IntVar()
        var_RR_lower_pec = tk.IntVar()
        var_GG_lower_pec = tk.IntVar()
        var_RR_thorax = tk.IntVar()
        var_GG_thorax = tk.IntVar()
        var_RR_epigastrium = tk.IntVar()
        var_GG_epigastrium = tk.IntVar()
        var_RR_hypogastrium = tk.IntVar()
        var_GG_hypogastrium = tk.IntVar()
        var_RR_inguina = tk.IntVar()
        var_GG_inguina = tk.IntVar()

        # Trup ve středu
        var_R_sternum = tk.IntVar()
        var_G_sternum = tk.IntVar()
        var_R_manubrium = tk.IntVar()
        var_G_manubrium = tk.IntVar()
        var_R_cervix = tk.IntVar()
        var_G_cervix = tk.IntVar()

        # P dolní končetina

        var_R_hip = tk.IntVar()
        var_G_hip = tk.IntVar()
        var_R_upper_thigh = tk.IntVar()
        var_G_upper_thigh = tk.IntVar()
        var_R_mid_thigh = tk.IntVar()
        var_G_mid_thigh = tk.IntVar()
        var_R_lower_thigh = tk.IntVar()
        var_G_lower_thigh = tk.IntVar()
        var_R_gracilis = tk.IntVar()
        var_G_gracilis = tk.IntVar()
        var_R_genus = tk.IntVar()
        var_G_genus = tk.IntVar()
        var_R_caput_fibulae = tk.IntVar()
        var_G_caput_fibulae = tk.IntVar()
        var_R_crux_lateralis = tk.IntVar()
        var_G_crux_lateralis = tk.IntVar()
        var_R_crux_medialis = tk.IntVar()
        var_G_crux_medialis = tk.IntVar()
        var_R_pes = tk.IntVar()
        var_G_pes = tk.IntVar()
        var_R_digitus_minimus = tk.IntVar()
        var_G_digitus_minimus = tk.IntVar()

        # L dolní končetina

        var_RR_hip = tk.IntVar()
        var_GG_hip = tk.IntVar()
        var_RR_upper_thigh = tk.IntVar()
        var_GG_upper_thigh = tk.IntVar()
        var_RR_mid_thigh = tk.IntVar()
        var_GG_mid_thigh = tk.IntVar()
        var_RR_lower_thigh = tk.IntVar()
        var_GG_lower_thigh = tk.IntVar()
        var_RR_gracilis = tk.IntVar()
        var_GG_gracilis = tk.IntVar()
        var_RR_genus = tk.IntVar()
        var_GG_genus = tk.IntVar()
        var_RR_caput_fibulae = tk.IntVar()
        var_GG_caput_fibulae = tk.IntVar()
        var_RR_crux_lateralis = tk.IntVar()
        var_GG_crux_lateralis = tk.IntVar()
        var_RR_crux_medialis = tk.IntVar()
        var_GG_crux_medialis = tk.IntVar()
        var_RR_pes = tk.IntVar()
        var_GG_pes = tk.IntVar()
        var_RR_digitus_minimus = tk.IntVar()
        var_GG_digitus_minimus = tk.IntVar()

        # Pravá paže a ruka
        var_R_omus = tk.IntVar()
        var_G_omus = tk.IntVar()
        var_R_brach_lat = tk.IntVar()
        var_G_brach_lat = tk.IntVar()
        var_R_brach_med = tk.IntVar()
        var_G_brach_med = tk.IntVar()
        var_R_ante_lat = tk.IntVar()
        var_G_ante_lat = tk.IntVar()
        var_R_ante_med = tk.IntVar()
        var_G_ante_med = tk.IntVar()
        var_R_manus_lat = tk.IntVar()
        var_G_manus_lat = tk.IntVar()
        var_R_manus_med = tk.IntVar()
        var_G_manus_med = tk.IntVar()

        # Levá paže a ruka
        var_RR_omus = tk.IntVar()
        var_GG_omus = tk.IntVar()
        var_RR_brach_lat = tk.IntVar()
        var_GG_brach_lat = tk.IntVar()
        var_RR_brach_med = tk.IntVar()
        var_GG_brach_med = tk.IntVar()
        var_RR_ante_lat = tk.IntVar()
        var_GG_ante_lat = tk.IntVar()
        var_RR_ante_med = tk.IntVar()
        var_GG_ante_med = tk.IntVar()
        var_RR_manus_lat = tk.IntVar()
        var_GG_manus_lat = tk.IntVar()
        var_RR_manus_med = tk.IntVar()
        var_GG_manus_med = tk.IntVar()

        seznamVar = [var_R_scalp, var_G_scalp, var_RR_scalp, var_GG_scalp, var_R_orbit, var_G_orbit, var_RR_orbita, var_GG_orbita, var_R_maxilla, var_G_maxilla, var_RR_maxilla, var_GG_maxilla, var_R_mandibula, var_G_mandibula, var_RR_mandibula, var_GG_mandibula, var_R_trapez, var_G_trapez, var_R_clavicle, var_G_clavicle, var_R_upper_pec, var_G_upper_pec, var_R_lower_pec, var_G_lower_pec, var_R_thorax, var_G_thorax, var_R_epigastrium, var_G_epigastrium, var_R_hypogastrium, var_G_hypogastrium, var_R_inguina, var_G_inguina, var_RR_trapez, var_GG_trapez, var_RR_clavicle, var_GG_clavicle, var_RR_upper_pec, var_GG_upper_pec, var_RR_lower_pec, var_GG_lower_pec, var_RR_thorax, var_GG_thorax, var_RR_epigastrium, var_GG_epigastrium, var_RR_hypogastrium, var_GG_hypogastrium, var_RR_inguina, var_GG_inguina, var_R_sternum, var_G_sternum, var_R_manubrium, var_G_manubrium, var_R_cervix, var_G_cervix, var_R_hip, var_G_hip, var_R_upper_thigh, var_G_upper_thigh, var_R_mid_thigh, var_G_mid_thigh, var_R_lower_thigh, var_G_lower_thigh, var_R_gracilis, var_G_gracilis, var_R_genus, var_G_genus, var_R_caput_fibulae, var_G_caput_fibulae, var_R_crux_lateralis, var_G_crux_lateralis, var_R_crux_medialis, var_G_crux_medialis, var_R_pes, var_G_pes, var_R_digitus_minimus, var_G_digitus_minimus, var_RR_hip, var_GG_hip, var_RR_upper_thigh, var_GG_upper_thigh, var_RR_mid_thigh, var_GG_mid_thigh, var_RR_lower_thigh, var_GG_lower_thigh, var_RR_gracilis, var_GG_gracilis, var_RR_genus, var_GG_genus, var_RR_caput_fibulae, var_GG_caput_fibulae, var_RR_crux_lateralis, var_GG_crux_lateralis, var_RR_crux_medialis, var_GG_crux_medialis, var_RR_pes, var_GG_pes, var_RR_digitus_minimus, var_GG_digitus_minimus, var_R_omus, var_G_omus, var_R_brach_lat, var_G_brach_lat, var_R_brach_med, var_G_brach_med, var_R_ante_lat, var_G_ante_lat, var_R_ante_med, var_G_ante_med, var_R_manus_lat, var_G_manus_lat, var_R_manus_med, var_G_manus_med, var_RR_omus, var_GG_omus, var_RR_brach_lat, var_GG_brach_lat, var_RR_brach_med, var_GG_brach_med, var_RR_ante_lat, var_GG_ante_lat, var_RR_ante_med, var_GG_ante_med, var_RR_manus_lat, var_GG_manus_lat, var_RR_manus_med, var_GG_manus_med]


        # hlava
        btn_R_scalp =bolest_menu.add_checkbutton(label=str(seznamVar[1]), variable=seznamVar[1], onvalue=1, offvalue=0)
        btn_G_scalp =bolest_menu.add_checkbutton(label=str(seznamVar[2]), variable=seznamVar[2], onvalue=1, offvalue=0)
        btn_RR_scalp =bolest_menu.add_checkbutton(label=str(seznamVar[3]), variable=seznamVar[3], onvalue=1, offvalue=0)
        btn_GG_scalp = bolest_menu.add_checkbutton(label=str(seznamVar[4]), variable=seznamVar[4], onvalue=1, offvalue=0)
        btn_R_orbit =bolest_menu.add_checkbutton(label=str(seznamVar[5]), variable=seznamVar[5], onvalue=1, offvalue=0)
        btn_G_orbit =bolest_menu.add_checkbutton(label=str(seznamVar[6]), variable=seznamVar[6], onvalue=1, offvalue=0)
        btn_RR_orbita =bolest_menu.add_checkbutton(label=str(seznamVar[7]), variable=seznamVar[7], onvalue=1, offvalue=0)
        btn_GG_orbita =bolest_menu.add_checkbutton(label=str(seznamVar[8]), variable=seznamVar[8], onvalue=1, offvalue=0)
        btn_R_maxilla =bolest_menu.add_checkbutton(label=str(seznamVar[9]), variable=seznamVar[9], onvalue=1, offvalue=0)
        btn_G_maxilla =bolest_menu.add_checkbutton(label=str(seznamVar[10]), variable=seznamVar[10], onvalue=1, offvalue=0)
        btn_RR_maxilla =bolest_menu.add_checkbutton(label=str(seznamVar[11]), variable=seznamVar[11], onvalue=1, offvalue=0)
        btn_GG_maxilla =bolest_menu.add_checkbutton(label=str(seznamVar[12]), variable=seznamVar[12], onvalue=1, offvalue=0)
        btn_R_mandibula =bolest_menu.add_checkbutton(label=str(seznamVar[13]), variable=seznamVar[13], onvalue=1, offvalue=0)
        btn_G_mandibula =bolest_menu.add_checkbutton(label=str(seznamVar[14]), variable=seznamVar[14], onvalue=1, offvalue=0)
        btn_RR_mandibula =bolest_menu.add_checkbutton(label=str(seznamVar[15]), variable=seznamVar[15], onvalue=1, offvalue=0)
        btn_GG_mandibula =bolest_menu.add_checkbutton(label=str(seznamVar[16]), variable=seznamVar[16], onvalue=1, offvalue=0)

        # Trup vpravo
        btn_R_trapez =bolest_menu.add_checkbutton(label=str(seznamVar[16]), variable=seznamVar[17], onvalue=1, offvalue=0)
        btn_G_trapez =bolest_menu.add_checkbutton(label=str(seznamVar[17]), variable=seznamVar[18], onvalue=1, offvalue=0)
        btn_R_clavicle =bolest_menu.add_checkbutton(label=str(seznamVar[18]), variable=seznamVar[19], onvalue=1, offvalue=0)
        btn_G_clavicle =bolest_menu.add_checkbutton(label=str(seznamVar[19]), variable=seznamVar[20], onvalue=1, offvalue=0)
        btn_R_upper_pec =bolest_menu.add_checkbutton(label=str(seznamVar[20]), variable=seznamVar[21], onvalue=1, offvalue=0)
        btn_G_upper_pec =bolest_menu.add_checkbutton(label=str(seznamVar[21]), variable=seznamVar[22], onvalue=1, offvalue=0)
        btn_R_lower_pec =bolest_menu.add_checkbutton(label=str(seznamVar[22]), variable=seznamVar[23], onvalue=1, offvalue=0)
        btn_G_lower_pec =bolest_menu.add_checkbutton(label=str(seznamVar[23]), variable=seznamVar[24], onvalue=1, offvalue=0)
        btn_R_thorax =bolest_menu.add_checkbutton(label=str(seznamVar[24]), variable=seznamVar[25], onvalue=1, offvalue=0)
        btn_G_thorax =bolest_menu.add_checkbutton(label=str(seznamVar[25]), variable=seznamVar[26], onvalue=1, offvalue=0)
        btn_G_epigastrium =bolest_menu.add_checkbutton(label=str(seznamVar[26]), variable=seznamVar[27], onvalue=1, offvalue=0)
        btn_R_epigastrium =bolest_menu.add_checkbutton(label=str(seznamVar[27]), variable=seznamVar[28], onvalue=1, offvalue=0)
        btn_R_hypogastrium =bolest_menu.add_checkbutton(label=str(seznamVar[28]), variable=seznamVar[29], onvalue=1, offvalue=0)
        btn_G_hypogastrium =bolest_menu.add_checkbutton(label=str(seznamVar[29]), variable=seznamVar[30], onvalue=1, offvalue=0)
        btn_R_inguina =bolest_menu.add_checkbutton(label=str(seznamVar[30]), variable=seznamVar[31], onvalue=1, offvalue=0)
        btn_G_inguina =bolest_menu.add_checkbutton(label=str(seznamVar[31]), variable=seznamVar[32], onvalue=1, offvalue=0)

        # Trup vlevo
        btn_RR_trapez =bolest_menu.add_checkbutton(label=str(seznamVar[32]), variable=seznamVar[33], onvalue=1, offvalue=0)
        btn_GG_trapez =bolest_menu.add_checkbutton(label=str(seznamVar[33]), variable=seznamVar[34], onvalue=1, offvalue=0)
        btn_RR_clavicle =bolest_menu.add_checkbutton(label=str(seznamVar[34]), variable=seznamVar[35], onvalue=1, offvalue=0)
        btn_GG_clavicle =bolest_menu.add_checkbutton(label=str(seznamVar[35]), variable=seznamVar[36], onvalue=1, offvalue=0)
        btn_RR_upper_pec =bolest_menu.add_checkbutton(label=str(seznamVar[36]), variable=seznamVar[37], onvalue=1, offvalue=0)
        btn_GG_upper_pec =bolest_menu.add_checkbutton(label=str(seznamVar[37]), variable=seznamVar[38], onvalue=1, offvalue=0)
        btn_RR_lower_pec =bolest_menu.add_checkbutton(label=str(seznamVar[38]), variable=seznamVar[39], onvalue=1, offvalue=0)
        btn_GG_lower_pec =bolest_menu.add_checkbutton(label=str(seznamVar[39]), variable=seznamVar[40], onvalue=1, offvalue=0)
        btn_RR_thorax =bolest_menu.add_checkbutton(label=str(seznamVar[40]), variable=seznamVar[41], onvalue=1, offvalue=0)
        btn_GG_thorax =bolest_menu.add_checkbutton(label=str(seznamVar[41]), variable=seznamVar[42], onvalue=1, offvalue=0)
        btn_RR_epigastrium =bolest_menu.add_checkbutton(label=str(seznamVar[42]), variable=seznamVar[43], onvalue=1, offvalue=0)
        btn_GG_epigastrium =bolest_menu.add_checkbutton(label=str(seznamVar[43]), variable=seznamVar[44], onvalue=1, offvalue=0)
        btn_RR_hypogastrium =bolest_menu.add_checkbutton(label=str(seznamVar[44]), variable=seznamVar[45], onvalue=1, offvalue=0)
        btn_GG_hypogastrium =bolest_menu.add_checkbutton(label=str(seznamVar[45]), variable=seznamVar[46], onvalue=1, offvalue=0)
        btn_RR_inguina =bolest_menu.add_checkbutton(label=str(seznamVar[46]), variable=seznamVar[47], onvalue=1, offvalue=0)
        btn_GG_inguina =bolest_menu.add_checkbutton(label=str(seznamVar[47]), variable=seznamVar[48], onvalue=1, offvalue=0)

        # Trup ve středu
        btn_R_sternum =bolest_menu.add_checkbutton(label=str(seznamVar[48]), variable=seznamVar[49], onvalue=1, offvalue=0)
        btn_G_sternum =bolest_menu.add_checkbutton(label=str(seznamVar[49]), variable=seznamVar[50], onvalue=1, offvalue=0)
        btn_R_manubrium =bolest_menu.add_checkbutton(label=str(seznamVar[50]), variable=seznamVar[51], onvalue=1, offvalue=0)
        btn_G_manubrium =bolest_menu.add_checkbutton(label=str(seznamVar[51]), variable=seznamVar[52], onvalue=1, offvalue=0)
        btn_R_cervix =bolest_menu.add_checkbutton(label=str(seznamVar[52]), variable=seznamVar[53], onvalue=1, offvalue=0)
        btn_G_cervix =bolest_menu.add_checkbutton(label=str(seznamVar[53]), variable=seznamVar[54], onvalue=1, offvalue=0)

        # P dolní končetina

        btn_G_hip =bolest_menu.add_checkbutton(label=str(seznamVar[54]), variable=seznamVar[55], onvalue=1, offvalue=0)
        btn_R_hip =bolest_menu.add_checkbutton(label=str(seznamVar[55]), variable=seznamVar[56], onvalue=1, offvalue=0)
        btn_R_upper_thigh =bolest_menu.add_checkbutton(label=str(seznamVar[56]), variable=seznamVar[57], onvalue=1, offvalue=0)
        btn_G_upper_thigh =bolest_menu.add_checkbutton(label=str(seznamVar[57]), variable=seznamVar[58], onvalue=1, offvalue=0)
        btn_R_mid_thigh =bolest_menu.add_checkbutton(label=str(seznamVar[58]), variable=seznamVar[59], onvalue=1, offvalue=0)
        btn_G_mid_thigh =bolest_menu.add_checkbutton(label=str(seznamVar[59]), variable=seznamVar[60], onvalue=1, offvalue=0)
        btn_R_lower_thigh =bolest_menu.add_checkbutton(label=str(seznamVar[60]), variable=seznamVar[61], onvalue=1, offvalue=0)
        btn_G_lower_thigh =bolest_menu.add_checkbutton(label=str(seznamVar[61]), variable=seznamVar[62], onvalue=1, offvalue=0)
        btn_R_gracilis =bolest_menu.add_checkbutton(label=str(seznamVar[62]), variable=seznamVar[63], onvalue=1, offvalue=0)
        btn_G_gracilis =bolest_menu.add_checkbutton(label=str(seznamVar[63]), variable=seznamVar[64], onvalue=1, offvalue=0)
        btn_R_genus =bolest_menu.add_checkbutton(label=str(seznamVar[64]), variable=seznamVar[65], onvalue=1, offvalue=0)
        btn_G_genus =bolest_menu.add_checkbutton(label=str(seznamVar[65]), variable=seznamVar[66], onvalue=1, offvalue=0)
        btn_R_caput_fibulae =bolest_menu.add_checkbutton(label=str(seznamVar[66]), variable=seznamVar[67], onvalue=1, offvalue=0)
        btn_G_caput_fibulae =bolest_menu.add_checkbutton(label=str(seznamVar[67]), variable=seznamVar[68], onvalue=1, offvalue=0)
        btn_R_crux_lateralis =bolest_menu.add_checkbutton(label=str(seznamVar[68]), variable=seznamVar[69], onvalue=1, offvalue=0)
        btn_G_crux_lateralis =bolest_menu.add_checkbutton(label=str(seznamVar[69]), variable=seznamVar[70], onvalue=1, offvalue=0)
        btn_R_crux_medialis =bolest_menu.add_checkbutton(label=str(seznamVar[70]), variable=seznamVar[71], onvalue=1, offvalue=0)
        btn_G_crux_medialis =bolest_menu.add_checkbutton(label=str(seznamVar[71]), variable=seznamVar[72], onvalue=1, offvalue=0)
        btn_R_pes =bolest_menu.add_checkbutton(label=str(seznamVar[72]), variable=seznamVar[73], onvalue=1, offvalue=0)
        btn_G_pes =bolest_menu.add_checkbutton(label=str(seznamVar[73]), variable=seznamVar[74], onvalue=1, offvalue=0)
        btn_R_digitus_minimus =bolest_menu.add_checkbutton(label=str(seznamVar[74]), variable=seznamVar[75], onvalue=1, offvalue=0)
        btn_G_digitus_minimus =bolest_menu.add_checkbutton(label=str(seznamVar[75]), variable=seznamVar[76], onvalue=1, offvalue=0)

        # L dolní končetina

        btn_RR_hip =bolest_menu.add_checkbutton(label=str(seznamVar[76]), variable=seznamVar[77], onvalue=1, offvalue=0)
        btn_GG_hip =bolest_menu.add_checkbutton(label=str(seznamVar[77]), variable=seznamVar[78], onvalue=1, offvalue=0)
        btn_RR_upper_thigh =bolest_menu.add_checkbutton(label=str(seznamVar[78]), variable=seznamVar[79], onvalue=1, offvalue=0)
        btn_GG_upper_thigh =bolest_menu.add_checkbutton(label=str(seznamVar[79]), variable=seznamVar[80], onvalue=1, offvalue=0)
        btn_RR_mid_thigh =bolest_menu.add_checkbutton(label=str(seznamVar[80]), variable=seznamVar[81], onvalue=1, offvalue=0)
        btn_GG_mid_thigh =bolest_menu.add_checkbutton(label=str(seznamVar[81]), variable=seznamVar[82], onvalue=1, offvalue=0)
        btn_RR_lower_thigh =bolest_menu.add_checkbutton(label=str(seznamVar[82]), variable=seznamVar[83], onvalue=1, offvalue=0)
        btn_GG_lower_thigh =bolest_menu.add_checkbutton(label=str(seznamVar[83]), variable=seznamVar[84], onvalue=1, offvalue=0)
        btn_RR_gracilis =bolest_menu.add_checkbutton(label=str(seznamVar[84]), variable=seznamVar[85], onvalue=1, offvalue=0)
        btn_GG_gracilis =bolest_menu.add_checkbutton(label=str(seznamVar[85]), variable=seznamVar[86], onvalue=1, offvalue=0)
        btn_RR_genus =bolest_menu.add_checkbutton(label=str(seznamVar[86]), variable=seznamVar[87], onvalue=1, offvalue=0)
        btn_GG_genus =bolest_menu.add_checkbutton(label=str(seznamVar[87]), variable=seznamVar[88], onvalue=1, offvalue=0)
        btn_RR_caput_fibulae =bolest_menu.add_checkbutton(label=str(seznamVar[88]), variable=seznamVar[89], onvalue=1, offvalue=0)
        btn_GG_caput_fibulae =bolest_menu.add_checkbutton(label=str(seznamVar[89]), variable=seznamVar[90], onvalue=1, offvalue=0)
        btn_RR_crux_lateralis =bolest_menu.add_checkbutton(label=str(seznamVar[90]), variable=seznamVar[91], onvalue=1, offvalue=0)
        btn_GG_crux_lateralis =bolest_menu.add_checkbutton(label=str(seznamVar[91]), variable=seznamVar[92], onvalue=1, offvalue=0)
        btn_RR_crux_medialis =bolest_menu.add_checkbutton(label=str(seznamVar[92]), variable=seznamVar[93], onvalue=1, offvalue=0)
        btn_GG_crux_medialis =bolest_menu.add_checkbutton(label=str(seznamVar[93]), variable=seznamVar[94], onvalue=1, offvalue=0)
        btn_RR_pes =bolest_menu.add_checkbutton(label=str(seznamVar[94]), variable=seznamVar[95], onvalue=1, offvalue=0)
        btn_GG_pes =bolest_menu.add_checkbutton(label=str(seznamVar[95]), variable=seznamVar[96], onvalue=1, offvalue=0)
        btn_RR_digitus_minimus =bolest_menu.add_checkbutton(label=str(seznamVar[96]), variable=seznamVar[97], onvalue=1, offvalue=0)
        btn_GG_digitus_minimus =bolest_menu.add_checkbutton(label=str(seznamVar[97]), variable=seznamVar[98], onvalue=1, offvalue=0)

        # Pravá paže a ruka
        btn_R_omus =bolest_menu.add_checkbutton(label=str(seznamVar[98]), variable=seznamVar[99], onvalue=1, offvalue=0)
        btn_G_omus =bolest_menu.add_checkbutton(label=str(seznamVar[99]), variable=seznamVar[100], onvalue=1, offvalue=0)
        btn_R_brach_lat =bolest_menu.add_checkbutton(label=str(seznamVar[100]), variable=seznamVar[101], onvalue=1, offvalue=0)
        btn_G_brach_lat =bolest_menu.add_checkbutton(label=str(seznamVar[101]), variable=seznamVar[102], onvalue=1, offvalue=0)
        btn_R_brach_med =bolest_menu.add_checkbutton(label=str(seznamVar[102]), variable=seznamVar[103], onvalue=1, offvalue=0)
        btn_G_brach_med =bolest_menu.add_checkbutton(label=str(seznamVar[103]), variable=seznamVar[104], onvalue=1, offvalue=0)
        btn_R_ante_lat =bolest_menu.add_checkbutton(label=str(seznamVar[104]), variable=seznamVar[105], onvalue=1, offvalue=0)
        btn_G_ante_lat =bolest_menu.add_checkbutton(label=str(seznamVar[105]), variable=seznamVar[106], onvalue=1, offvalue=0)
        btn_R_ante_med =bolest_menu.add_checkbutton(label=str(seznamVar[106]), variable=seznamVar[107], onvalue=1, offvalue=0)
        btn_G_ante_med =bolest_menu.add_checkbutton(label=str(seznamVar[107]), variable=seznamVar[108], onvalue=1, offvalue=0)
        btn_R_manus_lat =bolest_menu.add_checkbutton(label=str(seznamVar[108]), variable=seznamVar[109], onvalue=1, offvalue=0)
        btn_G_manus_lat =bolest_menu.add_checkbutton(label=str(seznamVar[109]), variable=seznamVar[110], onvalue=1, offvalue=0)
        btn_R_manus_med =bolest_menu.add_checkbutton(label=str(seznamVar[110]), variable=seznamVar[111], onvalue=1, offvalue=0)
        btn_G_manus_med =bolest_menu.add_checkbutton(label=str(seznamVar[111]), variable=seznamVar[112], onvalue=1, offvalue=0)

        # Levá paže a ruka
        btn_RR_omus =bolest_menu.add_checkbutton(label=str(seznamVar[112]), variable=seznamVar[113], onvalue=1, offvalue=0)
        btn_GG_omus =bolest_menu.add_checkbutton(label=str(seznamVar[113]), variable=seznamVar[114], onvalue=1, offvalue=0)
        btn_RR_brach_lat =bolest_menu.add_checkbutton(label=str(seznamVar[114]), variable=seznamVar[115], onvalue=1, offvalue=0)
        btn_GG_brach_lat =bolest_menu.add_checkbutton(label=str(seznamVar[115]), variable=seznamVar[116], onvalue=1, offvalue=0)
        btn_RR_brach_med =bolest_menu.add_checkbutton(label=str(seznamVar[116]), variable=seznamVar[117], onvalue=1, offvalue=0)
        btn_GG_brach_med =bolest_menu.add_checkbutton(label=str(seznamVar[117]), variable=seznamVar[118], onvalue=1, offvalue=0)
        btn_RR_ante_lat =bolest_menu.add_checkbutton(label=str(seznamVar[118]), variable=seznamVar[119], onvalue=1, offvalue=0)
        btn_GG_ante_lat =bolest_menu.add_checkbutton(label=str(seznamVar[119]), variable=seznamVar[120], onvalue=1, offvalue=0)
        btn_RR_ante_med =bolest_menu.add_checkbutton(label=str(seznamVar[120]), variable=seznamVar[121], onvalue=1, offvalue=0)
        btn_GG_ante_med =bolest_menu.add_checkbutton(label=str(seznamVar[121]), variable=seznamVar[122], onvalue=1, offvalue=0)
        btn_RR_manus_lat =bolest_menu.add_checkbutton(label=str(seznamVar[122]), variable=seznamVar[123], onvalue=1, offvalue=0)
        btn_GG_manus_lat =bolest_menu.add_checkbutton(label=str(seznamVar[123]), variable=seznamVar[124], onvalue=1, offvalue=0)
        btn_RR_manus_med = bolest_menu.add_checkbutton(label=str(seznamVar[124]), variable=seznamVar[125], onvalue=1, offvalue=0)
        btn_GG_manus_med = bolest_menu.add_checkbutton(label=str(seznamVar[125]), variable=seznamVar[125], onvalue=1, offvalue=0)






        DKK = tk.IntVar(self)
        HKK = tk.IntVar(self)

        bolest_menu.add_checkbutton(label="DK", variable=DKK, onvalue=1, offvalue=0)
        bolest_menu.add_checkbutton(label="HK", variable=HKK, onvalue=1, offvalue=0)


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
                    bolest_menu.invoke(self.boxnumber)




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
