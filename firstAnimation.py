from manim import *

class SquareToCircle(Scene):
    def construct(self):
        # Set Solarized Light background
        self.camera.background_color = "#fdf6e3"

        circle = Circle().set_color(BLACK)
        circle.set_fill(BLUE, opacity=0.5)
        circle.set_stroke(BLUE_E, width=4)

        square = Square().set_color(PURPLE)

        self.play(Create(square))
        self.wait()
        self.play(ReplacementTransform(square, circle))
        self.play(Wait(5))
        self.play(FadeOut(circle))