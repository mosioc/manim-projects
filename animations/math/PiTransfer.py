from manim import *
import math 

class AnimatingMethods(Scene):
    def construct(self):
        # Set Solarized Light background
        self.camera.background_color = "#fdf6e3"
        
        # Create a grid of pi symbols
        grid = VGroup(*[
            Tex(r"$\pi$") for _ in range(100)
        ]).arrange_in_grid(rows=10, cols=10, buff=0.2)
        grid.set_height(4)
        grid.set_color(BLACK)
        self.play(FadeIn(grid))

        # First shift animation
        self.play(grid.animate.shift(LEFT))
        
        # Second shift animation (corrected syntax)
        self.play(grid.animate.shift(LEFT))

        self.play(grid.animate.set_color(BLACK))
        self.wait()
        self.play(grid.animate.set_submobject_colors_by_gradient(BLUE, GREEN))
        self.wait()
        self.play(grid.animate.set_height(TAU - MED_SMALL_BUFF))
        self.wait()

        self.play(grid.animate.apply_complex_function(np.exp), run_time=5)
        self.wait()

        self.play(
            grid.animate.apply_function(
                lambda p: [
                    p[0] + 0.5 * math.sin(p[1]),
                    p[1] + 0.5 * math.sin(p[0]),
                    p[2]
                ]
            ),
            run_time=5,
        )
        self.wait()
        self.play(Wait(6))
        self.play(FadeOut(grid))