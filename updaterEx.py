import math
from manim import *

class UpdatersExample(Scene):
    def construct(self):

        # Set Solarized Light background
        self.camera.background_color = "#fdf6e3"

        square = Square()
        square.set_fill(BLUE_E, 1)

        # Fix the always_redraw usage by using a lambda function
        brace = always_redraw(lambda: Brace(square, UP)).set_color(BLACK)

        text, number = label = VGroup(
            Text("Width = "),
            DecimalNumber(
                0,
                show_ellipsis=True,
                num_decimal_places=2,
                include_sign=True,
            )
        )
        label.arrange(RIGHT)

        # This ensures that the method deicmal.next_to(square)
        # is called on every frame
        always(label.next_to, brace, UP)
        # You could also write the following equivalent line
        # label.add_updater(lambda m: m.next_to(brace, UP))

        # If the argument itself might change, you can use f_always,
        # for which the arguments following the initial Mobject method
        # should be functions returning arguments to that method.
        # The following line ensures that decimal.set_value(square.get_y())
        # is called every frame
        f_always(number.set_value, square.get_width)
        # You could also write the following equivalent line
        # number.add_updater(lambda m: m.set_value(square.get_width()))

        label.set_color(BLACK)
        brace.set_color(BLACK)

        self.play(FadeIn(square), FadeIn(brace), FadeIn(label))


        # Notice that the brace and label track with the square
        self.play(
            square.animate.scale(2),
            rate_func=there_and_back,
            run_time=2,
        )
        self.wait()
        
        # Fixed: Use stretch instead of set_width with stretch parameter
        self.play(
            square.animate.stretch(2.5, 0),  # stretch horizontally by factor of 2.5
            run_time=3,
        )
        self.wait()
        
        self.play(
            square.animate.set_width(2),
            run_time=3
        )
        self.wait()

        # In general, you can alway call Mobject.add_updater, and pass in
        # a function that you want to be called on every frame.  The function
        # should take in either one argument, the mobject, or two arguments,
        # the mobject and the amount of time since the last frame.
        now = self.time
        w0 = square.get_width()
        square.add_updater(
            lambda m: m.set_width(w0 * math.cos(self.time - now))
        )
        self.wait(6)
        self.play(FadeOut(square), FadeOut(brace), FadeOut(label))