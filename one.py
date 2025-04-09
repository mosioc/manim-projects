from manim import *

class One(Scene):
    def construct(self):
        self.camera.background_color = "#fdf6e3"  # Solarized Light background
        
        title = Text("Manim", font_size=102,  color="#073642")  # Darker Solarized base02
        subtitle = Text("Mehdi Maleki", font_size=48, color="#2aa198")  # Solarized Cyan for text
        year = Text("2025", font_size=36, color="#859900")  # Solarized Green for text
        
        title.move_to(ORIGIN, DOWN * 0.1)
        subtitle.next_to(title, DOWN * 0.8)
        year.next_to(subtitle, DOWN)
        
        self.play(Write(title), Write(subtitle), Write(year))
        self.wait(1)

class OneOne(Scene):
    def construct(self):
        # 1. Display the initial text
        self.camera.background_color = "#fdf6e3"  # Solarized Light background
        
        title = Text("Manim", font_size=102,  color="#073642")  # Darker Solarized base02
        subtitle = Text("Mehdi Maleki", font_size=48, color="#2aa198")  # Solarized Cyan for text
        year = Text("2025", font_size=36, color="#859900")  # Solarized Green for text
        
        # Positioning the text
        title.move_to(ORIGIN, DOWN * 0.1)
        subtitle.next_to(title, DOWN * 0.8)
        year.next_to(subtitle, DOWN)
        
        self.add(title, subtitle, year)

        # Fade out the year 2025
        self.play(FadeOut(year))

        # 1.1. Create the new title text with stronger color
        new_title = Text("M + Anim:", font_size=72, color="#073642")  # Darker Solarized base02
        
        # For accurate character highlighting, explicitly find the substrings
        math_text = "Mathematical Animation"
        math_animation = Text(math_text, font_size=48, color="#073642")  # Darker base color
        
        # Identify character indices of 'M' and 'Anim' in "Mathematical Animation"
        m_index = 0  # First character 'M'
        anim_start = math_text.find("Anim")  # Find where "Anim" starts
        
        # Highlight 'M' in "Mathematical"
        math_animation[m_index].set_color("#d3003f").set_weight(BOLD)
        
        # Highlight 'Anim' in "Animation" - using string search to ensure accuracy
        if anim_start != -1:
            for i in range(anim_start, anim_start + 4):  # "Anim" is 4 characters
                math_animation[i].set_color("#d3003f").set_weight(BOLD)
        
        # Position the new text
        new_text = VGroup(new_title, math_animation)
        new_text.arrange(DOWN, aligned_edge=LEFT)
        new_text.move_to(ORIGIN)
        
        # Transform the old text to the new text
        self.play(
            Transform(title, new_title),
            Transform(subtitle, math_animation)
        )
        
        # Add extra emphasis to the highlighted parts
        emphasis_animations = [math_animation[m_index].animate.scale(1.2)]
        if anim_start != -1:
            for i in range(anim_start, anim_start + 4):
                emphasis_animations.append(math_animation[i].animate.scale(1.2))
        
        self.play(*emphasis_animations)

        self.play(FadeOut(math_animation))
        self.wait(5)

        self.play(FadeOut(new_title))
        self.play(FadeOut(new_text))

class EngineSimulation(Scene):
    def construct(self):
        # Set the background color to Solarized Light
        self.camera.background_color = "#fdf6e3"
        
        # Define colors based on Solarized palette
        base_color = "#073642"  # Dark blue
        highlight_color = "#d3003f"  # Red for emphasis
        cyan_color = "#2aa198"  # Accent cyan
        
        # Create the flywheel (main rotating part)
        flywheel = Circle(radius=1.5, color=base_color, stroke_width=6)
        axle = Dot(radius=0.1, color=highlight_color)
        
        # Create the piston and connecting rod
        piston = Square(side_length=0.6, color=cyan_color, fill_opacity=1).move_to(UP * 2)
        rod = Line(piston.get_bottom(), axle.get_center(), color=highlight_color, stroke_width=4)
        
        # Group components together
        engine_parts = VGroup(flywheel, axle, piston, rod)
        self.add(engine_parts)
        
        # Define animations
        rotations = Rotate(flywheel, angle=TAU, about_point=flywheel.get_center(), run_time=2, rate_func=linear)
        
        def update_piston(mob, dt):
            time = self.time * 2 * PI  # Normalize time
            y_offset = np.sin(time) * 1.2  # Simulate up and down motion
            piston.move_to(UP * 2 + DOWN * y_offset)
            rod.put_start_and_end_on(piston.get_bottom(), axle.get_center())
        
        piston.add_updater(update_piston)
        
        # Play animations
        self.play(rotations, run_time=6)
        self.wait(2)   

class OneThree(Scene):
    def construct(self):
        self.camera.background_color = "#fdf6e3"  # Solarized Light background
        
        # Create an abstract engine shape using geometric shapes
        base_circle = Circle(radius=1.5, color="#268bd2")  # Solarized Blue
        inner_circle = Circle(radius=0.5, color="#2aa198")  # Solarized Cyan
        rods = VGroup(
            Line(ORIGIN, 1.5 * RIGHT, color="#b58900"),  # Solarized Yellow
            Line(ORIGIN, 1.5 * UP, color="#b58900"),
            Line(ORIGIN, 1.5 * LEFT, color="#b58900"),
            Line(ORIGIN, 1.5 * DOWN, color="#b58900")
        )
        
        engine_shape = VGroup(base_circle, inner_circle, rods)
        self.play(FadeIn(engine_shape))
        
        # Rotate the engine
        self.play(Rotate(engine_shape, angle=2*PI, run_time=3))
        self.wait(1)

class OneFive(Scene):
    def construct(self):
        self.camera.background_color = "#fdf6e3"  # Solarized Light background
        
        # Recreate the engine shape to match its last state
        base_circle = Circle(radius=1.5, color="#268bd2")
        inner_circle = Circle(radius=0.5, color="#2aa198")
        rods = VGroup(
            Line(ORIGIN, 1.5 * RIGHT, color="#b58900"),
            Line(ORIGIN, 1.5 * UP, color="#b58900"),
            Line(ORIGIN, 1.5 * LEFT, color="#b58900"),
            Line(ORIGIN, 1.5 * DOWN, color="#b58900")
        )
        
        engine_shape = VGroup(base_circle, inner_circle, rods)
        self.add(engine_shape)  # Present last state from previous scene
        self.wait(1)
        
        # Create the text
        text = VGroup(
            Text("Animation Engine:", font_size=48, color="#073642"),
            Text("An engine for precise programmatic animations.", font_size=36, color="#2aa198")
        ).arrange(DOWN)
        
        # Transform engine to text
        self.play(Transform(engine_shape, text))
        self.wait(2)

class Two(Scene):
    def construct(self):
        self.camera.background_color = "#fdf6e3"  # Solarized Light background
        
        # Create the initial text
        initial_text = VGroup(
            Text("Animation Engine:", font_size=48, color="#073642"),
            Text("An engine for precise programmatic animations.", font_size=36, color="#2aa198")
        ).arrange(DOWN)
        
        self.add(initial_text)
        self.wait(1)
        
        # Create the new text
        new_text = VGroup(
            Text("The ability to implement complicated and mathematically", font_size=32, color="#073642"),
            Text("intensive animations with just a few lines of code.", font_size=32, color="#073642")
        ).arrange(DOWN, aligned_edge=LEFT).move_to(ORIGIN)
        
        # Transform the previous text to the new text
        self.play(Transform(initial_text, new_text))
        self.wait(2)
