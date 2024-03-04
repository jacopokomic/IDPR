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
                  self.Ft.animate.next_to(self.sila.get_end() + [-1.5, 0.25, 0]),
                  man.FadeIn(self.F02, self.sin_omega_t2))
        self.wait()
        self.play(man.FadeIn(self.deljeno_m))
        self.play(man.FadeOut(self.deljeno_m))
        self.wait()

# ---------------------------------------------------------------------------------------------- klic

if __name__ == "__main__":
    scena = VsiljenaNihanja()
    scena







# cd DEsktop\PREDMETI\3._letnik\2._semester\IDPR\LADISK\projekt
# manim -pql p3.py VsiljenaNihanja
