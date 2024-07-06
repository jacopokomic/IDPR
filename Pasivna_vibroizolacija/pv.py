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

        self.s1 = man.Line(
            start = [-1, -3.2, 0],
            end = [-0.8, -3, 0],
            color = man.GRAY,
        )

        self.s2 = man.Line(
            start = [-0.8, -3.2, 0],
            end = [-0.6, -3, 0],
            color = man.GRAY,
        )

        self.s3 = man.Line(
            start = [-0.6, -3.2, 0],
            end = [-0.4, -3, 0],
            color = man.GRAY,
        )

        self.s4 = man.Line(
            start = [-0.4, -3.2, 0],
            end = [-0.2, -3, 0],
            color = man.GRAY,
        )

        self.s5 = man.Line(
            start = [-0.2, -3.2, 0],
            end = [0, -3, 0],
            color = man.GRAY,
        )

        self.s6 = man.Line(
            start = [0, -3.2, 0],
            end = [0.2, -3, 0],
            color = man.GRAY,
        )

        self.s7 = man.Line(
            start = [0.2, -3.2, 0],
            end = [0.4, -3, 0],
            color = man.GRAY,
        )

        self.s8 = man.Line(
            start = [0.4, -3.2, 0],
            end = [0.6, -3, 0],
            color = man.GRAY,
        )

        self.s9 = man.Line(
            start = [0.6, -3.2, 0],
            end = [0.8, -3, 0],
            color = man.GRAY,
        )

        self.s10 = man.Line(
            start = [0.8, -3.2, 0],
            end = [1, -3, 0],
            color = man.GRAY,
        )

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

        self.masa2 = self.masa.copy()
        self.m2 = self.m.copy()
        self.podlaga2 = self.podlaga.copy()
        self.vzmet2 = self.vzmet.copy()
        self.k2 = self.k.copy()
        self.dusilka_spodaj2 = self.dusilka_spodaj.copy()
        self.dusilka_zgoraj2 = self.dusilka_zgoraj.copy()
        self.d2 = self.d.copy()

        self.sistem = man.Group(
            self.masa, self.m,
            self.podlaga,
            self.vzmet, self.k,
            self.dusilka_spodaj, self.dusilka_zgoraj, self.d,
        )

        self.sistem_kopija = self.sistem.copy()

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

        self.vty_predznak = man.MathTex("+").move_to([-5.25, -2, 0])

        self.vty_velikost = man.MathTex("\\omega_0^2 Y", color = man.MAROON_B).move_to([-3.5, -2, 0])

        self.vty_smer = man.MathTex("\\mathrm{sin} (\\omega t)").move_to([-1.5, -2, 0])

        self.vdy_predznak = man.MathTex("+").move_to([-5.25, -1.2, 0])

        self.vdy_velikost = man.MathTex("2 \\delta \\omega_0 \\omega Y", color = man.MAROON_E).move_to([-3.5, -1.2, 0])

        self.vdy_smer = man.MathTex("\\mathrm{cos} (\\omega t)").move_to([-1.5, -1.2, 0])

        self.enacaj3 = man.MathTex("=").move_to([-3.5, -0.4, 0])

        self.vtx_predznak = man.MathTex("+").move_to([-5.25, 0.4, 0])

        self.vtx_velikost = man.MathTex("\\omega_0^2 X", color = man.BLUE_C).move_to([-3.5, 0.4, 0])

        self.vtx_smer = man.MathTex("\\mathrm{sin} (\\omega t - \\varphi_\\mathrm{z})").move_to([-1, 0.4, 0])

        self.vdx_predznak = man.MathTex("+").move_to([-5.25, 1.2, 0])

        self.vdx_velikost = man.MathTex("2 \\delta \\omega_0 \\omega X", color = man.BLUE_D).move_to([-3.5, 1.2, 0])

        self.vdx_smer = man.MathTex("\\mathrm{cos} (\\omega t - \\varphi_\\mathrm{z})").move_to([-1, 1.2, 0])

        self.vvx_predznak = man.MathTex("-").move_to([-5.25, 2, 0])

        self.vvx_velikost = man.MathTex("\\omega^2 X", color = man.BLUE_E).move_to([-3.5, 2, 0])

        self.vvx_smer = man.MathTex("\\mathrm{sin} (\\omega t - \\varphi_\\mathrm{z})").move_to([-1, 2, 0])

        self.gibalna_enacba = man.Group(
            self.vty_predznak, self.vty_velikost, self.vty_smer,
            self.vdy_predznak, self.vdy_velikost, self.vdy_smer,
            self.enacaj3,
            self.vtx_predznak, self.vtx_velikost, self.vtx_smer,
            self.vdx_predznak, self.vdx_velikost, self.vdx_smer,
            self.vvx_predznak, self.vvx_velikost, self.vvx_smer,
        )

        self.ref = man.NumberLine(
            x_range = [0, 5],
            length = 5,
            include_ticks = False,
            include_tip = True,
            tip_width = 0.2,
            tip_height = 0.2,
        ).move_to([2.5, -2, 0])

        self.referenca = man.Tex("referenca").next_to(self.ref.get_end(), man.DOWN, buff = 0.15).scale(0.4)

        self.vty = man.Arrow(
            start = self.ref.get_start(),
            end = self.ref.get_start() + [2.5 * man.np.cos((5/18) * man.PI), 2.5 * man.np.sin((5/18) * man.PI), 0],
            color = man.MAROON_B,
            max_stroke_width_to_length_ratio = 3.2,
            max_tip_length_to_length_ratio = 0.16,
            stroke_width = 5,
            buff = 0,
        )

        self.ot = man.Angle(
            line1 = self.ref,
            line2 = self.vty,
            radius = 0.5,
        )

        self.ot_velikost = man.MathTex("\\omega t").next_to(self.ot.get_center() + [-0.15, 0.2, 0])

        self.vtys = man.DashedLine(
            start = self.vty.get_end(),
            end = self.vty.get_end() + [2 * man.np.cos((5/18) * man.PI), 2 * man.np.sin((5/18) * man.PI), 0],
            stroke_opacity = 0.2,
        )

        self.vdy = man.Arrow(
            start = self.vty.get_end(),
            end = self.vty.get_end() + [-1 * man.np.sin((5/18) * man.PI), 1 * man.np.cos((5/18) * man.PI), 0],
            color = man.MAROON_E,
            max_stroke_width_to_length_ratio = 8,
            max_tip_length_to_length_ratio = 0.40,
            stroke_width = 5,
            buff = 0,
        )

        self.pk1 = man.Angle(
            line1 = self.vdy,
            line2 = self.vty,
            quadrant = (1, -1),
            elbow = True,
        )

        self.vdys = man.DashedLine(
            start = self.vdy.get_end(),
            end = self.vdy.get_end() + [-2 * man.np.sin((5/18) * man.PI), 2 * man.np.cos((5/18) * man.PI), 0],
            stroke_opacity = 0.2,
        )

        self.vk = man.Arrow(
            start = self.ref.get_start(),
            end = self.vdy.get_end(),
            color = man.RED,
            max_stroke_width_to_length_ratio = 3.713,
            max_tip_length_to_length_ratio = 0.186,
            stroke_width = 5,
            buff = 0,
        )

        self.vtx = man.Arrow(
            start = self.ref.get_start(),
            end = self.ref.get_start() + [5 * man.np.cos((1/18) * man.PI), 5 * man.np.sin((1/18) * man.PI), 0],
            color = man.BLUE_C,
            max_stroke_width_to_length_ratio = 2,
            max_tip_length_to_length_ratio = 0.10,
            stroke_width = 5,
            buff = 0,
        )

        self.phiz = man.Angle(
            line1 = self.vty,
            line2 = self.vtx,
            radius = 1.5,
            other_angle = True,
        )

        self.phiz_velikost = man.MathTex("\\varphi_\\mathrm{z}").next_to(self.phiz.get_center() + [-0.05, 0, 0])

        self.vtxs = man.DashedLine(
            start = self.vtx.get_end(),
            end = self.vtx.get_end() + [2 * man.np.cos((1/18) * man.PI), 2 * man.np.sin((1/18) * man.PI), 0],
            stroke_opacity = 0.2,
        )

        self.vdx = man.Arrow(
            start = self.vtx.get_end(),
            end = self.vtx.get_end() + [-2.373 * man.np.sin((1/18) * man.PI), 2.373 * man.np.cos((1/18) * man.PI), 0],
            color = man.BLUE_D,
            max_stroke_width_to_length_ratio = 3.371,
            max_tip_length_to_length_ratio = 0.169,
            stroke_width = 5,
            buff = 0,
        )

        self.pk2 = man.Angle(
            line1 = self.vdx,
            line2 = self.vtx,
            quadrant = (1, -1),
            elbow = True,
        )

        self.vdxs = man.DashedLine(
            start = self.vdx.get_end(),
            end = self.vdx.get_end() + [-2 * man.np.sin((1/18) * man.PI), 2 * man.np.cos((1/18) * man.PI), 0],
            stroke_opacity = 0.2,
        )

        self.vvx = man.Arrow(
            start = self.vdx.get_end(),
            end = self.vdx.get_end() + [-3.728 * man.np.cos((1/18) * man.PI), -3.728 * man.np.sin((1/18) * man.PI), 0],
            color = man.BLUE_E,
            max_stroke_width_to_length_ratio = 2.682,
            max_tip_length_to_length_ratio = 0.134,
            stroke_width = 5,
            buff = 0,
        )

        self.pk3 = man.Angle(
            line1 = self.vvx,
            line2 = self.vdx,
            quadrant = (1, -1),
            elbow = True,
        )

        self.vvxs = man.DashedLine(
            start = self.vvx.get_start(),
            end = self.vvx.get_start() + [2 * man.np.cos((1/18) * man.PI), 2 * man.np.sin((1/18) * man.PI), 0],
            stroke_opacity = 0.2,
        )

        self.nastavek_xt = man.MathTex("x(t) =").move_to([-5.15, 2.5, 0])

        self.nastavek_X = man.MathTex("X").next_to(self.nastavek_xt, man.RIGHT, buff = 0.1)

        self.nastavek_sin = man.MathTex("\\mathrm{sin} (\\omega t -").next_to(self.nastavek_X, man.RIGHT, buff = 0.1).shift(0.04*man.DOWN)

        self.nastavek_phiz = man.MathTex("\\varphi_\\mathrm{z}").next_to(self.nastavek_sin, man.RIGHT, buff = 0.06)

        self.nastavek_zaklepaj = man.MathTex(")").next_to(self.nastavek_phiz, man.RIGHT, buff = 0.02)

        self.vdx_kopija = self.vdx.copy().set_opacity(0.5)

        self.pitagora = man.Tex("Pitagorov izrek:").move_to([-3.75, -1, 0])

        self.z = man.MathTex("Z", color = man.RED).move_to(self.vk.get_center() + [-0.3, 0, 0])

        self.z1 = man.MathTex("Z^2 =").move_to([-6, -2, 0])

        self.vsota_kvadratov_1_1 = man.MathTex("(\\omega_0^2 Y)^2").next_to(self.z1, man.RIGHT)

        self.plus7 = man.MathTex("+").next_to(self.vsota_kvadratov_1_1, man.RIGHT)

        self.vsota_kvadratov_1_2 = man.MathTex("(2 \\delta \\omega_0 \\omega Y)^2").next_to(self.plus7, man.RIGHT)

        self.z2 = man.MathTex("Z^2 =").move_to([-6, -3, 0])

        self.vsota_kvadratov_2_1 = man.MathTex("(\\omega_0^2 X - \\omega^2 X)^2").next_to(self.z2, man.RIGHT)

        self.plus8 = man.MathTex("+").next_to(self.vsota_kvadratov_2_1, man.RIGHT)

        self.vsota_kvadratov_2_2 = man.MathTex("(2 \\delta \\omega_0 \\omega X)^2").next_to(self.plus8, man.RIGHT)

        self.enacaj4 = man.MathTex("=").move_to([-0.8, -3, 0])

        self.xy = man.MathTex("\\frac{X}{Y} =").move_to([-6, 0.5, 0])

        self.koren1 = man.MathTex("\\sqrt{\\frac{1 + (2 \\delta \\frac{\\omega}{\\omega_0})^2}{(1 - \\frac{\\omega^2}{\\omega_0^2})^2 + (2 \\delta \\frac{\\omega}{\\omega_0})^2}}")
        self.koren1.next_to(self.xy, man.RIGHT) # ker je dolgo

        self.alpha = man.Angle(
            line1 = self.vk,
            line2 = self.vty,
            radius = 1.7,
            other_angle = True,
        )

        self.alpha_velikost = man.MathTex("\\alpha").move_to(self.alpha.get_start() + [-0.3, 0, 0])

        self.gamma = man.Angle(
            line1 = self.vk,
            line2 = self.vtx,
            radius = 1.3,
            other_angle = True,
        )

        self.gamma_velikost = man.MathTex("\\gamma").move_to(self.gamma.get_start() + [-0.3, 0, 0])

        self.phiz_enacba = man.MathTex("\\varphi_\\mathrm{z} = \\gamma - \\alpha").move_to([-3.75, -1.5, 0])

        self.tan_alpha = man.MathTex("\\mathrm{tan} (\\alpha) =").move_to([-6, -3, 0])

        self.tan_alpha1 = man.MathTex("\\frac{2 \\delta \\omega_0 \\omega Y}{\\omega_0^2 Y}").next_to(self.tan_alpha)

        self.tan_gamma = man.MathTex("\\mathrm{tan} (\\gamma) =").move_to([-1, -3, 0])

        self.tan_gamma1 = man.MathTex("\\frac{2 \\delta \\omega_0 \\omega X}{\\omega_0^2 X - \\omega^2 X}").next_to(self.tan_gamma)

        self.r = man.MathTex("r = \\frac{\\omega}{\\omega_0}", color = man.GRAY).move_to([5, -3, 0])

        self.koren2 = man.MathTex("\\sqrt{\\frac{1 + (2 \\delta r)^2}{(1 - r^2)^2 + (2 \\delta r)^2}}").next_to(self.xy, man.RIGHT)

        self.tan_alpha2 = man.MathTex("2 \\delta r").next_to(self.tan_alpha)

        self.tan_gamma2 = man.MathTex("\\frac{2 \\delta r}{1 - r^2}").next_to(self.tan_gamma)

        self.tan_phiz = man.MathTex("\\mathrm{tan} (\\varphi_\\mathrm{z}) = \\frac{2 \\delta r^3}{1 - r^2 + (2 \\delta r)^2}").move_to([-3.75, -1.5, 0])

        self.kazalcni_diagram = man.Group(
            self.ref, self.referenca,
            self.vty, self.vtys, self.vty_velikost, self.vty_smer,
            self.ot, self.ot_velikost,
            self.vdy, self.vdys, self.vdy_velikost, self.vdy_smer,
            self.pk1,
            self.vk,
            self.vtx, self.vtxs, self.vtx_velikost, self.vtx_smer,
            self.phiz, self.phiz_velikost,
            self.vdx, self.vdxs, self.vdx_velikost, self.vdx_smer,
            self.pk2,
            self.vvx, self.vvxs, self.vvx_velikost, self.vvx_smer,
            self.pk3,
            self.vdx_kopija,
            self.alpha, self.alpha_velikost,
            self.gamma, self.gamma_velikost,
        )

        self.nastavek_enacba = man.Group(
            self.nastavek_xt,
            self.nastavek_X,
            self.nastavek_sin,
            self.nastavek_phiz,
            self.nastavek_zaklepaj,
        )

        self.delta = man.MathTex("\\delta = 0,1").scale(0.8).move_to([-5, 2, 0])

        self.tabela = man.MathTable([
            ["r", "0,5", "1", "2"],
            ["\\frac{X}{Y}", "1,33", "5,10", "0,36"],
            ["\\varphi_\\mathrm{z}", "0,03\\ \\mathrm{rad}", "1,37\\ \\mathrm{rad}", "2,63\\ \\mathrm{rad}"]
        ]).scale(0.8).move_to([1.5, 0, 0])

        self.tabela[0][1].set_color(man.GREEN)
        self.tabela[0][5].set_color(man.GREEN)
        self.tabela[0][9].set_color(man.GREEN)
        self.tabela[0][2].set_color(man.YELLOW_D)
        self.tabela[0][6].set_color(man.YELLOW_D)
        self.tabela[0][10].set_color(man.YELLOW_D)
        self.tabela[0][3].set_color(man.BLUE)
        self.tabela[0][7].set_color(man.BLUE)
        self.tabela[0][11].set_color(man.BLUE)

        self.xy_r = man.Axes(
            x_range = [0, 3.5],
            y_range = [0, 3.5],
            x_length = 4,
            y_length = 2.5,
            axis_config = {"tip_width": 0.2, "tip_height": 0.2, "include_ticks": True, "include_numbers": True},
        ).move_to([-1, -2, 0])

        self.x_label_xy_r = man.MathTex("r").scale(0.8).next_to(self.xy_r.x_axis.get_end(), man.DOWN)
        self.y_label_xy_r = man.MathTex("\\frac{X}{Y}").scale(0.8).move_to(self.xy_r.y_axis.get_end() + [-0.3, 0.3, 0])

        self.xy_r_ref1 = man.DashedLine(
            start = self.xy_r.coords_to_point(1, 0),
            end = self.xy_r.coords_to_point(1, 3.5),
            stroke_opacity = 0.1,
        )

        self.xy_r_ref2 = man.DashedLine(
            start = self.xy_r.coords_to_point(0, 1),
            end = self.xy_r.coords_to_point(3.5, 1),
            stroke_opacity = 0.1,
        )

        self.phiz_r = man.Axes(
            x_range = [0, 3.5],
            y_range = [0, man.PI + 0.5, (1/2) * man.PI],
            x_length = 4,
            y_length = 2.5,
            x_axis_config={"tip_width": 0.2, "tip_height": 0.2, "include_ticks": True, "include_numbers": True},
            y_axis_config={"tip_width": 0.2, "tip_height": 0.2, "include_ticks": True, "include_numbers": False},
        ).move_to([4, -2, 0])

        self.pi_label = man.MathTex("\\pi").scale(0.75).next_to(self.phiz_r.coords_to_point(0, man.PI), man.LEFT)
        self.pi_polovic_label = man.MathTex("\\frac{\\pi}{2}").scale(0.75).next_to(self.phiz_r.coords_to_point(0, (1/2) * man.PI), man.LEFT)

        self.x_label_phiz_r = man.MathTex("r").scale(0.8).next_to(self.phiz_r.x_axis.get_end(), man.DOWN)
        self.y_label_phiz_r = man.MathTex("\\varphi_\\mathrm{z}").scale(0.8).next_to(self.phiz_r.y_axis.get_end(), man.LEFT)

        self.phiz_r_ref1 = man.DashedLine(
            start = self.phiz_r.coords_to_point(1, 0),
            end = self.phiz_r.coords_to_point(1, 3.14),
            stroke_opacity = 0.1,
        )

        self.phiz_r_ref2 = man.DashedLine(
            start = self.phiz_r.coords_to_point(0, 1.57),
            end = self.phiz_r.coords_to_point(3.5, 1.57),
            stroke_opacity = 0.1,
        )

        self.phiz_r_ref3 = man.DashedLine(
            start = self.phiz_r.coords_to_point(0, 3.14),
            end = self.phiz_r.coords_to_point(3.5, 3.14),
            stroke_opacity = 0.1,
        )

        self.t1g1 = man.Dot(
            color = man.GREEN,
        ).move_to(self.xy_r.coords_to_point(0.5, 1.33))

        self.t1g1x = man.DashedLine(
            start = self.t1g1,
            end = self.xy_r.coords_to_point(0.5, 0),
            color = man.GREEN,
            stroke_opacity = 0.5,
        )

        self.t1g1y = man.DashedLine(
            start = self.t1g1,
            end = self.xy_r.coords_to_point(0, 1.33),
            color = man.GREEN,
            stroke_opacity = 0.5,
        )

        self.t1g2 = man.Dot(
            color = man.GREEN,
        ).move_to(self.phiz_r.coords_to_point(0.5, 0.03))

        self.t1g2x = man.DashedLine(
            start = self.t1g2,
            end = self.phiz_r.coords_to_point(0.5, 0),
            color = man.GREEN,
            stroke_opacity = 0.5,
        )

        self.t1g2y = man.DashedLine(
            start = self.t1g2,
            end = self.phiz_r.coords_to_point(0, 0.03),
            color = man.GREEN,
            stroke_opacity = 0.5,
        )

        self.t2g1 = man.Dot(
            color = man.YELLOW_D,
        ).move_to(self.xy_r.coords_to_point(1, 5.10))

        self.t2g1x = man.DashedLine(
            start = self.t2g1,
            end = self.xy_r.coords_to_point(1, 0),
            color = man.YELLOW_D,
            stroke_opacity = 0.5,
        )

        self.t2g1y = man.DashedLine(
            start = self.t2g1,
            end = self.xy_r.coords_to_point(0, 5.10),
            color = man.YELLOW_D,
            stroke_opacity = 0.5,
        )

        self.t2g2 = man.Dot(
            color = man.YELLOW_D,
        ).move_to(self.phiz_r.coords_to_point(1, 1.37))

        self.t2g2x = man.DashedLine(
            start = self.t2g2,
            end = self.phiz_r.coords_to_point(1, 0),
            color = man.YELLOW_D,
            stroke_opacity = 0.5,
        )

        self.t2g2y = man.DashedLine(
            start = self.t2g2,
            end = self.phiz_r.coords_to_point(0, 1.37),
            color = man.YELLOW_D,
            stroke_opacity = 0.5,
        )

        self.t3g1 = man.Dot(
            color = man.BLUE,
        ).move_to(self.xy_r.coords_to_point(2, 0.36))

        self.t3g1x = man.DashedLine(
            start = self.t3g1,
            end = self.xy_r.coords_to_point(2, 0),
            color = man.BLUE,
            stroke_opacity = 0.5,
        )

        self.t3g1y = man.DashedLine(
            start = self.t3g1,
            end = self.xy_r.coords_to_point(0, 0.36),
            color = man.BLUE,
            stroke_opacity = 0.5,
        )

        self.t3g2 = man.Dot(
            color = man.BLUE,
        ).move_to(self.phiz_r.coords_to_point(2, 2.63))

        self.t3g2x = man.DashedLine(
            start = self.t3g2,
            end = self.phiz_r.coords_to_point(2, 0),
            color = man.BLUE,
            stroke_opacity = 0.5,
        )

        self.t3g2y = man.DashedLine(
            start = self.t3g2,
            end = self.phiz_r.coords_to_point(0, 2.63),
            color = man.BLUE,
            stroke_opacity = 0.5,
        )

        self.xy_po_r = self.xy_r.plot(lambda x: man.np.sqrt((1 + (2*0.1*x)**2)/((1 - x**2)**2 + (2*0.1*x)**2)), [0, 3.5])

        self.phiz_po_r = self.phiz_r.plot(lambda x: man.np.arctan2(2*0.1*(x**3), 1 - x**2 + (2*0.1*x)**2), [0, 3.5])

        self.graf_xy = man.Group(
            self.xy_r,
            self.x_label_xy_r, self.y_label_xy_r,
            self.xy_r_ref1, self.xy_r_ref2,
            self.xy_po_r,
            self.t1g1, self.t1g1x, self.t1g1y,
            self.t2g1, self.t2g1x, self.t2g1y,
            self.t3g1, self.t3g1x, self.t3g1y,
        )

        self.graf_phiz = man.Group(
            self.phiz_r,
            self.pi_label, self.pi_polovic_label,
            self.x_label_phiz_r, self.y_label_phiz_r,
            self.phiz_r_ref1, self.phiz_r_ref2, self.phiz_r_ref3,
            self.phiz_po_r,
            self.t1g2, self.t1g2x, self.t1g2y,
            self.t2g2, self.t2g2x, self.t2g2y,
            self.t3g2, self.t3g2x, self.t3g2y,
        )

        self.delta2 = man.MathTex("\\delta = 0,3", color = man.PURPLE_B).scale(0.8).move_to([0, 2, 0])

        self.xy_po_r2 = self.xy_r.plot(lambda x: man.np.sqrt((1 + (2*0.3*x)**2)/((1 - x**2)**2 + (2*0.3*x)**2)), [0, 3.5]).set_color(man.PURPLE_B).shift(2*man.LEFT)
        
        self.phiz_po_r2 = self.phiz_r.plot(lambda x: man.np.arctan2(2*0.3*(x**3), 1 - x**2 + (2*0.3*x)**2), [0, 3.5]).set_color(man.PURPLE_B).shift(1*man.LEFT)

        self.delta3 = man.MathTex("\\delta = 0,8", color = man.PURPLE_E).scale(0.8).move_to([4, 2, 0])

        self.xy_po_r3 = self.xy_r.plot(lambda x: man.np.sqrt((1 + (2*0.8*x)**2)/((1 - x**2)**2 + (2*0.8*x)**2)), [0, 3.5]).set_color(man.PURPLE_E).shift(2*man.LEFT)
        
        self.phiz_po_r3 = self.phiz_r.plot(lambda x: man.np.arctan2(2*0.8*(x**3), 1 - x**2 + (2*0.8*x)**2), [0, 3.5]).set_color(man.PURPLE_E).shift(1*man.LEFT)

        self.presecisce = man.DashedLine(
            start = self.xy_r.coords_to_point(man.np.sqrt(2), 1),
            end = self.xy_r.coords_to_point(man.np.sqrt(2), -0.15),
            color = man.PURPLE_B,
            stroke_opacity = 0.5,
        ).shift(2*man.LEFT)

        self.dva_pod_koren = man.MathTex("\\sqrt{2}").scale(0.75).move_to(self.presecisce.get_end() + [0, -0.24, 0])

        self.ref2 = man.NumberLine(
            x_range = [0, 6],
            length = 6,
            include_ticks = False,
            include_tip = True,
            tip_width = 0.2,
            tip_height = 0.2,
        ).move_to([2, -0.25, 0])

        self.referenca2 = man.Tex("referenca").next_to(self.ref2.get_end(), man.DOWN, buff = 0.15).scale(0.4)

        self.Y = man.Arrow(
            start = self.ref2.get_start(),
            end = self.ref2.get_start() + [1 * 1.5 * man.np.cos((6/16) * man.PI), 1 * 1.5 * man.np.sin((6/16) * man.PI), 0],
            color = man.RED,
            max_stroke_width_to_length_ratio = 6.667,
            max_tip_length_to_length_ratio = 0.333,
            stroke_width = 5,
            buff = 0,
        )

        self.Y_velikost = man.MathTex("Y", color = man.RED).move_to(self.Y.get_center() + [-0.3, 0, 0])

        self.ot2 = man.Angle(
            line1 = self.ref2,
            line2 = self.Y,
            radius = 0.5,
        )

        self.ot2_velikost = man.MathTex("\\omega t").move_to(self.ot2.get_start() + [0.3, 0.3, 0])

        self.Ys = man.DashedLine(
            start = self.Y.get_end(),
            end = self.Y.get_end() + [2 * man.np.cos((6/16) * man.PI), 2 * man.np.sin((6/16) * man.PI), 0],
            stroke_opacity = 0.2,
        )

        self.Y_smer = man.MathTex("\\mathrm{sin} (\\omega t)").scale(0.5).rotate((6/16) * man.PI).move_to(self.Ys.get_end() + [-0.29, -0.33, 0])

        self.X1 = man.Arrow(
            start = self.ref2.get_start(),
            end = self.ref2.get_start() + [1.33 * 1.5 * man.np.cos((6/16) * man.PI - 0.03), 1.33 * 1.5 * man.np.sin((6/16) * man.PI - 0.03), 0],
            color = man.GREEN,
            max_stroke_width_to_length_ratio = 5.013,
            max_tip_length_to_length_ratio = 0.251,
            stroke_width = 5,
            buff = 0,
        )

        self.X1_velikost = man.MathTex("X", color = man.GREEN).move_to(self.X1.get_center() + [0.35, 0.1, 0])

        self.phiz1 = man.Angle(
            line1 = self.Y,
            line2 = self.X1,
            radius = 1,
            other_angle = True,
        )

        self.phiz1_velikost = man.MathTex("\\varphi_\\mathrm{z}").move_to(self.phiz1.get_start() + [-0.35, 0.2, 0])

        self.X1s = man.DashedLine(
            start = self.X1.get_end(),
            end = self.X1.get_end() + [2 * man.np.cos((6/16) * man.PI - 0.03), 2 * man.np.sin((6/16) * man.PI - 0.03), 0],
            stroke_opacity = 0.2,
        )

        self.X1_smer = man.MathTex("\\mathrm{sin} (\\omega t - \\varphi_\\mathrm{z})")
        self.X1_smer.scale(0.5).rotate((6/16) * man.PI - 0.03).move_to(self.X1s.get_end() + [-0.1, -0.7, 0])

        self.X2 = man.Arrow(
            start = self.ref2.get_start(),
            end = self.ref2.get_start() + [5.10 * 1.5 * man.np.cos((6/16) * man.PI - 1.37), 5.10 * 1.5 * man.np.sin((6/16) * man.PI - 1.37), 0],
            color = man.YELLOW_D,
            max_stroke_width_to_length_ratio = 1.307,
            max_tip_length_to_length_ratio = 0.065,
            stroke_width = 5,
            buff = 0,
        )

        self.X2_velikost = man.MathTex("X", color = man.YELLOW_D).move_to(self.X2.get_center() + [0.5, 0.25, 0])

        self.phiz2 = man.Angle(
            line1 = self.Y,
            line2 = self.X2,
            radius = 2,
            other_angle = True,
        )

        self.phiz2_velikost = man.MathTex("\\varphi_\\mathrm{z}").move_to(self.phiz2.get_center() + [0.8, 0, 0])

        self.X2s = man.DashedLine(
            start = self.X2.get_start(),
            end = self.X2.get_start() + [- 2 * man.np.cos((6/16) * man.PI - 1.37), - 2 * man.np.sin((6/16) * man.PI - 1.37), 0],
            stroke_opacity = 0.2,
        )

        self.X2_smer = man.MathTex("\\mathrm{sin} (\\omega t - \\varphi_\\mathrm{z})")
        self.X2_smer.scale(0.5).rotate((6/16) * man.PI - 1.37).move_to(self.X2s.get_end() + [0.7, 0.02, 0])

        self.X3 = man.Arrow(
            start = self.ref2.get_start(),
            end = self.ref2.get_start() + [0.36 * 1.5 * man.np.cos((6/16) * man.PI - 2.63), 0.36 * 1.5 * man.np.sin((6/16) * man.PI - 2.63), 0],
            color = man.BLUE,
            max_stroke_width_to_length_ratio = 18.519,
            max_tip_length_to_length_ratio = 0.926,
            stroke_width = 5,
            buff = 0,
        )

        self.X3_velikost = man.MathTex("X", color = man.BLUE).move_to(self.X3.get_center() + [0.4, 0, 0])

        self.phiz3 = man.Angle(
            line1 = self.Y,
            line2 = self.X3,
            radius = 0.1,
            other_angle = True,
        )

        self.phiz3_velikost = man.MathTex("\\varphi_\\mathrm{z}").move_to(self.phiz3.get_center() + [-0.4, 0, 0])

        self.X3s = man.DashedLine(
            start = self.X3.get_end(),
            end = self.X3.get_end() + [2 * man.np.cos((6/16) * man.PI - 2.63), 2 * man.np.sin((6/16) * man.PI - 2.63), 0],
            stroke_opacity = 0.2,
        )

        self.X3_smer = man.MathTex("\\mathrm{sin} (\\omega t - \\varphi_\\mathrm{z})")
        self.X3_smer.scale(0.5).rotate((6/16) * man.PI - 2.63).move_to(self.X3s.get_end() + [0.11, 0.7, 0])

        self.ref2_kopija = self.ref2.copy()

        self.referenca2_kopija = self.referenca2.copy()

        self.refgor = man.NumberLine(
            x_range = [0, 3],
            length = 3,
            include_ticks = False,
            include_tip = True,
            tip_width = 0.2,
            tip_height = 0.2,
        ).move_to([3, 1.9, 0])

        self.refdol = man.NumberLine(
            x_range = [0, 3],
            length = 3,
            include_ticks = False,
            include_tip = True,
            tip_width = 0.2,
            tip_height = 0.2,
        ).move_to([3, -2.6, 0])

        self.nsdol = self.refdol.get_start()
        self.neY = self.refdol.get_start() + [1 * 0.75 * man.np.cos((6/16) * man.PI), 1 * 0.75 * man.np.sin((6/16) * man.PI), 0]
        self.nsgor = self.refgor.get_start()
        self.neX1 = self.refgor.get_start() + [1.33 * 0.75 * man.np.cos((6/16) * man.PI - 0.03), 1.33 * 0.75 * man.np.sin((6/16) * man.PI - 0.03), 0]
        self.neX2 = self.refgor.get_start() + [5.10 * 0.75 * man.np.cos((6/16) * man.PI - 1.37), 5.10 * 0.75 * man.np.sin((6/16) * man.PI - 1.37), 0]
        self.neX3 = self.refgor.get_start() + [0.36 * 0.75 * man.np.cos((6/16) * man.PI - 2.63), 0.36 * 0.75 * man.np.sin((6/16) * man.PI - 2.63), 0]

        self.masa_pod = man.RoundedRectangle(
            color = man.GRAY,
            fill_color = man.GRAY,
            fill_opacity = 0.5,
            height = 0.5,
            width = 1,
            corner_radius = 0.1,
            ).move_to([-4, 0.25, 0]).shift(0.045*man.UP)

        self.m_pod = man.MathTex("m").scale(0.5).move_to(self.masa_pod.get_center() + [0.3, -0.1, 0])

        self.podlaga_pod = man.Rectangle(
            color = man.GRAY,
            fill_color = man.GRAY,
            fill_opacity = 0.5,
            height = 0.1,
            width = 1,
        ).move_to([-4, -3.05, 0]).shift(0.045*man.UP)

        self.s1_pod = man.Line(
            start = [-4.5, -3.1, 0],
            end = [-4.4, -3, 0],
            color = man.GRAY,
            stroke_width = 2,
        ).shift(0.045*man.UP)

        self.s2_pod = self.s1_pod.copy().move_to(self.s1_pod.get_center() + [0.1, 0, 0])
        self.s3_pod = self.s1_pod.copy().move_to(self.s1_pod.get_center() + [0.2, 0, 0])
        self.s4_pod = self.s1_pod.copy().move_to(self.s1_pod.get_center() + [0.3, 0, 0])
        self.s5_pod = self.s1_pod.copy().move_to(self.s1_pod.get_center() + [0.4, 0, 0])
        self.s6_pod = self.s1_pod.copy().move_to(self.s1_pod.get_center() + [0.5, 0, 0])
        self.s7_pod = self.s1_pod.copy().move_to(self.s1_pod.get_center() + [0.6, 0, 0])
        self.s8_pod = self.s1_pod.copy().move_to(self.s1_pod.get_center() + [0.7, 0, 0])
        self.s9_pod = self.s1_pod.copy().move_to(self.s1_pod.get_center() + [0.8, 0, 0])
        self.s10_pod = self.s1_pod.copy().move_to(self.s1_pod.get_center() + [0.9, 0, 0])

        self.podlaga_pod.add(self.s1_pod, self.s2_pod, self.s3_pod, self.s4_pod, self.s5_pod, self.s6_pod, self.s7_pod, self.s8_pod, self.s9_pod, self.s10_pod)

        self.vzmet_standard_pod = {1: [-1/4 - 4, -3, 0], 2: [-1/4 - 4, -27/10, 0],
                                   3: [-1/2 - 4 + 2*self.korekcija_x, -13/5, 0], 4: [0 - 4 - 2*self.korekcija_x, -12/5, 0],
                                   5: [-1/2 - 4 + 2*self.korekcija_x, -11/5, 0], 6: [0 - 4 - 2*self.korekcija_x, -2, 0],
                                   7: [-1/2 - 4 + 2*self.korekcija_x, -9/5, 0], 8: [0 - 4 - 2*self.korekcija_x, -8/5, 0],
                                   9: [-1/2 - 4 + 2*self.korekcija_x, -7/5, 0], 10: [0 - 4 - 2*self.korekcija_x, -6/5, 0],
                                   11: [-1/2 - 4 + 2*self.korekcija_x, -1, 0], 12: [0 - 4 - 2*self.korekcija_x, -4/5, 0],
                                   13: [-1/2 - 4 + 2*self.korekcija_x, -3/5, 0], 14: [0 - 4 - 2*self.korekcija_x, -2/5, 0],
                                   15: [-1/4 - 4, -3/10, 0], 16: [-1/4 - 4, 0, 0]}

        self.vzmet_pod = man.Graph([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
                                   [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10), (10, 11), (11, 12), (12, 13), (13, 14), (14, 15), (15, 16)],
                                   layout = self.vzmet_standard_pod,
                                   vertex_config = {'radius': 0},
                                   ).shift(0.045*man.UP)

        self.dusilka_spodaj_standard_pod = {1: [1/4 - 4, -3, 0], 2: [1/4 - 4, -2, 0],
                                            3: [0 - 4 + 2*self.korekcija_x, -2, 0], 4: [1/2 - 4 - 2*self.korekcija_x, -2, 0],
                                            5: [0 - 4 + 2*self.korekcija_x, -1, 0], 6: [1/2 - 4 - 2*self.korekcija_x, -1, 0]}

        self.dusilka_spodaj_pod = man.Graph([1, 2, 3, 4, 5, 6],
                                            [(1, 2), (2, 3), (2, 4), (3, 5), (4, 6)],
                                            layout = self.dusilka_spodaj_standard_pod,
                                            vertex_config = {'radius': 0},
                                            ).shift(0.045*man.UP)

        self.dusilka_zgoraj_standard_pod = {1: [1/4 - 4, 0, 0], 2: [1/4 - 4, -3/2, 0],
                                            3: [0 - 4 + 3*self.korekcija_x, -3/2, 0], 4: [1/2 - 4 - 3*self.korekcija_x, -3/2, 0]}

        self.dusilka_zgoraj_pod = man.Graph([1, 2, 3, 4],
                                            [(1, 2), (2, 3), (2, 4)],
                                            layout = self.dusilka_zgoraj_standard_pod,
                                            vertex_config = {'radius': 0},
                                            ).shift(0.045*man.UP)
        
        self.nihanje_pod = man.ValueTracker(0.120524)
        
        def update_masa_pod(masa_pod, dt):
            self.y_masa_pod = 1.33 * 0.75 * 0.5 * man.np.sin(self.nihanje_pod.get_value() - 0.03)
            new_pos_masa_pod = [-4, 0.25 + self.y_masa_pod, 0]
            self.masa_pod.move_to(new_pos_masa_pod)
        
        def update_m_pod(m_pod, dt):
            self.y_masa_pod = 1.33 * 0.75 * 0.5 * man.np.sin(self.nihanje_pod.get_value() - 0.03)
            new_pos_m_pod = [-4 + 0.3, 0.25 - 0.1 + self.y_masa_pod, 0]
            self.m_pod.move_to(new_pos_m_pod)
        
        def update_podlaga_pod(podlaga_pod, dt):
            self.y_podlaga_pod = 1 * 0.75 * 0.5 * man.np.sin(self.nihanje_pod.get_value())
            new_pos_podlaga_pod = [-4, -3.05 + self.y_podlaga_pod, 0]
            self.podlaga_pod.move_to(new_pos_podlaga_pod)
        
        def update_vzmet_pod(vzmet_pod, dt):
            self.y_masa_pod = 1.33 * 0.75 * 0.5 * man.np.sin(self.nihanje_pod.get_value() - 0.03 + 0.05) # ker nekaj zaostaja zaradi animacij
            self.y_podlaga_pod = 1 * 0.75 * 0.5 * man.np.sin(self.nihanje_pod.get_value())
            self.razlika = self.y_masa_pod - self.y_podlaga_pod
            new_layout_vzmet_pod = {1: [-1/4 - 4, -3 + self.y_podlaga_pod + 0/24*self.razlika, 0],
                                    2: [-1/4 - 4, -27/10 + self.y_podlaga_pod + 0/24*self.razlika, 0],
                                    3: [-1/2 - 4 + 2*self.korekcija_x, -13/5 + self.y_podlaga_pod + 1/24*self.razlika, 0],
                                    4: [0 - 4 - 2*self.korekcija_x, -12/5 + self.y_podlaga_pod + 3/24*self.razlika, 0],
                                    5: [-1/2 - 4 + 2*self.korekcija_x, -11/5 + self.y_podlaga_pod + 5/24*self.razlika, 0],
                                    6: [0 - 4 - 2*self.korekcija_x, -2 + self.y_podlaga_pod + 7/24*self.razlika, 0],
                                    7: [-1/2 - 4 + 2*self.korekcija_x, -9/5 + self.y_podlaga_pod + 9/24*self.razlika, 0],
                                    8: [0 - 4 - 2*self.korekcija_x, -8/5 + self.y_podlaga_pod + 11/24*self.razlika, 0],
                                    9: [-1/2 - 4 + 2*self.korekcija_x, -7/5 + self.y_podlaga_pod + 13/24*self.razlika, 0],
                                    10: [0 - 4 - 2*self.korekcija_x, -6/5 + self.y_podlaga_pod + 15/24*self.razlika, 0],
                                    11: [-1/2 - 4 + 2*self.korekcija_x, -1 + self.y_podlaga_pod + 17/24*self.razlika, 0],
                                    12: [0 - 4 - 2*self.korekcija_x, -4/5 + self.y_podlaga_pod + 19/24*self.razlika, 0],
                                    13: [-1/2 - 4 + 2*self.korekcija_x, -3/5 + self.y_podlaga_pod + 21/24*self.razlika, 0],
                                    14: [0 - 4 - 2*self.korekcija_x, -2/5 + self.y_podlaga_pod + 23/24*self.razlika, 0],
                                    15: [-1/4 - 4, -3/10 + self.y_podlaga_pod + 24/24*self.razlika, 0],
                                    16: [-1/4 - 4, 0 + self.y_podlaga_pod + 24/24*self.razlika, 0]}
            self.vzmet_pod.change_layout(new_layout_vzmet_pod)
        
        def update_dusilka_spodaj_pod(dusilka_spodaj_pod, dt):
            self.y_masa_pod = 1.33 * 0.75 * 0.5 * man.np.sin(self.nihanje_pod.get_value() - 0.03 + 0.05) # ker nekaj zaostaja zaradi animacij
            self.y_podlaga_pod = 1 * 0.75 * 0.5 * man.np.sin(self.nihanje_pod.get_value())
            self.razlika = self.y_masa_pod - self.y_podlaga_pod
            new_layout_dusilka_spodaj_pod = {1: [1/4 - 4, -3 + self.y_podlaga_pod + 0/2*self.razlika, 0],
                                             2: [1/4 - 4, -2 + self.y_podlaga_pod + 1/2*self.razlika, 0],
                                             3: [0 - 4 + 2*self.korekcija_x, -2 + self.y_podlaga_pod + 1/2*self.razlika, 0],
                                             4: [1/2 - 4 - 2*self.korekcija_x, -2 + self.y_podlaga_pod + 1/2*self.razlika, 0],
                                             5: [0 - 4 + 2*self.korekcija_x, -1 + self.y_podlaga_pod + 1/2*self.razlika, 0],
                                             6: [1/2 - 4 - 2*self.korekcija_x, -1 + self.y_podlaga_pod + 1/2*self.razlika, 0]}
            self.dusilka_spodaj_pod.change_layout(new_layout_dusilka_spodaj_pod)
        
        def update_dusilka_zgoraj_pod(dusilka_zgoraj_pod, dt):
            self.y_masa_pod = 1.33 * 0.75 * 0.5 * man.np.sin(self.nihanje_pod.get_value() - 0.03 + 0.05) # ker nekaj zaostaja zaradi animacij
            self.y_podlaga_pod = 1 * 0.75 * 0.5 * man.np.sin(self.nihanje_pod.get_value())
            self.razlika = self.y_masa_pod - self.y_podlaga_pod
            new_layout_dusilka_zgoraj_pod = {1: [1/4 - 4, 0 + self.y_podlaga_pod + 3/3*self.razlika, 0],
                                             2: [1/4 - 4, -3/2 + self.y_podlaga_pod + 2/3*self.razlika, 0],
                                             3: [0 - 4 + 3*self.korekcija_x, -3/2 + self.y_podlaga_pod + 2/3*self.razlika, 0],
                                             4: [1/2 - 4 - 3*self.korekcija_x, -3/2 + self.y_podlaga_pod + 2/3*self.razlika, 0]}
            self.dusilka_zgoraj_pod.change_layout(new_layout_dusilka_zgoraj_pod)

        self.masa_pod_orig = self.masa_pod.copy()
        self.m_pod_orig = self.m_pod.copy()
        self.podlaga_pod_orig = self.podlaga_pod.copy()
        self.vzmet_pod_orig = self.vzmet_pod.copy()
        self.dusilka_spodaj_pod_orig = self.dusilka_spodaj_pod.copy()
        self.dusilka_zgoraj_pod_orig = self.dusilka_zgoraj_pod.copy()

        self.masa_res = man.RoundedRectangle(
            color = man.GRAY,
            fill_color = man.GRAY,
            fill_opacity = 0.5,
            height = 0.5,
            width = 1,
            corner_radius = 0.1,
            ).move_to([0, 0.25, 0]).shift(0.375*man.UP)

        self.m_res = man.MathTex("m").scale(0.5).move_to(self.masa_res.get_center() + [0.3, -0.1, 0])

        self.podlaga_res = man.Rectangle(
            color = man.GRAY,
            fill_color = man.GRAY,
            fill_opacity = 0.5,
            height = 0.1,
            width = 1,
        ).move_to([0, -3.05, 0]).shift(0.375*man.UP)

        self.s1_res = man.Line(
            start = [-0.5, -3.1, 0],
            end = [-0.4, -3, 0],
            color = man.GRAY,
            stroke_width = 2,
        ).shift(0.375*man.UP)

        self.s2_res = self.s1_res.copy().move_to(self.s1_res.get_center() + [0.1, 0, 0])
        self.s3_res = self.s1_res.copy().move_to(self.s1_res.get_center() + [0.2, 0, 0])
        self.s4_res = self.s1_res.copy().move_to(self.s1_res.get_center() + [0.3, 0, 0])
        self.s5_res = self.s1_res.copy().move_to(self.s1_res.get_center() + [0.4, 0, 0])
        self.s6_res = self.s1_res.copy().move_to(self.s1_res.get_center() + [0.5, 0, 0])
        self.s7_res = self.s1_res.copy().move_to(self.s1_res.get_center() + [0.6, 0, 0])
        self.s8_res = self.s1_res.copy().move_to(self.s1_res.get_center() + [0.7, 0, 0])
        self.s9_res = self.s1_res.copy().move_to(self.s1_res.get_center() + [0.8, 0, 0])
        self.s10_res = self.s1_res.copy().move_to(self.s1_res.get_center() + [0.9, 0, 0])

        self.podlaga_res.add(self.s1_res, self.s2_res, self.s3_res, self.s4_res, self.s5_res, self.s6_res, self.s7_res, self.s8_res, self.s9_res, self.s10_res)

        self.vzmet_standard_res = {1: [-1/4, -3, 0], 2: [-1/4, -27/10, 0],
                                   3: [-1/2 + 2*self.korekcija_x, -13/5, 0], 4: [0 - 2*self.korekcija_x, -12/5, 0],
                                   5: [-1/2 + 2*self.korekcija_x, -11/5, 0], 6: [0 - 2*self.korekcija_x, -2, 0],
                                   7: [-1/2 + 2*self.korekcija_x, -9/5, 0], 8: [0 - 2*self.korekcija_x, -8/5, 0],
                                   9: [-1/2 + 2*self.korekcija_x, -7/5, 0], 10: [0 - 2*self.korekcija_x, -6/5, 0],
                                   11: [-1/2 + 2*self.korekcija_x, -1, 0], 12: [0 - 2*self.korekcija_x, -4/5, 0],
                                   13: [-1/2 + 2*self.korekcija_x, -3/5, 0], 14: [0 - 2*self.korekcija_x, -2/5, 0],
                                   15: [-1/4, -3/10, 0], 16: [-1/4, 0, 0]}

        self.vzmet_res = man.Graph([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
                                   [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10), (10, 11), (11, 12), (12, 13), (13, 14), (14, 15), (15, 16)],
                                   layout = self.vzmet_standard_res,
                                   vertex_config = {'radius': 0},
                                   ).shift(0.375*man.UP)

        self.dusilka_spodaj_standard_res = {1: [1/4, -3, 0], 2: [1/4, -2, 0],
                                            3: [0 + 2*self.korekcija_x, -2, 0], 4: [1/2 - 2*self.korekcija_x, -2, 0],
                                            5: [0 + 2*self.korekcija_x, -1, 0], 6: [1/2 - 2*self.korekcija_x, -1, 0]}

        self.dusilka_spodaj_res = man.Graph([1, 2, 3, 4, 5, 6],
                                            [(1, 2), (2, 3), (2, 4), (3, 5), (4, 6)],
                                            layout = self.dusilka_spodaj_standard_res,
                                            vertex_config = {'radius': 0},
                                            ).shift(0.375*man.UP)

        self.dusilka_zgoraj_standard_res = {1: [1/4, 0, 0], 2: [1/4, -3/2, 0],
                                            3: [0 + 3*self.korekcija_x, -3/2, 0], 4: [1/2 - 3*self.korekcija_x, -3/2, 0]}

        self.dusilka_zgoraj_res = man.Graph([1, 2, 3, 4],
                                            [(1, 2), (2, 3), (2, 4)],
                                            layout = self.dusilka_zgoraj_standard_res,
                                            vertex_config = {'radius': 0},
                                            ).shift(0.375*man.UP)
        
        self.nihanje_res = man.ValueTracker(1.56736)
        
        def update_masa_res(masa_res, dt):
            self.y_masa_res = 5.10 * 0.75 * 0.5 * man.np.sin(self.nihanje_res.get_value() - 1.37)
            new_pos_masa_res = [0, 0.25 + self.y_masa_res, 0]
            self.masa_res.move_to(new_pos_masa_res)
        
        def update_m_res(m_res, dt):
            self.y_masa_res = 5.10 * 0.75 * 0.5 * man.np.sin(self.nihanje_res.get_value() - 1.37)
            new_pos_m_res = [0 + 0.3, 0.25 - 0.1 + self.y_masa_res, 0]
            self.m_res.move_to(new_pos_m_res)
        
        def update_podlaga_res(podlaga_res, dt):
            self.y_podlaga_res = 1 * 0.75 * 0.5 * man.np.sin(self.nihanje_res.get_value())
            new_pos_podlaga_res = [0, -3.05 + self.y_podlaga_res, 0]
            self.podlaga_res.move_to(new_pos_podlaga_res)
        
        def update_vzmet_res(vzmet_res, dt):
            self.y_masa_res = 5.10 * 0.75 * 0.5 * man.np.sin(self.nihanje_res.get_value() - 1.37 + 0.05) # ker nekaj zaostaja zaradi animacij
            self.y_podlaga_res = 1 * 0.75 * 0.5 * man.np.sin(self.nihanje_res.get_value())
            self.razlika = self.y_masa_res - self.y_podlaga_res
            new_layout_vzmet_res = {1: [-1/4, -3 + self.y_podlaga_res + 0/24*self.razlika, 0],
                                    2: [-1/4, -27/10 + self.y_podlaga_res + 0/24*self.razlika, 0],
                                    3: [-1/2 + 2*self.korekcija_x, -13/5 + self.y_podlaga_res + 1/24*self.razlika, 0],
                                    4: [0 - 2*self.korekcija_x, -12/5 + self.y_podlaga_res + 3/24*self.razlika, 0],
                                    5: [-1/2 + 2*self.korekcija_x, -11/5 + self.y_podlaga_res + 5/24*self.razlika, 0],
                                    6: [0 - 2*self.korekcija_x, -2 + self.y_podlaga_res + 7/24*self.razlika, 0],
                                    7: [-1/2 + 2*self.korekcija_x, -9/5 + self.y_podlaga_res + 9/24*self.razlika, 0],
                                    8: [0 - 2*self.korekcija_x, -8/5 + self.y_podlaga_res + 11/24*self.razlika, 0],
                                    9: [-1/2 + 2*self.korekcija_x, -7/5 + self.y_podlaga_res + 13/24*self.razlika, 0],
                                    10: [0 - 2*self.korekcija_x, -6/5 + self.y_podlaga_res + 15/24*self.razlika, 0],
                                    11: [-1/2 + 2*self.korekcija_x, -1 + self.y_podlaga_res + 17/24*self.razlika, 0],
                                    12: [0 - 2*self.korekcija_x, -4/5 + self.y_podlaga_res + 19/24*self.razlika, 0],
                                    13: [-1/2 + 2*self.korekcija_x, -3/5 + self.y_podlaga_res + 21/24*self.razlika, 0],
                                    14: [0 - 2*self.korekcija_x, -2/5 + self.y_podlaga_res + 23/24*self.razlika, 0],
                                    15: [-1/4, -3/10 + self.y_podlaga_res + 24/24*self.razlika, 0],
                                    16: [-1/4, 0 + self.y_podlaga_res + 24/24*self.razlika, 0]}
            self.vzmet_res.change_layout(new_layout_vzmet_res)
        
        def update_dusilka_spodaj_res(dusilka_spodaj_res, dt):
            self.y_masa_res = 5.10 * 0.75 * 0.5 * man.np.sin(self.nihanje_res.get_value() - 1.37 + 0.05) # ker nekaj zaostaja zaradi animacij
            self.y_podlaga_res = 1 * 0.75 * 0.5 * man.np.sin(self.nihanje_res.get_value())
            self.razlika = self.y_masa_res - self.y_podlaga_res
            new_layout_dusilka_spodaj_res = {1: [1/4, -3 + self.y_podlaga_res + 0/2*self.razlika, 0],
                                             2: [1/4, -2 + self.y_podlaga_res + 1/2*self.razlika, 0],
                                             3: [0 + 2*self.korekcija_x, -2 + self.y_podlaga_res + 1/2*self.razlika, 0],
                                             4: [1/2 - 2*self.korekcija_x, -2 + self.y_podlaga_res + 1/2*self.razlika, 0],
                                             5: [0 + 2*self.korekcija_x, -1 + self.y_podlaga_res + 1/2*self.razlika, 0],
                                             6: [1/2 - 2*self.korekcija_x, -1 + self.y_podlaga_res + 1/2*self.razlika, 0]}
            self.dusilka_spodaj_res.change_layout(new_layout_dusilka_spodaj_res)
        
        def update_dusilka_zgoraj_res(dusilka_zgoraj_res, dt):
            self.y_masa_res = 5.10 * 0.75 * 0.5 * man.np.sin(self.nihanje_res.get_value() - 1.37 + 0.05) # ker nekaj zaostaja zaradi animacij
            self.y_podlaga_res = 1 * 0.75 * 0.5 * man.np.sin(self.nihanje_res.get_value())
            self.razlika = self.y_masa_res - self.y_podlaga_res
            new_layout_dusilka_zgoraj_res = {1: [1/4, 0 + self.y_podlaga_res + 3/3*self.razlika, 0],
                                             2: [1/4, -3/2 + self.y_podlaga_res + 2/3*self.razlika, 0],
                                             3: [0 + 3*self.korekcija_x, -3/2 + self.y_podlaga_res + 2/3*self.razlika, 0],
                                             4: [1/2 - 3*self.korekcija_x, -3/2 + self.y_podlaga_res + 2/3*self.razlika, 0]}
            self.dusilka_zgoraj_res.change_layout(new_layout_dusilka_zgoraj_res)

        self.masa_res_orig = self.masa_res.copy()
        self.m_res_orig = self.m_res.copy()
        self.podlaga_res_orig = self.podlaga_res.copy()
        self.vzmet_res_orig = self.vzmet_res.copy()
        self.dusilka_spodaj_res_orig = self.dusilka_spodaj_res.copy()
        self.dusilka_zgoraj_res_orig = self.dusilka_zgoraj_res.copy()

        self.masa_nad = man.RoundedRectangle(
            color = man.GRAY,
            fill_color = man.GRAY,
            fill_opacity = 0.5,
            height = 0.5,
            width = 1,
            corner_radius = 0.1,
            ).move_to([4, 0.25, 0]).shift(0.050*man.UP)

        self.m_nad = man.MathTex("m").scale(0.5).move_to(self.masa_nad.get_center() + [0.3, -0.1, 0])

        self.podlaga_nad = man.Rectangle(
            color = man.GRAY,
            fill_color = man.GRAY,
            fill_opacity = 0.5,
            height = 0.1,
            width = 1,
        ).move_to([4, -3.05, 0]).shift(0.050*man.UP)

        self.s1_nad = man.Line(
            start = [3.5, -3.1, 0],
            end = [3.6, -3, 0],
            color = man.GRAY,
            stroke_width = 2,
        ).shift(0.050*man.UP)

        self.s2_nad = self.s1_nad.copy().move_to(self.s1_nad.get_center() + [0.1, 0, 0])
        self.s3_nad = self.s1_nad.copy().move_to(self.s1_nad.get_center() + [0.2, 0, 0])
        self.s4_nad = self.s1_nad.copy().move_to(self.s1_nad.get_center() + [0.3, 0, 0])
        self.s5_nad = self.s1_nad.copy().move_to(self.s1_nad.get_center() + [0.4, 0, 0])
        self.s6_nad = self.s1_nad.copy().move_to(self.s1_nad.get_center() + [0.5, 0, 0])
        self.s7_nad = self.s1_nad.copy().move_to(self.s1_nad.get_center() + [0.6, 0, 0])
        self.s8_nad = self.s1_nad.copy().move_to(self.s1_nad.get_center() + [0.7, 0, 0])
        self.s9_nad = self.s1_nad.copy().move_to(self.s1_nad.get_center() + [0.8, 0, 0])
        self.s10_nad = self.s1_nad.copy().move_to(self.s1_nad.get_center() + [0.9, 0, 0])

        self.podlaga_nad.add(self.s1_nad, self.s2_nad, self.s3_nad, self.s4_nad, self.s5_nad, self.s6_nad, self.s7_nad, self.s8_nad, self.s9_nad, self.s10_nad)

        self.vzmet_standard_nad = {1: [-1/4 + 4, -3, 0], 2: [-1/4 + 4, -27/10, 0],
                                   3: [-1/2 + 4 + 2*self.korekcija_x, -13/5, 0], 4: [0 + 4 - 2*self.korekcija_x, -12/5, 0],
                                   5: [-1/2 + 4 + 2*self.korekcija_x, -11/5, 0], 6: [0 + 4 - 2*self.korekcija_x, -2, 0],
                                   7: [-1/2 + 4 + 2*self.korekcija_x, -9/5, 0], 8: [0 + 4 - 2*self.korekcija_x, -8/5, 0],
                                   9: [-1/2 + 4 + 2*self.korekcija_x, -7/5, 0], 10: [0 + 4 - 2*self.korekcija_x, -6/5, 0],
                                   11: [-1/2 + 4 + 2*self.korekcija_x, -1, 0], 12: [0 + 4 - 2*self.korekcija_x, -4/5, 0],
                                   13: [-1/2 + 4 + 2*self.korekcija_x, -3/5, 0], 14: [0 + 4 - 2*self.korekcija_x, -2/5, 0],
                                   15: [-1/4 + 4, -3/10, 0], 16: [-1/4 + 4, 0, 0]}

        self.vzmet_nad = man.Graph([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
                                   [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10), (10, 11), (11, 12), (12, 13), (13, 14), (14, 15), (15, 16)],
                                   layout = self.vzmet_standard_nad,
                                   vertex_config = {'radius': 0},
                                   ).shift(0.050*man.UP)

        self.dusilka_spodaj_standard_nad = {1: [1/4 + 4, -3, 0], 2: [1/4 + 4, -2, 0],
                                            3: [0 + 4 + 2*self.korekcija_x, -2, 0], 4: [1/2 + 4 - 2*self.korekcija_x, -2, 0],
                                            5: [0 + 4 + 2*self.korekcija_x, -1, 0], 6: [1/2 + 4 - 2*self.korekcija_x, -1, 0]}

        self.dusilka_spodaj_nad = man.Graph([1, 2, 3, 4, 5, 6],
                                            [(1, 2), (2, 3), (2, 4), (3, 5), (4, 6)],
                                            layout = self.dusilka_spodaj_standard_nad,
                                            vertex_config = {'radius': 0},
                                            ).shift(0.050*man.UP)

        self.dusilka_zgoraj_standard_nad = {1: [1/4 + 4, 0, 0], 2: [1/4 + 4, -3/2, 0],
                                            3: [0 + 4 + 3*self.korekcija_x, -3/2, 0], 4: [1/2 + 4 - 3*self.korekcija_x, -3/2, 0]}

        self.dusilka_zgoraj_nad = man.Graph([1, 2, 3, 4],
                                            [(1, 2), (2, 3), (2, 4)],
                                            layout = self.dusilka_zgoraj_standard_nad,
                                            vertex_config = {'radius': 0},
                                            ).shift(0.050*man.UP)
        
        self.nihanje_nad = man.ValueTracker(3.0082)
        
        def update_masa_nad(masa_nad, dt):
            self.y_masa_nad = 0.36 * 0.75 * 0.5 * man.np.sin(self.nihanje_nad.get_value() - 2.63)
            new_pos_masa_nad = [4, 0.25 + self.y_masa_nad, 0]
            self.masa_nad.move_to(new_pos_masa_nad)
        
        def update_m_nad(m_nad, dt):
            self.y_masa_nad = 0.36 * 0.75 * 0.5 * man.np.sin(self.nihanje_nad.get_value() - 2.63)
            new_pos_m_nad = [4 + 0.3, 0.25 - 0.1 + self.y_masa_nad, 0]
            self.m_nad.move_to(new_pos_m_nad)
        
        def update_podlaga_nad(podlaga_nad, dt):
            self.y_podlaga_nad = 1 * 0.75 * 0.5 * man.np.sin(self.nihanje_nad.get_value())
            new_pos_podlaga_nad = [4, -3.05 + self.y_podlaga_nad, 0]
            self.podlaga_nad.move_to(new_pos_podlaga_nad)
        
        def update_vzmet_nad(vzmet_nad, dt):
            self.y_masa_nad = 0.36 * 0.75 * 0.5 * man.np.sin(self.nihanje_nad.get_value() - 2.63 + 0.05) # ker nekaj zaostaja zaradi animacij
            self.y_podlaga_nad = 1 * 0.75 * 0.5 * man.np.sin(self.nihanje_nad.get_value())
            self.razlika = self.y_masa_nad - self.y_podlaga_nad
            new_layout_vzmet_nad = {1: [-1/4 + 4, -3 + self.y_podlaga_nad + 0/24*self.razlika, 0],
                                    2: [-1/4 + 4, -27/10 + self.y_podlaga_nad + 0/24*self.razlika, 0],
                                    3: [-1/2 + 4 + 2*self.korekcija_x, -13/5 + self.y_podlaga_nad + 1/24*self.razlika, 0],
                                    4: [0 + 4 - 2*self.korekcija_x, -12/5 + self.y_podlaga_nad + 3/24*self.razlika, 0],
                                    5: [-1/2 + 4 + 2*self.korekcija_x, -11/5 + self.y_podlaga_nad + 5/24*self.razlika, 0],
                                    6: [0 + 4 - 2*self.korekcija_x, -2 + self.y_podlaga_nad + 7/24*self.razlika, 0],
                                    7: [-1/2 + 4 + 2*self.korekcija_x, -9/5 + self.y_podlaga_nad + 9/24*self.razlika, 0],
                                    8: [0 + 4 - 2*self.korekcija_x, -8/5 + self.y_podlaga_nad + 11/24*self.razlika, 0],
                                    9: [-1/2 + 4 + 2*self.korekcija_x, -7/5 + self.y_podlaga_nad + 13/24*self.razlika, 0],
                                    10: [0 + 4 - 2*self.korekcija_x, -6/5 + self.y_podlaga_nad + 15/24*self.razlika, 0],
                                    11: [-1/2 + 4 + 2*self.korekcija_x, -1 + self.y_podlaga_nad + 17/24*self.razlika, 0],
                                    12: [0 + 4 - 2*self.korekcija_x, -4/5 + self.y_podlaga_nad + 19/24*self.razlika, 0],
                                    13: [-1/2 + 4 + 2*self.korekcija_x, -3/5 + self.y_podlaga_nad + 21/24*self.razlika, 0],
                                    14: [0 + 4 - 2*self.korekcija_x, -2/5 + self.y_podlaga_nad + 23/24*self.razlika, 0],
                                    15: [-1/4 + 4, -3/10 + self.y_podlaga_nad + 24/24*self.razlika, 0],
                                    16: [-1/4 + 4, 0 + self.y_podlaga_nad + 24/24*self.razlika, 0]}
            self.vzmet_nad.change_layout(new_layout_vzmet_nad)
        
        def update_dusilka_spodaj_nad(dusilka_spodaj_nad, dt):
            self.y_masa_nad = 0.36 * 0.75 * 0.5 * man.np.sin(self.nihanje_nad.get_value() - 2.63 + 0.05) # ker nekaj zaostaja zaradi animacij
            self.y_podlaga_nad = 1 * 0.75 * 0.5 * man.np.sin(self.nihanje_nad.get_value())
            self.razlika = self.y_masa_nad - self.y_podlaga_nad
            new_layout_dusilka_spodaj_nad = {1: [1/4 + 4, -3 + self.y_podlaga_nad + 0/2*self.razlika, 0],
                                             2: [1/4 + 4, -2 + self.y_podlaga_nad + 1/2*self.razlika, 0],
                                             3: [0 + 4 + 2*self.korekcija_x, -2 + self.y_podlaga_nad + 1/2*self.razlika, 0],
                                             4: [1/2 + 4 - 2*self.korekcija_x, -2 + self.y_podlaga_nad + 1/2*self.razlika, 0],
                                             5: [0 + 4 + 2*self.korekcija_x, -1 + self.y_podlaga_nad + 1/2*self.razlika, 0],
                                             6: [1/2 + 4 - 2*self.korekcija_x, -1 + self.y_podlaga_nad + 1/2*self.razlika, 0]}
            self.dusilka_spodaj_nad.change_layout(new_layout_dusilka_spodaj_nad)
        
        def update_dusilka_zgoraj_nad(dusilka_zgoraj_nad, dt):
            self.y_masa_nad = 0.36 * 0.75 * 0.5 * man.np.sin(self.nihanje_nad.get_value() - 2.63 + 0.05) # ker nekaj zaostaja zaradi animacij
            self.y_podlaga_nad = 1 * 0.75 * 0.5 * man.np.sin(self.nihanje_nad.get_value())
            self.razlika = self.y_masa_nad - self.y_podlaga_nad
            new_layout_dusilka_zgoraj_nad = {1: [1/4 + 4, 0 + self.y_podlaga_nad + 3/3*self.razlika, 0],
                                             2: [1/4 + 4, -3/2 + self.y_podlaga_nad + 2/3*self.razlika, 0],
                                             3: [0 + 4 + 3*self.korekcija_x, -3/2 + self.y_podlaga_nad + 2/3*self.razlika, 0],
                                             4: [1/2 + 4 - 3*self.korekcija_x, -3/2 + self.y_podlaga_nad + 2/3*self.razlika, 0]}
            self.dusilka_zgoraj_nad.change_layout(new_layout_dusilka_zgoraj_nad)

        self.masa_nad_orig = self.masa_nad.copy()
        self.m_nad_orig = self.m_nad.copy()
        self.podlaga_nad_orig = self.podlaga_nad.copy()
        self.vzmet_nad_orig = self.vzmet_nad.copy()
        self.dusilka_spodaj_nad_orig = self.dusilka_spodaj_nad.copy()
        self.dusilka_zgoraj_nad_orig = self.dusilka_zgoraj_nad.copy()

        self.r_pod = man.MathTex("r = 0,5").move_to([-4, 3, 0])

        self.r_res = man.MathTex("r = 1").move_to([0, 3, 0])

        self.r_nad = man.MathTex("r = 2").move_to([4, 3, 0])

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
        self.wait()
        self.play(man.Write(self.vty_predznak),
                  self.plus3.animate.shift(1*man.RIGHT),
                  self.kmy.animate.shift(1*man.RIGHT),
                  self.ydef.animate.shift(1*man.RIGHT))
        self.play(man.Write(self.vty_velikost))
        self.play(man.Write(self.vty_smer), man.FadeOut(self.plus3, self.kmy, self.ydef))
        self.wait()
        self.play(man.Write(self.vdy_predznak),
                  self.dmy.animate.shift(4*man.RIGHT),
                  self.yddef.animate.shift(4*man.RIGHT))
        self.play(man.Write(self.vdy_velikost))
        self.play(man.Write(self.vdy_smer), man.FadeOut(self.dmy, self.yddef))
        self.wait()
        self.play(man.Write(self.enacaj3), man.FadeOut(self.enacaj2))
        self.wait()
        self.play(man.Write(self.vtx_predznak),
                  self.plus6.animate.shift(1*man.RIGHT),
                  self.kmx.animate.shift(1*man.RIGHT),
                  self.x.animate.shift(1*man.RIGHT),
                  self.xt.animate.move_to([self.xt.get_center()[0], self.de_pred_nastavkom.get_center()[1], 0]),
                  self.xdef.animate.move_to([self.xdef.get_center()[0], self.de_pred_nastavkom.get_center()[1], 0]))
        self.play(man.Write(self.vtx_velikost))
        self.play(man.Write(self.vtx_smer), man.FadeOut(self.plus6, self.kmx, self.x, self.xt, self.xdef))
        self.wait()
        self.play(man.Write(self.vdx_predznak),
                  self.plus5.animate.shift(2*man.RIGHT),
                  self.dmx.animate.shift(2*man.RIGHT),
                  self.xd.animate.shift(2*man.RIGHT),
                  self.xtd.animate.move_to([self.xtd.get_center()[0], self.de_pred_nastavkom.get_center()[1], 0]),
                  self.xddef.animate.move_to([self.xddef.get_center()[0], self.de_pred_nastavkom.get_center()[1], 0]))
        self.play(man.Write(self.vdx_velikost))
        self.play(man.Write(self.vdx_smer), man.FadeOut(self.plus5, self.dmx, self.xd, self.xtd, self.xddef))
        self.wait()
        self.play(man.Write(self.vvx_predznak),
                  self.xdd.animate.shift(3*man.RIGHT),
                  self.xtdd.animate.move_to([self.xtdd.get_center()[0], self.de_pred_nastavkom.get_center()[1], 0]),
                  self.xdddef.animate.move_to([self.xdddef.get_center()[0], self.de_pred_nastavkom.get_center()[1], 0]))
        self.play(man.Write(self.vvx_velikost))
        self.play(man.Write(self.vvx_smer), man.FadeOut(self.xdd, self.xtdd, self.xdddef))
        self.wait()
        self.play(self.gibalna_enacba.animate.move_to([-3.75, 0, 0]), man.Create(self.ref))
        self.play(man.Write(self.referenca))
        self.wait()
        self.play(man.GrowArrow(self.vty))
        self.play(man.Create(self.ot))
        self.play(man.Write(self.ot_velikost))
        self.play(man.GrowFromPoint(self.vtys, self.vtys.get_start()))
        self.play(self.vty_smer.animate.scale(0.5).rotate((5/18) * man.PI).next_to(self.vtys.get_end() + [-0.88, -0.2, 0]))
        self.play(self.vty_velikost.animate.move_to(self.vty.get_center() + [0.9, 0.3, 0]), man.FadeOut(self.vty_predznak))
        self.wait()
        self.play(man.GrowArrow(self.vdy))
        self.play(man.Create(self.pk1))
        self.play(man.GrowFromPoint(self.vdys, self.vdys.get_start()))
        self.play(self.vdy_smer.animate.scale(0.5).rotate((5/18 - 1/2) * man.PI).next_to(self.vdys.get_end() + [-0.13, -0.15, 0]))
        self.play(self.vdy_velikost.animate.move_to(self.vdy.get_center() + [1.1, 0.1, 0]), man.FadeOut(self.vdy_predznak, self.enacaj3))
        self.wait()
        self.play(man.GrowArrow(self.vk))
        self.wait()
        self.play(man.GrowArrow(self.vtx))
        self.play(man.Create(self.phiz))
        self.play(man.Write(self.phiz_velikost))
        self.play(man.GrowFromPoint(self.vtxs, self.vtxs.get_start()))
        self.play(self.vtx_smer.animate.scale(0.5).rotate((1/18) * man.PI).next_to(self.vtxs.get_end() + [-1.59, 0.09, 0]))
        self.play(self.vtx_velikost.animate.move_to(self.vtx.get_center() + [0.6, 0.4, 0]), man.FadeOut(self.vtx_predznak))
        self.wait()
        self.play(man.GrowArrow(self.vdx))
        self.play(man.Create(self.pk2))
        self.play(man.GrowFromPoint(self.vdxs, self.vdxs.get_start()))
        self.play(self.vdx_smer.animate.scale(0.5).rotate((1/18 - 1/2) * man.PI).next_to(self.vdxs.get_end() + [-0.13, -0.66, 0]))
        self.play(self.vdx_velikost.animate.move_to(self.vdx.get_center() + [1, 0.4, 0]), man.FadeOut(self.vdx_predznak))
        self.wait()
        self.play(man.GrowArrow(self.vvx))
        self.play(man.Create(self.pk3))
        self.play(man.GrowFromPoint(self.vvxs, self.vvxs.get_start()))
        self.play(self.vvx_smer.animate.scale(0.5).rotate(1/18 * man.PI).next_to(self.vvxs.get_end() + [-1.59, 0.09, 0]))
        self.play(self.vvx_velikost.animate.move_to(self.vvx.get_center() + [-1.1, 0.25, 0]), man.FadeOut(self.vvx_predznak))
        self.wait()
        self.play(man.Write(self.nastavek_xt),
                  man.Write(self.nastavek_X,),
                  man.Write(self.nastavek_sin),
                  man.Write(self.nastavek_phiz),
                  man.Write(self.nastavek_zaklepaj))
        self.wait()
        self.play(man.Wiggle(self.nastavek_X, scale_value = 1.5), man.Wiggle(self.nastavek_phiz, scale_value = 1.5))
        self.wait()
        self.play(man.Write(self.pitagora))
        self.play(man.Write(self.z))
        self.wait()
        self.play(man.Write(self.z1), man.Wiggle(self.vk, rotation_angle = 0))
        self.play(man.Write(self.vsota_kvadratov_1_1), man.Wiggle(self.vty, rotation_angle = 0))
        self.play(man.Write(self.plus7))
        self.play(man.Write(self.vsota_kvadratov_1_2), man.Wiggle(self.vdy, rotation_angle = 0))
        self.wait()
        self.add(self.vdx_kopija)
        self.play(self.vdx_kopija.animate.shift((3.728 * man.np.cos((1/18) * man.PI))*man.LEFT + (3.728 * man.np.sin((1/18) * man.PI)*man.DOWN)))
        self.play(man.Write(self.z2), man.Wiggle(self.vk, rotation_angle = 0))
        self.play(man.Write(self.vsota_kvadratov_2_1), man.Wiggle(self.vtx, rotation_angle = 0), man.Wiggle(self.vvx, rotation_angle = 0))
        self.play(man.Write(self.plus8))
        self.play(man.Write(self.vsota_kvadratov_2_2), man.Wiggle(self.vdx, rotation_angle = 0))
        self.wait()
        self.play(man.Write(self.enacaj4),
                  self.vsota_kvadratov_2_1.animate.shift(4.8*man.RIGHT),
                  self.plus8.animate.shift(4.8*man.RIGHT),
                  self.vsota_kvadratov_2_2.animate.shift(4.8*man.RIGHT),
                  self.vsota_kvadratov_1_1.animate.shift(0.6*man.LEFT + 1*man.DOWN),
                  self.plus7.animate.shift(0.6*man.LEFT + 1*man.DOWN),
                  self.vsota_kvadratov_1_2.animate.shift(0.6*man.LEFT + 1*man.DOWN),
                  man.FadeOut(self.pitagora, self.z, self.z1, self.z2))
        self.wait()
        self.play(man.Write(self.xy))
        self.play(man.Write(self.koren1),
                  man.Unwrite(self.vsota_kvadratov_1_1),
                  man.Unwrite(self.plus7),
                  man.Unwrite(self.vsota_kvadratov_1_2),
                  man.Unwrite(self.enacaj4),
                  man.Unwrite(self.vsota_kvadratov_2_1),
                  man.Unwrite(self.plus8),
                  man.Unwrite(self.vsota_kvadratov_2_2))
        self.wait()
        self.play(man.Create(self.alpha))
        self.play(man.Write(self.alpha_velikost))
        self.wait()
        self.play(man.Create(self.gamma))
        self.play(man.Write(self.gamma_velikost))
        self.wait()
        self.play(man.Write(self.phiz_enacba))
        self.wait()
        self.play(self.kazalcni_diagram.animate.scale(0.7))
        self.wait()
        self.play(man.Write(self.tan_alpha))
        self.play(man.Write(self.tan_alpha1),
                  man.Wiggle(self.vty, rotation_angle = 0), man.Wiggle(self.vdy, rotation_angle = 0))
        self.wait()
        self.play(man.Write(self.tan_gamma))
        self.play(man.Write(self.tan_gamma1),
                  man.Wiggle(self.vtx, rotation_angle = 0), man.Wiggle(self.vdx, rotation_angle = 0), man.Wiggle(self.vvx, rotation_angle = 0))
        self.wait()
        self.play(man.Write(self.r))
        self.play(man.Unwrite(self.koren1))
        self.play(man.Write(self.koren2))
        self.play(man.Unwrite(self.tan_alpha1))
        self.play(man.Write(self.tan_alpha2))
        self.play(man.Unwrite(self.tan_gamma1))
        self.play(man.Write(self.tan_gamma2))
        self.wait()
        self.play(man.Unwrite(self.phiz_enacba))
        self.play(man.Write(self.tan_phiz))
        self.play(man.Unwrite(self.tan_alpha), man.Unwrite(self.tan_alpha2), man.Unwrite(self.tan_gamma), man.Unwrite(self.tan_gamma2))
        self.play(self.r.animate.move_to([-3.75, -3, 0]))
        self.wait()
        self.play(man.FadeOut(self.nastavek_enacba, self.xy, self.koren2, self.tan_phiz, self.r, self.kazalcni_diagram))

# definiram tukaj elemente, ker so premaknjeni glede na njihovo originalno pozicijo -----------------------------------------------
        self.sistem_kopija.move_to([-5, -1, 0])
# ---------------------------------------------------------------------------------------------------------------------------------

        self.play(man.FadeIn(self.sistem_kopija), man.Write(self.delta))
        self.wait()
        self.play(man.Create(self.tabela), run_time = 5)
        self.wait()
        self.play(self.tabela.animate.scale(0.7).move_to([1.5, 2, 0]))
        self.play(man.Create(self.xy_r), man.Create(self.phiz_r), man.Write(self.pi_label), man.Write(self.pi_polovic_label))
        self.play(man.Write(self.x_label_xy_r), man.Write(self.y_label_xy_r), man.Write(self.x_label_phiz_r), man.Write(self.y_label_phiz_r),
                  man.Create(self.xy_r_ref1), man.Create(self.xy_r_ref2), man.Create(self.phiz_r_ref1), man.Create(self.phiz_r_ref2), man.Create(self.phiz_r_ref3))
        self.play(man.Create(self.t1g1), man.GrowFromPoint(self.t1g1x, self.t1g1x.get_start()), man.GrowFromPoint(self.t1g1y, self.t1g1y.get_start()))
        self.play(man.Create(self.t1g2), man.GrowFromPoint(self.t1g2x, self.t1g2x.get_start()), man.GrowFromPoint(self.t1g2y, self.t1g2y.get_start()))
        self.play(man.Create(self.t2g1), man.GrowFromPoint(self.t2g1x, self.t2g1x.get_start()), man.GrowFromPoint(self.t2g1y, self.t2g1y.get_start()))
        self.play(man.Create(self.t2g2), man.GrowFromPoint(self.t2g2x, self.t2g2x.get_start()), man.GrowFromPoint(self.t2g2y, self.t2g2y.get_start()))
        self.play(man.Create(self.t3g1), man.GrowFromPoint(self.t3g1x, self.t3g1x.get_start()), man.GrowFromPoint(self.t3g1y, self.t3g1y.get_start()))
        self.play(man.Create(self.t3g2), man.GrowFromPoint(self.t3g2x, self.t3g2x.get_start()), man.GrowFromPoint(self.t3g2y, self.t3g2y.get_start()))
        self.wait()
        self.play(man.Create(self.xy_po_r))
        self.add(self.t1g1, self.t2g1, self.t3g1)
        self.play(man.Create(self.phiz_po_r))
        self.add(self.t1g2, self.t2g2, self.t3g2)
        self.wait()
        self.play(man.FadeOut(self.sistem_kopija, self.tabela),
                  self.delta.animate.move_to([-4, 2, 0]),
                  self.graf_xy.animate.shift(2*man.LEFT),
                  self.graf_phiz.animate.shift(1*man.LEFT))
        self.wait()
        self.play(man.Write(self.delta2))
        self.play(man.Create(self.xy_po_r2))
        self.play(man.Create(self.phiz_po_r2))
        self.wait()
        self.play(man.Write(self.delta3))
        self.play(man.Create(self.xy_po_r3))
        self.play(man.Create(self.phiz_po_r3))
        self.wait()
        self.play(man.GrowFromPoint(self.presecisce, self.presecisce.get_start()))
        self.play(man.Write(self.dva_pod_koren))
        self.wait()
        self.play(man.FadeOut(self.delta, self.delta2, self.xy_po_r2, self.phiz_po_r2, self.delta3, self.xy_po_r3, self.phiz_po_r3, self.presecisce, self.dva_pod_koren))
        self.play(self.graf_xy.animate.scale(0.7).move_to([-5, 1.75, 0]), self.graf_phiz.animate.scale(0.7).move_to([-5, -1.75, 0]))
        self.wait()
        self.play(man.Create(self.ref2))
        self.play(man.Write(self.referenca2))
        self.wait()
        self.play(man.GrowArrow(self.Y))
        self.play(man.Write(self.Y_velikost))
        self.play(man.Create(self.ot2))
        self.play(man.Write(self.ot2_velikost))
        self.play(man.GrowFromPoint(self.Ys, self.Ys.get_start()))
        self.play(man.Write(self.Y_smer))
        self.wait()
        self.play(man.GrowArrow(self.X1))
        self.play(man.Write(self.X1_velikost))
        self.play(man.Create(self.phiz1))
        self.play(man.Write(self.phiz1_velikost))
        self.play(man.GrowFromPoint(self.X1s, self.X1s.get_start()))
        self.play(man.Write(self.X1_smer))
        self.wait()
        self.play(man.FadeOut(self.X1, self.X1_velikost, self.phiz1, self.phiz1_velikost, self.X1s, self.X1_smer))
        self.wait()
        self.play(man.GrowArrow(self.X2))
        self.play(man.Write(self.X2_velikost))
        self.play(man.Create(self.phiz2))
        self.play(man.Write(self.phiz2_velikost))
        self.play(man.GrowFromPoint(self.X2s, self.X2s.get_start()))
        self.play(man.Write(self.X2_smer))
        self.wait()
        self.play(man.FadeOut(self.X2, self.X2_velikost, self.phiz2, self.phiz2_velikost, self.X2s, self.X2_smer))
        self.wait()
        self.play(man.GrowArrow(self.X3))
        self.play(man.Write(self.X3_velikost))
        self.play(man.Create(self.phiz3))
        self.play(man.Write(self.phiz3_velikost))
        self.play(man.GrowFromPoint(self.X3s, self.X3s.get_start()))
        self.play(man.Write(self.X3_smer))
        self.wait()
        self.play(man.FadeOut(self.X3, self.X3_velikost, self.phiz3, self.phiz3_velikost, self.X3s, self.X3_smer))
        self.play(man.FadeIn(self.X1, self.X1_velikost, self.phiz1, self.phiz1_velikost, self.X1s, self.X1_smer))
        self.wait()
        self.add(self.ref2_kopija, self.referenca2_kopija)
        self.play(man.FadeOut(self.graf_xy, self.graf_phiz,
                              self.Y_velikost, self.X1_velikost,
                              self.ot2, self.ot2_velikost, self.phiz1, self.phiz1_velikost,
                              self.Ys, self.Y_smer, self.X1s, self.X1_smer))
        self.play(man.Transform(self.ref2_kopija, self.refdol), self.referenca2_kopija.animate.shift(0.5*man.LEFT + 2.35*man.DOWN),
                  man.Transform(self.ref2, self.refgor), self.referenca2.animate.shift(0.5*man.LEFT + 2.15*man.UP),
                  self.Y.animate.set_max_stroke_width_to_length_ratio(13.334).put_start_and_end_on(self.nsdol, self.neY),
                  self.X1.animate.set_max_stroke_width_to_length_ratio(10.026).put_start_and_end_on(self.nsgor, self.neX1))
        self.wait()
        
# definiram tukaj elemente, ker so premaknjeni glede na njihovo originalno pozicijo -----------------------------------------------
        self.X2.set_max_stroke_width_to_length_ratio(2.614).put_start_and_end_on(self.nsgor, self.neX2)
        self.X3.set_max_stroke_width_to_length_ratio(37.038).put_start_and_end_on(self.nsgor, self.neX3)

        self.masa.move_to([-3, 1.9, 0])
        self.m.move_to(self.masa.get_center() + [0.6, -0.2, 0])
        self.podlaga.move_to([-3, -2.6, 0])
        self.s1.move_to([-3.9, -2.6, 0])
        self.s2.move_to([-3.7, -2.6, 0])
        self.s3.move_to([-3.5, -2.6, 0])
        self.s4.move_to([-3.3, -2.6, 0])
        self.s5.move_to([-3.1, -2.6, 0])
        self.s6.move_to([-2.9, -2.6, 0])
        self.s7.move_to([-2.7, -2.6, 0])
        self.s8.move_to([-2.5, -2.6, 0])
        self.s9.move_to([-2.3, -2.6, 0])
        self.s10.move_to([-2.1, -2.6, 0])

        self.povY = man.DashedLine(
            start = self.Y.get_end(),
            end = [-2, self.Y.get_end()[1], 0],
            stroke_opacity = 0.2,
        )

        self.povX1 = man.DashedLine(
            start = self.X1.get_end(),
            end = [-2, self.X1.get_end()[1], 0],
            stroke_opacity = 0.2,
        )

        self.povX2 = man.DashedLine(
            start = self.X2.get_end(),
            end = [-2, self.X2.get_end()[1], 0],
            stroke_opacity = 0.2,
        )

        self.povX3 = man.DashedLine(
            start = self.X3.get_end(),
            end = [-2, self.X3.get_end()[1], 0],
            stroke_opacity = 0.2,
        )
# ---------------------------------------------------------------------------------------------------------------------------------

        self.play(man.FadeIn(self.masa, self.m, self.podlaga))
        self.wait()
        self.play(man.FadeIn(self.s1), run_time = 0.1)
        self.play(man.FadeIn(self.s2), run_time = 0.1)
        self.play(man.FadeIn(self.s3), run_time = 0.1)
        self.play(man.FadeIn(self.s4), run_time = 0.1)
        self.play(man.FadeIn(self.s5), run_time = 0.1)
        self.play(man.FadeIn(self.s6), run_time = 0.1)
        self.play(man.FadeIn(self.s7), run_time = 0.1)
        self.play(man.FadeIn(self.s8), run_time = 0.1)
        self.play(man.FadeIn(self.s9), run_time = 0.1)
        self.play(man.FadeIn(self.s10), run_time = 0.1)
        self.wait()

# definiram tukaj elemente, ker so premaknjeni glede na njihovo originalno pozicijo -----------------------------------------------
        self.podlaga.add(self.s1, self.s2, self.s3, self.s4, self.s5, self.s6, self.s7, self.s8, self.s9, self.s10)
# ---------------------------------------------------------------------------------------------------------------------------------

        self.play(self.masa.animate.shift((1.33 * 0.75 * man.np.sin((6/16) * man.PI - 0.03))*man.UP),
                  self.m.animate.shift((1.33 * 0.75 * man.np.sin((6/16) * man.PI - 0.03))*man.UP),
                  self.podlaga.animate.shift((1 * 0.75 * man.np.sin((6/16) * man.PI))*man.UP),
                  man.GrowFromPoint(self.povY, self.povY.get_start()), man.GrowFromPoint(self.povX1, self.povX1.get_start()))
        self.wait()

# definiram tukaj elemente, ker so premaknjeni glede na njihovo originalno pozicijo -----------------------------------------------
        self.tracker1 = man.ValueTracker((6/16) * man.PI)

        def update_Y(Y, dt):
            new_start_Y = self.refdol.get_start()
            new_end_Y = self.refdol.get_start() + [1 * 0.75 * man.np.cos(self.tracker1.get_value()), 1 * 0.75 * man.np.sin(self.tracker1.get_value()), 0]
            self.Y.put_start_and_end_on(new_start_Y, new_end_Y)
        
        def update_podlaga(podlaga, dt):
            new_pos_podlaga = [-3, -2.6 + 1 * 0.75 * man.np.sin(self.tracker1.get_value()), 0]
            self.podlaga.move_to(new_pos_podlaga)
        
        def update_povY(povY, dt):
            new_start_povY = self.Y.get_end()
            new_end_povY = self.podlaga.get_center() + [1, 0, 0]
            self.povY.put_start_and_end_on(new_start_povY, new_end_povY)
        
        def update_X1(X1, dt):
            new_start_X1 = self.refgor.get_start()
            new_end_X1 = self.refgor.get_start() + [1.33 * 0.75 * man.np.cos(self.tracker1.get_value() - 0.03), 1.33 * 0.75 * man.np.sin(self.tracker1.get_value() - 0.03), 0]
            self.X1.put_start_and_end_on(new_start_X1, new_end_X1)
        
        def update_X2(X2, dt):
            new_start_X2 = self.refgor.get_start()
            new_end_X2 = self.refgor.get_start() + [5.10 * 0.75 * man.np.cos(self.tracker1.get_value() - 1.37), 5.10 * 0.75 * man.np.sin(self.tracker1.get_value() - 1.37), 0]
            self.X2.put_start_and_end_on(new_start_X2, new_end_X2)
        
        def update_X3(X3, dt):
            new_start_X3 = self.refgor.get_start()
            new_end_X3 = self.refgor.get_start() + [0.36 * 0.75 * man.np.cos(self.tracker1.get_value() - 2.63), 0.36 * 0.75 * man.np.sin(self.tracker1.get_value() - 2.63), 0]
            self.X3.put_start_and_end_on(new_start_X3, new_end_X3)
        
        def update_masa1(masa1, dt):
            new_pos_masa1 = [-3, 1.9 + 1.33 * 0.75 * man.np.sin(self.tracker1.get_value() - 0.03), 0]
            self.masa.move_to(new_pos_masa1)
        
        def update_masa2(masa2, dt):
            new_pos_masa2 = [-3, 1.9 + 5.10 * 0.75 * man.np.sin(self.tracker1.get_value() - 1.37), 0]
            self.masa.move_to(new_pos_masa2)
        
        def update_masa3(masa3, dt):
            new_pos_masa3 = [-3, 1.9 + 0.36 * 0.75 * man.np.sin(self.tracker1.get_value() - 2.63), 0]
            self.masa.move_to(new_pos_masa3)
        
        def update_m1(m1, dt):
            new_pos_m1 = [-3 + 0.6, 1.9 - 0.2 + 1.33 * 0.75 * man.np.sin(self.tracker1.get_value() - 0.03), 0]
            self.m.move_to(new_pos_m1)
        
        def update_m2(m2, dt):
            new_pos_m2 = [-3 + 0.6, 1.9 - 0.2 + 5.10 * 0.75 * man.np.sin(self.tracker1.get_value() - 1.37), 0]
            self.m.move_to(new_pos_m2)
        
        def update_m3(m3, dt):
            new_pos_m3 = [-3 + 0.6, 1.9 - 0.2 + 0.36 * 0.75 * man.np.sin(self.tracker1.get_value() - 2.63), 0]
            self.m.move_to(new_pos_m3)
        
        def update_povX1(povX1, dt):
            new_start_povX1 = self.X1.get_end()
            new_end_povX1 = self.masa.get_center() + [1, 0, 0]
            self.povX1.put_start_and_end_on(new_start_povX1, new_end_povX1)
        
        def update_povX2(povX2, dt):
            new_start_povX2 = self.X2.get_end()
            new_end_povX2 = self.masa.get_center() + [1, 0, 0]
            self.povX2.put_start_and_end_on(new_start_povX2, new_end_povX2)
        
        def update_povX3(povX3, dt):
            new_start_povX3 = self.X3.get_end()
            new_end_povX3 = self.masa.get_center() + [1, 0, 0]
            self.povX3.put_start_and_end_on(new_start_povX3, new_end_povX3)
        
        self.Y.add_updater(update_Y)
        self.podlaga.add_updater(update_podlaga)
        self.povY.add_updater(update_povY)
        self.X1.add_updater(update_X1)
        self.masa.add_updater(update_masa1)
        self.m.add_updater(update_m1)
        self.povX1.add_updater(update_povX1)
# ---------------------------------------------------------------------------------------------------------------------------------

        self.play(self.tracker1.animate.set_value((6/16) * man.PI + 4 * man.PI),
                  rate_func = man.linear, run_time = 8)
        self.wait()

# definiram tukaj elemente, ker so premaknjeni glede na njihovo originalno pozicijo -----------------------------------------------
        self.tracker1.set_value((6/16) * man.PI)
        self.masa.clear_updaters()
        self.m.clear_updaters()
        self.X2.add_updater(update_X2)
        self.masa.add_updater(update_masa2)
        self.m.add_updater(update_m2)
        self.povX2.add_updater(update_povX2)
# ---------------------------------------------------------------------------------------------------------------------------------

        self.play(man.FadeOut(self.X1, self.povX1), man.FadeIn(self.X2, self.povX2),
                  self.masa.animate.shift((5.10 * 0.75 * man.np.sin((6/16) * man.PI - 1.37) - 1.33 * 0.75 * man.np.sin((6/16) * man.PI - 0.03))*man.UP),
                  self.m.animate.shift((5.10 * 0.75 * man.np.sin((6/16) * man.PI - 1.37) - 1.33 * 0.75 * man.np.sin((6/16) * man.PI - 0.03))*man.UP))
        self.wait()
        self.play(self.tracker1.animate.set_value((6/16) * man.PI + 8 * man.PI),
                  rate_func = man.linear, run_time = 8)
        self.wait()

# definiram tukaj elemente, ker so premaknjeni glede na njihovo originalno pozicijo -----------------------------------------------
        self.tracker1.set_value((6/16) * man.PI)
        self.masa.clear_updaters()
        self.m.clear_updaters()
        self.X3.add_updater(update_X3)
        self.masa.add_updater(update_masa3)
        self.m.add_updater(update_m3)
        self.povX3.add_updater(update_povX3)
# ---------------------------------------------------------------------------------------------------------------------------------

        self.play(man.FadeOut(self.X2, self.povX2), man.FadeIn(self.X3, self.povX3),
                  self.masa.animate.shift((0.36 * 0.75 * man.np.sin((6/16) * man.PI - 2.63) - 5.10 * 0.75 * man.np.sin((6/16) * man.PI - 1.37))*man.UP),
                  self.m.animate.shift((0.36 * 0.75 * man.np.sin((6/16) * man.PI - 2.63) - 5.10 * 0.75 * man.np.sin((6/16) * man.PI - 1.37))*man.UP))
        self.wait()
        self.play(self.tracker1.animate.set_value((6/16) * man.PI + 16 * man.PI),
                  rate_func = man.linear, run_time = 8)
        self.wait()

# definiram tukaj elemente, ker so premaknjeni glede na njihovo originalno pozicijo -----------------------------------------------
        self.tracker1.set_value((6/16) * man.PI)
        self.podlaga.clear_updaters()
        self.Y.clear_updaters()
        self.povY.clear_updaters()
        self.masa.clear_updaters()
        self.m.clear_updaters()
        self.X1.clear_updaters()
        self.X2.clear_updaters()
        self.X3.clear_updaters()
        self.povX1.clear_updaters()
        self.povX2.clear_updaters()
        self.povX3.clear_updaters()
# ---------------------------------------------------------------------------------------------------------------------------------

        self.play(man.FadeOut(self.refgor, self.ref2, self.referenca2, self.masa, self.m, self.X3, self.povX3,
                              self.refdol, self.ref2_kopija, self.referenca2_kopija, self.podlaga, self.Y, self.povY))
        self.wait()
        self.play(man.Create(self.masa_pod), man.Create(self.m_pod), man.Create(self.podlaga_pod),
                  man.Create(self.vzmet_pod), man.Create(self.dusilka_spodaj_pod), man.Create(self.dusilka_zgoraj_pod),
                  man.Create(self.masa_res), man.Create(self.m_res), man.Create(self.podlaga_res),
                  man.Create(self.vzmet_res), man.Create(self.dusilka_spodaj_res), man.Create(self.dusilka_zgoraj_res),
                  man.Create(self.masa_nad), man.Create(self.m_nad), man.Create(self.podlaga_nad),
                  man.Create(self.vzmet_nad), man.Create(self.dusilka_spodaj_nad), man.Create(self.dusilka_zgoraj_nad))
        self.play(man.Write(self.r_pod))
        self.play(man.Write(self.r_res))
        self.play(man.Write(self.r_nad))

# definiram tukaj elemente, ker so premaknjeni glede na njihovo originalno pozicijo -----------------------------------------------
        self.masa_pod.add_updater(update_masa_pod)
        self.m_pod.add_updater(update_m_pod)
        self.podlaga_pod.add_updater(update_podlaga_pod)
        self.vzmet_pod.add_updater(update_vzmet_pod)
        self.dusilka_spodaj_pod.add_updater(update_dusilka_spodaj_pod)
        self.dusilka_zgoraj_pod.add_updater(update_dusilka_zgoraj_pod)

        self.masa_res.add_updater(update_masa_res)
        self.m_res.add_updater(update_m_res)
        self.podlaga_res.add_updater(update_podlaga_res)
        self.vzmet_res.add_updater(update_vzmet_res)
        self.dusilka_spodaj_res.add_updater(update_dusilka_spodaj_res)
        self.dusilka_zgoraj_res.add_updater(update_dusilka_zgoraj_res)

        self.masa_nad.add_updater(update_masa_nad)
        self.m_nad.add_updater(update_m_nad)
        self.podlaga_nad.add_updater(update_podlaga_nad)
        self.vzmet_nad.add_updater(update_vzmet_nad)
        self.dusilka_spodaj_nad.add_updater(update_dusilka_spodaj_nad)
        self.dusilka_zgoraj_nad.add_updater(update_dusilka_zgoraj_nad)
# ---------------------------------------------------------------------------------------------------------------------------------

        self.play(self.nihanje_pod.animate.set_value(0.120524 + 8 * man.PI),
                  self.nihanje_res.animate.set_value(1.56736 + 16 * man.PI),
                  self.nihanje_nad.animate.set_value(3.0082 + 32 * man.PI),
                  rate_func = man.linear, run_time = 16)
        
# definiram tukaj elemente, ker so premaknjeni glede na njihovo originalno pozicijo -----------------------------------------------
        self.nihanje_pod.set_value(0.120524)
        self.nihanje_res.set_value(1.56736)
        self.nihanje_nad.set_value(3.0082)

        self.masa_pod.clear_updaters()
        self.m_pod.clear_updaters()
        self.podlaga_pod.clear_updaters()
        self.vzmet_pod.clear_updaters()
        self.dusilka_spodaj_pod.clear_updaters()
        self.dusilka_zgoraj_pod.clear_updaters()

        self.masa_res.clear_updaters()
        self.m_res.clear_updaters()
        self.podlaga_res.clear_updaters()
        self.vzmet_res.clear_updaters()
        self.dusilka_spodaj_res.clear_updaters()
        self.dusilka_zgoraj_res.clear_updaters()

        self.masa_nad.clear_updaters()
        self.m_nad.clear_updaters()
        self.podlaga_nad.clear_updaters()
        self.vzmet_nad.clear_updaters()
        self.dusilka_spodaj_nad.clear_updaters()
        self.dusilka_zgoraj_nad.clear_updaters()
# ---------------------------------------------------------------------------------------------------------------------------------
        
        self.remove(self.masa_pod, self.m_pod, self.podlaga_pod, self.vzmet_pod, self.dusilka_spodaj_pod, self.dusilka_zgoraj_pod,
                    self.masa_res, self.m_res, self.podlaga_res, self.vzmet_res, self.dusilka_spodaj_res, self.dusilka_zgoraj_res,
                    self.masa_nad, self.m_nad, self.podlaga_nad, self.vzmet_nad, self.dusilka_spodaj_nad, self.dusilka_zgoraj_nad)
        self.add(self.masa_pod_orig, self.m_pod_orig, self.podlaga_pod_orig, self.vzmet_pod_orig, self.dusilka_spodaj_pod_orig, self.dusilka_zgoraj_pod_orig,
                 self.masa_res_orig, self.m_res_orig, self.podlaga_res_orig, self.vzmet_res_orig, self.dusilka_spodaj_res_orig, self.dusilka_zgoraj_res_orig,
                 self.masa_nad_orig, self.m_nad_orig, self.podlaga_nad_orig, self.vzmet_nad_orig, self.dusilka_spodaj_nad_orig, self.dusilka_zgoraj_nad_orig)
        self.wait()
        self.play(man.FadeOut(self.r_pod, self.masa_pod_orig, self.m_pod_orig, self.podlaga_pod_orig,
                              self.vzmet_pod_orig, self.dusilka_spodaj_pod_orig, self.dusilka_zgoraj_pod_orig,
                              self.r_res, self.masa_res_orig, self.m_res_orig, self.podlaga_res_orig,
                              self.vzmet_res_orig, self.dusilka_spodaj_res_orig, self.dusilka_zgoraj_res_orig,
                              self.r_nad, self.masa_nad_orig, self.m_nad_orig, self.podlaga_nad_orig,
                              self.vzmet_nad_orig, self.dusilka_spodaj_nad_orig, self.dusilka_zgoraj_nad_orig))
        self.wait()

# definiram tukaj elemente, ker so premaknjeni glede na njihovo originalno pozicijo -----------------------------------------------
        self.kazalcni_diagram.scale(1/0.7).move_to([0, 0.25, 0])

        self.ot3 = man.Angle(
            line1 = self.ref,
            line2 = self.vk,
            radius = 0.5,
        )

        self.ot3_velikost = man.MathTex("\\omega t").move_to(self.ot3.get_end() + [-0.4, -0.1, 0])

        self.theta = man.np.arctan((self.vk.get_end()[1] - self.vk.get_start()[1])/(self.vk.get_end()[0] - self.vk.get_start()[0]))

        self.vks = man.DashedLine(
            start = self.vk.get_end(),
            end = self.vk.get_end() + [2 * man.np.cos(self.theta), 2 * man.np.sin(self.theta), 0],
            stroke_opacity = 0.2,
        )

        self.vk_smer = man.MathTex("\mathrm{sin} (\omega t)").scale(0.5).rotate(self.theta).move_to(self.vks.get_end() + [-0.27, -0.32, 0])

        self.vk_velikost = man.MathTex("f_0", color = man.RED).move_to(self.vk.get_center() + [-0.4, 0, 0])

        self.phiz4 = man.Angle(
            line1 = self.vk,
            line2 = self.vtx,
            radius = 1,
            other_angle = True,
        )

        self.phiz4_velikost = man.MathTex("\\varphi_\\mathrm{z}").move_to(self.phiz4.get_center() + [0.15, 0.5, 0])

        self.ft = man.Arrow(
            start = self.ref.get_start(),
            end = self.vdx.get_end(),
            color = man.ORANGE,
            max_stroke_width_to_length_ratio = 1.445,
            max_tip_length_to_length_ratio = 0.072,
            stroke_width = 5,
            buff = 0,
        )

        self.ft_velikost = man.MathTex("f_\mathrm{T}", color = man.ORANGE).move_to(self.ft.get_center() + [0, 0.45, 0])

        self.transmisivnost = man.Tex("prenosnost").move_to([-3.5, 2, 0])

        self.T = man.MathTex("T =").move_to([-3.95, 1, 0])

        self.f0ft = man.MathTex("\\frac{f_\mathrm{T}}{f_0}").next_to(self.T, man.RIGHT)

        self.pitagora2 = man.Tex("Pitagorov izrek:").move_to([-3.5, -0.5, 0])

        self.ft_kvadrat = man.MathTex("f_\mathrm{T}^2").move_to([-6.5, -1.5, 0])

        self.enacaj6 = man.MathTex("=").next_to(self.ft_kvadrat, man.RIGHT)

        self.kateta1ft = man.MathTex("(\omega_0^2 X)^2").next_to(self.enacaj6, man.RIGHT)

        self.plus10 = man.MathTex("+").next_to(self.kateta1ft, man.RIGHT)

        self.kateta2ft = man.MathTex("(2 \delta \omega_0 \omega X)^2").next_to(self.plus10, man.RIGHT)

        self.f0_kvadrat = man.MathTex("f_0^2").move_to([-6.5, -2.5, 0])

        self.enacaj5 = man.MathTex("=").next_to(self.f0_kvadrat, man.RIGHT)

        self.kateta1f0 = man.MathTex("(\omega_0^2 X - \omega^2 X)^2").next_to(self.enacaj5, man.RIGHT)

        self.plus9 = man.MathTex("+").next_to(self.kateta1f0, man.RIGHT)

        self.kateta2f0 = man.MathTex("(2 \delta \omega_0 \omega X)^2").next_to(self.plus9, man.RIGHT)

        self.enacaj7 = man.MathTex("=").next_to(self.f0ft, man.RIGHT)

        self.f0ft_pod_koren = man.MathTex("\sqrt{\\frac{f_\mathrm{T}^2}{f_0^2}}").next_to(self.enacaj7, man.RIGHT)

        self.T_koren1 = man.MathTex("\sqrt{\\frac{(\omega_0^2 X)^2 + (2 \delta \omega_0 \omega X)^2}{(\omega_0^2 X - \omega^2 X)^2 + (2 \delta \omega_0 \omega X)^2}}")
        self.T_koren1.next_to(self.T, man.RIGHT).shift(2*man.LEFT + 0.5*man.DOWN) # da ni predolgo

        self.r.move_to([-3.5, -1.5, 0])

        self.T_koren2 = man.MathTex("\sqrt{\\frac{1 + (2 \delta r)^2}{(1 - r^2)^2 + (2 \delta r)^2}}").next_to(self.T, man.RIGHT).shift(2*man.LEFT + 0.5*man.DOWN)

        self.phit = man.Angle(
            line1 = self.vk,
            line2 = self.ft,
            radius = 1.8,
            other_angle = True,
        )

        self.phit_velikost = man.MathTex("\\varphi_\\mathrm{T}").move_to(self.phit.get_center() + [0.3, 0.35, 0])

        self.theta2 = man.np.arctan((self.ft.get_end()[1] - self.ft.get_start()[1])/(self.ft.get_end()[0] - self.ft.get_start()[0]))

        self.fts = man.DashedLine(
            start = self.ft.get_end(),
            end = self.ft.get_end() + [2 * man.np.cos(self.theta2), 2 * man.np.sin(self.theta2), 0],
            stroke_opacity = 0.2,
        )

        self.ft_smer = man.MathTex("\mathrm{sin} (\omega t - \\varphi_\\mathrm{T})").scale(0.5).rotate(self.theta2).move_to(self.fts.get_end() + [-0.65, -0.26, 0])

        self.thetat = man.Angle(
            line1 = self.vtx,
            line2 = self.ft,
            radius = 1.6,
        )

        self.thetat_velikost = man.MathTex("\\theta_\\mathrm{T}").move_to(self.thetat.get_center() + [0.38, 0.15, 0])
# ---------------------------------------------------------------------------------------------------------------------------------

        self.play(man.FadeIn(self.kazalcni_diagram))
        self.wait()
        self.play(man.FadeOut(self.ot, self.ot_velikost, self.phiz, self.phiz_velikost, self.pk1, self.alpha, self.alpha_velikost, self.gamma, self.gamma_velikost,
                              self.vty, self.vty_velikost, self.vtys, self.vty_smer, self.vdy, self.vdy_velikost, self.vdys, self.vdy_smer))
        self.play(self.vvx_velikost.animate.move_to(self.vvx.get_center() + [0, 0.45, 0]))
        self.play(man.Create(self.ot3))
        self.play(man.Write(self.ot3_velikost))
        self.play(man.GrowFromPoint(self.vks, self.vks.get_start()))
        self.play(man.Write(self.vk_smer))
        self.play(man.Write(self.vk_velikost))
        self.play(man.Create(self.phiz4))
        self.play(man.Write(self.phiz4_velikost))
        self.wait()
        self.play(man.GrowArrow(self.ft))
        self.play(man.Write(self.ft_velikost))
        self.wait()
        self.play(man.Create(self.phit))
        self.play(man.Write(self.phit_velikost))
        self.play(man.GrowFromPoint(self.fts, self.fts.get_start()))
        self.play(man.Write(self.ft_smer))
        self.play(man.Create(self.thetat))
        self.play(man.Write(self.thetat_velikost))
        self.wait()

# definiram tukaj elemente, ker so premaknjeni glede na njihovo originalno pozicijo -----------------------------------------------
        self.kazalcni_diagram.remove(self.ot, self.ot_velikost, self.phiz, self.phiz_velikost, self.pk1,
                                     self.alpha, self.alpha_velikost, self.gamma, self.gamma_velikost,
                                     self.vty, self.vty_velikost, self.vtys, self.vty_smer, self.vdy, self.vdy_velikost, self.vdys, self.vdy_smer)
        self.kazalcni_diagram.add(self.ot3, self.ot3_velikost, self.vks, self.vk_smer, self.vk_velikost, self.phiz4, self.phiz4_velikost,
                                  self.ft, self.ft_velikost, self.fts, self.ft_smer, self.phit, self.phit_velikost, self.thetat, self.thetat_velikost)
# ---------------------------------------------------------------------------------------------------------------------------------

        self.play(self.kazalcni_diagram.animate.move_to([3, 0.25, 0]))
        self.play(man.Write(self.transmisivnost))
        self.play(man.Write(self.T))
        self.play(man.Write(self.f0ft))
        self.wait()
        self.play(self.kazalcni_diagram.animate.scale(0.7).move_to([4, 0.25, 0]))
        self.play(man.Write(self.pitagora2))
        self.wait()
        self.play(man.Write(self.ft_kvadrat), man.Wiggle(self.ft, rotation_angle = 0))
        self.play(man.Write(self.enacaj6))
        self.play(man.Write(self.kateta1ft), man.Wiggle(self.vtx, rotation_angle = 0))
        self.play(man.Write(self.plus10))
        self.play(man.Write(self.kateta2ft), man.Wiggle(self.vdx, rotation_angle = 0))
        self.wait()
        self.play(man.Write(self.f0_kvadrat), man.Wiggle(self.vk, rotation_angle = 0))
        self.play(man.Write(self.enacaj5))
        self.play(man.Write(self.kateta1f0), man.Wiggle(self.vtx, rotation_angle = 0), man.Wiggle(self.vvx, rotation_angle = 0))
        self.play(man.Write(self.plus9))
        self.play(man.Write(self.kateta2f0), man.Wiggle(self.vdx, rotation_angle = 0))
        self.wait()
        self.play(man.Write(self.enacaj7))
        self.play(man.Write(self.f0ft_pod_koren))
        self.wait()
        self.play(man.FadeOut(self.pitagora2), man.Unwrite(self.f0ft), man.Unwrite(self.enacaj7), man.Unwrite(self.f0ft_pod_koren))
        self.play(self.T.animate.shift(2*man.LEFT + 0.5*man.DOWN))
        self.play(man.Write(self.T_koren1))
        self.play(man.Unwrite(self.f0_kvadrat), man.Unwrite(self.enacaj5), man.Unwrite(self.kateta1f0), man.Unwrite(self.plus9), man.Unwrite(self.kateta2f0),
                  man.Unwrite(self.ft_kvadrat), man.Unwrite(self.enacaj6), man.Unwrite(self.kateta1ft), man.Unwrite(self.plus10), man.Unwrite(self.kateta2ft))
        self.wait()
        self.play(man.Write(self.r))
        self.play(man.Unwrite(self.T_koren1))
        self.play(man.Write(self.T_koren2))
        self.play(self.kazalcni_diagram.animate.scale(1/0.7).move_to([3, 0.25, 0]))
        self.wait()

# definiram tukaj elemente, ker so premaknjeni glede na njihovo originalno pozicijo -----------------------------------------------
        self.phit_def = man.MathTex("\\varphi_\\mathrm{T} = \\varphi_\\mathrm{z} - \\theta_\\mathrm{T}").move_to([-3.5, -1.8, 0])

        self.phiz_def = man.MathTex("\\mathrm{tan}(\\varphi_\\mathrm{z}) = \\frac{2 \\delta r}{1 - r^2}").move_to([-5, -2.9, 0])

        self.thetat_def = man.MathTex("\\mathrm{tan}(\\theta_\\mathrm{T}) = 2 \\delta r").move_to([-1, -2.9, 0])

        self.tan_phit = man.MathTex("\\mathrm{tan} (\\varphi_\\mathrm{T}) = \\frac{2 \\delta r^3}{1 - r^2 + (2 \\delta r)^2}").move_to([-3.5, -2.2, 0])
# ---------------------------------------------------------------------------------------------------------------------------------

        self.play(self.transmisivnost.animate.shift(0.75*man.UP),
                  self.T.animate.shift(0.75*man.UP),
                  self.T_koren2.animate.shift(0.75*man.UP),
                  self.r.animate.shift(1*man.UP))
        self.play(man.Write(self.phit_def))
        self.wait()
        self.play(man.Write(self.phiz_def))
        self.wait()
        self.play(man.Write(self.thetat_def))
        self.wait()
        self.play(man.Unwrite(self.phit_def), man.Unwrite(self.phiz_def), man.Unwrite(self.thetat_def))
        self.play(man.Write(self.tan_phit))
        self.wait()
        self.play(man.FadeOut(self.kazalcni_diagram, self.transmisivnost, self.T, self.T_koren2, self.r, self.tan_phit))
        self.wait()

# definiram tukaj elemente, ker so premaknjeni glede na njihovo originalno pozicijo -----------------------------------------------
        self.sistem21 = man.Group(
            self.masa2, self.m2,
            self.vzmet2, self.k2,
            self.dusilka_spodaj2, self.dusilka_zgoraj2, self.d2,
            self.podlaga2,
        ).shift(1*man.UP)

        self.delta.move_to([0, 2.5, 0])

        self.pod00 = man.Rectangle(
            stroke_opacity = 0,
            fill_color = "#995c00",
            fill_opacity = 0.8,
            height = 1,
            width = 2,
        ).move_to([0, -2.5, 0])

        self.pod0 = man.Line(
            start = [-1, -2, 0],
            end = [1, -2, 0],
        )
        
        self.sr1 = man.Line(
            start = [-1, -2.25, 0],
            end = [-0.75, -2, 0],
        )
        
        self.sr2 = man.Line(
            start = [-1, -2.75, 0],
            end = [-0.25, -2, 0],
        )
        
        self.sr3 = man.Line(
            start = [-0.75, -3, 0],
            end = [0.25, -2, 0],
        )
        
        self.sr4 = man.Line(
            start = [-0.25, -3, 0],
            end = [0.75, -2, 0],
        )
        
        self.sr5 = man.Line(
            start = [0.25, -3, 0],
            end = [1, -2.25, 0],
        )
        
        self.sr6 = man.Line(
            start = [0.75, -3, 0],
            end = [1, -2.75, 0],
        )
        
        self.podlaga_srafura = man.Group(
            self.pod00,
            self.pod0,
            self.sr1, self.sr2, self.sr3, self.sr4, self.sr5, self.sr6,
        )

        self.sila_f0 = man.Arrow(
            start = self.masa2.get_center(),
            end = self.masa2.get_center() + [0, 1, 0],
            color = man.RED,
            max_stroke_width_to_length_ratio = 8,
            max_tip_length_to_length_ratio = 0.40,
            buff = 0,
        )

        self.sila_f0_velikost = man.MathTex("\\def\\mathbi#1{\\textbf{\\em #1}}\\mathbi{F}", color = man.RED).move_to(self.sila_f0.get_end() + [-0.4, -0.1, 0])

        self.sila_ft = man.Arrow(
            start = self.pod0.get_center(),
            end = self.pod0.get_center() + [0, 0.5, 0],
            color = man.ORANGE,
            max_stroke_width_to_length_ratio = 16,
            max_tip_length_to_length_ratio = 0.80,
            buff = 0,
        )

        self.sila_ft_velikost = man.MathTex("\\def\\mathbi#1{\\textbf{\\em #1}}\\mathbi{F}_\\mathrm{T}", color = man.ORANGE)
        self.sila_ft_velikost.move_to(self.sila_ft.get_end() + [0.1, 0.2, 0]) # da ni predolgo
# ---------------------------------------------------------------------------------------------------------------------------------

        self.play(man.FadeIn(self.sistem21), man.Write(self.delta))
        self.wait()
        self.play(man.FadeOut(self.podlaga2), man.FadeIn(self.podlaga_srafura))
        self.wait()
        self.play(man.GrowArrow(self.sila_f0))
        self.play(man.Write(self.sila_f0_velikost))
        self.wait()
        self.play(man.GrowArrow(self.sila_ft))
        self.play(man.Write(self.sila_ft_velikost))
        self.wait()

# definiram tukaj elemente, ker so premaknjeni glede na njihovo originalno pozicijo -----------------------------------------------
        self.sistem21.remove(self.podlaga2)
        self.sistem21.add(self.podlaga_srafura, self.sila_f0, self.sila_f0_velikost, self.sila_ft, self.sila_ft_velikost)

        self.tabela2 = man.MathTable([
            ["r", "0,5", "1", "2"],
            ["\\frac{X}{Y}", "1,33", "5,10", "0,36"],
            ["\\varphi_\\mathrm{z}", "0,03\\ \\mathrm{rad}", "1,37\\ \\mathrm{rad}", "2,63\\ \\mathrm{rad}"]
        ]).scale(0.8).move_to([1.5, 0, 0])

        self.tabela2[0][1].set_color(man.GREEN)
        self.tabela2[0][5].set_color(man.GREEN)
        self.tabela2[0][9].set_color(man.GREEN)
        self.tabela2[0][2].set_color(man.YELLOW_D)
        self.tabela2[0][6].set_color(man.YELLOW_D)
        self.tabela2[0][10].set_color(man.YELLOW_D)
        self.tabela2[0][3].set_color(man.BLUE)
        self.tabela2[0][7].set_color(man.BLUE)
        self.tabela2[0][11].set_color(man.BLUE)

        self.tabT = man.MathTex("T").scale(0.8).move_to(self.tabela2[0][4].get_center())
        self.tabphit = man.MathTex("\\varphi_\\mathrm{T}").scale(0.8).move_to(self.tabela2[0][8].get_center())
# ---------------------------------------------------------------------------------------------------------------------------------

        self.play(self.sistem21.animate.move_to([-5, -0.5, 0]), self.delta.animate.move_to([-5, 2.5, 0]))
        self.wait()
        self.play(man.FadeIn(self.tabela2))
        self.wait()
        self.play(man.Unwrite(self.tabela2[0][4]))
        self.play(man.Write(self.tabT))
        self.play(man.Unwrite(self.tabela2[0][8]))
        self.play(man.Write(self.tabphit))
        self.wait()
        self.play(man.FadeOut(self.sistem21, self.delta, self.tabela2, self.tabT, self.tabphit))
        self.wait()

# definiram tukaj elemente, ker so premaknjeni glede na njihovo originalno pozicijo -----------------------------------------------
        self.ref3 = man.NumberLine(
            x_range = [0, 6],
            length = 6,
            include_ticks = False,
            include_tip = True,
            tip_width = 0.2,
            tip_height = 0.2,
        )

        self.referenca3 = man.Tex("referenca").next_to(self.ref3.get_end(), man.DOWN, buff = 0.15).scale(0.4)

        self.f0k = man.Arrow(
            start = self.ref3.get_start(),
            end = self.ref3.get_start() + [1 * 1.5 * man.np.cos((6/16) * man.PI), 1 * 1.5 * man.np.sin((6/16) * man.PI), 0],
            color = man.RED,
            max_stroke_width_to_length_ratio = 5.333,
            max_tip_length_to_length_ratio = 0.267,
            stroke_width = 5,
            buff = 0,
        )

        self.f0k_velikost = man.MathTex("f_0", color = man.RED).move_to(self.f0k.get_center() + [-0.35, 0, 0])

        self.ot4 = man.Angle(
            line1 = self.ref3,
            line2 = self.f0k,
            radius = 0.5,
        )

        self.ot4_velikost = man.MathTex("\\omega t").move_to(self.ot4.get_start() + [0.3, 0.3, 0])

        self.f0ks = man.DashedLine(
            start = self.f0k.get_end(),
            end = self.f0k.get_end() + [2 * man.np.cos((6/16) * man.PI), 2 * man.np.sin((6/16) * man.PI), 0],
            stroke_opacity = 0.2,
        )

        self.f0k_smer = man.MathTex("\\mathrm{sin} (\\omega t)").scale(0.5).rotate((6/16) * man.PI).move_to(self.f0ks.get_end() + [-0.29, -0.33, 0])

        self.r1 = man.MathTex("r = 0,5").scale(0.8).move_to([-4.5, 2.5, 0])

        self.ft1 = man.Arrow(
            start = self.ref3.get_start(),
            end = self.ref3.get_start() + [1.33 * 1.5 * man.np.cos((6/16) * man.PI - 0.03), 1.33 * 1.5 * man.np.sin((6/16) * man.PI - 0.03), 0],
            color = man.ORANGE,
            max_stroke_width_to_length_ratio = 4.010,
            max_tip_length_to_length_ratio = 0.201,
            stroke_width = 5,
            buff = 0,
        )

        self.ft1_velikost = man.MathTex("f_\\mathrm{T}", color = man.ORANGE).move_to(self.ft1.get_center() + [0.5, 0.2, 0])

        self.phit1 = man.Angle(
            line1 = self.f0k,
            line2 = self.ft1,
            radius = 1,
            other_angle = True,
        )

        self.phit1_velikost = man.MathTex("\\varphi_\\mathrm{T}").move_to(self.phit1.get_start() + [-0.35, 0.25, 0])

        self.ft1s = man.DashedLine(
            start = self.ft1.get_end(),
            end = self.ft1.get_end() + [2 * man.np.cos((6/16) * man.PI - 0.03), 2 * man.np.sin((6/16) * man.PI - 0.03), 0],
            stroke_opacity = 0.2,
        )

        self.ft1_smer = man.MathTex("\\mathrm{sin} (\\omega t - \\varphi_\\mathrm{T})")
        self.ft1_smer.scale(0.5).rotate((6/16) * man.PI - 0.03).move_to(self.ft1s.get_end() + [-0.12, -0.73, 0])

        self.r2 = man.MathTex("r = 1").scale(0.8).move_to([-4.5, 2.5, 0])

        self.ft2 = man.Arrow(
            start = self.ref3.get_start(),
            end = self.ref3.get_start() + [5.10 * 1.5 * man.np.cos((6/16) * man.PI - 1.37), 5.10 * 1.5 * man.np.sin((6/16) * man.PI - 1.37), 0],
            color = man.ORANGE,
            max_stroke_width_to_length_ratio = 1.046,
            max_tip_length_to_length_ratio = 0.052,
            stroke_width = 5,
            buff = 0,
        )

        self.ft2_velikost = man.MathTex("f_\\mathrm{T}", color = man.ORANGE).move_to(self.ft2.get_center() + [0.5, 0.3, 0])

        self.phit2 = man.Angle(
            line1 = self.f0k,
            line2 = self.ft2,
            radius = 2,
            other_angle = True,
        )

        self.phit2_velikost = man.MathTex("\\varphi_\\mathrm{T}").move_to(self.phit2.get_center() + [0.85, 0, 0])

        self.ft2s = man.DashedLine(
            start = self.ft2.get_start(),
            end = self.ft2.get_start() + [-2 * man.np.cos((6/16) * man.PI - 1.37), -2 * man.np.sin((6/16) * man.PI - 1.37), 0],
            stroke_opacity = 0.2,
        )

        self.ft2_smer = man.MathTex("\\mathrm{sin} (\\omega t - \\varphi_\\mathrm{T})")
        self.ft2_smer.scale(0.5).rotate((6/16) * man.PI - 1.37).move_to(self.ft2s.get_end() + [0.73, 0.01, 0])

        self.r3 = man.MathTex("r = 2").scale(0.8).move_to([-4.5, 2.5, 0])

        self.ft3 = man.Arrow(
            start = self.ref3.get_start(),
            end = self.ref3.get_start() + [0.36 * 1.5 * man.np.cos((6/16) * man.PI - 2.63), 0.36 * 1.5 * man.np.sin((6/16) * man.PI - 2.63), 0],
            color = man.ORANGE,
            max_stroke_width_to_length_ratio = 14.815,
            max_tip_length_to_length_ratio = 0.741,
            stroke_width = 5,
            buff = 0,
        )

        self.ft3_velikost = man.MathTex("f_\\mathrm{T}", color = man.ORANGE).move_to(self.ft3.get_center() + [0.4, -0.02, 0])

        self.phit3 = man.Angle(
            line1 = self.f0k,
            line2 = self.ft3,
            radius = 0.1,
            other_angle = True,
        )

        self.phit3_velikost = man.MathTex("\\varphi_\\mathrm{T}").move_to(self.phit3.get_center() + [-0.4, 0, 0])

        self.ft3s = man.DashedLine(
            start = self.ft3.get_end(),
            end = self.ft3.get_end() + [2 * man.np.cos((6/16) * man.PI - 2.63), 2 * man.np.sin((6/16) * man.PI - 2.63), 0],
            stroke_opacity = 0.2,
        )

        self.ft3_smer = man.MathTex("\\mathrm{sin} (\\omega t - \\varphi_\\mathrm{T})")
        self.ft3_smer.scale(0.5).rotate((6/16) * man.PI - 2.63).move_to(self.ft3s.get_end() + [0.12, 0.71, 0])

        self.r12 = man.MathTex("r = 0,5").scale(0.8).move_to([-4.5, 2.5, 0])

        self.ref3_kopija = self.ref3.copy()

        self.referenca3_kopija = self.referenca3.copy()

        self.refgor2 = man.NumberLine(
            x_range = [0, 3],
            length = 3,
            include_ticks = False,
            include_tip = True,
            tip_width = 0.2,
            tip_height = 0.2,
        ).move_to([3, 2.35, 0])

        self.refdol2 = man.NumberLine(
            x_range = [0, 3],
            length = 3,
            include_ticks = False,
            include_tip = True,
            tip_width = 0.2,
            tip_height = 0.2,
        ).move_to([3, -1.85, 0])

        self.nsgor2 = self.refgor2.get_start()
        self.nef0k = self.refgor2.get_start() + [1 * 0.75 * man.np.cos((6/16) * man.PI), 1 * 0.75 * man.np.sin((6/16) * man.PI), 0]
        self.nsdol2 = self.refdol2.get_start()
        self.neft1 = self.refdol2.get_start() + [1.33 * 0.75 * man.np.cos((6/16) * man.PI - 0.03), 1.33 * 0.75 * man.np.sin((6/16) * man.PI - 0.03), 0]
        self.neft2 = self.refdol2.get_start() + [5.10 * 0.75 * man.np.cos((6/16) * man.PI - 1.37), 5.10 * 0.75 * man.np.sin((6/16) * man.PI - 1.37), 0]
        self.neft3 = self.refdol2.get_start() + [0.36 * 0.75 * man.np.cos((6/16) * man.PI - 2.63), 0.36 * 0.75 * man.np.sin((6/16) * man.PI - 2.63), 0]
# ---------------------------------------------------------------------------------------------------------------------------------

        self.play(man.Create(self.ref3))
        self.play(man.Write(self.referenca3))
        self.wait()
        self.play(man.GrowArrow(self.f0k))
        self.play(man.Write(self.f0k_velikost))
        self.play(man.Create(self.ot4))
        self.play(man.Write(self.ot4_velikost))
        self.play(man.GrowFromPoint(self.f0ks, self.f0ks.get_start()))
        self.play(man.Write(self.f0k_smer))
        self.wait()
        self.play(man.Write(self.r1))
        self.wait()
        self.play(man.GrowArrow(self.ft1))
        self.play(man.Write(self.ft1_velikost))
        self.play(man.Create(self.phit1))
        self.play(man.Write(self.phit1_velikost))
        self.play(man.GrowFromPoint(self.ft1s, self.ft1s.get_start()))
        self.play(man.Write(self.ft1_smer))
        self.wait()
        self.play(man.Unwrite(self.r1), man.FadeOut(self.ft1, self.ft1_velikost, self.phit1, self.phit1_velikost, self.ft1s, self.ft1_smer))
        self.wait()
        self.play(man.Write(self.r2))
        self.wait()
        self.play(man.GrowArrow(self.ft2))
        self.play(man.Write(self.ft2_velikost))
        self.play(man.Create(self.phit2))
        self.play(man.Write(self.phit2_velikost))
        self.play(man.GrowFromPoint(self.ft2s, self.ft2s.get_start()))
        self.play(man.Write(self.ft2_smer))
        self.wait()
        self.play(man.Unwrite(self.r2), man.FadeOut(self.ft2, self.ft2_velikost, self.phit2, self.phit2_velikost, self.ft2s, self.ft2_smer))
        self.wait()
        self.play(man.Write(self.r3))
        self.wait()
        self.play(man.GrowArrow(self.ft3))
        self.play(man.Write(self.ft3_velikost))
        self.play(man.Create(self.phit3))
        self.play(man.Write(self.phit3_velikost))
        self.play(man.GrowFromPoint(self.ft3s, self.ft3s.get_start()))
        self.play(man.Write(self.ft3_smer))
        self.wait()
        self.play(man.Unwrite(self.r3), man.FadeOut(self.ft3, self.ft3_velikost, self.phit3, self.phit3_velikost, self.ft3s, self.ft3_smer))
        self.play(man.FadeIn(self.r12, self.ft1, self.ft1_velikost, self.phit1, self.phit1_velikost, self.ft1s, self.ft1_smer))
        self.wait()
        self.add(self.ref3_kopija, self.referenca3_kopija)
        self.play(man.FadeOut(self.f0k_velikost, self.ft1_velikost,
                              self.ot4, self.ot4_velikost, self.phit1, self.phit1_velikost,
                              self.f0ks, self.f0k_smer, self.ft1s, self.ft1_smer))
        self.play(man.Transform(self.ref3, self.refgor2), self.referenca3.animate.shift(1.5*man.RIGHT + 2.4*man.UP),
                  man.Transform(self.ref3_kopija, self.refdol2), self.referenca3_kopija.animate.shift(1.5*man.RIGHT + 1.8*man.DOWN),
                  self.f0k.animate.set_max_stroke_width_to_length_ratio(10.667).put_start_and_end_on(self.nsgor2, self.nef0k),
                  self.ft1.animate.set_max_stroke_width_to_length_ratio(8.020).put_start_and_end_on(self.nsdol2, self.neft1),
                  self.r12.animate.move_to([3, 0.25, 0]))
        self.wait()
        
# definiram tukaj elemente, ker so premaknjeni glede na njihovo originalno pozicijo -----------------------------------------------
        self.ft2.set_max_stroke_width_to_length_ratio(2.092).put_start_and_end_on(self.nsdol2, self.neft2)
        self.ft3.set_max_stroke_width_to_length_ratio(29.630).put_start_and_end_on(self.nsdol2, self.neft3)

        self.masa.move_to([-3, 2.35, 0])
        self.m.move_to(self.masa.get_center() + [0.6, -0.2, 0])
        self.podlaga_srafura.move_to([-3, -2.35, 0])

        self.r22 = man.MathTex("r = 1").scale(0.8).move_to([3, 0.25, 0])
        self.r32 = man.MathTex("r = 2").scale(0.8).move_to([3, 0.25, 0])

        self.tracker_sil = man.ValueTracker((6/16) * man.PI)

        self.sila_masa = man.Arrow(
            start = self.masa.get_center(),
            end = self.masa.get_center() + [0, 1 * 0.75 * man.np.sin((6/16) * man.PI), 0],
            color = man.RED,
            max_stroke_width_to_length_ratio = 10.667/man.np.abs(man.np.sin((6/16) * man.PI)),
            max_tip_length_to_length_ratio = 0.534/man.np.abs(man.np.sin((6/16) * man.PI)),
            stroke_width = 5,
            buff = 0,
        )

        self.sila_podlaga1 = man.Arrow(
            start = self.podlaga_srafura.get_center() + [0, 0.5, 0],
            end = self.podlaga_srafura.get_center() + [0, 0.5, 0] + [0, 1.33 * 0.75 * man.np.sin((6/16) * man.PI - 0.03), 0],
            color = man.ORANGE,
            max_stroke_width_to_length_ratio = 8.020/man.np.abs(man.np.sin((6/16) * man.PI - 0.03)),
            max_tip_length_to_length_ratio = 0.402/man.np.abs(man.np.sin((6/16) * man.PI - 0.03)),
            stroke_width = 5,
            buff = 0,
        )

        self.povf0k = man.DashedLine(
            start = self.f0k.get_end(),
            end = self.sila_masa.get_end(),
            stroke_opacity = 0.2,
        )

        self.povft1 = man.DashedLine(
            start = self.ft1.get_end(),
            end = self.sila_podlaga1.get_end(),
            stroke_opacity = 0.2,
        )

        def update_f0k(f0k, dt):
            new_start_f0k = self.refgor2.get_start()
            new_end_f0k = self.refgor2.get_start() + [1 * 0.75 * man.np.cos(self.tracker_sil.get_value()), 1 * 0.75 * man.np.sin(self.tracker_sil.get_value()), 0]
            self.f0k.put_start_and_end_on(new_start_f0k, new_end_f0k)
        
        def update_sila_masa(sila_masa, dt):
            new_start_sila_masa = self.masa.get_center()
            new_end_sila_masa = self.masa.get_center() + [0, 1 * 0.75 * man.np.sin(self.tracker_sil.get_value()), 0]
            self.sila_masa.put_start_and_end_on(new_start_sila_masa, new_end_sila_masa)
        
        def update_povf0k(povf0k, dt):
            new_start_povf0k = self.f0k.get_end()
            new_end_povf0k = self.sila_masa.get_end()
            self.povf0k.put_start_and_end_on(new_start_povf0k, new_end_povf0k)
        
        def update_ft1(ft1, dt):
            new_start_ft1 = self.refdol2.get_start()
            new_end_ft1 = self.refdol2.get_start() + [1.33 * 0.75 * man.np.cos(self.tracker_sil.get_value() - 0.03), 1.33 * 0.75 * man.np.sin(self.tracker_sil.get_value() - 0.03), 0]
            self.ft1.put_start_and_end_on(new_start_ft1, new_end_ft1)
        
        def update_sila_podlaga1(sila_podlaga1, dt):
            new_start_sila_podlaga1 = self.podlaga_srafura.get_center() + [0, 0.5, 0]
            new_end_sila_podlaga1 = self.podlaga_srafura.get_center() + [0, 0.5, 0] + [0, 1.33 * 0.75 * man.np.sin(self.tracker_sil.get_value() - 0.03), 0]
            self.sila_podlaga1.put_start_and_end_on(new_start_sila_podlaga1, new_end_sila_podlaga1)
        
        def update_povft1(povft1, dt):
            new_start_povft1 = self.ft1.get_end()
            new_end_povft1 = self.sila_podlaga1.get_end()
            self.povft1.put_start_and_end_on(new_start_povft1, new_end_povft1)
        
        self.sila_podlaga2 = man.Arrow(
            start = self.podlaga_srafura.get_center() + [0, 0.5, 0],
            end = self.podlaga_srafura.get_center() + [0, 0.5, 0] + [0, 5.10 * 0.75 * man.np.sin((6/16) * man.PI - 1.37), 0],
            color = man.ORANGE,
            max_stroke_width_to_length_ratio = 2.092/man.np.abs(man.np.sin((6/16) * man.PI - 1.37)),
            max_tip_length_to_length_ratio = 0.105/man.np.abs(man.np.sin((6/16) * man.PI - 1.37)),
            stroke_width = 5,
            buff = 0,
        )

        self.povft2 = man.DashedLine(
            start = self.ft2.get_end(),
            end = self.sila_podlaga2.get_end(),
            stroke_opacity = 0.2,
        )

        def update_ft2(ft2, dt):
            new_start_ft2 = self.refdol2.get_start()
            new_end_ft2 = self.refdol2.get_start() + [5.10 * 0.75 * man.np.cos(self.tracker_sil.get_value() - 1.37), 5.10 * 0.75 * man.np.sin(self.tracker_sil.get_value() - 1.37), 0]
            self.ft2.put_start_and_end_on(new_start_ft2, new_end_ft2)
        
        def update_sila_podlaga2(sila_podlaga2, dt):
            new_start_sila_podlaga2 = self.podlaga_srafura.get_center() + [0, 0.5, 0]
            new_end_sila_podlaga2 = self.podlaga_srafura.get_center() + [0, 0.5, 0] + [0, 5.10 * 0.75 * man.np.sin(self.tracker_sil.get_value() - 1.37), 0]
            self.sila_podlaga2.put_start_and_end_on(new_start_sila_podlaga2, new_end_sila_podlaga2)
        
        def update_povft2(povft2, dt):
            new_start_povft2 = self.ft2.get_end()
            new_end_povft2 = self.sila_podlaga2.get_end()
            self.povft2.put_start_and_end_on(new_start_povft2, new_end_povft2)
        
        self.sila_podlaga3 = man.Arrow(
            start = self.podlaga_srafura.get_center() + [0, 0.5, 0],
            end = self.podlaga_srafura.get_center() + [0, 0.5, 0] + [0, 0.36 * 0.75 * man.np.sin((6/16) * man.PI - 2.63), 0],
            color = man.ORANGE,
            max_stroke_width_to_length_ratio = 29.630/man.np.abs(man.np.sin((6/16) * man.PI - 2.63)),
            max_tip_length_to_length_ratio = 1.481/man.np.abs(man.np.sin((6/16) * man.PI - 2.63)),
            stroke_width = 5,
            buff = 0,
        )

        self.povft3 = man.DashedLine(
            start = self.ft3.get_end(),
            end = self.sila_podlaga3.get_end(),
            stroke_opacity = 0.2,
        )

        def update_ft3(ft3, dt):
            new_start_ft3 = self.refdol2.get_start()
            new_end_ft3 = self.refdol2.get_start() + [0.36 * 0.75 * man.np.cos(self.tracker_sil.get_value() - 2.63), 0.36 * 0.75 * man.np.sin(self.tracker_sil.get_value() - 2.63), 0]
            self.ft3.put_start_and_end_on(new_start_ft3, new_end_ft3)
        
        def update_sila_podlaga3(sila_podlaga3, dt):
            new_start_sila_podlaga3 = self.podlaga_srafura.get_center() + [0, 0.5, 0]
            new_end_sila_podlaga3 = self.podlaga_srafura.get_center() + [0, 0.5, 0] + [0, 0.36 * 0.75 * man.np.sin(self.tracker_sil.get_value() - 2.63), 0]
            self.sila_podlaga3.put_start_and_end_on(new_start_sila_podlaga3, new_end_sila_podlaga3)
        
        def update_povft3(povft3, dt):
            new_start_povft3 = self.ft3.get_end()
            new_end_povft3 = self.sila_podlaga3.get_end()
            self.povft3.put_start_and_end_on(new_start_povft3, new_end_povft3)
# ---------------------------------------------------------------------------------------------------------------------------------

        self.play(man.FadeIn(self.masa, self.m, self.podlaga_srafura))
        self.wait()
        self.play(man.GrowArrow(self.sila_masa), man.GrowFromPoint(self.povf0k, self.povf0k.get_start()),
                  man.GrowArrow(self.sila_podlaga1), man.GrowFromPoint(self.povft1, self.povft1.get_start()))
        self.wait()

# definiram tukaj elemente, ker so premaknjeni glede na njihovo originalno pozicijo -----------------------------------------------
        self.f0k.add_updater(update_f0k)
        self.sila_masa.add_updater(update_sila_masa)
        self.povf0k.add_updater(update_povf0k)
        self.ft1.add_updater(update_ft1)
        self.sila_podlaga1.add_updater(update_sila_podlaga1)
        self.povft1.add_updater(update_povft1)
# ---------------------------------------------------------------------------------------------------------------------------------

        self.play(self.tracker_sil.animate.set_value((6/16) * man.PI + 4 * man.PI),
                  rate_func = man.linear, run_time = 8)
        self.wait()

# definiram tukaj elemente, ker so premaknjeni glede na njihovo originalno pozicijo -----------------------------------------------
        self.tracker_sil.set_value((6/16) * man.PI)

        self.ft1.clear_updaters()
        self.sila_podlaga1.clear_updaters()
        self.povft1.clear_updaters()
# ---------------------------------------------------------------------------------------------------------------------------------

        self.play(man.FadeOut(self.ft1, self.sila_podlaga1, self.povft1, self.r12))
        self.play(man.GrowArrow(self.ft2), man.FadeIn(self.r22))
        self.play(man.GrowArrow(self.sila_podlaga2), man.GrowFromPoint(self.povft2, self.povft2.get_start()))
        self.wait()

# definiram tukaj elemente, ker so premaknjeni glede na njihovo originalno pozicijo -----------------------------------------------
        self.ft2.add_updater(update_ft2)
        self.sila_podlaga2.add_updater(update_sila_podlaga2)
        self.povft2.add_updater(update_povft2)
# ---------------------------------------------------------------------------------------------------------------------------------

        self.play(self.tracker_sil.animate.set_value((6/16) * man.PI + 8 * man.PI),
                  rate_func = man.linear, run_time = 8)
        self.wait()

# definiram tukaj elemente, ker so premaknjeni glede na njihovo originalno pozicijo -----------------------------------------------
        self.tracker_sil.set_value((6/16) * man.PI)

        self.ft2.clear_updaters()
        self.sila_podlaga2.clear_updaters()
        self.povft2.clear_updaters()
# ---------------------------------------------------------------------------------------------------------------------------------

        self.play(man.FadeOut(self.ft2, self.sila_podlaga2, self.povft2, self.r22))
        self.play(man.GrowArrow(self.ft3), man.FadeIn(self.r32))
        self.play(man.GrowArrow(self.sila_podlaga3), man.GrowFromPoint(self.povft3, self.povft3.get_start()))
        self.wait()

# definiram tukaj elemente, ker so premaknjeni glede na njihovo originalno pozicijo -----------------------------------------------
        self.ft3.add_updater(update_ft3)
        self.sila_podlaga3.add_updater(update_sila_podlaga3)
        self.povft3.add_updater(update_povft3)
# ---------------------------------------------------------------------------------------------------------------------------------

        self.play(self.tracker_sil.animate.set_value((6/16) * man.PI + 16 * man.PI),
                  rate_func = man.linear, run_time = 8)
        self.wait()

# definiram tukaj elemente, ker so premaknjeni glede na njihovo originalno pozicijo -----------------------------------------------
        self.tracker_sil.set_value((6/16) * man.PI)

        self.f0k.clear_updaters()
        self.sila_masa.clear_updaters()
        self.povf0k.clear_updaters()
        self.ft3.clear_updaters()
        self.sila_podlaga3.clear_updaters()
        self.povft3.clear_updaters()
# ---------------------------------------------------------------------------------------------------------------------------------

        self.play(man.FadeOut(self.masa, self.m, self.sila_masa, self.ref3, self.refgor2, self.referenca3, self.f0k, self.povf0k, self.r32,
                              self.podlaga_srafura, self.sila_podlaga3, self.ref3_kopija, self.refdol2, self.referenca3_kopija, self.ft3, self.povft3))
        self.wait()

# definiram tukaj elemente, ker so premaknjeni glede na njihovo originalno pozicijo -----------------------------------------------
        self.pod00k = man.Rectangle(
            stroke_opacity = 0,
            fill_color = "#995c00",
            fill_opacity = 0.8,
            height = 5,
            width = 15,
            ).move_to([0, -4.5, 0])
        
        self.pod0k = man.Line(
            start = [-7.5, -2, 0],
            end = [7.5, -2, 0],
            )
        
        self.srafurak = man.Group()
        i = 0
        xs = -12.25
        xe = -7.25
        while i < 35:
            pod = man.Line(
                start = [xs, -7, 0],
                end = [xe, -2, 0],
                )
            self.srafurak.add(pod)
            xs += 0.5
            xe += 0.5
            i += 1
        
        self.podlagak = man.Group(
            self.pod00k,
            self.srafurak,
            self.pod0k,
            )
        
        self.masa_podk = man.RoundedRectangle(
            color = man.GRAY,
            fill_color = man.GRAY,
            fill_opacity = 0.5,
            height = 0.5,
            width = 1,
            corner_radius = 0.1,
            ).move_to([-4, 1.25, 0])

        self.m_podk = man.MathTex("m").scale(0.5).move_to(self.masa_podk.get_center() + [0.3, -0.1, 0])
        
        self.sila_masa_podk = man.Arrow(
            start = self.masa_podk.get_center(),
            end = self.masa_podk.get_center() + [0, 1 * 0.75 * 0.5 * man.np.sin((6/16) * man.PI), 0],
            color = man.RED,
            max_stroke_width_to_length_ratio = 10.667/man.np.abs(man.np.sin((6/16) * man.PI)),
            max_tip_length_to_length_ratio = 0.533/man.np.abs(man.np.sin((6/16) * man.PI)),
            stroke_width = 5,
            buff = 0,
        )

        self.sila_podlaga_podk = man.Arrow(
            start = self.pod00k.get_center() + [-4, 2.5, 0],
            end = self.pod00k.get_center() + [-4, 2.5, 0] + [0, 1.33 * 0.75 * 0.5 * man.np.sin((6/16) * man.PI - 0.03), 0],
            color = man.ORANGE,
            max_stroke_width_to_length_ratio = 8.020/man.np.abs(man.np.sin((6/16) * man.PI - 0.03)),
            max_tip_length_to_length_ratio = 0.401/man.np.abs(man.np.sin((6/16) * man.PI - 0.03)),
            stroke_width = 5,
            buff = 0,
        )

        self.r_podk = man.MathTex("r = 0,5", color = man.BLACK).move_to([-4, -3, 0])

        self.vzmet_standard_podk = {1: [-1/4 - 4, -2, 0], 2: [-1/4 - 4, -17/10, 0],
                                   3: [-1/2 - 4 + 2*self.korekcija_x, -8/5, 0], 4: [0 - 4 - 2*self.korekcija_x, -7/5, 0],
                                   5: [-1/2 - 4 + 2*self.korekcija_x, -6/5, 0], 6: [0 - 4 - 2*self.korekcija_x, -1, 0],
                                   7: [-1/2 - 4 + 2*self.korekcija_x, -4/5, 0], 8: [0 - 4 - 2*self.korekcija_x, -3/5, 0],
                                   9: [-1/2 - 4 + 2*self.korekcija_x, -2/5, 0], 10: [0 - 4 - 2*self.korekcija_x, -1/5, 0],
                                   11: [-1/2 - 4 + 2*self.korekcija_x, 0, 0], 12: [0 - 4 - 2*self.korekcija_x, 1/5, 0],
                                   13: [-1/2 - 4 + 2*self.korekcija_x, 2/5, 0], 14: [0 - 4 - 2*self.korekcija_x, 3/5, 0],
                                   15: [-1/4 - 4, 7/10, 0], 16: [-1/4 - 4, 1, 0]}

        self.vzmet_podk = man.Graph([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
                                   [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10), (10, 11), (11, 12), (12, 13), (13, 14), (14, 15), (15, 16)],
                                   layout = self.vzmet_standard_podk,
                                   vertex_config = {'radius': 0},
                                   )

        self.dusilka_spodaj_standard_podk = {1: [1/4 - 4, -2, 0], 2: [1/4 - 4, -1, 0],
                                            3: [0 - 4 + 2*self.korekcija_x, -1, 0], 4: [1/2 - 4 - 2*self.korekcija_x, -1, 0],
                                            5: [0 - 4 + 2*self.korekcija_x, 0, 0], 6: [1/2 - 4 - 2*self.korekcija_x, 0, 0]}

        self.dusilka_spodaj_podk = man.Graph([1, 2, 3, 4, 5, 6],
                                            [(1, 2), (2, 3), (2, 4), (3, 5), (4, 6)],
                                            layout = self.dusilka_spodaj_standard_podk,
                                            vertex_config = {'radius': 0},
                                            )

        self.dusilka_zgoraj_standard_podk = {1: [1/4 - 4, 1, 0], 2: [1/4 - 4, -1/2, 0],
                                            3: [0 - 4 + 3*self.korekcija_x, -1/2, 0], 4: [1/2 - 4 - 3*self.korekcija_x, -1/2, 0]}

        self.dusilka_zgoraj_podk = man.Graph([1, 2, 3, 4],
                                            [(1, 2), (2, 3), (2, 4)],
                                            layout = self.dusilka_zgoraj_standard_podk,
                                            vertex_config = {'radius': 0},
                                            )
        
        self.nihanje_podk = man.ValueTracker(0.13)
        
        def update_masa_podk(masa_podk, dt):
            self.y_masa_podk = 1.32 * 0.75 * 0.5 * man.np.sin(self.nihanje_podk.get_value() - 0.13)
            new_pos_masa_podk = [-4, 1.25 + self.y_masa_podk, 0]
            self.masa_podk.move_to(new_pos_masa_podk)
        
        def update_m_podk(m_podk, dt):
            self.y_masa_podk = 1.32 * 0.75 * 0.5 * man.np.sin(self.nihanje_podk.get_value() - 0.13)
            new_pos_m_podk = [-4 + 0.3, 1.25 - 0.1 + self.y_masa_podk, 0]
            self.m_podk.move_to(new_pos_m_podk)
        
        def update_sila_masa_podk(sila_masa_podk, dt):
            new_start_sila_masa_podk = self.masa_podk.get_center()
            new_end_sila_masa_podk = self.masa_podk.get_center() + [0, 1 * 0.75 * 0.5 * man.np.sin(self.nihanje_podk.get_value()), 0]
            self.sila_masa_podk.put_start_and_end_on(new_start_sila_masa_podk, new_end_sila_masa_podk)
        
        def update_sila_podlaga_podk(sila_podlaga_podk, dt):
            new_start_sila_podlaga_podk = self.pod00k.get_center() + [-4, 2.5, 0]
            new_end_sila_podlaga_podk = self.pod00k.get_center() + [-4, 2.5, 0] + [0, 1.33 * 0.75 * 0.5 * man.np.sin(self.nihanje_podk.get_value() - 0.03), 0]
            self.sila_podlaga_podk.put_start_and_end_on(new_start_sila_podlaga_podk, new_end_sila_podlaga_podk)
        
        def update_vzmet_podk(vzmet_podk, dt):
            self.y_masa_podk = 1.32 * 0.75 * 0.5 * man.np.sin(self.nihanje_podk.get_value() - 0.13 + 0.05) # ker nekaj zaostaja zaradi animacij
            new_layout_vzmet_podk = {1: [-1/4 - 4, -2 + 0/24*self.y_masa_podk, 0],
                                    2: [-1/4 - 4, -17/10 + 0/24*self.y_masa_podk, 0],
                                   3: [-1/2 - 4 + 2*self.korekcija_x, -8/5 + 1/24*self.y_masa_podk, 0],
                                   4: [0 - 4 - 2*self.korekcija_x, -7/5 + 3/24*self.y_masa_podk, 0],
                                   5: [-1/2 - 4 + 2*self.korekcija_x, -6/5 + 5/24*self.y_masa_podk, 0],
                                   6: [0 - 4 - 2*self.korekcija_x, -1 + 7/24*self.y_masa_podk, 0],
                                   7: [-1/2 - 4 + 2*self.korekcija_x, -4/5 + 9/24*self.y_masa_podk, 0],
                                   8: [0 - 4 - 2*self.korekcija_x, -3/5 + 11/24*self.y_masa_podk, 0],
                                   9: [-1/2 - 4 + 2*self.korekcija_x, -2/5 + 13/24*self.y_masa_podk, 0],
                                   10: [0 - 4 - 2*self.korekcija_x, -1/5 + 15/24*self.y_masa_podk, 0],
                                   11: [-1/2 - 4 + 2*self.korekcija_x, 0 + 17/24*self.y_masa_podk, 0],
                                   12: [0 - 4 - 2*self.korekcija_x, 1/5 + 19/24*self.y_masa_podk, 0],
                                   13: [-1/2 - 4 + 2*self.korekcija_x, 2/5 + 21/24*self.y_masa_podk, 0],
                                   14: [0 - 4 - 2*self.korekcija_x, 3/5 + 23/24*self.y_masa_podk, 0],
                                   15: [-1/4 - 4, 7/10 + 24/24*self.y_masa_podk, 0],
                                   16: [-1/4 - 4, 1 + 24/24*self.y_masa_podk, 0]}
            self.vzmet_podk.change_layout(new_layout_vzmet_podk)
        
        def update_dusilka_spodaj_podk(dusilka_spodaj_podk, dt):
            self.y_masa_podk = 1.32 * 0.75 * 0.5 * man.np.sin(self.nihanje_podk.get_value() - 0.13 + 0.05) # ker nekaj zaostaja zaradi animacij
            new_layout_dusilka_spodaj_podk = {1: [1/4 - 4, -2 + 0/2*self.y_masa_podk, 0],
                                             2: [1/4 - 4, -1 + 1/2*self.y_masa_podk, 0],
                                            3: [0 - 4 + 2*self.korekcija_x, -1 + 1/2*self.y_masa_podk, 0],
                                            4: [1/2 - 4 - 2*self.korekcija_x, -1 + 1/2*self.y_masa_podk, 0],
                                            5: [0 - 4 + 2*self.korekcija_x, 0 + 1/2*self.y_masa_podk, 0],
                                            6: [1/2 - 4 - 2*self.korekcija_x, 0 + 1/2*self.y_masa_podk, 0]}
            self.dusilka_spodaj_podk.change_layout(new_layout_dusilka_spodaj_podk)
        
        def update_dusilka_zgoraj_podk(dusilka_zgoraj_podk, dt):
            self.y_masa_podk = 1.32 * 0.75 * 0.5 * man.np.sin(self.nihanje_podk.get_value() - 0.13 + 0.05) # ker nekaj zaostaja zaradi animacij
            new_layout_dusilka_zgoraj_podk = {1: [1/4 - 4, 1 + 3/3*self.y_masa_podk, 0],
                                             2: [1/4 - 4, -1/2 + 2/3*self.y_masa_podk, 0],
                                            3: [0 - 4 + 3*self.korekcija_x, -1/2 + 2/3*self.y_masa_podk, 0],
                                            4: [1/2 - 4 - 3*self.korekcija_x, -1/2 + 2/3*self.y_masa_podk, 0]}
            self.dusilka_zgoraj_podk.change_layout(new_layout_dusilka_zgoraj_podk)
        
        self.masa_resk = man.RoundedRectangle(
            color = man.GRAY,
            fill_color = man.GRAY,
            fill_opacity = 0.5,
            height = 0.5,
            width = 1,
            corner_radius = 0.1,
            ).move_to([0, 1.25, 0])

        self.m_resk = man.MathTex("m").scale(0.5).move_to(self.masa_resk.get_center() + [0.3, -0.1, 0])
        
        self.sila_masa_resk = man.Arrow(
            start = self.masa_resk.get_center(),
            end = self.masa_resk.get_center() + [0, 1 * 0.75 * 0.5 * man.np.sin((6/16) * man.PI), 0],
            color = man.RED,
            max_stroke_width_to_length_ratio = 10.667/man.np.abs(man.np.sin((6/16) * man.PI)),
            max_tip_length_to_length_ratio = 0.533/man.np.abs(man.np.sin((6/16) * man.PI)),
            stroke_width = 5,
            buff = 0,
        )

        self.sila_podlaga_resk = man.Arrow(
            start = self.pod00k.get_center() + [0, 2.5, 0],
            end = self.pod00k.get_center() + [0, 2.5, 0] + [0, 5.10 * 0.75 * 0.5 * man.np.sin((6/16) * man.PI - 1.37), 0],
            color = man.ORANGE,
            max_stroke_width_to_length_ratio = 2.092/man.np.abs(man.np.sin((6/16) * man.PI - 1.37)),
            max_tip_length_to_length_ratio = 0.105/man.np.abs(man.np.sin((6/16) * man.PI - 1.37)),
            stroke_width = 5,
            buff = 0,
        )

        self.r_resk = man.MathTex("r = 1", color = man.BLACK).move_to([0, -3, 0])

        self.vzmet_standard_resk = {1: [-1/4, -2, 0], 2: [-1/4, -17/10, 0],
                                   3: [-1/2 + 2*self.korekcija_x, -8/5, 0], 4: [0 - 2*self.korekcija_x, -7/5, 0],
                                   5: [-1/2 + 2*self.korekcija_x, -6/5, 0], 6: [0 - 2*self.korekcija_x, -1, 0],
                                   7: [-1/2 + 2*self.korekcija_x, -4/5, 0], 8: [0 - 2*self.korekcija_x, -3/5, 0],
                                   9: [-1/2 + 2*self.korekcija_x, -2/5, 0], 10: [0 - 2*self.korekcija_x, -1/5, 0],
                                   11: [-1/2 + 2*self.korekcija_x, 0, 0], 12: [0 - 2*self.korekcija_x, 1/5, 0],
                                   13: [-1/2 + 2*self.korekcija_x, 2/5, 0], 14: [0 - 2*self.korekcija_x, 3/5, 0],
                                   15: [-1/4, 7/10, 0], 16: [-1/4, 1, 0]}

        self.vzmet_resk = man.Graph([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
                                   [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10), (10, 11), (11, 12), (12, 13), (13, 14), (14, 15), (15, 16)],
                                   layout = self.vzmet_standard_resk,
                                   vertex_config = {'radius': 0},
                                   )

        self.dusilka_spodaj_standard_resk = {1: [1/4, -2, 0], 2: [1/4, -1, 0],
                                            3: [0 + 2*self.korekcija_x, -1, 0], 4: [1/2 - 2*self.korekcija_x, -1, 0],
                                            5: [0 + 2*self.korekcija_x, 0, 0], 6: [1/2 - 2*self.korekcija_x, 0, 0]}

        self.dusilka_spodaj_resk = man.Graph([1, 2, 3, 4, 5, 6],
                                            [(1, 2), (2, 3), (2, 4), (3, 5), (4, 6)],
                                            layout = self.dusilka_spodaj_standard_resk,
                                            vertex_config = {'radius': 0},
                                            )

        self.dusilka_zgoraj_standard_resk = {1: [1/4, 1, 0], 2: [1/4, -1/2, 0],
                                            3: [0 + 3*self.korekcija_x, -1/2, 0], 4: [1/2 - 3*self.korekcija_x, -1/2, 0]}

        self.dusilka_zgoraj_resk = man.Graph([1, 2, 3, 4],
                                            [(1, 2), (2, 3), (2, 4)],
                                            layout = self.dusilka_zgoraj_standard_resk,
                                            vertex_config = {'radius': 0},
                                            )
        
        self.nihanje_resk = man.ValueTracker(1.57)
        
        def update_masa_resk(masa_resk, dt):
            self.y_masa_resk = 5 * 0.75 * 0.5 * man.np.sin(self.nihanje_resk.get_value() - 1.57)
            new_pos_masa_resk = [0, 1.25 + self.y_masa_resk, 0]
            self.masa_resk.move_to(new_pos_masa_resk)
        
        def update_m_resk(m_resk, dt):
            self.y_masa_resk = 5 * 0.75 * 0.5 * man.np.sin(self.nihanje_resk.get_value() - 1.57)
            new_pos_m_resk = [0 + 0.3, 1.25 - 0.1 + self.y_masa_resk, 0]
            self.m_resk.move_to(new_pos_m_resk)
        
        def update_sila_masa_resk(sila_masa_resk, dt):
            new_start_sila_masa_resk = self.masa_resk.get_center()
            new_end_sila_masa_resk = self.masa_resk.get_center() + [0, 1 * 0.75 * 0.5 * man.np.sin(self.nihanje_resk.get_value()), 0]
            self.sila_masa_resk.put_start_and_end_on(new_start_sila_masa_resk, new_end_sila_masa_resk)
        
        def update_sila_podlaga_resk(sila_podlaga_resk, dt):
            new_start_sila_podlaga_resk = self.pod00k.get_center() + [0, 2.5, 0]
            new_end_sila_podlaga_resk = self.pod00k.get_center() + [0, 2.5, 0] + [0, 5.10 * 0.75 * 0.5 * man.np.sin(self.nihanje_resk.get_value() - 1.37), 0]
            self.sila_podlaga_resk.put_start_and_end_on(new_start_sila_podlaga_resk, new_end_sila_podlaga_resk)
        
        def update_vzmet_resk(vzmet_resk, dt):
            self.y_masa_resk = 5 * 0.75 * 0.5 * man.np.sin(self.nihanje_resk.get_value() - 1.57 + 0.05) # ker nekaj zaostaja zaradi animacij
            new_layout_vzmet_resk = {1: [-1/4, -2 + 0/24*self.y_masa_resk, 0],
                                    2: [-1/4, -17/10 + 0/24*self.y_masa_resk, 0],
                                   3: [-1/2 + 2*self.korekcija_x, -8/5 + 1/24*self.y_masa_resk, 0],
                                   4: [0 - 2*self.korekcija_x, -7/5 + 3/24*self.y_masa_resk, 0],
                                   5: [-1/2 + 2*self.korekcija_x, -6/5 + 5/24*self.y_masa_resk, 0],
                                   6: [0 - 2*self.korekcija_x, -1 + 7/24*self.y_masa_resk, 0],
                                   7: [-1/2 + 2*self.korekcija_x, -4/5 + 9/24*self.y_masa_resk, 0],
                                   8: [0 - 2*self.korekcija_x, -3/5 + 11/24*self.y_masa_resk, 0],
                                   9: [-1/2 + 2*self.korekcija_x, -2/5 + 13/24*self.y_masa_resk, 0],
                                   10: [0 - 2*self.korekcija_x, -1/5 + 15/24*self.y_masa_resk, 0],
                                   11: [-1/2 + 2*self.korekcija_x, 0 + 17/24*self.y_masa_resk, 0],
                                   12: [0 - 2*self.korekcija_x, 1/5 + 19/24*self.y_masa_resk, 0],
                                   13: [-1/2 + 2*self.korekcija_x, 2/5 + 21/24*self.y_masa_resk, 0],
                                   14: [0 - 2*self.korekcija_x, 3/5 + 23/24*self.y_masa_resk, 0],
                                   15: [-1/4, 7/10 + 24/24*self.y_masa_resk, 0],
                                   16: [-1/4, 1 + 24/24*self.y_masa_resk, 0]}
            self.vzmet_resk.change_layout(new_layout_vzmet_resk)
        
        def update_dusilka_spodaj_resk(dusilka_spodaj_resk, dt):
            self.y_masa_resk = 5 * 0.75 * 0.5 * man.np.sin(self.nihanje_resk.get_value() - 1.57 + 0.05) # ker nekaj zaostaja zaradi animacij
            new_layout_dusilka_spodaj_resk = {1: [1/4, -2 + 0/2*self.y_masa_resk, 0],
                                             2: [1/4, -1 + 1/2*self.y_masa_resk, 0],
                                            3: [0 + 2*self.korekcija_x, -1 + 1/2*self.y_masa_resk, 0],
                                            4: [1/2 - 2*self.korekcija_x, -1 + 1/2*self.y_masa_resk, 0],
                                            5: [0 + 2*self.korekcija_x, 0 + 1/2*self.y_masa_resk, 0],
                                            6: [1/2 - 2*self.korekcija_x, 0 + 1/2*self.y_masa_resk, 0]}
            self.dusilka_spodaj_resk.change_layout(new_layout_dusilka_spodaj_resk)
        
        def update_dusilka_zgoraj_resk(dusilka_zgoraj_resk, dt):
            self.y_masa_resk = 5 * 0.75 * 0.5 * man.np.sin(self.nihanje_resk.get_value() - 1.57 + 0.05) # ker nekaj zaostaja zaradi animacij
            new_layout_dusilka_zgoraj_resk = {1: [1/4, 1 + 3/3*self.y_masa_resk, 0],
                                             2: [1/4, -1/2 + 2/3*self.y_masa_resk, 0],
                                            3: [0 + 3*self.korekcija_x, -1/2 + 2/3*self.y_masa_resk, 0],
                                            4: [1/2 - 3*self.korekcija_x, -1/2 + 2/3*self.y_masa_resk, 0]}
            self.dusilka_zgoraj_resk.change_layout(new_layout_dusilka_zgoraj_resk)
        
        self.masa_nadk = man.RoundedRectangle(
            color = man.GRAY,
            fill_color = man.GRAY,
            fill_opacity = 0.5,
            height = 0.5,
            width = 1,
            corner_radius = 0.1,
            ).move_to([4, 1.25, 0])

        self.m_nadk = man.MathTex("m").scale(0.5).move_to(self.masa_nadk.get_center() + [0.3, -0.1, 0])
        
        self.sila_masa_nadk = man.Arrow(
            start = self.masa_nadk.get_center(),
            end = self.masa_nadk.get_center() + [0, 1 * 0.75 * 0.5 * man.np.sin((6/16) * man.PI), 0],
            color = man.RED,
            max_stroke_width_to_length_ratio = 10.667/man.np.abs(man.np.sin((6/16) * man.PI)),
            max_tip_length_to_length_ratio = 0.533/man.np.abs(man.np.sin((6/16) * man.PI)),
            stroke_width = 5,
            buff = 0,
        )

        self.sila_podlaga_nadk = man.Arrow(
            start = self.pod00k.get_center() + [4, 2.5, 0],
            end = self.pod00k.get_center() + [4, 2.5, 0] + [0, 0.36 * 0.75 * 0.5 * man.np.sin((6/16) * man.PI - 2.63), 0],
            color = man.ORANGE,
            max_stroke_width_to_length_ratio = 29.630/man.np.abs(man.np.sin((6/16) * man.PI - 2.63)),
            max_tip_length_to_length_ratio = 1.481/man.np.abs(man.np.sin((6/16) * man.PI - 2.63)),
            stroke_width = 5,
            buff = 0,
        )

        self.r_nadk = man.MathTex("r = 2", color = man.BLACK).move_to([4, -3, 0])

        self.vzmet_standard_nadk = {1: [-1/4 + 4, -2, 0], 2: [-1/4 + 4, -17/10, 0],
                                   3: [-1/2 + 4 + 2*self.korekcija_x, -8/5, 0], 4: [0 + 4 - 2*self.korekcija_x, -7/5, 0],
                                   5: [-1/2 + 4 + 2*self.korekcija_x, -6/5, 0], 6: [0 + 4 - 2*self.korekcija_x, -1, 0],
                                   7: [-1/2 + 4 + 2*self.korekcija_x, -4/5, 0], 8: [0 + 4 - 2*self.korekcija_x, -3/5, 0],
                                   9: [-1/2 + 4 + 2*self.korekcija_x, -2/5, 0], 10: [0 + 4 - 2*self.korekcija_x, -1/5, 0],
                                   11: [-1/2 + 4 + 2*self.korekcija_x, 0, 0], 12: [0 + 4 - 2*self.korekcija_x, 1/5, 0],
                                   13: [-1/2 + 4 + 2*self.korekcija_x, 2/5, 0], 14: [0 + 4 - 2*self.korekcija_x, 3/5, 0],
                                   15: [-1/4 + 4, 7/10, 0], 16: [-1/4 + 4, 1, 0]}

        self.vzmet_nadk = man.Graph([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
                                   [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10), (10, 11), (11, 12), (12, 13), (13, 14), (14, 15), (15, 16)],
                                   layout = self.vzmet_standard_nadk,
                                   vertex_config = {'radius': 0},
                                   )

        self.dusilka_spodaj_standard_nadk = {1: [1/4 + 4, -2, 0], 2: [1/4 + 4, -1, 0],
                                            3: [0 + 4 + 2*self.korekcija_x, -1, 0], 4: [1/2 + 4 - 2*self.korekcija_x, -1, 0],
                                            5: [0 + 4 + 2*self.korekcija_x, 0, 0], 6: [1/2 + 4 - 2*self.korekcija_x, 0, 0]}

        self.dusilka_spodaj_nadk = man.Graph([1, 2, 3, 4, 5, 6],
                                            [(1, 2), (2, 3), (2, 4), (3, 5), (4, 6)],
                                            layout = self.dusilka_spodaj_standard_nadk,
                                            vertex_config = {'radius': 0},
                                            )

        self.dusilka_zgoraj_standard_nadk = {1: [1/4 + 4, 1, 0], 2: [1/4 + 4, -1/2, 0],
                                            3: [0 + 4 + 3*self.korekcija_x, -1/2, 0], 4: [1/2 + 4 - 3*self.korekcija_x, -1/2, 0]}

        self.dusilka_zgoraj_nadk = man.Graph([1, 2, 3, 4],
                                            [(1, 2), (2, 3), (2, 4)],
                                            layout = self.dusilka_zgoraj_standard_nadk,
                                            vertex_config = {'radius': 0},
                                            )
        
        self.nihanje_nadk = man.ValueTracker(3.01)
        
        def update_masa_nadk(masa_nadk, dt):
            self.y_masa_nadk = 0.33 * 0.75 * 0.5 * man.np.sin(self.nihanje_nadk.get_value() - 3.01)
            new_pos_masa_nadk = [4, 1.25 + self.y_masa_nadk, 0]
            self.masa_nadk.move_to(new_pos_masa_nadk)
        
        def update_m_nadk(m_nadk, dt):
            self.y_masa_nadk = 0.33 * 0.75 * 0.5 * man.np.sin(self.nihanje_nadk.get_value() - 3.01)
            new_pos_m_nadk = [4 + 0.3, 1.25 - 0.1 + self.y_masa_nadk, 0]
            self.m_nadk.move_to(new_pos_m_nadk)
        
        def update_sila_masa_nadk(sila_masa_nadk, dt):
            new_start_sila_masa_nadk = self.masa_nadk.get_center()
            new_end_sila_masa_nadk = self.masa_nadk.get_center() + [0, 1 * 0.75 * 0.5 * man.np.sin(self.nihanje_nadk.get_value()), 0]
            self.sila_masa_nadk.put_start_and_end_on(new_start_sila_masa_nadk, new_end_sila_masa_nadk)
        
        def update_sila_podlaga_nadk(sila_podlaga_nadk, dt):
            new_start_sila_podlaga_nadk = self.pod00k.get_center() + [4, 2.5, 0]
            new_end_sila_podlaga_nadk = self.pod00k.get_center() + [4, 2.5, 0] + [0, 0.36 * 0.75 * 0.5 * man.np.sin(self.nihanje_nadk.get_value() - 2.63), 0]
            self.sila_podlaga_nadk.put_start_and_end_on(new_start_sila_podlaga_nadk, new_end_sila_podlaga_nadk)
        
        def update_vzmet_nadk(vzmet_nadk, dt):
            self.y_masa_nadk = 0.33 * 0.75 * 0.5 * man.np.sin(self.nihanje_nadk.get_value() - 3.01 + 0.05) # ker nekaj zaostaja zaradi animacij
            new_layout_vzmet_nadk = {1: [-1/4 + 4, -2 + 0/24*self.y_masa_nadk, 0],
                                    2: [-1/4 + 4, -17/10 + 0/24*self.y_masa_nadk, 0],
                                   3: [-1/2 + 4 + 2*self.korekcija_x, -8/5 + 1/24*self.y_masa_nadk, 0],
                                   4: [0 + 4 - 2*self.korekcija_x, -7/5 + 3/24*self.y_masa_nadk, 0],
                                   5: [-1/2 + 4 + 2*self.korekcija_x, -6/5 + 5/24*self.y_masa_nadk, 0],
                                   6: [0 + 4 - 2*self.korekcija_x, -1 + 7/24*self.y_masa_nadk, 0],
                                   7: [-1/2 + 4 + 2*self.korekcija_x, -4/5 + 9/24*self.y_masa_nadk, 0],
                                   8: [0 + 4 - 2*self.korekcija_x, -3/5 + 11/24*self.y_masa_nadk, 0],
                                   9: [-1/2 + 4 + 2*self.korekcija_x, -2/5 + 13/24*self.y_masa_nadk, 0],
                                   10: [0 + 4 - 2*self.korekcija_x, -1/5 + 15/24*self.y_masa_nadk, 0],
                                   11: [-1/2 + 4 + 2*self.korekcija_x, 0 + 17/24*self.y_masa_nadk, 0],
                                   12: [0 + 4 - 2*self.korekcija_x, 1/5 + 19/24*self.y_masa_nadk, 0],
                                   13: [-1/2 + 4 + 2*self.korekcija_x, 2/5 + 21/24*self.y_masa_nadk, 0],
                                   14: [0 + 4 - 2*self.korekcija_x, 3/5 + 23/24*self.y_masa_nadk, 0],
                                   15: [-1/4 + 4, 7/10 + 24/24*self.y_masa_nadk, 0],
                                   16: [-1/4 + 4, 1 + 24/24*self.y_masa_nadk, 0]}
            self.vzmet_nadk.change_layout(new_layout_vzmet_nadk)
        
        def update_dusilka_spodaj_nadk(dusilka_spodaj_nadk, dt):
            self.y_masa_nadk = 0.33 * 0.75 * 0.5 * man.np.sin(self.nihanje_nadk.get_value() - 3.01 + 0.05) # ker nekaj zaostaja zaradi animacij
            new_layout_dusilka_spodaj_nadk = {1: [1/4 + 4, -2 + 0/2*self.y_masa_nadk, 0],
                                             2: [1/4 + 4, -1 + 1/2*self.y_masa_nadk, 0],
                                            3: [0 + 4 + 2*self.korekcija_x, -1 + 1/2*self.y_masa_nadk, 0],
                                            4: [1/2 + 4 - 2*self.korekcija_x, -1 + 1/2*self.y_masa_nadk, 0],
                                            5: [0 + 4 + 2*self.korekcija_x, 0 + 1/2*self.y_masa_nadk, 0],
                                            6: [1/2 + 4 - 2*self.korekcija_x, 0 + 1/2*self.y_masa_nadk, 0]}
            self.dusilka_spodaj_nadk.change_layout(new_layout_dusilka_spodaj_nadk)
        
        def update_dusilka_zgoraj_nadk(dusilka_zgoraj_nadk, dt):
            self.y_masa_nadk = 0.33 * 0.75 * 0.5 * man.np.sin(self.nihanje_nadk.get_value() - 3.01 + 0.05) # ker nekaj zaostaja zaradi animacij
            new_layout_dusilka_zgoraj_nadk = {1: [1/4 + 4, 1 + 3/3*self.y_masa_nadk, 0],
                                             2: [1/4 + 4, -1/2 + 2/3*self.y_masa_nadk, 0],
                                            3: [0 + 4 + 3*self.korekcija_x, -1/2 + 2/3*self.y_masa_nadk, 0],
                                            4: [1/2 + 4 - 3*self.korekcija_x, -1/2 + 2/3*self.y_masa_nadk, 0]}
            self.dusilka_zgoraj_nadk.change_layout(new_layout_dusilka_zgoraj_nadk)
# ---------------------------------------------------------------------------------------------------------------------------------

        self.play(man.FadeIn(self.podlagak,
                             self.masa_podk, self.m_podk, self.sila_masa_podk, self.sila_podlaga_podk,
                             self.vzmet_podk, self.dusilka_spodaj_podk, self.dusilka_zgoraj_podk,
                             self.masa_resk, self.m_resk, self.sila_masa_resk, self.sila_podlaga_resk,
                             self.vzmet_resk, self.dusilka_spodaj_resk, self.dusilka_zgoraj_resk,
                             self.masa_nadk, self.m_nadk, self.sila_masa_nadk, self.sila_podlaga_nadk,
                             self.vzmet_nadk, self.dusilka_spodaj_nadk, self.dusilka_zgoraj_nadk))
        self.play(man.Write(self.r_podk))
        self.play(man.Write(self.r_resk))
        self.play(man.Write(self.r_nadk))

# definiram tukaj elemente, ker so premaknjeni glede na njihovo originalno pozicijo -----------------------------------------------
        self.masa_podk.add_updater(update_masa_podk)
        self.m_podk.add_updater(update_m_podk)
        self.sila_masa_podk.add_updater(update_sila_masa_podk)
        self.sila_podlaga_podk.add_updater(update_sila_podlaga_podk)
        self.vzmet_podk.add_updater(update_vzmet_podk)
        self.dusilka_spodaj_podk.add_updater(update_dusilka_spodaj_podk)
        self.dusilka_zgoraj_podk.add_updater(update_dusilka_zgoraj_podk)
        
        self.masa_resk.add_updater(update_masa_resk)
        self.m_resk.add_updater(update_m_resk)
        self.sila_masa_resk.add_updater(update_sila_masa_resk)
        self.sila_podlaga_resk.add_updater(update_sila_podlaga_resk)
        self.vzmet_resk.add_updater(update_vzmet_resk)
        self.dusilka_spodaj_resk.add_updater(update_dusilka_spodaj_resk)
        self.dusilka_zgoraj_resk.add_updater(update_dusilka_zgoraj_resk)

        self.masa_nadk.add_updater(update_masa_nadk)
        self.m_nadk.add_updater(update_m_nadk)
        self.sila_masa_nadk.add_updater(update_sila_masa_nadk)
        self.sila_podlaga_nadk.add_updater(update_sila_podlaga_nadk)
        self.vzmet_nadk.add_updater(update_vzmet_nadk)
        self.dusilka_spodaj_nadk.add_updater(update_dusilka_spodaj_nadk)
        self.dusilka_zgoraj_nadk.add_updater(update_dusilka_zgoraj_nadk)
# ---------------------------------------------------------------------------------------------------------------------------------

        self.play(self.nihanje_podk.animate.set_value(0.13 + 8 * man.PI),
                  self.nihanje_resk.animate.set_value(1.57 + 16 * man.PI),
                  self.nihanje_nadk.animate.set_value(3.01 + 32 * man.PI),
                  rate_func = man.linear, run_time = 16)
        
# definiram tukaj elemente, ker so premaknjeni glede na njihovo originalno pozicijo -----------------------------------------------
        self.masa_podk.clear_updaters()
        self.m_podk.clear_updaters()
        self.sila_masa_podk.clear_updaters()
        self.sila_podlaga_podk.clear_updaters()
        self.vzmet_podk.clear_updaters()
        self.dusilka_spodaj_podk.clear_updaters()
        self.dusilka_zgoraj_podk.clear_updaters()
        
        self.masa_resk.clear_updaters()
        self.m_resk.clear_updaters()
        self.sila_masa_resk.clear_updaters()
        self.sila_podlaga_resk.clear_updaters()
        self.vzmet_resk.clear_updaters()
        self.dusilka_spodaj_resk.clear_updaters()
        self.dusilka_zgoraj_resk.clear_updaters()

        self.masa_nadk.clear_updaters()
        self.m_nadk.clear_updaters()
        self.sila_masa_nadk.clear_updaters()
        self.sila_podlaga_nadk.clear_updaters()
        self.vzmet_nadk.clear_updaters()
        self.dusilka_spodaj_nadk.clear_updaters()
        self.dusilka_zgoraj_nadk.clear_updaters()
# ---------------------------------------------------------------------------------------------------------------------------------
        
        self.play(man.FadeOut(self.podlagak,
                              self.masa_podk, self.m_podk, self.sila_masa_podk, self.sila_podlaga_podk,
                              self.vzmet_podk, self.dusilka_spodaj_podk, self.dusilka_zgoraj_podk, self.r_podk,
                              self.masa_resk, self.m_resk, self.sila_masa_resk, self.sila_podlaga_resk,
                              self.vzmet_resk, self.dusilka_spodaj_resk, self.dusilka_zgoraj_resk, self.r_resk,
                              self.masa_nadk, self.m_nadk, self.sila_masa_nadk, self.sila_podlaga_nadk,
                              self.vzmet_nadk, self.dusilka_spodaj_nadk, self.dusilka_zgoraj_nadk, self.r_nadk))
        self.wait()

# ---------------------------------------------------------------------------------------------- klic

if __name__ == "__main__":
    scena = PasivnaVibroizolacija()
    scena

# cd Desktop\PREDMETI\3._letnik\2._semester\IDPR\LADISK\projekt
# manim -pql pv.py PasivnaVibroizolacija