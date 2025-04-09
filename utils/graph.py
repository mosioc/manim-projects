from manim import *
import math

class GraphExample(Scene):
    def construct(self):
        # Set Solarized Light background
        self.camera.background_color = "#fdf6e3"
        # Create axes with labels
        axes = Axes(
            x_range=(-3, 10),
            y_range=(-1, 8),
            axis_config={"include_numbers": True}  # This adds the coordinate labels
        ).set_color(BLACK)

        self.play(Write(axes, lag_ratio=0.01, run_time=1))

        # Axes.get_graph will return the graph of a function
        sin_graph = axes.plot(
            lambda x: 2 * math.sin(x),
            x_range=[-3, 10],
            color=BLUE
        )
        
        relu_graph = axes.plot(
            lambda x: max(x, 0),
            x_range=[-3, 10],
            color=YELLOW
        )
        
        step_graph = axes.plot(
            lambda x: 2.0 if x > 3 else 1.0,
            x_range=[-3, 10],
            discontinuities=[3],
            color=GREEN
        )

        # By default, it draws it so as to somewhat smoothly interpolate
        # between sampled points (x, f(x)).  If the graph is meant to have
        # a corner, though, you can set use_smoothing to False

        # For discontinuous functions, you can specify the point of
        # discontinuity so that it does not try to draw over the gap.

        # Axes.get_graph_label takes in either a string or a mobject.
        # If it's a string, it treats it as a LaTeX expression.  By default
        # it places the label next to the graph near the right side, and
        # has it match the color of the graph
        # Create and animate labels
        sin_label = axes.get_graph_label(sin_graph, "\\sin(x)")
        relu_label = axes.get_graph_label(relu_graph, Text("ReLU"))
        step_label = axes.get_graph_label(
            step_graph, 
            Text("Step")
        ).next_to(step_graph.point_from_proportion(0.7), UP)

        # Fixed animation sequences
        self.play(
            Create(sin_graph),
            FadeIn(sin_label)  # Removed RIGHT parameter
        )
        self.wait(2)
        self.play(
            ReplacementTransform(sin_graph, relu_graph),
            FadeTransform(sin_label, relu_label)
        )
        self.wait()
        self.play(
            ReplacementTransform(relu_graph, step_graph),
            FadeTransform(relu_label, step_label)
        )
        self.wait()

        # Create parabola using plot() instead of get_graph()
        parabola = axes.plot(
            lambda x: 0.25 * x**2,
            x_range=[-3, 10],
            color=BLUE
        )
        self.play(
            FadeOut(step_graph),
            FadeOut(step_label),
            Create(parabola)
        )
        self.wait()

        # You can use axes.input_to_graph_point, abbreviated
        # to axes.i2gp, to find a particular point on a graph
        dot = Dot(color=RED)
        dot.move_to(axes.i2gp(2, parabola))
        self.play(FadeIn(dot, scale=0.5))

        # A value tracker lets us animate a parameter, usually
        # with the intent of having other mobjects update based
        # on the parameter
        x_tracker = ValueTracker(2)
        f_always(
            dot.move_to,
            lambda: axes.i2gp(x_tracker.get_value(), parabola)
        )

        self.play(x_tracker.animate.set_value(4), run_time=3)
        self.play(x_tracker.animate.set_value(-2), run_time=3)
        self.wait()