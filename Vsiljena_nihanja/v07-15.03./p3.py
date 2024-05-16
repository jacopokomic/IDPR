import manim as man

class VsiljenaNihanja(man.Scene):
    def construct(self):

# ---------------------------------------------------------------------------------------------- elementi
        
        self.naslov = man.Tex("Vsiljena nihanja")

        self.masa = man.RoundedRectangle(
            color = man.GRAY,
            fill_color = man.GRAY,
            fill_opacity = 0.5,
            height = 1,
            width = 2,
            corner_radius = 0.2,
            )
        
        self.m = man.MathTex("m").shift(man.DOWN*0.2 + man.RIGHT*0.6)
        
        self.pod00 = man.Rectangle(
            stroke_opacity = 0,
            fill_color = "#995c00",
            fill_opacity = 0.8,
            height = 1,
            width = 15,
            ).shift(man.DOWN*3.5)
        
        self.pod0 = man.Line(
            start = [-7.5, -3, 0],
            end = [7.5, -3, 0],
            )
        
        self.srafura = man.Group()
        i = 0
        xs = -7.75
        xe = -6.75
        while i < 30:
            pod = man.Line(
                start = [xs, -4, 0],
                end = [xe, -3, 0],
                )
            self.srafura.add(pod)
            xs += 0.5
            xe += 0.5
            i += 1
        
        self.podlaga = man.Group(
            self.pod00,
            self.srafura,
            self.pod0,
            )
        
        self.vzmet_spodaj = man.Line(
            start = [-0.5, -3, 0],
            end = [-0.5, -2.5, 0],
            )
        
        self.vz1 = man.Line(
            start = [-0.5, -2.5, 0],
            end = [-0.75, -2.375, 0],
            )
        
        self.vz2 = man.Line(
            start = [-0.75, -2.375, 0],
            end = [-0.25, -2.125, 0],
            )
        
        self.vz3 = man.Line(
            start = [-0.25, -2.125, 0],
            end = [-0.75, -1.875, 0],
            )
        
        self.vz4 = man.Line(
            start = [-0.75, -1.875, 0],
            end = [-0.25, -1.625, 0],
            )
        
        self.vz5 = man.Line(
            start = [-0.25, -1.625, 0],
            end = [-0.75, -1.375, 0],
            )
        
        self.vz6 = man.Line(
            start = [-0.75, -1.375, 0],
            end = [-0.25, -1.125, 0],
            )
        
        self.vz7 = man.Line(
            start = [-0.25, -1.125, 0],
            end = [-0.5, -1, 0],
            )
        
        self.vzmet_zgoraj = man.Line(
            start = [-0.5, -1, 0],
            end = [-0.5, -0.5, 0],
            )
        
        self.vzmet = man.Group(
            self.vzmet_spodaj,
            self.vz1,
            self.vz2,
            self.vz3,
            self.vz4,
            self.vz5,
            self.vz6,
            self.vz7,
            self.vzmet_zgoraj,
            )
        
        self.vr1 = man.Line(
            start = [-0.5, -2.5, 0],
            end = [-0.75, -2.333, 0],
            )
        
        self.vr2 = man.Line(
            start = [-0.75, -2.333, 0],
            end = [-0.25, -2, 0],
            )
        
        self.vr3 = man.Line(
            start = [-0.25, -2, 0],
            end = [-0.75, -1.667, 0],
            )
        
        self.vr4 = man.Line(
            start = [-0.75, -1.667, 0],
            end = [-0.25, -1.333, 0],
            )
        
        self.vr5 = man.Line(
            start = [-0.25, -1.333, 0],
            end = [-0.75, -1, 0],
            )
        
        self.vr6 = man.Line(
            start = [-0.75, -1, 0],
            end = [-0.25, -0.667, 0],
            )
        
        self.vr7 = man.Line(
            start = [-0.25, -0.667, 0],
            end = [-0.5, -0.5, 0],
            )
        
        self.vr_zgoraj = man.Line(
            start = [-0.5, -0.5, 0],
            end = [-0.5, 0, 0],
            )
        
        self.vzmet_raztegnjena = man.Group(
            self.vzmet_spodaj,
            self.vr1,
            self.vr2,
            self.vr3,
            self.vr4,
            self.vr5,
            self.vr6,
            self.vr7,
            self.vr_zgoraj,
            )
        
        self.vs1 = man.Line(
            start = [-0.5, -2.5, 0],
            end = [-0.75, -2.417, 0],
            )
        
        self.vs2 = man.Line(
            start = [-0.75, -2.417, 0],
            end = [-0.25, -2.25, 0],
            )
        
        self.vs3 = man.Line(
            start = [-0.25, -2.25, 0],
            end = [-0.75, -2.083, 0],
            )
        
        self.vs4 = man.Line(
            start = [-0.75, -2.083, 0],
            end = [-0.25, -1.917, 0],
            )
        
        self.vs5 = man.Line(
            start = [-0.25, -1.917, 0],
            end = [-0.75, -1.75, 0],
            )
        
        self.vs6 = man.Line(
            start = [-0.75, -1.75, 0],
            end = [-0.25, -1.583, 0],
            )
        
        self.vs7 = man.Line(
            start = [-0.25, -1.583, 0],
            end = [-0.5, -1.5, 0],
            )
        
        self.vs_zgoraj = man.Line(
            start = [-0.5, -1.5, 0],
            end = [-0.5, -1, 0],
            )
        
        self.vzmet_stisnjena = man.Group(
            self.vzmet_spodaj,
            self.vs1,
            self.vs2,
            self.vs3,
            self.vs4,
            self.vs5,
            self.vs6,
            self.vs7,
            self.vs_zgoraj,
            )
        
        self.k = man.MathTex("k").shift(man.DOWN*1.3 + man.LEFT*1.1)
        
        self.dsp0 = man.Line(
            start = [0.5, -3, 0],
            end = [0.5, -2, 0],
            )
        
        self.dsp1 = man.Line(
            start = [0.24, -2, 0],
            end = [0.76, -2, 0],
            )
        
        self.dsp2 = man.Line(
            start = [0.25, -2, 0],
            end = [0.25, -1.5, 0],
            )
        
        self.dsp3 = man.Line(
            start = [0.75, -2, 0],
            end = [0.75, -1.5, 0],
            )
        
        self.dusilka_spodaj_prej = man.Group(
            self.dsp0,
            self.dsp1,
            self.dsp2,
            self.dsp3,
            )
        
        self.ds0 = man.Line(
            start = [0.5, -3, 0],
            end = [0.5, -2.3, 0],
            )
        
        self.ds1 = man.Line(
            start = [0.24, -2.3, 0],
            end = [0.76, -2.3, 0],
            )
        
        self.ds2 = man.Line(
            start = [0.25, -2.3, 0],
            end = [0.25, -1.2, 0],
            )
        
        self.ds3 = man.Line(
            start = [0.75, -2.3, 0],
            end = [0.75, -1.2, 0],
            )
        
        self.dusilka_spodaj = man.Group(
            self.ds0,
            self.ds1,
            self.ds2,
            self.ds3,
            )
        
        self.dz0 = man.Line(
            start = [0.5, -1.75, 0],
            end = [0.5, -0.5, 0],
            )
        
        self.dz1 = man.Line(
            start = [0.3, -1.75, 0],
            end = [0.7, -1.75, 0],
            )
        
        self.dusilka_zgoraj = man.Group(
            self.dz0,
            self.dz1,
            )
        
        self.dusilka_prej = man.Group(
            self.dusilka_spodaj_prej,
            self.dusilka_zgoraj,
            )
        
        self.d = man.MathTex("d").shift(man.DOWN*2 + man.RIGHT*1.1)
        
        self.vz_01 = man.Line(
            start = [-0.5, -2.5, 0],
            end = [-0.75, -2.375, 0],
            )
        
        self.vz_02 = man.Line(
            start = [-0.75, -2.375, 0],
            end = [-0.25, -2.125, 0],
            )
        
        self.vz_03 = man.Line(
            start = [-0.25, -2.125, 0],
            end = [-0.75, -1.875, 0],
            )
        
        self.vz_04 = man.Line(
            start = [-0.75, -1.875, 0],
            end = [-0.25, -1.625, 0],
            )
        
        self.vz_05 = man.Line(
            start = [-0.25, -1.625, 0],
            end = [-0.75, -1.375, 0],
            )
        
        self.vz_06 = man.Line(
            start = [-0.75, -1.375, 0],
            end = [-0.25, -1.125, 0],
            )
        
        self.vz_07 = man.Line(
            start = [-0.25, -1.125, 0],
            end = [-0.5, -1, 0],
            )
        
        self.vzmet_0_zgoraj = man.Line(
            start = [-0.5, -1, 0],
            end = [-0.5, -0.5, 0],
            )
        
        self.vzmet_0 = man.Group(
            self.vzmet_spodaj,
            self.vz_01,
            self.vz_02,
            self.vz_03,
            self.vz_04,
            self.vz_05,
            self.vz_06,
            self.vz_07,
            self.vzmet_0_zgoraj,
            )

        self.F = man.ValueTracker((1/4) * man.PI)
        
        self.ozadje = man.Rectangle(
            width = 8,
            height = 5,
            color = man.BLACK,
            stroke_opacity = 0,
            fill_opacity = 0,
        )

        self.sila = man.Arrow(
            start = self.masa.get_center(),
            end = [0, self.masa.get_center()[1] + 1.5 * man.np.sin(self.F.get_value()), 0],
            color = man.RED,
            max_tip_length_to_length_ratio = 0.25,
            buff = 0,
        )

        self.sila_help = man.Arrow(
            start = self.masa.get_center(),
            end = [0, self.masa.get_center()[1] + 1.5 * man.np.sin(self.F.get_value()), 0],
            color = man.RED,
            max_tip_length_to_length_ratio = 0.25,
            stroke_width = 4,
            buff = 0,
        )

        self.Ftex = man.MathTex("F", color = man.RED).next_to(self.sila.get_end(), man.LEFT)

        self.motnja = man.Tex("harmonska zunanja motnja").shift(man.UP*3.25)

        self.valovanje = man.TracedPath(self.sila.get_end, stroke_color = man.RED)
        
        def update_sila(sila, dt):
            new_start = self.masa.get_center()
            new_end = [0, self.masa.get_center()[1] + 1.5 * man.np.sin(self.F.get_value()), 0]
            self.sila.put_start_and_end_on(new_start, new_end)

        def update_ozadje(ozadje, dt):
            self.ozadje.shift(0.5 * man.LEFT * dt)

        self.sila.add_updater(update_sila)
        self.ozadje.add_updater(update_ozadje)
        self.ozadje.add(self.valovanje)

        self.visina = man.DashedLine(
            start = [-1, self.masa.get_center()[1], 0],
            end = [-3.25, self.masa.get_center()[1], 0],
            stroke_opacity = 0.2,
        )

        self.razdalja = man.DoubleArrow(
            start = [-3, -3, 0],
            end = [self.visina.get_end()[0] + 0.25, self.visina.get_end()[1], 0],
            buff = 0,
            stroke_width = 2,
            max_tip_length_to_length_ratio = 0.08,
        )

        self.koordinata = man.DoubleArrow(
            start = [-3, self.visina.get_end()[1] - 1, 0],
            end = [-3, self.visina.get_end()[1] + 1, 0],
            buff = 0,
            stroke_width = 2,
            max_tip_length_to_length_ratio = 0.12,
        )

        self.x = man.MathTex("x").shift(man.DOWN*1.5 + man.LEFT*3.25)

        self.plus = man.MathTex("+").shift(man.UP*1 + man.LEFT*2.75).scale(0.5)
        self.minus = man.MathTex("-").shift(man.DOWN*1 + man.LEFT*2.75).scale(0.5)

        self.ks = man.Axes(
            x_range = [-0.25, 1.75],
            y_range = [-2, 2],
            x_length = 2,
            y_length = 4,
            axis_config = {"tip_width": 0.2, "tip_height": 0.2, "include_ticks": False},
        ).shift(man.RIGHT*0.75)

        self.x_label = man.MathTex("t").next_to(self.ks.x_axis.get_end(), man.DOWN)
        self.y_label = man.MathTex("F").next_to(self.ks.y_axis.get_end(), man.LEFT)

        self.ks2 = man.Axes(
            x_range = [-0.25, 3.75],
            y_range = [-2, 2],
            x_length = 4,
            y_length = 4,
            axis_config = {"tip_width": 0.2, "tip_height": 0.2, "include_ticks": False},
        ).shift(man.LEFT*0.25)

        self.x_label2 = man.MathTex("t").next_to(self.ks2.x_axis.get_end(), man.DOWN)
        self.y_label2 = man.MathTex("F").next_to(self.ks2.y_axis.get_end(), man.LEFT)

        self.ks3 = man.Axes(
            x_range = [-0.25, 4.5],
            y_range = [-2, 2],
            x_length = 4.75,
            y_length = 4,
            axis_config = {"tip_width": 0.2, "tip_height": 0.2, "include_ticks": False},
        ).shift(man.LEFT*0.625)

        self.x_label3 = man.MathTex("t").next_to(self.ks3.x_axis.get_end(), man.DOWN)
        self.y_label3 = man.MathTex("F").next_to(self.ks3.y_axis.get_end(), man.LEFT)

        self.ozadje.add(self.ks, self.x_label, self.y_label)

        self.ref = man.NumberLine(
            x_range = [0, 2],
            length = 2,
            include_ticks = False,
            include_tip = True,
            tip_width = 0.2,
            tip_height = 0.2,
        ).shift(man.RIGHT*5)

        self.referenca = man.Tex("referenca").next_to(self.ref.get_end(), man.DOWN, buff = 0.15).scale(0.4)

        self.krog = man.Circle(
            radius = 1.5,
            color = man.WHITE,
            stroke_opacity = 0.2,
            ).shift(man.RIGHT*4)
        
        self.kazalec = man.Arrow(
            start = self.krog.get_center(),
            end = [self.krog.get_center()[0] + 1.5 * man.np.cos(self.F.get_value()), self.krog.get_center()[1] + 1.5 * man.np.sin(self.F.get_value()), 0],
            color = man.RED,
            max_tip_length_to_length_ratio = 0.18,
            buff = 0,
        )

        self.kazalec_help = man.Arrow(
            start = self.krog.get_center(),
            end = [self.krog.get_center()[0] + 1.5 * man.np.cos((1/4) * man.PI), self.krog.get_center()[1] + 1.5 * man.np.sin((1/4) * man.PI), 0],
            color = man.RED,
            max_tip_length_to_length_ratio = 0.18,
            buff = 0,
        )

        self.povezava = man.DashedLine(
            start = self.sila.get_end(),
            end = self.kazalec.get_end(),
            stroke_opacity = 0.2,
        )

        self.povezava_help = man.DashedLine(
            start = self.sila.get_end(),
            end = self.kazalec.get_end(),
            stroke_opacity = 0.2,
        )

        def update_kazalec(kazalec, dt):
            new_start_kazalec = self.krog.get_center()
            new_end_kazalec = [self.krog.get_center()[0] + 1.5 * man.np.cos(self.F.get_value()), self.krog.get_center()[1] + 1.5 * man.np.sin(self.F.get_value()), 0]
            self.kazalec.put_start_and_end_on(new_start_kazalec, new_end_kazalec)

        self.kazalec.add_updater(update_kazalec)

        def update_povezava(povezava, dt):
            new_start_povezava = self.sila.get_end()
            new_end_povezava = self.kazalec.get_end()
            self.povezava.put_start_and_end_on(new_start_povezava, new_end_povezava)

        self.povezava.add_updater(update_povezava)

        self.majhen_kot = man.Arc(
            radius = 0.5,
            arc_center = self.krog.get_center(),
            start_angle = 0,
            angle = (1/4) * man.PI,
        )

        self.majhen_kot2 = man.Arc(
            radius = 0.5,
            arc_center = self.krog.get_center(),
            start_angle = 0,
            angle = (1/4) * man.PI,
        )

        self.velik_kot = man.Arc(
            radius = 0.5,
            arc_center = self.krog.get_center(),
            start_angle = 0,
            angle = (3/4) * man.PI,
        )

        self.drugi_kot = man.Arc(
            radius = 0.5,
            arc_center = self.krog.get_center(),
            start_angle = (3/4) * man.PI,
            angle = (5/4) * man.PI,
        )

        self.cel_kot = man.Arc(
            radius = 0.5,
            arc_center = self.krog.get_center(),
            start_angle = 0,
            angle = 2 * man.PI,
        )

        self.Ft = man.MathTex("F(t)", color = man.RED).move_to([-1.5, 2.5, 0])
        self.enacaj = man.MathTex("=").next_to(self.Ft, man.RIGHT)

        self.kopija = self.kazalec.copy()

        self.F0 = man.MathTex("F_0").next_to(self.enacaj, man.RIGHT)
        self.F0tex1 =  man.MathTex("F_0", color = man.RED).next_to(self.kazalec.get_end(), man.UP + man.RIGHT, buff = 0.1)
        self.F0tex2 =  man.MathTex("F_0", color = man.RED)

        self.sinus = man.Tex("sin").next_to(self.F0, man.RIGHT)
        self.omega_t = man.MathTex("(\\omega t)").next_to(self.sinus, man.RIGHT, buff = 0.1)
        self.omega_t2 = man.MathTex("\\omega t").move_to(self.omega_t.get_center())
        self.phitex = man.MathTex("\\varphi").move_to([4.75, 0.25, 0])

        self.kotna_hitrost_linija = man.Arc(
            radius = 0.5,
            arc_center = self.krog.get_center(),
            start_angle = (3/4) * man.PI,
            angle = (3/4) * man.PI,
        )

        self.kotna_hitrost_tip = man.Arrow(
            start = [3, -0.5, 0],
            end = [self.kotna_hitrost_linija.get_end()[0] + 0.15, self.kotna_hitrost_linija.get_end()[1], 0],
            stroke_width = 0,
            max_tip_length_to_length_ratio = 0.18,
            buff = 0,
        )

        self.kotna_hitrost = man.Group(
            self.kotna_hitrost_linija,
            self.kotna_hitrost_tip,
        )

        self.omegatex = man.MathTex("\\omega").next_to(self.kotna_hitrost_tip.get_end(), man.RIGHT, buff = 0.1)

        self.povezava2 = man.DashedLine(
            start = [-3.5, 1.5 * man.np.sin((3/4) * man.PI), 0],
            end = [-3.5, 1.5 * man.np.sin((3/4) * man.PI) - 3, 0],
            stroke_opacity = 0.2,
        )

        self.cas = man.DoubleArrow(
            start = [-6.25, 1.5 * man.np.sin((3/4) * man.PI) - 2.75, 0],
            end = [-3.5, 1.5 * man.np.sin((3/4) * man.PI) - 2.75, 0],
            buff = 0,
            stroke_width = 2,
            max_tip_length_to_length_ratio = 0.08,
        )

        self.ttex = man.MathTex("t").next_to(self.cas.get_center(), man.DOWN, buff = 0.1)

        self.kazalec2 = man.Arrow(
            start = self.krog.get_center(),
            end = [self.krog.get_center()[0] + 1.5 * man.np.cos((1/4) * man.PI), self.krog.get_center()[1] + 1.5 * man.np.sin((1/4) * man.PI), 0],
            color = man.BLUE,
            max_tip_length_to_length_ratio = 0.18,
            buff = 0,
        )

        self.smer_sin = man.DashedLine(
            start = self.kazalec.get_end(),
            end = self.kazalec.get_end() + [1, 1, 0],
            stroke_opacity = 0.2,
        )

        self.sin_omega_t = man.MathTex("\\mathrm{sin}(\\omega t)").scale(0.5).rotate((1/4) * man.PI).move_to([5.5, 1.75, 0])

        self.sila_vzmeti = man.Arrow(
            start = [self.vzmet_zgoraj.get_end()[0], 0, 0],
            end = [self.vzmet_zgoraj.get_end()[0], -1, 0],
            color = man.RED,
            max_tip_length_to_length_ratio = 0.25,
            buff = 0,
        )

        self.sila_dusilke = man.Arrow(
            start = [self.dz0.get_end()[0], 0, 0],
            end = [self.dz0.get_end()[0], -1, 0],
            color = man.RED,
            max_tip_length_to_length_ratio = 0.25,
            buff = 0,
        )

        self.gor = man.Group(
            self.masa,
            self.m,
            self.sila,
            self.vzmet_zgoraj,
            self.dusilka_zgoraj,
        )

        self.Fv = man.MathTex("F_v", color = man.RED).next_to(self.sila_vzmeti.get_end() + [-0.75, -0.25, 0])
        self.Fd = man.MathTex("F_d", color = man.RED).next_to(self.sila_dusilke.get_end() + [0, 0.25, 0])

        self.IINZ = man.Tex("II. Newtonov zakon").move_to([4, 1, 0])
        self.vsota_sil = man.MathTex("\\sum F").move_to([3.25, 0, 0])
        self.enacaj3 = man.MathTex("=").next_to(self.vsota_sil, man.RIGHT)
        self.m2 = man.MathTex("m").next_to(self.enacaj3, man.RIGHT)
        self.a = man.MathTex("a").next_to(self.m2, man.RIGHT, buff = 0.05)
        self.xdd = man.MathTex("\\ddot{x}").move_to(self.a.get_center() + [0, 0.06, 0])

        self.skica = man.Group(
            self.motnja,
            self.masa,
            self.m,
            self.sila,
            self.Ft,
            self.enacaj,
            self.F0,
            self.sinus,
            self.omega_t,
            self.sila_vzmeti,
            self.Fv,
            self.sila_dusilke,
            self.Fd,
            self.visina,
            self.koordinata,
            self.x,
            self.plus,
            self.minus,
        )

        self.enacba = man.Group(
            self.IINZ,
            self.vsota_sil,
            self.enacaj3,
            self.m2,
            self.xdd,
        )

        self.mxdd = man.Group(
            self.m2,
            self.xdd,
        )

        self.deljeno_m = man.MathTex(":m").move_to([3.25, -1, 0])

        self.skica2 = man.Group(
            self.masa,
            self.m,
            self.sila,
            self.Ft,
            self.sila_vzmeti,
            self.Fv,
            self.sila_dusilke,
            self.Fd,
            self.visina,
            self.koordinata,
            self.x,
            self.plus,
            self.minus,
            self.podlaga,
        )

        self.res = man.MathTex("x(t) = x_\\mathrm{h} (t) + x_\\mathrm{p} (t)").move_to([0, 2, 0])
        self.resitev = man.Tex("rešitev:").next_to(self.res, man.LEFT)
        self.homogena = man.MathTex("x_\\mathrm{h} (t)").move_to([-0.125, 2, 0])
        self.partikularna = man.MathTex("x_\\mathrm{p} (t)").move_to([1.5, 2, 0])

        self.ref2 = man.NumberLine(
            x_range = [0, 4],
            length = 4,
            include_ticks = False,
            include_tip = True,
            tip_width = 0.2,
            tip_height = 0.2,
        ).move_to([3, -2, 0])

        self.referenca2 = man.Tex("referenca").next_to(self.ref2.get_end(), man.DOWN, buff = 0.15).scale(0.4)

        self.vsiljena_komponenta = man.Arrow(
            start = self.ref2.get_start(),
            end = self.ref2.get_start() + [2.5 * man.np.cos((6/16) * man.PI), 2.5 * man.np.sin((6/16) * man.PI), 0],
            color = man.RED,
            max_stroke_width_to_length_ratio = 3,
            max_tip_length_to_length_ratio = 0.10,
            stroke_width = 5,
            buff = 0,
        )

        self.kot = man.Angle(
            line1 = self.ref2,
            line2 = self.vsiljena_komponenta,
            radius = 0.5,
        )

        self.velikost_kota = man.MathTex("\\omega t").next_to(self.kot.get_end(), man.RIGHT, buff = 0.3)

        self.smer_vsiljene_komponente = man.DashedLine(
            start = self.vsiljena_komponenta.get_end(),
            end = self.vsiljena_komponenta.get_end() + [2 * man.np.cos((6/16) * man.PI), 2 * man.np.sin((6/16) * man.PI), 0],
            stroke_opacity = 0.2,
        )

        self.vpliv_togosti = man.Arrow(
            start = self.ref2.get_start(),
            end = self.ref2.get_start() + [4 * man.np.cos((1/16) * man.PI), 4 * man.np.sin((1/16) * man.PI), 0],
            color = man.BLUE_C,
            max_stroke_width_to_length_ratio = 3,
            max_tip_length_to_length_ratio = 0.0625,
            stroke_width = 5,
            buff = 0,
        )

        self.kot2 = man.Angle(
            line1 = self.vsiljena_komponenta,
            line2 = self.vpliv_togosti,
            radius = 1.25,
            other_angle = True,
        )

        self.velikost_kota2 = man.MathTex("\\varphi_\\mathrm{z}").next_to(self.kot2.get_start(), man.RIGHT, buff = 0.4)

        self.smer_vpliva_togosti = man.DashedLine(
            start = self.vpliv_togosti.get_end(),
            end = self.vpliv_togosti.get_end() + [2 * man.np.cos((1/16) * man.PI), 2 * man.np.sin((1/16) * man.PI), 0],
            stroke_opacity = 0.2,
        )

        self.vpliv_dusenja = man.Arrow(
            start = self.vpliv_togosti.get_end(),
            end = self.vpliv_togosti.get_end() + [-2.0787 * man.np.sin((1/16) * man.PI), 2.0787 * man.np.cos((1/16) * man.PI), 0],
            color = man.BLUE_D,
            max_stroke_width_to_length_ratio = 3,
            max_tip_length_to_length_ratio = 0.1203,
            stroke_width = 5,
            buff = 0,
        )

        self.kot3 = man.Angle(
            line1 = self.vpliv_dusenja,
            line2 = self.vpliv_togosti,
            quadrant = (1, -1),
            elbow = True,
        )

        self.smer_vpliva_dusenja = man.DashedLine(
            start = self.vpliv_dusenja.get_end(),
            end = self.vpliv_dusenja.get_end() + [-2 * man.np.sin((1/16) * man.PI), 2 * man.np.cos((1/16) * man.PI), 0],
            stroke_opacity = 0.2,
        )

        self.vpliv_vztrajnosti = man.Arrow(
            start = self.vpliv_dusenja.get_end(),
            end = self.vpliv_dusenja.get_end() + [-2.6111 * man.np.cos((1/16) * man.PI), -2.6111 * man.np.sin((1/16) * man.PI), 0],
            color = man.BLUE_E,
            max_stroke_width_to_length_ratio = 3,
            max_tip_length_to_length_ratio = 0.0957,
            stroke_width = 5,
            buff = 0,
        )

        self.kot4 = man.Angle(
            line1 = self.vpliv_vztrajnosti,
            line2 = self.vpliv_dusenja,
            quadrant = (1, -1),
            elbow = True,
        )

        self.smer_vpliva_vztrajnosti = man.DashedLine(
            start = self.vpliv_vztrajnosti.get_start(),
            end = self.vpliv_vztrajnosti.get_start() + [2 * man.np.cos((1/16) * man.PI), 2 * man.np.sin((1/16) * man.PI), 0],
            stroke_opacity = 0.2,
        )

        self.pitagora = man.Tex("Pitagorov izrek").move_to([-2.75, 1.5, 0])
        self.f0_kvadrat = man.MathTex("f_0^2").move_to([-6.25, 0.5, 0])
        self.enacaj10 = man.MathTex("=").next_to(self.f0_kvadrat, man.RIGHT)
        self.kateta1 = man.MathTex("(\\omega_0^2 X - \\omega^2 X)^2").next_to(self.enacaj10, man.RIGHT)
        self.plus4 = man.MathTex("+").next_to(self.kateta1, man.RIGHT)
        self.kateta2 = man.MathTex("(2 \\delta \\omega_0 \\omega X)^2").next_to(self.plus4, man.RIGHT)

        self.korak2 = man.MathTex("""
                                  f_0^2
                                  =
                                  (X(\\omega_0^2 - \\omega^2))^2
                                  +
                                  (X(2 \\delta \\omega_0 \\omega))^2
                                  """).move_to([-2.75, 0.5, 0])
        
        self.korak3 = man.MathTex("""
                                  f_0^2
                                  =
                                  X^2 (\\omega_0^2 - \\omega^2)^2
                                  +
                                  X^2 (2 \\delta \\omega_0 \\omega)^2
                                  """).move_to([-2.75, 0.5, 0])
        
        self.korak4 = man.MathTex("""
                                  f_0^2
                                  =
                                  X^2 [(\\omega_0^2 - \\omega^2)^2
                                  +
                                  (2 \\delta \\omega_0 \\omega)^2]
                                  """).move_to([-2.75, 0.5, 0])
        
        self.deljeno_omega0_na_cetrto = man.MathTex(": \\omega_0^4").move_to([-2.75, -1.5, 0])
        
        self.korak5 = man.MathTex("""
                                  \\frac{f_0^2}{\\omega_0^4}
                                  =
                                  X^2 \\left[ \\frac{(\\omega_0^2 - \\omega^2)^2}{\\omega_0^4}
                                  +
                                  \\frac{(2 \\delta \\omega_0 \\omega)^2}{\\omega_0^4} \\right]
                                  """).move_to([-2.75, 0.5, 0])
        
        self.korak6 = man.MathTex("""
                                  \\frac{f_0^2}{\\omega_0^4}
                                  =
                                  X^2 \\left[ \\left( \\frac{\\omega_0^2 - \\omega^2}{\\omega_0^2} \\right)^2
                                  +
                                  \\left( \\frac{2 \\delta \\omega_0 \\omega}{\\omega_0^2} \\right)^2 \\right]
                                  """).move_to([-2.75, 0.5, 0])
        
        self.korak7 = man.MathTex("""
                                  \\frac{f_0^2}{\\omega_0^4}
                                  =
                                  X^2 \\left[ \\left( 1 - \\frac{\\omega^2}{\\omega_0^2} \\right)^2
                                  +
                                  \\left( 2 \\delta \\frac{\\omega}{\\omega_0} \\right)^2 \\right]
                                  """).move_to([-2.75, 0.5, 0])
        
        self.razmernik_frekvenc = man.MathTex("\\frac{\\omega}{\\omega_0} = r").move_to([-2.75, -1.5, 0])

        self.korak8 = man.MathTex("""
                                  \\frac{f_0^2}{\\omega_0^4}
                                  =
                                  X^2 [(1 - r^2)^2
                                  +
                                  (2 \\delta r)^2]
                                  """).move_to([-2.75, 0.5, 0])
        
        self.korak9 = man.MathTex("X^2 = \\frac{f_0^2}{\\omega_0^4} \\frac{1}{(1 - r^2)^2 + (2 \\delta r)^2}").move_to([-2.75, 0.5, 0])
        
        self.koren = man.MathTex("\\sqrt").move_to([-2.75, -1.5, 0])

        self.korak10 = man.MathTex("X = \\frac{f_0}{\\omega_0^2} \\sqrt{\\frac{1}{(1 - r^2)^2 + (2 \\delta r)^2}}").move_to([-2.75, 0.5, 0])

        self.staticni_faktor = man.MathTex("\\frac{f_0}{\\omega_0^2} = X_0").move_to([-2.75, -1.5, 0])
        self.dinamicni_faktor = man.MathTex("\\sqrt{\\frac{1}{(1 - r^2)^2 + (2 \\delta r)^2}} = \\beta").move_to([-2.75, -3, 0])

        self.korak11 = man.MathTex("X = X_0 \\beta").move_to([-2.75, 0.5, 0])

        self.staticni_faktor2 = man.MathTex("X_0 = \\frac{f_0}{\\omega_0^2}").move_to([-3.25, 3, 0]).set_opacity(0.4).scale(0.7)
        self.dinamicni_faktor2 = man.MathTex("\\beta = \\sqrt{\\frac{1}{(1 - r^2)^2 + (2 \\delta r)^2}}").move_to([0, 3, 0]).set_opacity(0.4).scale(0.7)

        self.tangens1 = man.MathTex("""
                                    \\mathrm{tan} (\\varphi_\\mathrm{z}})
                                    =
                                    \\frac{2 \\delta \\omega_0 \\omega X}{\\omega_0^2 X - \\omega^2 X}
                                    """).move_to([-2.75, -0.5, 0])
        
        self.tangens2 = man.MathTex("""
                                    \\mathrm{tan} (\\varphi_\\mathrm{z}})
                                    =
                                    \\frac{2 \\delta \\omega_0 \\omega X}{(\\omega_0^2 - \\omega^2) X}
                                    """).move_to([-2.75, -0.5, 0])
        
        self.ulomek_deljeno_omega0_kvadrat = man.MathTex("\\frac{:\\omega_0^2}{:\\omega_0^2}").move_to([-2.75, -2.5, 0])

        self.tangens3 = man.MathTex("""
                                    \\mathrm{tan} (\\varphi_\\mathrm{z}})
                                    =
                                    \\frac{2 \\delta \\frac{\\omega_0 \\omega}{\\omega_0^2}}{\\frac{\\omega_0^2}{\\omega_0^2} - \\frac{\\omega^2}{\\omega_0^2}}
                                    """).move_to([-2.75, -0.5, 0])
        
        self.razmernik_frekvenc2 = man.MathTex("\\frac{\\omega}{\\omega_0} = r").move_to([-2.75, -2.5, 0])

        self.tangens4 = man.MathTex("""
                                    \\mathrm{tan} (\\varphi_\\mathrm{z}})
                                    =
                                    \\frac{2 \\delta r}{1 - r^2}
                                    """).move_to([-2.75, -0.5, 0])

# ---------------------------------------------------------------------------------------------- prikaz animacij

        self.wait()
        self.play(man.Write(self.naslov))
        self.wait()
        self.play(man.Unwrite(self.naslov))
        self.wait()
        self.play(man.GrowFromCenter(self.masa))
        self.wait()
        self.play(man.Write(self.m))
        self.wait()
        self.play(man.FadeIn(self.podlaga))
        self.wait()
        self.play(man.GrowFromPoint(self.visina, self.visina.get_start()))
        self.play(man.FadeIn(self.razdalja))
        self.play(man.Write(self.x))
        self.wait()
        self.wait()
        self.play(man.Transform(self.razdalja, self.koordinata), self.x.animate.shift(man.UP*1.9))

        self.koordinata = self.razdalja

        self.wait()
        self.play(man.Write(self.plus), man.Write(self.minus))
        self.wait()

        self.vzmet.shift(man.RIGHT*0.5)
        self.k.shift(man.RIGHT*0.5)
        self.dusilka_prej.shift(man.LEFT*0.5)
        self.d.shift(man.LEFT*0.5)

        self.play(man.GrowFromCenter(self.vzmet))
        self.wait()
        self.play(man.Write(self.k))
        self.wait()
        self.play(man.FadeOut(self.vzmet, self.k))

        self.vzmet.shift(man.LEFT*0.5) 
        self.k.shift(man.LEFT*0.5)

        self.play(man.GrowFromCenter(self.dusilka_prej))
        self.wait()
        self.play(man.Write(self.d))
        self.wait()
        self.play(self.dusilka_prej.animate.shift(man.RIGHT*0.5), self.d.animate.shift(man.RIGHT*0.5))
        self.play(man.FadeIn(self.vzmet, self.k))
        self.wait()
        self.play(man.GrowArrow(self.sila_help))
        self.remove(self.sila_help)
        self.add(self.sila)
        self.wait()
        self.play(man.Write(self.Ftex))
        self.wait()
        self.play(man.FadeOut(self.podlaga, self.vzmet, self.k, self.dusilka_prej, self.d, self.visina, self.koordinata, self.x, self.plus, self.minus))
        self.wait()
        self.play(man.Write(self.motnja))
        self.wait()
        self.play(man.Transform(self.Ftex, self.Ft))
        self.play(man.Write(self.enacaj))
        self.play(man.Write(self.F0), man.Write(self.sinus), man.Write(self.omega_t))
        self.wait() 
        self.play(man.Create(self.ref))
        self.play(man.Write(self.referenca))
        self.play(man.Create(self.krog))
        self.play(man.GrowArrow(self.kazalec_help))
        self.play(man.GrowFromEdge(self.povezava_help, self.kazalec_help.get_end()))
        self.play(man.Create(self.majhen_kot))
        self.play(man.Write(self.phitex))
        self.wait()
        self.play(self.phitex.animate.shift(man.DOWN*3 + man.LEFT*1.5))
        self.remove(self.kazalec_help, self.povezava_help)
        self.add(self.kazalec, self.povezava)

        self.enacaj2 = man.MathTex("=").next_to(self.phitex, man.RIGHT)
        self.vrednost = man.DecimalNumber(0, num_decimal_places = 2).next_to(self.enacaj2, man.RIGHT)
        self.vrednost.add_updater(lambda x: x.set_value(self.F.get_value() / man.PI))
        self.pi = man.MathTex("\\pi").next_to(self.vrednost, man.RIGHT)

        self.play(self.F.animate.set_value(0.001), # da ostane obrnjena navzgor
                  man.Uncreate(self.majhen_kot),
                  man.Write(self.enacaj2),
                  run_time = 1, rate_func = man.linear)
        self.play(man.Write(self.vrednost))
        self.play(man.Write(self.pi))
        self.wait()
        self.play(man.Create(self.ks))
        self.play(man.Write(self.y_label))
        self.play(man.Write(self.x_label))
        self.add(self.ozadje, self.valovanje)
        self.play(self.F.animate.set_value((8/4) * man.PI),
                  man.Create(self.cel_kot),
                  man.Transform(self.ks, self.ks2),
                  man.Transform(self.x_label, self.x_label2),
                  man.Transform(self.y_label, self.y_label2),
                  run_time = 4, rate_func = man.linear)
        self.remove(self.cel_kot)
        self.play(self.F.animate.set_value((11/4) * man.PI),
                  man.Create(self.velik_kot),
                  man.Transform(self.ks, self.ks3),
                  man.Transform(self.x_label, self.x_label3),
                  man.Transform(self.y_label, self.y_label3),
                  run_time = 1.5, rate_func = man.linear)
        
        self.valovanje.clear_updaters()
        self.ozadje.clear_updaters()

        self.play(self.ks.animate.shift(man.LEFT*3.5),
                  self.x_label.animate.shift(man.LEFT*3.5),
                  self.y_label.animate.shift(man.LEFT*3.5),
                  self.valovanje.animate.shift(man.LEFT*3.5))
        
        self.vrednost.clear_updaters()

        self.wait()
        self.add(self.omega_t2)
        self.play(man.FadeOut(self.vrednost, self.pi), self.omega_t2.animate.move_to([self.vrednost.get_center()[0] - 0.15, self.vrednost.get_center()[1] + 0.05, 0]))
        self.wait()
        self.play(man.FadeOut(self.velik_kot))
        self.play(self.F.animate.set_value((16/4) * man.PI),
                  man.FadeIn(self.kotna_hitrost),
                  man.Write(self.omegatex),
                  run_time = 2.5, rate_func = man.linear)
        self.play(self.F.animate.set_value((17/4) * man.PI),
                  man.FadeOut(self.kotna_hitrost, self.omegatex),
                  run_time = 0.5, rate_func = man.linear)
        self.wait()
        self.play(man.GrowFromPoint(self.povezava2, self.povezava2.get_start()))
        self.play(man.FadeIn(self.cas))
        self.play(man.Write(self.ttex))
        self.wait()
        self.play(man.FadeOut(self.povezava2, self.cas, self.ttex))
        self.wait()

        self.povezava.clear_updaters()
        self.sila.clear_updaters()
        self.valovanje2 = self.valovanje.copy().set_color(man.BLUE)

        self.play(man.Create(self.majhen_kot2), man.FadeOut(self.phitex, self.enacaj2, self.povezava), self.omega_t2.animate.move_to([4.85, 0.3, 0]))
        self.wait()
        self.play(man.GrowFromPoint(self.smer_sin, self.kazalec.get_end()))
        self.play(man.Write(self.sin_omega_t))
        self.wait()
        self.play(man.GrowArrow(self.kazalec2), man.Create(self.valovanje2))
        self.wait()
        self.play(man.Rotate(self.kazalec2, angle = (2/4) * man.PI, about_point = self.kazalec2.get_start()),
                  self.valovanje2.animate.shift(man.LEFT*0.5),
                  run_time = 2, rate_func = man.linear)
        self.wait()

        self.pravi_kot = man.Angle(
            line1 = self.kazalec,
            line2 = self.kazalec2,
            elbow = True,
        )

        self.smer_cos = man.DashedLine(
            start = self.kazalec2.get_end(),
            end = self.kazalec2.get_end() + [-1, 1, 0],
            stroke_opacity = 0.2,
        )

        self.cos_omega_t = man.MathTex("\\mathrm{cos}(\\omega t)").scale(0.5).rotate(-(1/4) * man.PI).move_to([2.5, 1.75, 0])

        self.play(man.GrowFromPoint(self.smer_cos, self.kazalec2.get_end()), man.Create(self.pravi_kot))
        self.play(man.Write(self.cos_omega_t))
        self.wait()
        self.play(man.FadeOut(self.kazalec2, self.pravi_kot, self.smer_sin, self.sin_omega_t, self.smer_cos, self.cos_omega_t, self.valovanje2))
        self.wait()
        self.play(man.Write(self.F0tex1))
        self.add(self.kopija)
        self.wait()
        self.play(self.kopija.animate.shift(man.UP*0.22 + man.LEFT*10.26).rotate((1/4) * man.PI))
        self.wait()

        self.F0tex2.next_to(self.kopija.get_end(), man.UP, buff = 0.1)

        self.play(man.Write(self.F0tex2))
        self.wait()

        self.levi_del = man.Group(
            self.ks,
            self.x_label,
            self.y_label,
            self.valovanje,
            self.ozadje,
            self.kopija,
            self.F0tex2,
        )

        self.desni_del = man.Group(
            self.ref,
            self.referenca,
            self.krog,
            self.kazalec,
            self.F0tex1,
            self.majhen_kot2,
            self.omega_t2,
        )

        self.wait()
        self.play(self.levi_del.animate.shift(man.LEFT*8), self.desni_del.animate.shift(man.RIGHT*8))
        self.play(man.FadeIn(self.podlaga, self.vzmet, self.k, self.dusilka_prej, self.d, self.visina, self.koordinata, self.x, self.plus, self.minus))
        self.wait()
        self.play(man.Transform(self.dusilka_spodaj_prej, self.dusilka_spodaj))
        self.wait()
        self.play(self.gor.animate.shift(man.UP*0.5), man.Transform(self.vzmet, self.vzmet_raztegnjena),
                  run_time = 2, rate_func = man.rush_from)
        self.wait()
        self.play(man.FadeOut(self.vzmet, self.k), man.GrowArrow(self.sila_vzmeti))
        self.play(man.Write(self.Fv))
        self.play(man.FadeOut(self.dusilka_prej, self.d), man.GrowArrow(self.sila_dusilke))
        self.play(man.Write(self.Fd))
        self.wait()
        self.play(man.Write(self.IINZ))
        self.wait()
        self.play(man.Write(self.vsota_sil), man.Write(self.enacaj3), man.Write(self.m2), man.Write(self.a))
        self.wait()
        self.play(man.Transform(self.a, self.xdd))
        self.wait()
        self.remove(self.a, self.razdalja, self.Ftex)
        self.play(self.skica.animate.shift(man.LEFT*2), self.enacba.animate.shift(man.LEFT*1))
        self.wait()
        
        self.lok1 = man.Arc(
            arc_center = [self.mxdd.get_center()[0] - 0.75, self.mxdd.get_center()[1], 0],
            radius = 0.75,
            start_angle = 0,
            angle = man.PI,
            )
        
        self.lok2 = man.Arc(
            arc_center = [self.vsota_sil.get_center()[0] + 1, self.vsota_sil.get_center()[1], 0],
            radius = 1,
            start_angle = man.PI,
            angle = man.PI,
            )
        
        self.Ft2 = self.Ft.copy()
        self.Fv2 = self.Fv.copy()
        self.Fd2 = self.Fd.copy()
        
        self.play(man.MoveAlongPath(self.mxdd, self.lok1), man.MoveAlongPath(self.vsota_sil, self.lok2), man.FadeOut(self.IINZ), run_time = 1.5)
        self.add(self.Ft2, self.Fv2, self.Fd2)
        self.wait()
        self.play(self.vsota_sil.animate.shift(man.LEFT*1.9), self.mxdd.animate.shift(man.LEFT*1.9), self.enacaj3.animate.shift(man.LEFT*1.9))
        self.play(man.FadeOut(self.vsota_sil))

        self.plus1 = man.MathTex("+").next_to(self.enacaj3, man.RIGHT)

        self.play(man.Write(self.plus1), self.Ft2.animate.next_to(self.plus1, man.RIGHT))
        self.wait()

        self.minus1 = man.MathTex("-").next_to(self.Ft2, man.RIGHT)

        self.play(man.Write(self.minus1), self.Fv2.animate.next_to(self.minus1, man.RIGHT))
        self.wait()

        self.minus2 = man.MathTex("-").next_to(self.Fv2, man.RIGHT)

        self.play(man.Write(self.minus2), self.Fd2.animate.next_to(self.minus2, man.RIGHT))
        self.wait()

        self.enacaj4 = man.MathTex("=").next_to(self.Fv, man.RIGHT)
        self.kx = man.MathTex("kx").next_to(self.enacaj4, man.RIGHT)
        self.enacaj5 = man.MathTex("=").next_to(self.Fd, man.RIGHT)
        self.dxd = man.MathTex("d \\dot{x}").next_to(self.enacaj5, man.RIGHT)

        self.play(man.Write(self.enacaj4), man.Write(self.kx))
        self.wait()
        self.play(man.Write(self.enacaj5), man.Write(self.dxd))
        self.wait()

        self.plus2 = man.MathTex("+").next_to(self.xdd, man.RIGHT)
        self.d2 = man.MathTex("d").next_to(self.plus2, man.RIGHT)
        self.xd = man.MathTex("\\dot{x}").next_to(self.d2, man.RIGHT, buff = 0.05)
        self.plus3 = man.MathTex("+").next_to(self.xd, man.RIGHT)
        self.k2 = man.MathTex("k").next_to(self.plus3, man.RIGHT)
        self.x2 = man.MathTex("x").move_to(self.k2.get_center() + [0.26, -0.06, 0])

        self.play(man.FadeOut(self.Fd2, self.minus2, self.enacaj5, self.dxd),
                  self.enacaj3.animate.shift(man.RIGHT*1.4),
                  self.plus1.animate.shift(man.RIGHT*1.4),
                  self.Ft2.animate.shift(man.RIGHT*1.4),
                  self.minus1.animate.shift(man.RIGHT*1.4),
                  self.Fv2.animate.shift(man.RIGHT*1.4),
                  man.FadeIn(self.plus2, self.d2, self.xd))
        self.wait()
        self.play(man.FadeOut(self.Fv2, self.minus1, self.enacaj4, self.kx),
                  self.enacaj3.animate.shift(man.RIGHT*1.4),
                  self.plus1.animate.shift(man.RIGHT*1.4),
                  self.Ft2.animate.shift(man.RIGHT*1.4),
                  man.FadeIn(self.plus3, self.k2, self.x2))
        self.wait()

        self.F02 = man.MathTex("F_0").next_to(self.enacaj3, man.RIGHT)
        self.sin_omega_t2 = man.MathTex("\\mathrm{sin} (\\omega t)").next_to(self.F02)

        self.play(man.FadeOut(self.Ft2, self.plus1, self.enacaj, self.F0, self.sinus, self.omega_t, self.motnja),
                  self.Ft.animate.next_to(self.sila.get_end() + [-1.25, 0.25, 0]),
                  man.FadeIn(self.F02, self.sin_omega_t2))
        self.wait()
        self.play(man.FadeIn(self.deljeno_m))
        self.play(man.FadeOut(self.deljeno_m),
                  self.m2.animate.shift(man.UP*0.35), self.xdd.animate.shift(man.RIGHT*0.1),
                  self.d2.animate.shift(man.UP*0.35), self.xd.animate.shift(man.RIGHT*0.15),
                  self.k2.animate.shift(man.UP*0.35), self.x2.animate.shift(man.RIGHT*0.2),
                  self.F02.animate.shift(man.UP*0.4))

        self.deljeno_m1 = man.MathTex("\\frac{}{m}").next_to(self.m2, man.DOWN, buff = 0.2)
        self.deljeno_m2 = man.MathTex("\\frac{}{m}").next_to(self.d2, man.DOWN, buff = 0.2)
        self.deljeno_m3 = man.MathTex("\\frac{}{m}").next_to(self.k2, man.DOWN, buff = 0.2)
        self.deljeno_m4 = man.MathTex("\\frac{}{m}").next_to(self.F02, man.DOWN, buff = 0.2)

        self.play(man.Write(self.deljeno_m1), man.Write(self.deljeno_m2), man.Write(self.deljeno_m3), man.Write(self.deljeno_m4))
        self.wait()
        self.play(man.FadeOut(self.m2, self.deljeno_m1))
        self.wait()

        self.dva_delta_omega_0 = man.MathTex("2 \\delta \\omega_0").move_to(self.d2.get_center() + [-0.25, -0.35, 0])
        self.omega_0_kvadrat = man.MathTex("\\omega_0^2").move_to(self.k2.get_center() + [0, -0.35, 0])
        self.f0 = man.MathTex("f_0").move_to(self.F02.get_center() + [-0.125, -0.4, 0])

        self.play(man.Unwrite(self.d2), man.Unwrite(self.deljeno_m2), self.xdd.animate.shift(man.LEFT*0.5), self.plus2.animate.shift(man.LEFT*0.5))
        self.play(man.Write(self.dva_delta_omega_0))
        self.play(man.Unwrite(self.k2), man.Unwrite(self.deljeno_m3))
        self.play(man.Write(self.omega_0_kvadrat))
        self.play(man.Unwrite(self.F02), man.Unwrite(self.deljeno_m4))
        self.play(self.sin_omega_t2.animate.shift(man.LEFT*0.25), man.Write(self.f0))
        self.wait()

        self.dif_enacba = man.Group(
            self.xdd,
            self.plus2,
            self.dva_delta_omega_0,
            self.xd,
            self.plus3,
            self.omega_0_kvadrat,
            self.x2,
            self.enacaj3,
            self.f0,
            self.sin_omega_t2,
        )

        self.play(man.FadeOut(self.skica2), self.dif_enacba.animate.shift(man.LEFT*3.375))
        self.wait()
        self.play(man.Write(self.resitev))
        self.play(man.Write(self.res))
        self.wait()
        self.add(self.homogena)
        self.play(self.homogena.animate.shift(man.DOWN*3 + man.LEFT*2.625))
        self.wait()

        self.nic = man.MathTex("0").next_to(self.enacaj3, man.RIGHT)

        self.play(man.FadeOut(self.f0, self.sin_omega_t2))
        self.play(man.FadeIn(self.nic))
        self.wait()

        self.enacaj6 = man.MathTex("=").next_to(self.homogena, man.RIGHT)
        self.homogena2 = man.MathTex("X \\mathrm{e}^{-\\delta \\omega_0 t} \\mathrm{sin} (\\omega_{0 \\mathrm{d}} t - \\varphi_\\mathrm{z})", color = man.YELLOW)
        self.homogena2.next_to(self.enacaj6, man.RIGHT) # da ni predolga vrstica

        self.play(man.Write(self.enacaj6))
        self.play(man.Write(self.homogena2))
        self.wait()
        self.play(man.FadeOut(self.nic))
        self.play(man.FadeIn(self.f0, self.sin_omega_t2))
        self.wait()
        self.add(self.partikularna)
        self.play(self.partikularna.animate.next_to(self.homogena, man.DOWN))
        self.wait()

        self.nastavek = man.Tex("nastavek:").next_to(self.partikularna, man.LEFT)
        self.enacaj7 = man.MathTex("=").next_to(self.partikularna, man.RIGHT)
        self.partikularna2 = man.MathTex("X \\mathrm{sin} (\\omega t - \\varphi_\\mathrm{z})", color = man.BLUE).next_to(self.enacaj7, man.RIGHT)

        self.play(man.Write(self.nastavek), man.Write(self.enacaj7))
        self.play(man.Write(self.partikularna2))
        self.wait()
        self.play(man.FadeOut(self.resitev, self.res, self.homogena, self.enacaj6, self.homogena2, self.nastavek))
        self.play(self.dif_enacba.animate.shift(man.UP*2),
                  self.partikularna.animate.shift(man.UP*2),
                  self.enacaj7.animate.shift(man.UP*2),
                  self.partikularna2.animate.shift(man.UP*2))
        self.wait()

        self.odvod1 = man.MathTex("/\\frac{\\mathrm{d}}{\\mathrm{d}x}").next_to(self.partikularna2, man.RIGHT)
        self.prvi_odvod = man.MathTex("\\dot{x}_\\mathrm{p} (t)").next_to(self.partikularna, man.DOWN)
        self.enacaj8 = man.MathTex("=").next_to(self.prvi_odvod, man.RIGHT)
        self.prvi_odvod2 = man.MathTex("\\omega X \\mathrm{cos} (\\omega t - \\varphi_\\mathrm{z})", color = man.BLUE_D).next_to(self.enacaj8, man.RIGHT)
        self.odvod2 = man.MathTex("/\\frac{\\mathrm{d}}{\\mathrm{d}x}").next_to(self.prvi_odvod2, man.RIGHT)
        self.drugi_odvod = man.MathTex("\\ddot{x}_\\mathrm{p} (t)").next_to(self.prvi_odvod, man.DOWN)
        self.enacaj9 = man.MathTex("=").next_to(self.drugi_odvod, man.RIGHT)
        self.drugi_odvod2 = man.MathTex("-\\omega^2 X \\mathrm{sin} (\\omega t - \\varphi_\\mathrm{z})", color = man.BLUE_E).next_to(self.enacaj9, man.RIGHT)

        self.play(man.FadeIn(self.odvod1))
        self.play(man.FadeOut(self.odvod1), man.Write(self.prvi_odvod))
        self.play(man.Write(self.enacaj8))
        self.play(man.Write(self.prvi_odvod2))
        self.wait()
        self.play(man.FadeIn(self.odvod2))
        self.play(man.FadeOut(self.odvod2), man.Write(self.drugi_odvod))
        self.play(man.Write(self.enacaj9))
        self.play(man.Write(self.drugi_odvod2))
        self.wait()
        self.play(self.partikularna.animate.shift(man.DOWN*2), self.enacaj7.animate.shift(man.DOWN*2), self.partikularna2.animate.shift(man.DOWN*2),
                  self.prvi_odvod.animate.shift(man.DOWN*2), self.enacaj8.animate.shift(man.DOWN*2), self.prvi_odvod2.animate.shift(man.DOWN*2),
                  self.drugi_odvod.animate.shift(man.DOWN*2), self.enacaj9.animate.shift(man.DOWN*2), self.drugi_odvod2.animate.shift(man.DOWN*2))
        self.wait()
        self.play(self.f0.animate.move_to([-1, -0.5, 0]), self.sin_omega_t2.animate.move_to([0.5, -0.5, 0]))
        self.play(self.enacaj3.animate.move_to([0, 0.25, 0]))
        self.play(self.plus3.animate.move_to([-2, 1, 0]), self.omega_0_kvadrat.animate.move_to([-1, 1, 0]), self.x2.animate.move_to([0, 1, 0]))
        self.play(self.plus2.animate.move_to([-2, 1.75, 0]), self.dva_delta_omega_0.animate.move_to([-1, 1.75, 0]), self.xd.animate.move_to([0, 1.75, 0]))
        self.play(self.xdd.animate.move_to([0, 2.5, 0]))
        self.wait()
        self.play(man.FadeOut(self.drugi_odvod, self.enacaj9, self.xdd), self.drugi_odvod2.animate.move_to([1.75, 2.5, 0]))
        self.play(man.FadeOut(self.prvi_odvod, self.enacaj8, self.xd), self.prvi_odvod2.animate.move_to([1.75, 1.75, 0]))
        self.play(man.FadeOut(self.partikularna, self.enacaj7, self.x2), self.partikularna2.animate.move_to([1.75, 1, 0]))
        self.wait()

        self.predznak1 = man.MathTex("-").move_to([-2.5, 2.5, 0])
        self.velikost1 = man.MathTex("\\omega^2 X", color = man.BLUE_E).move_to([-1, 2.5, 0])
        self.smer1 = man.MathTex("\\mathrm{sin} (\\omega t - \\varphi_\\mathrm{z})").move_to([1.5, 2.5, 0])
        self.predznak2 = man.MathTex("+").move_to([-2.5, 1.75, 0])
        self.velikost2 = man.MathTex("2 \\delta \\omega_0 \\omega X", color = man.BLUE_D).move_to([-1, 1.75, 0])
        self.smer2 = man.MathTex("\\mathrm{cos} (\\omega t - \\varphi_\\mathrm{z})").move_to([1.5, 1.75, 0])
        self.predznak3 = man.MathTex("+").move_to([-2.5, 1, 0])
        self.velikost3 = man.MathTex("\\omega_0^2 X", color = man.BLUE_C).move_to([-1, 1, 0])
        self.smer3 = man.MathTex("\\mathrm{sin} (\\omega t - \\varphi_\\mathrm{z})").move_to([1.5, 1, 0])
        self.predznak4 = man.MathTex("+").move_to([-2.5, -0.5, 0])
        self.velikost4 = man.MathTex("f_0", color = man.RED).move_to([-1, -0.5, 0])
        self.smer4 = man.MathTex("\\mathrm{sin} (\\omega t)").move_to([0.95, -0.5, 0])

        self.glavna_enacba = man.Group(
            self.predznak1,
            self.velikost1,
            self.smer1,
            self.predznak2,
            self.velikost2,
            self.smer2,
            self.predznak3,
            self.velikost3,
            self.smer3,
            self.enacaj3,
            self.predznak4,
            self.velikost4,
            self.smer4,
        )

        self.play(man.Unwrite(self.drugi_odvod2))
        self.play(man.Write(self.predznak1), man.Write(self.velikost1), man.Write(self.smer1))
        self.play(man.Unwrite(self.plus2), man.Unwrite(self.dva_delta_omega_0), man.Unwrite(self.prvi_odvod2))
        self.play(man.Write(self.predznak2), man.Write(self.velikost2), man.Write(self.smer2))
        self.play(man.Unwrite(self.plus3), man.Unwrite(self.omega_0_kvadrat), man.Unwrite(self.partikularna2))
        self.play(man.Write(self.predznak3), man.Write(self.velikost3), man.Write(self.smer3))
        self.play(man.Unwrite(self.f0), man.Unwrite(self.sin_omega_t2))
        self.play(man.Write(self.predznak4), man.Write(self.velikost4), man.Write(self.smer4))
        self.wait()
        self.play(self.glavna_enacba.animate.shift(man.DOWN*1 + man.LEFT*3.5))
        self.wait()
        self.play(man.Create(self.ref2))
        self.play(man.Write(self.referenca2))
        self.wait()
        self.play(man.GrowArrow(self.vsiljena_komponenta))
        self.play(man.Create(self.kot))
        self.play(man.Write(self.velikost_kota))
        self.play(man.GrowFromPoint(self.smer_vsiljene_komponente, self.smer_vsiljene_komponente.get_start()))
        self.play(self.smer4.animate.scale(0.5).rotate((6/16) * man.PI).next_to(self.smer_vsiljene_komponente.get_center(), man.LEFT, buff = 0.01))
        self.play(self.velikost4.animate.next_to(self.vsiljena_komponenta.get_center(), man.LEFT, buff = 0.2), man.FadeOut(self.predznak4, self.enacaj3))
        self.wait()
        self.play(man.GrowArrow(self.vpliv_togosti))
        self.play(man.Create(self.kot2))
        self.play(man.Write(self.velikost_kota2))
        self.play(man.GrowFromPoint(self.smer_vpliva_togosti, self.smer_vpliva_togosti.get_start()))
        self.play(self.smer3.animate.scale(0.5).rotate((1/16) * man.PI).next_to(self.smer_vpliva_togosti.get_center(), man.UP, buff = 0.01))
        self.play(self.velikost3.animate.next_to(self.vpliv_togosti.get_center(), man.UP, buff = 0.05), man.FadeOut(self.predznak3))
        self.wait()
        self.play(man.GrowArrow(self.vpliv_dusenja))
        self.play(man.Create(self.kot3))
        self.play(man.GrowFromPoint(self.smer_vpliva_dusenja, self.smer_vpliva_dusenja.get_start()))
        self.play(self.smer2.animate.scale(0.5).rotate(-(7/16) * man.PI).next_to(self.smer_vpliva_dusenja.get_center(), man.RIGHT, buff = 0.01))
        self.play(self.velikost2.animate.next_to(self.vpliv_dusenja.get_center(), man.RIGHT, buff = 0.2), man.FadeOut(self.predznak2))
        self.wait()
        self.play(man.GrowArrow(self.vpliv_vztrajnosti))
        self.play(man.Create(self.kot4))
        self.play(man.GrowFromPoint(self.smer_vpliva_vztrajnosti, self.smer_vpliva_vztrajnosti.get_start()))
        self.play(self.smer1.animate.scale(0.5).rotate((1/16) * man.PI).next_to(self.smer_vpliva_vztrajnosti.get_center(), man.UP, buff = 0.01))
        self.play(self.velikost1.animate.next_to(self.vpliv_vztrajnosti.get_center(), man.UP, buff = 0.25), man.FadeOut(self.predznak1))
        self.wait()
        self.play(man.Write(self.pitagora))
        self.wait()

        self.vpliv_dusenja_kopija = self.vpliv_dusenja.copy().set_opacity(0.4)

        self.add(self.vpliv_dusenja_kopija)
        self.play(self.vpliv_dusenja_kopija.animate.shift(man.DOWN * 2.6111 * man.np.sin((1/16) * man.PI) + man.LEFT * 2.6111 * man.np.cos((1/16) * man.PI)))
        self.wait()
        self.play(man.Write(self.f0_kvadrat))
        self.play(man.Write(self.enacaj10))
        self.play(man.Write(self.kateta1))
        self.play(man.Write(self.plus4))
        self.play(man.Write(self.kateta2))
        self.wait()

        self.korak1 = man.Group(
            self.f0_kvadrat,
            self.enacaj10,
            self.kateta1,
            self.plus4,
            self.kateta2,
        )

        self.play(man.FadeOut(self.pitagora), self.korak1.animate.shift(man.DOWN*3.5 + man.RIGHT*6.5).scale(0.7))
        self.play(man.Write(self.korak2))
        self.wait()
        self.play(self.korak2.animate.shift(man.UP*1.5).set_opacity(0.4).scale(0.7))
        self.play(man.Write(self.korak3))
        self.wait()
        self.play(self.korak2.animate.shift(man.UP*1.25).set_opacity(0),
                  self.korak3.animate.shift(man.UP*1.5).set_opacity(0.4).scale(0.7))
        self.play(man.Write(self.korak4))
        self.wait()
        self.play(man.FadeIn(self.deljeno_omega0_na_cetrto))
        self.play(man.FadeOut(self.deljeno_omega0_na_cetrto))
        self.play(self.korak3.animate.shift(man.UP*1.25).set_opacity(0),
                  self.korak4.animate.shift(man.UP*1.5).set_opacity(0.4).scale(0.7))
        self.play(man.Write(self.korak5))
        self.wait()
        self.play(man.FadeOut(self.korak2),
                  self.korak4.animate.shift(man.UP*1.25).set_opacity(0),
                  self.korak5.animate.shift(man.UP*1.5).set_opacity(0.4).scale(0.7))
        self.play(man.Write(self.korak6))
        self.wait()
        self.play(man.FadeOut(self.korak3),
                  self.korak5.animate.shift(man.UP*1.25).set_opacity(0),
                  self.korak6.animate.shift(man.UP*1.5).set_opacity(0.4).scale(0.7))
        self.play(man.Write(self.korak7))
        self.wait()
        self.play(man.Write(self.razmernik_frekvenc))
        self.play(man.FadeOut(self.korak4),
                  self.korak6.animate.shift(man.UP*1.25).set_opacity(0),
                  self.korak7.animate.shift(man.UP*1.5).set_opacity(0.4).scale(0.7))
        self.play(man.Write(self.korak8))
        self.play(man.FadeOut(self.razmernik_frekvenc))
        self.wait()
        self.play(man.FadeOut(self.korak5),
                  self.korak7.animate.shift(man.UP*1.25).set_opacity(0),
                  self.korak8.animate.shift(man.UP*1.5).set_opacity(0.4).scale(0.7))
        self.play(man.Write(self.korak9))
        self.wait()
        self.play(man.FadeIn(self.koren))
        self.play(man.FadeOut(self.koren))
        self.play(man.FadeOut(self.korak6),
                  self.korak8.animate.shift(man.UP*1.25).set_opacity(0),
                  self.korak9.animate.shift(man.UP*1.5).set_opacity(0.4).scale(0.7))
        self.play(man.Write(self.korak10))
        self.wait()
        self.play(man.Write(self.staticni_faktor))
        self.play(man.Write(self.dinamicni_faktor))
        self.play(man.FadeOut(self.korak7),
                  self.korak9.animate.shift(man.UP*1.25).set_opacity(0),
                  self.korak10.animate.shift(man.UP*1.5).set_opacity(0.4).scale(0.7))
        self.play(man.Write(self.korak11))
        self.play(man.FadeOut(self.staticni_faktor, self.dinamicni_faktor))
        self.wait()
        self.play(self.korak11.animate.move_to([-5.5, 3, 0]),
                  man.FadeOut(self.korak9, self.korak10, self.korak1), man.FadeIn(self.staticni_faktor2, self.dinamicni_faktor2))
        self.wait()
        self.play(man.Write(self.tangens1))
        self.wait()
        self.play(self.tangens1.animate.shift(man.UP*1.5).set_opacity(0.4).scale(0.7))
        self.play(man.Write(self.tangens2))
        self.wait()
        self.play(man.FadeIn(self.ulomek_deljeno_omega0_kvadrat))
        self.play(man.FadeOut(self.ulomek_deljeno_omega0_kvadrat))
        self.play(self.tangens1.animate.shift(man.UP*1.25).set_opacity(0),
                  self.tangens2.animate.shift(man.UP*1.5).set_opacity(0.4).scale(0.7))
        self.play(man.Write(self.tangens3))
        self.wait()
        self.play(man.FadeIn(self.razmernik_frekvenc2))
        self.play(man.FadeOut(self.tangens1),
                  self.tangens2.animate.shift(man.UP*1.25).set_opacity(0),
                  self.tangens3.animate.shift(man.UP*1.5).set_opacity(0.4).scale(0.7))
        self.play(man.Write(self.tangens4))
        self.play(man.FadeOut(self.razmernik_frekvenc2, self.tangens2, self.tangens3))
        self.wait()

# ---------------------------------------------------------------------------------------------- klic

if __name__ == "__main__":
    scena = VsiljenaNihanja()
    scena







# cd Desktop\PREDMETI\3._letnik\2._semester\IDPR\LADISK\projekt
# manim -pql p3.py VsiljenaNihanja
