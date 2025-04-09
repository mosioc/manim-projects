from manim import *

class EyeStructure3D(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)

        # Cornea (Transparent Outer Layer)
        cornea = Sphere(radius=1.1, color=BLUE_E, fill_opacity=0.2).shift(OUT * 0.2)

        # Iris (Colored Part)
        iris = Annulus(inner_radius=0.3, outer_radius=0.6, color=GREEN_E, fill_opacity=1).shift(OUT * 0.1)

        # Lens (Convex Shape)
        lens = Sphere(radius=0.4, color=WHITE, fill_opacity=0.8).scale([1, 0.5, 1]).shift(IN * 0.2)

        # Retina (Back Inner Layer)
        retina = Surface(
            lambda u, v: np.array([
                np.cos(u) * np.sin(v),
                np.sin(u) * np.sin(v),
                np.cos(v) - 0.8
            ]),
            u_range=[0, TAU],
            v_range=[PI / 2, PI],
            resolution=(30, 30),
            color=RED_E,
            fill_opacity=0.6
        )

        # Optic Nerve (Cylinder Extending from the Back)
        optic_nerve = Cylinder(radius=0.15, height=1.2, color=YELLOW, fill_opacity=1).rotate(PI / 2, axis=RIGHT).shift(IN * 1.4)

        # Light Path Simulation (Rays entering the eye)
        rays = VGroup(*[
            DashedLine(start=3 * LEFT + 1.5 * UP, end=lens.get_center(), color=WHITE),
            DashedLine(start=3 * LEFT + 0.5 * UP, end=lens.get_center(), color=WHITE),
            DashedLine(start=3 * LEFT + 0.5 * DOWN, end=lens.get_center(), color=WHITE),
            DashedLine(start=3 * LEFT + 1.5 * DOWN, end=lens.get_center(), color=WHITE)
        ])
        
        # Labels with Arrows
        def create_label(text, obj, direction):
            arrow = Arrow(start=obj.get_center() + direction * 0.7, end=obj.get_center(), color=WHITE)
            label = Text(text, color=WHITE).scale(0.5).next_to(arrow, direction)
            return VGroup(arrow, label)

        labels = VGroup(
            create_label("Cornea", cornea, UP),
            create_label("Iris", iris, LEFT),
            create_label("Lens", lens, RIGHT),
            create_label("Retina", retina, LEFT),
            create_label("Optic Nerve", optic_nerve, DOWN)
        )

        # Animation sequence
        self.add(cornea, iris, lens, retina, optic_nerve)
        self.play(Create(labels), run_time=2)
        self.play(Create(rays), run_time=1)
        self.begin_ambient_camera_rotation(rate=0.3)
        self.wait(5)
