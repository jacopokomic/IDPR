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

        self.enacaj1 = man.MathTex("=").next_to(self.vsota_sil, man.RIGHT)

        self.ma = man.MathTex("m \\def\\mathbi#1{\\textbf{\\em #1}}\\mathbi{a}").next_to(self.enacaj1, man.RIGHT)

        self.lok1 = man.Arc(
            arc_center = self.enacaj1.get_center(),
            radius = self.ma.get_center()[0] - self.enacaj1.get_center()[0],
            start_angle = 0,
            angle = man.PI,
            )
        
        self.lok2 = man.Arc(
            arc_center = self.enacaj1.get_center(),
            radius = self.enacaj1.get_center()[0] - self.vsota_sil.get_center()[0],
            start_angle = man.PI,
            angle = man.PI,
            )
        
        self.mxdd = man.MathTex("m \ddot{x}").move_to([-6.5, -0.5, 0])

        self.enacaj2 = man.MathTex("=").next_to(self.mxdd, man.RIGHT)

        self.minus1 = man.MathTex("-").next_to(self.enacaj2, man.RIGHT)

        self.kxy = man.MathTex("k (x - y)").next_to(self.minus1, man.RIGHT)

        self.minus2 = man.MathTex("-").next_to(self.kxy, man.RIGHT)

        self.dxy = man.MathTex("d ( \dot{x} - \dot{y})").next_to(self.minus2, man.RIGHT)

        self.minus3 = man.MathTex("-").next_to(self.enacaj2, man.RIGHT)

        self.kx = man.MathTex("kx").next_to(self.minus3, man.RIGHT)

        self.plus3 = man.MathTex("+").next_to(self.kx, man.RIGHT)

        self.ky = man.MathTex("ky").next_to(self.plus3, man.RIGHT)

        self.minus4 = man.MathTex("-").next_to(self.ky, man.RIGHT)

        self.dxd = man.MathTex("d \dot{x}").next_to(self.minus4, man.RIGHT)

        self.plus4 = man.MathTex("+").next_to(self.dxd, man.RIGHT)

        self.dyd = man.MathTex("d \dot{y}").next_to(self.plus4, man.RIGHT)

        self.deljeno_m = man.MathTex(": m").move_to([-3.75, -2, 0])

        self.nastavek = man.Tex("nastavek:").move_to([-5, 1, 0])

        self.xt = man.MathTex("x(t) =").next_to(self.nastavek, man.RIGHT)

        self.xdef = man.MathTex("X \\mathrm{sin} (\\omega t - \\varphi_\\mathrm{z})").next_to(self.xt, man.RIGHT)

        self.odvod2 = man.MathTex("/ \\frac{\mathrm{d}}{\mathrm{d}t}").next_to(self.xdef, man.RIGHT)

        self.xtd = man.MathTex("\\dot{x}(t) =").move_to(self.xt.get_center() + [0, -1, 0])

        self.xddef = man.MathTex("\\omega X \\mathrm{cos} (\\omega t - \\varphi_\\mathrm{z})").next_to(self.xtd, man.RIGHT)

        self.odvod3 = man.MathTex("/ \\frac{\mathrm{d}}{\mathrm{d}t}").next_to(self.xddef, man.RIGHT)

        self.xtdd = man.MathTex("\\ddot{x}(t) =").move_to(self.xtd.get_center() + [0, -1, 0])

        self.xdddef = man.MathTex("- \\omega^2 X \\mathrm{sin} (\\omega t - \\varphi_\\mathrm{z})").next_to(self.xtdd, man.RIGHT)

        self.vty_predznak = man.MathTex("+").move_to([-5.5, -2, 0])

        self.vty_velikost = man.MathTex("\\omega_0^2 Y", color = man.GREEN_C).move_to([-3.5, -2, 0])

        self.vty_smer = man.MathTex("\\mathrm{sin} (\\omega t)").move_to([-1.5, -2, 0])

        self.vdy_predznak = man.MathTex("+").move_to([-5.5, -1, 0])

        self.vdy_velikost = man.MathTex("2 \\delta \\omega_0 \\omega Y", color = man.GREEN_E).move_to([-3.5, -1, 0])

        self.vdy_smer = man.MathTex("\\mathrm{cos} (\\omega t)").move_to([-1.5, -1, 0])

        self.enacaj3 = man.MathTex("=").move_to([-3.5, 0, 0])

        self.vtx_predznak = man.MathTex("+").move_to([-5.5, 1, 0])

        self.vtx_velikost = man.MathTex("\\omega_0^2 X", color = man.BLUE_C).move_to([-3.5, 1, 0])

        self.vtx_smer = man.MathTex("\\mathrm{sin} (\\omega t - \\varphi_\\mathrm{z})").move_to([-1, 1, 0])

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
        self.play(self.sistem2.animate.shift(man.RIGHT*1.5),
                  self.x_vecji_od_y.animate.move_to([5, 1, 0]), self.xd_vecji_od_yd.animate.move_to([5, 0.4, 0]),
                  self.nihanje_podlage.animate.move_to([5, -2.1, 0]))
        self.play(man.Write(self.IINZ))
        self.play(man.Write(self.vsota_sil))
        self.play(man.Write(self.enacaj1))
        self.play(man.Write(self.ma))
        self.wait()
        self.play(man.FadeOut(self.IINZ), man.MoveAlongPath(self.ma, self.lok1), man.MoveAlongPath(self.vsota_sil, self.lok2))
        self.play(man.FadeOut(self.vsota_sil), self.ma.animate.shift(man.LEFT*1), self.enacaj1.animate.shift(man.LEFT*1))

# definiram tukaj elemente, ker so premaknjeni glede na njihovo originalno pozicijo -----------------------------------------------
        self.plus1 = man.MathTex("+").next_to(self.enacaj1, man.RIGHT)
        self.kopija_Fv = self.Fv.copy()
# ---------------------------------------------------------------------------------------------------------------------------------

        self.add(self.kopija_Fv)
        self.play(man.Write(self.plus1))
        self.play(self.kopija_Fv.animate.next_to(self.plus1, man.RIGHT))

# definiram tukaj elemente, ker so premaknjeni glede na njihovo originalno pozicijo -----------------------------------------------
        self.plus2 = man.MathTex("+").next_to(self.kopija_Fv, man.RIGHT)
        self.kopija_Fd = self.Fd.copy()

        self.vektorska_enacba = man.Group(
            self.ma,
            self.enacaj1,
            self.plus1,
            self.kopija_Fv,
            self.plus2,
            self.kopija_Fd,
        )
# ---------------------------------------------------------------------------------------------------------------------------------

        self.add(self.kopija_Fd)
        self.play(man.Write(self.plus2))
        self.play(self.kopija_Fd.animate.next_to(self.plus2, man.RIGHT))
        self.wait()
        self.play(self.vektorska_enacba.animate.shift(man.UP*1))
        self.play(man.Write(self.mxdd), self.ma.animate.move_to(self.mxdd.get_center() + [0, 1, 0]))
        self.play(man.Write(self.enacaj2), self.enacaj1.animate.move_to(self.enacaj2.get_center() + [0, 1, 0]))
        self.play(man.Write(self.minus1), self.plus1.animate.move_to(self.minus1.get_center() + [0, 1, 0]))
        self.play(man.Write(self.kxy), self.kopija_Fv.animate.move_to(self.kxy.get_center() + [0, 1, 0]))
        self.play(man.Write(self.minus2), self.plus2.animate.move_to(self.minus2.get_center() + [0, 1, 0]))
        self.play(man.Write(self.dxy), self.kopija_Fd.animate.move_to(self.dxy.get_center() + [0, 1, 0]))
        self.wait()
        self.play(man.FadeOut(self.vektorska_enacba))
        self.play(man.Unwrite(self.minus1), man.Unwrite(self.kxy))
        self.play(man.Write(self.minus3))
        self.play(man.Write(self.kx))
        self.play(man.Write(self.plus3))
        self.play(man.Write(self.ky))
        self.play(man.Unwrite(self.minus2), man.Unwrite(self.dxy))
        self.play(man.Write(self.minus4))
        self.play(man.Write(self.dxd))
        self.play(man.Write(self.plus4))
        self.play(man.Write(self.dyd))
        self.wait()

# definiram tukaj elemente, ker so premaknjeni glede na njihovo originalno pozicijo -----------------------------------------------
        self.plus5 = man.MathTex("+").next_to(self.mxdd, man.RIGHT)

        self.dxd_help = self.dxd.copy().next_to(self.plus5, man.RIGHT)

        self.lok3 = man.Arc(
            arc_center = [(1/2)*(self.dxd.get_center()[0] + self.dxd_help.get_center()[0]), self.dxd.get_center()[1], 0],
            radius = (1/2)*(self.dxd.get_center()[0] - self.dxd_help.get_center()[0]),
            start_angle = 0,
            angle = man.PI,
            )
        
        self.ky_help = self.ky.copy().next_to(self.plus4, man.LEFT)

        self.shift1 = self.ky_help.get_center()[0] - self.ky.get_center()[0]
# ---------------------------------------------------------------------------------------------------------------------------------

        self.play(man.FadeOut(self.minus4), man.Write(self.plus5), man.MoveAlongPath(self.dxd, self.lok3),
                  self.ky.animate.shift(self.shift1*man.RIGHT),
                  self.plus3.animate.shift(self.shift1*man.RIGHT),
                  self.kx.animate.shift(self.shift1*man.RIGHT),
                  self.minus3.animate.shift(self.shift1*man.RIGHT),
                  self.enacaj2.animate.shift(self.shift1*man.RIGHT))
        
# definiram tukaj elemente, ker so premaknjeni glede na njihovo originalno pozicijo -----------------------------------------------
        self.plus6 = man.MathTex("+").next_to(self.dxd, man.RIGHT)

        self.kx_help = self.kx.copy().next_to(self.plus6, man.RIGHT)

        self.lok4 = man.Arc(
            arc_center = [(1/2)*(self.kx.get_center()[0] + self.kx_help.get_center()[0]), self.kx.get_center()[1], 0],
            radius = (1/2)*(self.kx.get_center()[0] - self.kx_help.get_center()[0]),
            start_angle = 0,
            angle = man.PI,
            )
        
        self.enacaj2_help = self.enacaj2.copy().next_to(self.plus3, man.LEFT)

        self.shift2 = self.enacaj2_help.get_center()[0] - self.enacaj2.get_center()[0]
# ---------------------------------------------------------------------------------------------------------------------------------

        self.play(man.FadeOut(self.minus3), man.Write(self.plus6), man.MoveAlongPath(self.kx, self.lok4),
                  self.enacaj2.animate.shift(self.shift2*man.RIGHT))

# definiram tukaj elemente, ker so premaknjeni glede na njihovo originalno pozicijo -----------------------------------------------
        self.dyd_help = self.dyd.copy().next_to(self.enacaj2, man.RIGHT)

        self.lok5 = man.Arc(
            arc_center = [(1/2)*(self.dyd.get_center()[0] + self.dyd_help.get_center()[0]), self.dyd.get_center()[1], 0],
            radius = (1/2)*(self.dyd.get_center()[0] - self.dyd_help.get_center()[0]),
            start_angle = 0,
            angle = man.PI,
            )
        
        self.plus3_help = self.plus3.copy().next_to(self.dyd_help, man.RIGHT)

        self.shift3 = self.plus3_help.get_center()[0] - self.plus3.get_center()[0]

        self.skalarna_enacba = man.Group(
            self.mxdd,
            self.plus5,
            self.dxd,
            self.plus6,
            self.kx,
            self.enacaj2,
            self.dyd,
            self.plus3,
            self.ky,
        )

        self.mmxdd = man.MathTex("\frac{m}{m} \ddot{x}")
# ---------------------------------------------------------------------------------------------------------------------------------

        self.play(man.FadeOut(self.plus4), man.MoveAlongPath(self.dyd, self.lok5),
                  self.ky.animate.shift(self.shift3*man.RIGHT),
                  self.plus3.animate.shift(self.shift3*man.RIGHT))
        self.play(self.skalarna_enacba.animate.shift(0.25*man.RIGHT))
        self.wait()

# definiram tukaj elemente, ker so premaknjeni glede na njihovo originalno pozicijo -----------------------------------------------
        self.mm = man.MathTex("\\frac{m}{m}").move_to(self.mxdd.get_center() + [-0.2, -0.06, 0])

        self.xdd = man.MathTex("\ddot{x}").move_to(self.mxdd.get_center() + [0.21, 0, 0])

        self.dmx = man.MathTex("\\frac{d}{m}").move_to(self.dxd.get_center() + [-0.3, 0, 0])

        self.xd = man.MathTex("\dot{x}").move_to(self.dxd.get_center() + [0.12, 0, 0])

        self.kmx = man.MathTex("\\frac{k}{m}").move_to(self.kx.get_center() + [-0.3, 0, 0])

        self.x = man.MathTex("x").move_to(self.kx.get_center() + [0.13, -0.06, 0])
        
        self.dmy = man.MathTex("\\frac{d}{m}").move_to(self.dyd.get_center() + [-0.3, 0, 0])

        self.yd = man.MathTex("\dot{y}").move_to(self.dyd.get_center() + [0.12, 0, 0])

        self.kmy = man.MathTex("\\frac{k}{m}").move_to(self.ky.get_center() + [-0.3, 0, 0])

        self.y = man.MathTex("y").move_to(self.ky.get_center() + [0.13, -0.06, 0])

        self.ddonx = man.MathTex("2 \delta \omega_0").move_to(self.dmx.get_center() + [-0.25, 0, 0])

        self.onkx = man.MathTex("\omega_0^2").move_to(self.kmx.get_center())

        self.ddony = man.MathTex("2 \delta \omega_0").move_to(self.dmy.get_center() + [0.25, 0, 0])

        self.onky = man.MathTex("\omega_0^2").move_to(self.kmy.get_center() + [0.5, 0, 0])
# ---------------------------------------------------------------------------------------------------------------------------------

        self.play(man.FadeIn(self.deljeno_m))
        self.add(self.xdd, self.xd, self.x, self.yd, self.y)
        self.play(man.FadeOut(self.deljeno_m, self.mxdd))
        self.play(man.Write(self.mm), self.plus5.animate.shift(0.12*man.LEFT), man.FadeOut(self.dxd))
        self.play(man.Write(self.dmx), self.plus6.animate.shift(0.12*man.LEFT), man.FadeOut(self.kx))
        self.play(man.Write(self.kmx), self.enacaj2.animate.shift(0.12*man.LEFT), man.FadeOut(self.dyd))
        self.play(man.Write(self.dmy), self.plus3.animate.shift(0.12*man.LEFT), (man.FadeOut(self.ky)))
        self.play(man.Write(self.kmy))
        self.wait()
        self.play(man.Unwrite(self.mm))
        self.play(self.xdd.animate.shift(0.5*man.LEFT),
                  self.plus5.animate.shift(0.5*man.LEFT),
                  man.Transform(self.dmx, self.ddonx))
        self.play(man.Transform(self.kmx, self.onkx))
        self.remove(self.ddonx, self.onkx)
        self.play(self.yd.animate.shift(0.5*man.RIGHT),
                  self.plus3.animate.shift(0.5*man.RIGHT),
                  self.kmy.animate.shift(0.5*man.RIGHT),
                  self.y.animate.shift(0.5*man.RIGHT),
                  man.Transform(self.dmy, self.ddony))
        self.play(man.Transform(self.kmy, self.onky))
        self.remove(self.ddony, self.onky)
        self.wait()
        self.play(self.sistem2.animate.shift(3*man.RIGHT),
                  self.x_vecji_od_y.animate.shift(8.4*man.LEFT + 0.5*man.UP),
                  self.xd_vecji_od_yd.animate.shift(8.4*man.LEFT + 0.5*man.UP),
                  self.nihanje_podlage.animate.shift(8.4*man.LEFT + 0.5*man.UP))
        self.wait()

# definiram tukaj elemente, ker so premaknjeni glede na njihovo originalno pozicijo -----------------------------------------------
        self.yt = man.MathTex("y(t) =").move_to(self.nihanje_podlage.get_center() + [-1.01, 0, 0])

        self.ydef = man.MathTex("Y \\mathrm{sin} (\\omega t)").next_to(self.yt, man.RIGHT, buff = 0.18)

        self.odvod1 = man.MathTex("/ \\frac{\mathrm{d}}{\mathrm{d}t}").next_to(self.ydef, man.RIGHT)

        self.ytd = man.MathTex("\dot{y}(t) =").move_to(self.yt.get_center() + [0, -1, 0])

        self.yddef = man.MathTex("\omega Y \\mathrm{cos} (\\omega t)").next_to(self.ytd, man.RIGHT, buff = 0.18)
# ---------------------------------------------------------------------------------------------------------------------------------

        self.add(self.yt, self.ydef)
        self.remove(self.nihanje_podlage)
        self.play(man.FadeIn(self.odvod1))
        self.play(man.FadeOut(self.odvod1))
        self.play(man.Write(self.ytd))
        self.play(man.Write(self.yddef))
        self.wait()
        self.play(self.plus3.animate.shift(2*man.RIGHT),
                  self.kmy.animate.shift(2*man.RIGHT),
                  self.y.animate.shift(2*man.RIGHT),
                  self.yddef.animate.move_to(self.yd.get_center() + [1, -0.02, 0]),
                  man.FadeOut(self.ytd, self.yd))
        self.play(self.ydef.animate.move_to(self.y.get_center() + [0.8, 0.02, 0]),
                  man.FadeOut(self.yt, self.y))
        self.wait()

# definiram tukaj elemente, ker so premaknjeni glede na njihovo originalno pozicijo -----------------------------------------------
        self.de_pred_nastavkom = man.Group(
            self.xdd,
            self.plus5,
            self.dmx, self.xd,
            self.plus6,
            self.kmx, self.x,
            self.enacaj2,
            self.dmy, self.yddef,
            self.plus3,
            self.kmy, self.ydef,
        )
# ---------------------------------------------------------------------------------------------------------------------------------

        self.play(self.sistem2.animate.shift(0.5*man.RIGHT + 0.7*man.DOWN),
                  self.x_vecji_od_y.animate.move_to(self.masa.get_center() + [0.5, 1.2, 0]),
                  self.xd_vecji_od_yd.animate.move_to(self.masa.get_center() + [0.5, 0.6, 0]),
                  self.de_pred_nastavkom.animate.shift(3.2*man.UP))
        self.wait()
        self.play(man.Write(self.nastavek))
        self.play(man.Write(self.xt))
        self.play(man.Write(self.xdef))
        self.wait()
        self.play(man.FadeIn(self.odvod2))
        self.play(man.FadeOut(self.odvod2))
        self.play(man.Write(self.xtd))
        self.play(man.Write(self.xddef))
        self.wait()
        self.play(man.FadeIn(self.odvod3))
        self.play(man.FadeOut(self.odvod3))
        self.play(man.Write(self.xtdd))
        self.play(man.Write(self.xdddef))
        self.wait()
        self.play(man.FadeOut(self.sistem2, self.x_vecji_od_y, self.xd_vecji_od_yd, self.nastavek))
        self.play(self.xt.animate.shift(4.5*man.RIGHT), self.xdef.animate.shift(4.5*man.RIGHT),
                  self.xtd.animate.shift(4.5*man.RIGHT), self.xddef.animate.shift(4.5*man.RIGHT),
                  self.xtdd.animate.shift(4.5*man.RIGHT), self.xdddef.animate.shift(4.5*man.RIGHT))
        self.play(man.Write(self.vty_predznak))
        self.play(man.Write(self.vty_velikost))
        self.play(man.Write(self.vty_smer), man.Unwrite(self.plus3), man.Unwrite(self.kmy), man.Unwrite(self.ydef))
        self.play(man.Write(self.vdy_predznak))
        self.play(man.Write(self.vdy_velikost))
        self.play(man.Write(self.vdy_smer), man.Unwrite(self.dmy), man.Unwrite(self.yddef))
        self.play(man.Write(self.enacaj3), man.Unwrite(self.enacaj2))
        self.play(man.Write(self.vtx_predznak))
        self.play(man.Write(self.vtx_velikost))
        self.play(man.Write(self.vtx_smer), man.Unwrite(self.plus6), man.Unwrite(self.kmx), man.Unwrite(self.x), man.Unwrite(self.xdef), man.Unwrite(self.xt))
        self.wait()

# ---------------------------------------------------------------------------------------------- klic

if __name__ == "__main__":
    scena = PasivnaVibroizolacija()
    scena

# cd Desktop\PREDMETI\3._letnik\2._semester\IDPR\LADISK\projekt
# manim -pql pv.py PasivnaVibroizolacija
