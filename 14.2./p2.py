import manim as man

class VsiljenaNihanja(man.Scene):
    def construct(self):

# ---------------------------------------------------------------------------------------------- elementi

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

        self.F = man.ValueTracker((3/4) * man.PI)
        
        self.ozadje = man.Rectangle(
            width = 8,
            height = 5,
            color = man.BLACK,
            stroke_opacity = 0,
            fill_opacity = 0,
        )

        self.sila = man.Arrow(
            start = [0, self.masa.get_center()[1], 0],
            end = [0, self.masa.get_center()[1] + 1.5 * man.np.sin(self.F.get_value()), 0],
            color = man.RED,
            max_tip_length_to_length_ratio = 0.5,
        )

        self.valovanje = man.TracedPath(self.sila.get_end)

        def update_sila(sila, dt):
            new_start = [0, self.masa.get_center()[1], 0]
            new_end = [0, self.masa.get_center()[1] + 1.5 * man.np.sin(self.F.get_value()), 0]
            self.sila.put_start_and_end_on(new_start, new_end)

        def update_ozadje(ozadje, dt):
            self.ozadje.shift(0.5 * man.LEFT * dt)

        self.sila.add_updater(update_sila)
        self.ozadje.add_updater(update_ozadje)
        self.ozadje.add(self.valovanje)

        self.S = man.ValueTracker((3/4) * man.PI)

        self.arrow = man.Arrow(
            start = [0, self.masa.get_center()[1], 0],
            end = [0, self.masa.get_center()[1] + 1.5 * man.np.sin(self.F.get_value()), 0],
            color = man.YELLOW,
            max_tip_length_to_length_ratio = 0.5,
        )

        def update_arrow(arrow, dt):
            new_s = [0, self.masa.get_center()[1], 0]
            new_e = [0, self.masa.get_center()[1] + 1.5 * man.np.sin(self.S.get_value()), 0]
            self.arrow.put_start_and_end_on(new_s, new_e)
        
        self.arrow.add_updater(update_arrow)

        self.gor0 = man.AnimationGroup(
            self.masa.animate.shift(man.UP*0),
            self.dusilka_zgoraj.animate.shift(man.UP*0),
            self.m.animate.shift(man.UP*0),
            self.d.animate.shift(man.UP*0),
            self.k.animate.shift(man.UP*0),
            man.Transform(self.vzmet, self.vzmet_0),
        )

        self.gor = man.AnimationGroup(
            self.masa.animate.shift(man.UP*0.5),
            self.dusilka_zgoraj.animate.shift(man.UP*0.5),
            self.m.animate.shift(man.UP*0.5),
            self.d.animate.shift(man.UP*0.25),
            self.k.animate.shift(man.UP*0.25),
            man.Transform(self.vzmet, self.vzmet_raztegnjena),
        )

        self.dol = man.AnimationGroup(
            self.masa.animate.shift(man.DOWN*0.5),
            self.dusilka_zgoraj.animate.shift(man.DOWN*0.5),
            self.m.animate.shift(man.DOWN*0.5),
            self.d.animate.shift(man.DOWN*0.25),
            self.k.animate.shift(man.DOWN*0.25),
            man.Transform(self.vzmet, self.vzmet_stisnjena),
        )
        
# ---------------------------------------------------------------------------------------------- prikaz animacij

        self.play(man.FadeIn(self.masa))
        self.wait()
        self.play(man.FadeIn(self.m))
        self.wait()
        self.play(man.FadeIn(self.podlaga))
        self.wait()
        self.play(man.FadeIn(self.vzmet))
        self.wait()
        self.play(man.FadeIn(self.k))
        self.wait()
        self.play(man.FadeIn(self.dusilka_prej))
        self.wait()
        self.play(man.FadeIn(self.d))
        self.wait()
        self.play(man.Transform(self.dusilka_spodaj_prej, self.dusilka_spodaj))
        self.wait()
        self.add(self.arrow)
        self.wait()
        self.play(self.gor, self.S.animate.set_value((5/4) * man.PI))
        self.play(self.dol, self.S.animate.set_value((9/4) * man.PI))
        self.play(self.gor, self.S.animate.set_value((13/4) * man.PI))
        self.play(self.dol, self.S.animate.set_value((17/4) * man.PI))
        self.play(self.gor0, self.S.animate.set_value((19/4) * man.PI))
        self.wait()
        self.remove(self.arrow)
        self.add(self.sila)
        self.wait()
        self.add(self.ozadje, self.valovanje)
        self.play(self.F.animate.set_value((19/4) * man.PI), run_time = 10, rate_func = man.linear)
        self.valovanje.clear_updaters()
        self.wait()

# ---------------------------------------------------------------------------------------------- klic

if __name__ == "__main__":
    scena = VsiljenaNihanja()
    scena








# manim -pql p2.py VsiljenaNihanja
