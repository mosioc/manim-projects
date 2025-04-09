from manim import *

class TestThree(Scene): # extend Scene
    def construct(self):
        text = Tex(r"$E=mc^2$")
        self.play(Wait(10))
        self.play(Write(text))
        self.play(Wait(10))
