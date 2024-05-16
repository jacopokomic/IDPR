import manim as man

class PasivnaVibroizolacija(man.Scene):
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
        
        self.m = man.MathTex("m").move_to([0.6, -0.2, 0])

        self.podlaga = man.Rectangle(
            color = man.GRAY,
            fill_color = man.GRAY,
            fill_opacity = 0.5,
            height = 0.2,
            width = 2,
        ).move_to([0, -3.1, 0])

        self.vzmet_standard = {1: [-1/2, -3, 0], 2: [-1/2, -5/2, 0],
                               3: [-3/4, -19/8, 0], 4: [-1/4, -17/8, 0],
                               5: [-3/4, -15/8, 0], 6: [-1/4, -13/8, 0],
                               7: [-3/4, -11/8, 0], 8: [-1/4, -9/8, 0],
                               9: [-1/2, -1, 0], 10: [-1/2, -1/2, 0]}

        self.vzmet = man.Graph([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                               [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10)],
                               layout = self.vzmet_standard,
                               vertex_config = {'radius': 0},
                               )
        
        self.k = man.MathTex("k").move_to([-1.1, -1.3, 0])

        self.dusilka_spodaj_majhna_standard = {1: [1/2, -3, 0], 2: [1/2, -2, 0],
                                               3: [1/4, -2, 0], 4: [3/4, -2, 0],
                                               5: [1/4, -3/2, 0], 6: [3/4, -3/2, 0]}

        self.dusilka_spodaj_standard = {1: [1/2, -2, 0], 2: [1/2, -5/4, 0],
                                        3: [1/4, -5/4, 0], 4: [3/4, -5/4, 0],
                                        5: [1/4, -1/4, 0], 6: [3/4, -1/4, 0]}

        self.dusilka_spodaj = man.Graph([1, 2, 3, 4, 5, 6],
                                        [(1, 2), (2, 3), (2, 4), (3, 5), (4, 6)],
                                        layout = self.dusilka_spodaj_majhna_standard,
                                        vertex_config = {'radius': 0},
                                        )

        self.korekcija_x = 0.05

        self.dusilka_zgoraj_standard = {1: [1/2, -1/2, 0], 2: [1/2, -7/4, 0],
                                        3: [1/4 + self.korekcija_x, -7/4, 0], 4: [3/4 - self.korekcija_x, -7/4, 0]}

        self.dusilka_zgoraj = man.Graph([1, 2, 3, 4],
                                        [(1, 2), (2, 3), (2, 4)],
                                        layout = self.dusilka_zgoraj_standard,
                                        vertex_config = {'radius': 0},
                                        )

        self.d = man.MathTex("d").move_to([1.1, -2, 0])

        self.sistem = man.Group(
            self.masa, self.m,
            self.podlaga,
            self.vzmet, self.k,
            self.dusilka_spodaj, self.dusilka_zgoraj, self.d,
        )

        self.visina_x = man.DashedLine(
            start = [-1, 1, 0],
            end = [-3.1, 1, 0],
            stroke_opacity = 0.2,
        )

        self.koordinata_x = man.DoubleArrow(
            start = [-3, 0, 0],
            end = [-3, 2, 0],
            buff = 0,
            stroke_width = 2,
            max_tip_length_to_length_ratio = 0.12,
        )

        self.oznaka_x = man.MathTex("x").move_to([-3.1 - 0.2, 1, 0])

        self.x_plus = man.MathTex("+").next_to(self.koordinata_x.get_end(), man.LEFT, buff = 0.1).scale(0.5)
        self.x_minus = man.MathTex("-").next_to(self.koordinata_x.get_start(), man.LEFT, buff = 0.1).scale(0.5)

        self.visina_y = man.DashedLine(
            start = [-1, -2.1, 0],
            end = [-3.1, -2.1, 0],
            stroke_opacity = 0.2,
        )

        self.koordinata_y = man.DoubleArrow(
            start = [-3, -3.1, 0],
            end = [-3, -1.1, 0],
            buff = 0,
            stroke_width = 2,
            max_tip_length_to_length_ratio = 0.12,
        )

        self.oznaka_y = man.MathTex("y").move_to([-3.1 - 0.2, -2.1, 0])

        self.y_plus = man.MathTex("+").next_to(self.koordinata_y.get_end(), man.LEFT, buff = 0.1).scale(0.5)
        self.y_minus = man.MathTex("-").next_to(self.koordinata_y.get_start(), man.LEFT, buff = 0.1).scale(0.5)

        self.nihanje_podlage = man.MathTex("y(t) = Y \\mathrm{sin} (\\omega t)").move_to([3, -2.1, 0])

        self.kopija_mase = self.masa.copy().shift(man.UP*1).set_opacity(0.2)

        self.kopija_podlage = self.podlaga.copy().shift(man.UP*1).set_opacity(0.2)

        self.vzmet_raztegnjena_prvic = {1: [-1/2, -3 + 1 + 1/4 + (0/12)*1/4, 0], 2: [-1/2, -5/2 + 1 + 1/4 + (0/12)*1/4, 0],
                                        3: [-3/4, -19/8 + 1 + 1/4 + (1/12)*1/4, 0], 4: [-1/4, -17/8 + 1 + 1/4 + (3/12)*1/4, 0],
                                        5: [-3/4, -15/8 + 1 + 1/4 + (5/12)*1/4, 0], 6: [-1/4, -13/8 + 1 + 1/4 + (7/12)*1/4, 0],
                                        7: [-3/4, -11/8 + 1 + 1/4 + (9/12)*1/4, 0], 8: [-1/4, -9/8 + 1 + 1/4 + (11/12)*1/4, 0],
                                        9: [-1/2, -1 + 1 + 1/4 + (12/12)*1/4, 0], 10: [-1/2, -1/2 + 1 + 1/4 + (12/12)*1/4, 0]}
        
        self.druga_visina_x = man.DashedLine(
            start = [-1, 1, 0],
            end = [-1.6, 1, 0],
            stroke_opacity = 0.2,
        )
        
        self.tretja_visina_x = man.DashedLine(
            start = [-1, 1 + 1/2, 0],
            end = [-1.6, 1 + 1/2, 0],
            stroke_opacity = 0.2,
        )

        self.druga_koordinata_x = man.Arrow(
            start = [-1.5, 1, 0],
            end = [-1.5, 1 + 1/2, 0],
            buff = 0,
            stroke_width = 8,
            max_tip_length_to_length_ratio = (3/4)*0.48, # tip na 3/4 navadnega
        )

        self.druga_visina_y = man.DashedLine(
            start = [-1, -2.1, 0],
            end = [-1.6, -2.1, 0],
            stroke_opacity = 0.2,
        )

        self.tretja_visina_y = man.DashedLine(
            start = [-1, -2.1 + 1/4, 0],
            end = [-1.6, -2.1 + 1/4, 0],
            stroke_opacity = 0.2,
        )

        self.druga_koordinata_y = man.Arrow(
            start = [-1.5, -2.1, 0],
            end = [-1.5, -2.1 + 1/4, 0],
            buff = 0,
            stroke_width = 16,
            max_tip_length_to_length_ratio = (3/4)*0.96, # tip na 3/4 navadnega
        )

        self.x_vecji_od_y = man.MathTex("x > y").move_to([4, 1, 0])

        self.xd_vecji_od_yd = man.MathTex("\\dot{x} > \\dot{y}").move_to([4, 0.4, 0])

        self.sila_vzmeti = man.Arrow(
            start = [-1/2, 1, 0],
            end = [-1/2, 0, 0],
            color = man.RED,
            max_tip_length_to_length_ratio = 0.25,
            buff = 0,
        )

        self.Fv = man.MathTex("\\def\\mathbi#1{\\textbf{\\em #1}}\\mathbi{F}_v", color = man.RED).next_to(self.sila_vzmeti.get_end(), man.DOWN)

        self.sila_dusilke = man.Arrow(
            start = [1/2, 1, 0],
            end = [1/2, 0, 0],
            color = man.RED,
            max_tip_length_to_length_ratio = 0.25,
            buff = 0,
        )

        self.Fd = man.MathTex("\\def\\mathbi#1{\\textbf{\\em #1}}\\mathbi{F}_d", color = man.RED).next_to(self.sila_dusilke.get_end(), man.DOWN)

        self.sistem2 = man.Group(
            self.masa, self.m, self.kopija_mase,
            self.podlaga, self.kopija_podlage,
            self.sila_vzmeti, self.Fv,
            self.sila_dusilke, self.Fd,
            self.visina_x, self.druga_visina_x, self.tretja_visina_x, self.koordinata_x, self.druga_koordinata_x, self.oznaka_x,
            self.visina_y, self.druga_visina_y, self.tretja_visina_y, self.koordinata_y, self.druga_koordinata_y, self.oznaka_y,
        )

        self.IINZ = man.Tex("II. Newtonov zakon:").move_to([-4, 0.5, 0])

        self.vsota_sil = man.MathTex("\\sum_{i = 1}^{n} \\def\\mathbi#1{\\textbf{\\em #1}}\\mathbi{F}_i").move_to([-4.7, -0.5, 0])

        self.enacaj = man.MathTex("=").next_to(self.vsota_sil, man.RIGHT)

        self.ma = man.MathTex("m \\def\\mathbi#1{\\textbf{\\em #1}}\\mathbi{a}").next_to(self.enacaj, man.RIGHT)

        self.lok1 = man.Arc(
            arc_center = self.enacaj.get_center(),
            radius = self.ma.get_center()[0] - self.enacaj.get_center()[0],
            start_angle = 0,
            angle = man.PI,
            )
        
        self.lok2 = man.Arc(
            arc_center = self.enacaj.get_center(),
            radius = self.enacaj.get_center()[0] - self.vsota_sil.get_center()[0],
            start_angle = man.PI,
            angle = man.PI,
            )

# ---------------------------------------------------------------------------------------------- prikaz animacij

        self.wait()
        self.play(man.GrowFromCenter(self.masa))
        self.play(man.Write(self.m))
        self.wait()
        self.play(man.GrowFromCenter(self.podlaga))
        self.wait()
        self.play(man.FadeIn(self.vzmet))
        self.play(man.Write(self.k))
        self.play(man.FadeIn(self.dusilka_spodaj, self.dusilka_zgoraj))
        self.play(man.Write(self.d))
        self.wait()
        self.play(self.sistem.animate.shift(man.UP*1), self.dusilka_spodaj.animate.change_layout(self.dusilka_spodaj_standard))
        self.wait()
        self.play(man.GrowFromPoint(self.visina_x, self.visina_x.get_start()))
        self.play(man.FadeIn(self.koordinata_x))
        self.play(man.Write(self.oznaka_x))
        self.play(man.Write(self.x_plus), man.Write(self.x_minus))
        self.play(man.GrowFromPoint(self.visina_y, self.visina_y.get_start()))
        self.play(man.FadeIn(self.koordinata_y))
        self.play(man.Write(self.oznaka_y))
        self.play(man.Write(self.y_plus), man.Write(self.y_minus))
        self.wait()
        self.play(man.Write(self.nihanje_podlage))
        self.wait()
        self.play(man.FadeIn(self.kopija_mase, self.kopija_podlage),
                  self.masa.animate.shift(man.UP*1/2), self.m.animate.shift(man.UP*1/2),
                  self.podlaga.animate.shift(man.UP*1/4),
                  self.vzmet.animate.change_layout(self.vzmet_raztegnjena_prvic), self.k.animate.shift(man.UP*3/8),
                  self.dusilka_spodaj.animate.shift(man.UP*1/4), self.dusilka_zgoraj.animate.shift(man.UP*1/2), self.d.animate.shift(man.UP*3/8),
                  run_time = 2, rate_func = man.rush_from)
        self.wait()
        self.play(man.GrowFromPoint(self.tretja_visina_x, self.tretja_visina_x.get_start()))
        self.play(man.FadeOut(self.x_plus, self.x_minus),
                  man.Transform(self.visina_x, self.druga_visina_x), man.Transform(self.koordinata_x, self.druga_koordinata_x),
                  self.oznaka_x.animate.move_to([-1.6 - 0.2, 1 + (1/2)*1/2, 0]))
        self.play(man.GrowFromPoint(self.tretja_visina_y, self.tretja_visina_y.get_start()))
        self.play(man.FadeOut(self.y_plus, self.y_minus),
                  man.Transform(self.visina_y, self.druga_visina_y), man.Transform(self.koordinata_y, self.druga_koordinata_y),
                  self.oznaka_y.animate.move_to([-1.6 - 0.2, -2.1 + (1/2)*1/4, 0]))
        self.wait()
        self.play(man.Write(self.x_vecji_od_y))
        self.play(man.Write(self.xd_vecji_od_yd))
        self.wait()
        self.play(man.FadeOut(self.vzmet, self.k))
        self.play(man.GrowArrow(self.sila_vzmeti))
        self.play(man.Write(self.Fv))
        self.play(man.FadeOut(self.dusilka_spodaj, self.dusilka_zgoraj, self.d))
        self.play(man.GrowArrow(self.sila_dusilke))
        self.play(man.Write(self.Fd))
        self.wait()
        self.play(self.sistem2.animate.shift(man.RIGHT*1),
                  self.x_vecji_od_y.animate.move_to([4.5, 1, 0]), self.xd_vecji_od_yd.animate.move_to([4.5, 0.4, 0]),
                  self.nihanje_podlage.animate.move_to([4.5, -2.1, 0]))
        self.play(man.Write(self.IINZ))
        self.play(man.Write(self.vsota_sil))
        self.play(man.Write(self.enacaj))
        self.play(man.Write(self.ma))
        self.wait()
        self.play(man.FadeOut(self.IINZ), man.MoveAlongPath(self.ma, self.lok1), man.MoveAlongPath(self.vsota_sil, self.lok2))
        self.play(man.FadeOut(self.vsota_sil), self.ma.animate.shift(man.LEFT*1), self.enacaj.animate.shift(man.LEFT*1))

# definiram tukaj elemente, ker so premaknjeni glede na njihovo originalno pozicijo -----------------------------------------------
        self.plus1 = man.MathTex("+").next_to(self.enacaj, man.RIGHT)
        self.kopija_Fv = self.Fv.copy()
# ---------------------------------------------------------------------------------------------------------------------------------

        self.add(self.kopija_Fv)
        self.play(man.Write(self.plus1))
        self.play(self.kopija_Fv.animate.next_to(self.plus1, man.RIGHT))

# definiram tukaj elemente, ker so premaknjeni glede na njihovo originalno pozicijo -----------------------------------------------
        self.plus2 = man.MathTex("+").next_to(self.kopija_Fv, man.RIGHT)
        self.kopija_Fd = self.Fd.copy()
# ---------------------------------------------------------------------------------------------------------------------------------

        self.add(self.kopija_Fd)
        self.play(man.Write(self.plus2))
        self.play(self.kopija_Fd.animate.next_to(self.plus2, man.RIGHT))
        self.wait()

# ---------------------------------------------------------------------------------------------- klic

if __name__ == "__main__":
    scena = PasivnaVibroizolacija()
    scena

# cd Desktop\PREDMETI\3._letnik\2._semester\IDPR\LADISK\projekt
# manim -pql pv.py PasivnaVibroizolacija
