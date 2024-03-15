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
            x_range = [-0.25, 4.75],
            y_range = [-2, 2],
            x_length = 5,
            y_length = 4,
            axis_config = {"tip_width": 0.2, "tip_height": 0.2, "include_ticks": False},
        ).shift(man.RIGHT*2.25)

        self.x_label = man.MathTex("t").next_to(self.ks.x_axis.get_end(), man.DOWN)
        self.y_label = man.MathTex("F").next_to(self.ks.y_axis.get_end(), man.LEFT)

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

        self.majhen_kot = man.Angle(
            line1 = self.ref,
            line2 = self.kazalec,
            radius = 0.75,
        )

        self.kot = man.TracedPath(self.kazalec.get_center, stroke_width = 4)

        self.Ft = man.MathTex("F(t)", color = man.RED).move_to([-1.5, 2.5, 0])
        self.enacaj = man.MathTex("=").next_to(self.Ft, man.RIGHT)

        self.kopija = self.kazalec.copy()

        self.F0 = man.MathTex("F_0").next_to(self.enacaj, man.RIGHT)
        self.F0tex1 =  man.MathTex("F_0", color = man.RED).next_to(self.kazalec.get_end(), man.UP + man.RIGHT, buff = 0.1)
        self.F0tex2 =  man.MathTex("F_0", color = man.RED)

        self.sinus = man.Tex("sin").next_to(self.F0, man.RIGHT)
        self.omega_t = man.MathTex("(\\omega t)").next_to(self.sinus, man.RIGHT, buff = 0.1)
        #self.omegatex = man.MathTex("\\omega").next_to(self.kotna_hitrost.get_end(), man.RIGHT, buff = 0.1)
        self.phi = man.MathTex("(\\varphi)").next_to(self.sinus, man.RIGHT, buff = 0.1)
        #self.phitex = man.MathTex("\\varphi").next_to(self.kot.get_end(), man.DOWN, buff = 0.25)

        """self.levi_del = man.Group(
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
            self.povezava,
            self.kazalec,
            self.F0tex1,
            self.lok2,
            self.kotna_hitrost,
            self.omegatex,
        )"""

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

        """self.e1 = man.Group(
            self.Ft,
            self.enacaj,
            self.F0,
            self.sinus,
            self.omega_t,
        )"""
        
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
        self.play(man.GrowFromPoint(self.visina, [-1, self.masa.get_center()[1], 0]))
        self.play(man.FadeIn(self.razdalja))
        self.wait()
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
        self.play(man.GrowFromEdge(self.povezava_help, self.kazalec.get_end()))
        self.play(man.GrowFromPoint(self.majhen_kot, [4.75, 0, 0]))
        self.play(man.FadeIn(self.dot))
        self.remove(self.kazalec_help, self.povezava_help)
        self.add(self.kazalec, self.povezava)
        self.wait()
        self.add(self.kot)
        self.play(self.F.animate.set_value((8/4) * man.PI + 0.001), # da se obrne navzgor
                  run_time = 3.5, rate_func = man.linear)
        
        self.remove(self.kot, self.majhen_kot)
        self.kot = man.TracedPath(self.kazalec.get_center, stroke_width = 4)
        self.add(self.kot)

        self.wait()
        self.play(man.Create(self.ks))
        self.play(man.Write(self.y_label))
        self.play(man.Write(self.x_label))
        self.add(self.ozadje, self.valovanje)
        self.play(self.F.animate.set_value((16/4) * man.PI),
                  run_time = 4, rate_func = man.linear)
        
        self.remove(self.kot)
        self.kot = man.TracedPath(self.kazalec.get_center, stroke_width = 4)
        self.add(self.kot)

        self.play(self.F.animate.set_value((19/4) * man.PI),
                  run_time = 1.5, rate_func = man.linear)
        
        self.valovanje.clear_updaters()
        self.ozadje.clear_updaters()

        self.play(self.ks.animate.shift(man.LEFT*3.5),
                  self.x_label.animate.shift(man.LEFT*3.5),
                  self.y_label.animate.shift(man.LEFT*3.5),
                  self.valovanje.animate.shift(man.LEFT*3.5))
        self.wait(3)
        self.play(self.ks.animate.shift(man.RIGHT*3.5),
                  self.x_label.animate.shift(man.RIGHT*3.5),
                  self.y_label.animate.shift(man.RIGHT*3.5),
                  self.valovanje.animate.shift(man.RIGHT*3.5))

        self.valovanje = man.TracedPath(self.sila.get_end, stroke_color = man.RED)
        self.ozadje.add_updater(update_ozadje)
        self.ozadje.add(self.valovanje)

        self.play(self.F.animate.set_value((24/4) * man.PI),
                  run_time = 2.5, rate_func = man.linear)

        self.remove(self.kot)
        self.kot = man.TracedPath(self.kazalec.get_center, stroke_width = 4)
        self.add(self.kot)

        self.play(self.F.animate.set_value((25/4) * man.PI),
                  run_time = 0.5, rate_func = man.linear)
        
        self.valovanje.clear_updaters()

        self.play(self.F.animate.set_value((32/4) * man.PI),
                  run_time = 3.5, rate_func = man.linear)

        self.remove(self.kot)
        self.kot = man.TracedPath(self.kazalec.get_center, stroke_width = 4)
        self.add(self.kot)
        
        self.play(self.F.animate.set_value((33/4) * man.PI),
                  run_time = 0.5, rate_func = man.linear)
        
        self.ozadje.clear_updaters()

        self.wait(3)
        """

        self.povezava.clear_updaters()

        self.play(man.Transform(self.Ftex, self.Ft))
        self.wait()
        self.play(man.Write(self.enacaj))
        self.wait()
        self.play(man.Wiggle(self.kazalec, rotation_angle = (1/8) * man.PI), scale_value = 1.1, run_time = 2.5)
        self.wait()
        self.play(man.Write(self.F0tex1))
        self.add(self.kopija)
        self.wait()
        self.play(man.FadeIn(self.lok1, self.kot))
        self.play(man.Write(self.phitex))
        self.wait()
        self.play(self.kopija.animate.shift(man.UP*0.22 + man.LEFT*10.061).rotate((1/4) * man.PI))
        self.wait()

        self.F0tex2.next_to(self.kopija.get_end(), man.UP, buff = 0.1)

        self.play(man.Write(self.F0tex2))
        self.wait()
        self.play(man.Write(self.F0))
        self.play(man.Write(self.sinus))
        self.play(man.Write(self.phi))
        self.wait()
        self.play(man.FadeOut(self.lok1, self.kot, self.phitex))
        self.play(man.FadeIn(self.lok2, self.kotna_hitrost))
        self.play(man.Write(self.omegatex))
        self.wait()
        self.play(man.Transform(self.phi, self.omega_t))
        self.wait()
        self.play(self.levi_del.animate.shift(man.LEFT*8), self.desni_del.animate.shift(man.RIGHT*8))
        self.play(man.FadeIn(self.podlaga, self.vzmet, self.k, self.dusilka_prej, self.d, self.visina, self.koordinata, self.x, self.plus, self.minus))
        self.wait()
        self.play(man.Transform(self.dusilka_spodaj_prej, self.dusilka_spodaj))
        self.wait()
        self.play(self.gor.animate.shift(man.UP*0.25), man.Transform(self.vzmet, self.vzmet_raztegnjena),
                  man.GrowArrow(self.sila_vzmeti), man.GrowArrow(self.sila_dusilke),
                  rate_func = man.rush_from)
        #self.play(man.GrowArrow(self.sila_vzmeti), man.GrowArrow(self.sila_dusilke))
        self.remove(self.Ftex, self.theta)
        self.play(self.e1.animate.shift(man.DOWN*0.75 + man.RIGHT*2.25))
        self.wait()"""

# ---------------------------------------------------------------------------------------------- klic

if __name__ == "__main__":
    scena = VsiljenaNihanja()
    scena








# manim -pql p3.py VsiljenaNihanja
