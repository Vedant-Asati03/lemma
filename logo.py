from manim import *


class MyScene(Scene):
    def construct(self):
        plane = NumberPlane(
            background_line_style={
                "stroke_color": BLUE_A,
                "stroke_opacity": 0.22,
                "stroke_width": 1,
            },
            axis_config={
                "stroke_color": DARK_BLUE,
                "stroke_opacity": 0.5,
                "stroke_width": 1.5,
                "include_numbers": False,
                "tick_size": 0,
            },
            faded_line_ratio=3,
        )

        c = GREEN_A
        sw = 3.5
        sy = -0.5  # baseline y; letters span [sy, sy+1.0], 'l' up to sy+1.5

        # ── l ──────────────────────────────────────────────────────────────
        # gentle S-curve vertical stroke (ascender)
        lx = -3.20
        letter_l = ParametricFunction(
            lambda t: np.array([lx + 0.07 * np.sin(PI * t), sy + 1.5 * t, 0]),
            t_range=[0, 1],
            color=c,
            stroke_width=sw,
        )

        # ── e ──────────────────────────────────────────────────────────────
        # almost-full circle (gap on the right) + horizontal midline bar
        ex = -2.23
        letter_e = VGroup(
            Arc(
                radius=0.5,
                start_angle=PI / 8,
                angle=2 * PI - PI / 4,
                arc_center=[ex, sy + 0.5, 0],
                color=c,
                stroke_width=sw,
            ),
            Line(
                [ex - 0.5, sy + 0.5, 0],
                [ex + 0.5, sy + 0.5, 0],
                color=c,
                stroke_width=sw,
            ),
        )

        # ── m × 2 ──────────────────────────────────────────────────────────
        # two consecutive positive sine arches — literally y = sin(πt), t∈[0,1]
        def make_m(left_x):
            hw = 0.7  # width of each arch
            return VGroup(
                ParametricFunction(
                    lambda t: np.array([left_x + hw * t, sy + np.sin(PI * t), 0]),
                    t_range=[0, 1],
                    color=c,
                    stroke_width=sw,
                ),
                ParametricFunction(
                    lambda t: np.array([left_x + hw + hw * t, sy + np.sin(PI * t), 0]),
                    t_range=[0, 1],
                    color=c,
                    stroke_width=sw,
                ),
            )

        letter_m1 = make_m(-1.33)
        letter_m2 = make_m(0.47)

        # ── a ──────────────────────────────────────────────────────────────
        # full circle + right vertical stem
        ax = 2.27
        letter_a = VGroup(
            Circle(radius=0.5, color=c, stroke_width=sw).move_to(
                [ax + 0.5, sy + 0.5, 0]
            ),
            Line([ax + 1.0, sy, 0], [ax + 1.0, sy + 1.0, 0], color=c, stroke_width=sw),
        )

        self.add(plane, letter_l, letter_e, letter_m1, letter_m2, letter_a)
