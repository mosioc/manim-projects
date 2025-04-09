from manim import *

class AnimatedManimCELogoSolarizedDark(Scene):
    def construct(self):
        # Set Solarized dark background color
        self.camera.background_color = "#002b36"  # Solarized dark background

        # Define Solarized colors for the logo
        logo_green = "#859900"  # Solarized green
        logo_blue = "#268bd2"   # Solarized blue
        logo_red = "#dc322f"    # Solarized red
        logo_black = "#eee8d5"  # Solarized base2 (light)

        # Create the MathTex object (M)
        ds_m = MathTex(r"\mathbb{M}", fill_color=logo_black).scale(7)
        ds_m.shift(2.25 * LEFT + 1.5 * UP)

        # Create the shapes
        circle = Circle(color=logo_green, fill_opacity=1).shift(LEFT)
        square = Square(color=logo_blue, fill_opacity=1).shift(UP)
        triangle = Triangle(color=logo_red, fill_opacity=1).shift(RIGHT)

        # Group the shapes and text
        logo = VGroup(triangle, square, circle, ds_m)
        logo.move_to(ORIGIN)

        # Animate each component sequentially
        self.play(FadeIn(triangle, shift=DOWN))  # Triangle fades in from the bottom
        self.play(FadeIn(square, shift=LEFT))   # Square fades in from the left
        self.play(FadeIn(circle, shift=RIGHT))  # Circle fades in from the right
        self.play(Write(ds_m))                  # MathTex (M) is written
        self.wait(1)

        # Add a rotation effect to the entire logo
        self.play(Rotate(logo, angle=2 * PI, about_point=ORIGIN, run_time=3))
        self.wait(1)

        # Scale up the logo and fade out
        self.play(logo.animate.scale(1.5))
        self.play(FadeOut(logo))
        self.wait(1)