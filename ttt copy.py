from manim import *

class OpeningScene(Scene):
    def construct(self):
        # Set Solarized Light background
        self.camera.background_color = "#fdf6e3"
        
        # Create text objects with Solarized colors
        title = Text("Manim", font_size=102, color="#073642")
        subtitle = Text("Mehdi Maleki", font_size=48, color="#2aa198")
        year = Text("2025", font_size=36, color="#859900")
        
        initial_group = VGroup(title, subtitle, year)
        # Position the text
        initial_group.arrange(DOWN)

        # Animate the text appearance
        self.play(Write(title))
        self.play(Write(subtitle))
        self.play(Write(year))
        self.wait(2)

class TransitionScene(Scene):
    def construct(self):
        self.camera.background_color = "#fdf6e3"
        
        # Initial text
        initial_title = Text("Manim", font_size=102, color="#073642")
        initial_subtitle = Text("Mehdi Maleki", font_size=48, color="#2aa198")
        initial_year = Text("2025", font_size=36, color="#859900")
        
        initial_group = VGroup(initial_title, initial_subtitle, initial_year)
        initial_group.arrange(DOWN)
        
        # New text
        new_title = Text("M + Anim:", font_size=72, color="#073642")
        math_text = Text("Mathematical Animation", font_size=48, color="#073642")
        
        # Highlight specific parts - only 'M' and 'Anim'
        math_text[0].set_color("#d3003f").set_weight(BOLD)  # Only 'M'
        math_text[12:16].set_color("#d3003f").set_weight(BOLD)  # 'Anim'
        
        new_group = VGroup(new_title, math_text)
        new_group.arrange(DOWN, aligned_edge=LEFT)
        
        # Animations
        self.add(initial_group)
        self.play(FadeOut(initial_year))
        self.play(
            Transform(initial_title, new_title),
            Transform(initial_subtitle, math_text)
        )
        self.wait(5)
        

        
class EngineShape(Scene):
            def construct(self):
                self.camera.background_color = "#fdf6e3"
                
                # Create abstract engine shape
                base_circle = Circle(radius=1.5, color="#268bd2")
                inner_circle = Circle(radius=0.5, color="#2aa198")
                rods = VGroup(
                    Line(ORIGIN, 1.5 * RIGHT, color="#b58900"),
                    Line(ORIGIN, 1.5 * UP, color="#b58900"),
                    Line(ORIGIN, 1.5 * LEFT, color="#b58900"),
                    Line(ORIGIN, 1.5 * DOWN, color="#b58900")
                )
                
                engine_shape = VGroup(base_circle, inner_circle, rods)
                
                # Animation
                self.play(Create(engine_shape))
                self.play(Rotate(engine_shape, angle=TAU, run_time=3))
                self.wait(1)


class EngineFadeOut(Scene):
    def construct(self):
        self.camera.background_color = "#fdf6e3"
        
        # Create the engine shape
        base_circle = Circle(radius=1.5, color="#268bd2")
        inner_circle = Circle(radius=0.5, color="#2aa198")
        rods = VGroup(
            Line(ORIGIN, 1.5 * RIGHT, color="#b58900"),
            Line(ORIGIN, 1.5 * UP, color="#b58900"),
            Line(ORIGIN, 1.5 * LEFT, color="#b58900"),
            Line(ORIGIN, 1.5 * DOWN, color="#b58900")
        )
        
        engine_shape = VGroup(base_circle, inner_circle, rods)
        self.add(engine_shape)
        
        # Fade out animation
        self.play(FadeOut(engine_shape))
        self.wait(1)


class AnimationEngineText(Scene):
    def construct(self):
        self.camera.background_color = "#fdf6e3"
        
        # Create text with Solarized colors
        title = Text("Animation Engine:", font_size=48, color="#073642")
        subtitle = Text("An engine for precise programmatic animations.", 
                       font_size=36, color="#2aa198")
        
        # Arrange text
        text_group = VGroup(title, subtitle).arrange(DOWN)
        
        # Animate text appearance
        self.play(Write(title))
        self.play(Write(subtitle))
        self.wait(2)

class FadeOutText(Scene):
    def construct(self):
        self.camera.background_color = "#fdf6e3"
        
        # Create the text to fade out
        title = Text("Animation Engine:", font_size=48, color="#073642")
        subtitle = Text("An engine for precise programmatic animations.", 
                       font_size=36, color="#2aa198")
        
        text_group = VGroup(title, subtitle).arrange(DOWN)
        self.add(text_group)
        
        # Fade out animation
        self.play(FadeOut(text_group))
        self.wait(1)


class HeterochromiaText(Scene):
    def construct(self):
        self.camera.background_color = "#fdf6e3"
        
        # Create text with Solarized colors
        title = Text("Heterochromia Iridum", font_size=48, color="#073642")
        subtitle = Text("3Blue 1Brown", font_size=42, color="#268bd2")
        
        # Arrange text
        text_group = VGroup(title, subtitle).arrange(DOWN, buff=0.5)
        
        # Animate text appearance
        self.play(Write(title))
        self.play(Write(subtitle))
        self.wait(2)

class FadeAllTexts(Scene):
    def construct(self):
        self.camera.background_color = "#fdf6e3"
        
        # Create texts with Solarized colors
        title = Text("Heterochromia Iridum", font_size=48, color="#073642")
        subtitle = Text("3Blue 1Brown", font_size=42, color="#268bd2")
        author = Text("- by Grant Sanderson", font_size=36, color="#2aa198")
        
        text_group = VGroup(title, subtitle, author).arrange(DOWN, buff=0.5)
        self.add(text_group)
        
        # Fade out all texts
        self.play(FadeOut(text_group))
        self.wait(1)

class ImplementationText(Scene):
    def construct(self):
        self.camera.background_color = "#fdf6e3"
        
        # Create two separate lines of text
        text1 = Text(
            "The ability to implement complicated and mathematically",
            font_size=30,
            color="#073642"
        ).move_to(UP * 0.5)
        
        text2 = Text(
            "intensive animations with just a few lines of code.",
            font_size=30,
            color="#073642"
        ).move_to(DOWN * 0.5)
        
        # Group the texts
        text_group = VGroup(text1, text2)
        
        # Animate text appearance word by word
        self.play(
            Write(text1),
            run_time=2
        )
        self.play(
            Write(text2), 
            run_time=2
        )
        self.wait(8)
        
        # Fade out animation
        self.play(FadeOut(text_group))

class IntegralMeaning(Scene):
    def construct(self):
        self.camera.background_color = "#fdf6e3"
        
        # Create title
        title = Text("Area Under the Curve", font_size=48, color="#073642").to_edge(UP)
        
        # Create code text on the left
        code_text = Code(
            code_string='''def area_under_curve():
    dx = 0.001
    x = np.arange(0, 1, dx)
    y = x**2
    return np.sum(y * dx)''',
            language="python",
        ).scale(0.8).next_to(title, DOWN).to_edge(LEFT)
        
        # Create curve and area
        axes = Axes(
            x_range=[0, 1, 0.2],
            y_range=[0, 1, 0.2],
            axis_config={"color": "#073642"},
            x_axis_config={"numbers_to_include": np.arange(0, 1.1, 0.2)},
            y_axis_config={"numbers_to_include": np.arange(0, 1.1, 0.2)}
        ).scale(3).shift(RIGHT * 3 + DOWN)
        
        # Add labels
        x_label = Tex("x", color="#073642").next_to(axes.x_axis.get_end(), RIGHT)
        y_label = Tex("y", color="#073642").next_to(axes.y_axis.get_end(), UP)
        
        curve = axes.plot(
            lambda x: x**2,
            color="#268bd2",
            stroke_width=3
        )
        
        area = axes.get_area(
            curve,
            x_range=(0, 1),
            color="#2aa198",
            opacity=0.5
        )
        
        # Create formula
        formula = MathTex(
            r"\int_0^1 x^2 dx = \frac{1}{3}",
            color="#d33682"
        ).next_to(code_text, DOWN, buff=1)
        
        # Animations
        self.play(Write(title))
        self.play(Write(code_text))
        self.play(Create(axes), Write(x_label), Write(y_label))
        self.play(Create(curve))
        self.play(FadeIn(area))
        self.play(Write(formula))
        self.wait(2)


class CodeExplanation(Scene):
    def construct(self):
        self.camera.background_color = "#fdf6e3"
        
        # Create the code display
        code = Code(
            code_string='''from manim import *

class SquareToCircle(Scene):
    def construct(self):
        square = Square()
        circle = Circle()

        self.play(Create(square))
        self.play(Transform(square, circle))
        self.play(Wait(10))
        
        self.play(FadeOut(circle))''',
            language="python",
        ).scale(0.8).to_edge(LEFT)

        # Create explanations with arrows
        explanations = [
            ("Import manim library", 1),
            ("Define scene class", 2),
            ("Main animation method", 3),
            ("Create geometric shapes", 5),
            ("Animate square creation", 7),
            ("Transform S to C", 8),
            ("Wait for 10 seconds", 9),
            ("Fade out the circle", 11)
        ]

        # Show code first
        self.play(Write(code))
        self.wait(1)

        # Add explanations with arrows one by one
        for explanation, line_num in explanations:
            # Create arrow and text
            arrow = Arrow(
                start=LEFT * 2,
                end=LEFT * 0.5,
                color="#b58900",
                max_tip_length_to_length_ratio=0.15,
                buff=0.1
            )
            text = Text(explanation, font_size=20, color="#073642")
            
            # Position arrow and text
            group = VGroup(arrow, text)
            group.arrange(RIGHT, buff=0.2)
            
            # Position relative to code line
            line_pos = code.line_numbers[line_num-1].get_center()
            group.next_to(code, RIGHT, buff=0.5)
            group.align_to(line_pos, UP)
            
            # Animate
            self.play(
                GrowArrow(arrow),
                Write(text)
            )
            self.wait(0.5)


class VectorRenderingAdvantage(Scene):
    def construct(self):
        self.camera.background_color = "#fdf6e3"
        
        # Create title
        title = Text(
            "- Vector-based rendering: Smooth animations at any resolution.",
            font_size=26,
            color="#073642"
        ).to_edge(UP)
        
        # Create example code
        code = Code(
            code_string='''
def vector_demo(self):
    vector = Vector([2, 1])
    circle = Circle()
    
    self.play(
        GrowArrow(vector),
        Create(circle)
    )
            ''',
            language="python",
        ).scale(0.8).to_edge(LEFT)
        
        # Create demonstration
        vector = Vector([2, 1], color="#268bd2")
        circle = Circle(color="#2aa198")
        demo_group = VGroup(vector, circle).arrange(RIGHT, buff=1).next_to(code, RIGHT, buff=1)
        
        # Animations
        self.play(Write(title))
        self.play(Write(code))
        self.play(
            GrowArrow(vector),
            Create(circle)
        )
        self.play(
            vector.animate.scale(1.5),
            circle.animate.scale(0.5)
        )
        self.wait(2)

class LaTeXAdvantage(Scene):
    def construct(self):
        self.camera.background_color = "#fdf6e3"
        
        # Create title
        title = Text(
            "- LaTeX support: Elegant mathematical formulas.",
            font_size=36,
            color="#073642"
        ).to_edge(UP)
        
        # Create example code
        code = Code(
            code_string='''
def latex_demo(self):
    formula = MathTex(
        r"\int_{0}^{\infty} "
        r"e^{-x^2} dx = "
        r"\frac{\sqrt{\pi}}{2}"
    )
    self.play(Write(formula))
            ''',
            language="python",
        ).scale(0.8).to_edge(LEFT)
        
        # Create LaTeX demonstration
        formula = MathTex(
            r"\int_{0}^{\infty} e^{-x^2} dx = \frac{\sqrt{\pi}}{2}",
            color="#268bd2"
        ).next_to(code, RIGHT, buff=1)
        
        # Animations
        self.play(Write(title))
        self.play(Write(code))
        self.play(Write(formula))
        self.wait(2)

class FrameByFrameExplanation(Scene):
    def construct(self):
        self.camera.background_color = "#fdf6e3"
        
        # Create title with more spacing
        title = Text("How?", font_size=48, color="#073642").to_edge(UP, buff=0.5)
        subtitle = Text(
            "Frame by Frame => Partial Movie",
            font_size=36,
            color="#2aa198"
        ).next_to(title, DOWN, buff=0.5)
        
        # Create demonstration frames with better sizing and spacing
        frames = VGroup()
        for i in range(5):
            frame = Rectangle(
                height=1.5,    # Increased height
                width=2.5,     # Increased width
                color="#268bd2",
                stroke_width=3  # Thicker stroke
            ).shift(RIGHT * (i - 2) * 3)  # Increased spacing between frames
            
            frame_text = Text(
                f"Frame {i+1}",
                font_size=24,  # Larger text
                color="#073642"
            ).move_to(frame)
            
            frames.add(VGroup(frame, frame_text))
        
        # Better positioning of frame group
        frames.scale(0.7)  # Scale down the entire group
        frames.next_to(subtitle, DOWN, buff=1.5)
        
        # Add arrows between frames with better visibility
        arrows = VGroup()
        for i in range(4):
            arrow = Arrow(
                frames[i].get_right(),
                frames[i+1].get_left(),
                color="#b58900",
                buff=0.3,
                max_tip_length_to_length_ratio=0.2,  # Larger arrow tips
                stroke_width=3  # Thicker arrows
            )
            arrows.add(arrow)
        
        # Create a better-positioned code box
        code_box = Rectangle(
            width=7,      # Wider box
            height=3,     # Taller box
            color="#2aa198",
            fill_color="#fdf6e3",
            fill_opacity=0.9,
            stroke_width=3
        ).to_edge(DOWN, buff=0.5)
        
        # Code block with better formatting and size
        code = Code(
            code_string='''def render_frame(self, t):
    circle = Circle()
    circle.shift(RIGHT * np.sin(t))
    self.add(circle)''',
            language="python",
        ).move_to(code_box.get_center())
        
        # Refined animations with better timing
        self.play(Write(title), run_time=1)
        self.play(Write(subtitle), run_time=1)
        self.play(
            Create(code_box),
            Write(code),
            run_time=2
        )
        
        # Create frames one by one with better timing
        for frame in frames:
            self.play(Create(frame), run_time=0.5)
        
        # Add arrows with animation
        for arrow in arrows:
            self.play(GrowArrow(arrow), run_time=0.5)
        
        self.wait(3)

class MultimediaSystemsIntro(Scene):
    def construct(self):
        self.camera.background_color = "#fdf6e3"
        
        # Create title and main text
        title = Text(
            "Multimedia systems refer to the integration\nof multiple forms of media in this condition:",
            font_size=36,
            color="#073642",
            line_spacing=1.5
        ).to_edge(UP)
        
        # Create conditions list
        conditions = VGroup(
            *[Text(text, font_size=32, color="#2aa198") 
              for text in [
                " Digital Format",
                " Control with Computer",
                " Integrated",
                " Interactivity",
                " Time Continuity"
            ]]
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        conditions.next_to(title, DOWN * 2)
        
        # Create icons/symbols for each condition
        icons = VGroup()
        
        # Digital Format icon (binary numbers)
        digital = VGroup(
            *[Circle(radius=0.2, color="#d33682").shift(RIGHT * i) for i in range(1)]
        )
        
        # Computer Control icon (monitor shape)
        computer = VGroup(
            *[Circle(radius=0.2, color="#d33682").shift(RIGHT * i) for i in range(2)]
        )
        
        # Integration icon (connecting circles)
        integration = VGroup(
            *[Circle(radius=0.2, color="#d33682").shift(RIGHT * i) for i in range(3)]
        )
        
        # Interactivity icon (mouse pointer)
        pointer = VGroup(
            *[Circle(radius=0.2, color="#d33682").shift(RIGHT * i) for i in range(4)]
        )
        
        # Time Continuity icon (clock-like shape)
        time = VGroup(
            *[Circle(radius=0.2, color="#d33682").shift(RIGHT * i) for i in range(5)]
        )
        
        icons.add(digital, computer, integration, pointer, time)
        
        # Position icons next to conditions
        for icon, condition in zip(icons, conditions):
            icon.scale(0.7)
            icon.next_to(condition, LEFT)
        
        # Animations
        self.play(Write(title))
        self.wait(1)
        
        for condition, icon in zip(conditions, icons):
            self.play(
                Write(condition),
                Create(icon)
            )
            self.wait(0.5)
        
        self.wait(2)

class AudioIntroduction(Scene):
    def construct(self):
        self.camera.background_color = "#fdf6e3"
        
        # Create title
        title = Text("What is Audio?", font_size=48, color="#073642").to_edge(UP)
        
        description = Text(
            "Audio refers to sound, specifically the range of frequencies\n" +
            "that can be heard by the human ear,\n" +
            "typically from 20 Hz to 20 kHz:",
            font_size=32,
            color="#2aa198", 
            line_spacing=1.5
        ).next_to(title, DOWN)
        
        # Create wave visualization
        axes = Axes(
            x_range=[0, 4*PI, PI/2],
            y_range=[-1.5, 1.5, 0.5],
            color="#073642"
        ).scale(0.8).shift(DOWN)
        
        # Create different frequency waves
        wave1 = axes.plot(lambda x: np.sin(x), color="#268bd2")
        wave2 = axes.plot(lambda x: 0.5*np.sin(2*x), color="#859900")
        wave3 = axes.plot(lambda x: 0.25*np.sin(4*x), color="#d33682")
        
        # Labels
        labels = VGroup(
            Text("Low Frequency", font_size=24, color="#268bd2"),
            Text("Medium Frequency", font_size=24, color="#859900"),
            Text("High Frequency", font_size=24, color="#d33682")
        ).arrange(DOWN, aligned_edge=RIGHT).to_edge(RIGHT)
        
        # Animations
        self.play(Write(title))
        self.play(Write(description))
        self.play(Create(axes))
        
        for wave, label in zip([wave1, wave2, wave3], labels):
            self.play(
                Create(wave),
                Write(label)
            )
            self.wait(1)
        
        self.wait(2)


class AudioComponents(Scene):
    def construct(self):
        self.camera.background_color = "#fdf6e3"
        
        # Create components list
        components = VGroup(
            Text("Sound Waves", color="#268bd2"),
            Text("Frequency", color="#859900"),
            Text("Amplitude", color="#d33682"),
            Text("Waveform", color="#2aa198")
        ).arrange(DOWN, buff=0.8)
        
        # Create wave demonstration
        axes = Axes(
            x_range=[0, 2*PI, PI/2],
            y_range=[-1.5, 1.5, 0.5],
            color="#073642"
        ).scale(0.8)
        
        wave = axes.plot(
            lambda x: np.sin(2*x)*np.exp(-x/3),
            color="#268bd2"
        )
        
        demo_group = VGroup(axes, wave).to_edge(RIGHT)
        
        # Animations
        self.play(Write(components[0]))
        self.play(Create(axes))
        self.play(Create(wave))
        
        for component in components[1:]:
            self.play(Write(component))
            self.wait(0.5)
        
        self.wait(2)


class DigitalAudioRepresentation(Scene):
    def construct(self):
        self.camera.background_color = "#fdf6e3"
        
        # Create title
        title = Text(
            "Digital Audio Representation",
            font_size=48,
            color="#073642"
        ).to_edge(UP)
        
        description = Text(
            "Converting analog sound waves into digital data through:",
            font_size=32,
            color="#2aa198"
        ).next_to(title, DOWN)
        
        # Create process steps
        steps = VGroup(
            Text("1. Sampling", color="#268bd2"),
            Text("2. Quantization", color="#859900"),
            Text("3. Encoding", color="#d33682")
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.8).to_edge(LEFT)
        
        # Create wave visualization
        axes = Axes(
            x_range=[0, 4, 0.5],
            y_range=[-1.5, 1.5, 0.5],
            color="#073642"
        ).scale(0.8).shift(RIGHT * 3)
        
        # Create analog wave
        wave = axes.plot(
            lambda x: np.sin(2*PI*x),
            color="#268bd2"
        )
        
        # Create sampling points
        sample_points = VGroup(*[
            Dot(
                axes.c2p(x, np.sin(2*PI*x)),
                color="#d3003f"
            ) for x in np.arange(0, 4, 0.5)
        ])
        
        # Create quantization levels
        quant_lines = VGroup(*[
            DashedLine(
                axes.c2p(0, y),
                axes.c2p(4, y),
                color="#859900",
                dash_length=0.1
            ) for y in np.arange(-1, 1.1, 0.5)
        ])
        
        # Animations
        self.play(Write(title))
        self.play(Write(description))
        self.play(Create(axes), Create(wave))
        
        # Sampling animation
        self.play(Write(steps[0]))
        self.play(Create(sample_points))
        
        # Quantization animation
        self.play(Write(steps[1]))
        self.play(Create(quant_lines))
        
        # Encoding animation
        self.play(Write(steps[2]))
        binary = Text(
            "01101001",
            font_size=24,
            color="#cb4b16"
        ).next_to(axes, DOWN)
        self.play(Write(binary))
        
        self.wait(2)

class AudioProcessing(Scene):
    def construct(self):
        self.camera.background_color = "#fdf6e3"
        
        # Create title and descriptions
        title = Text("Audio Processing & Modeling", font_size=48, color="#073642").to_edge(UP)
        
        # Create sections for modeling and synthesis
        modeling_title = Text("Modeling:", font_size=36, color="#268bd2")
        modeling_desc = Text(
            "Creating a mathematical model of the sound wave\n"
            "using Fourier Transform to represent frequency components",
            font_size=24,
            color="#2aa198",
            line_spacing=1.5
        )
        
        modeling_group = VGroup(modeling_title, modeling_desc).arrange(DOWN, aligned_edge=LEFT)
        
        # Create Fourier components visualization
        axes = Axes(
            x_range=[0, 2*PI, PI/2],
            y_range=[-1.5, 1.5, 0.5],
            color="#073642"
        ).scale(0.6)
        
        waves = VGroup(*[
            axes.plot(
                lambda x: (1/(i+1))*np.sin((i+1)*x),
                color=color
            ) for i, color in enumerate(["#268bd2", "#859900", "#d33682"])
        ])
        
        sum_wave = axes.plot(
            lambda x: sum([(1/(i+1))*np.sin((i+1)*x) for i in range(3)]),
            color="#cb4b16"
        )
        
        wave_group = VGroup(axes, waves, sum_wave).next_to(modeling_group, DOWN)
        
        # Create synthesis section
        synthesis_title = Text("Synthesizing:", font_size=36, color="#268bd2")
        synthesis_desc = Text(
            "Using the model to generate digital representation\n"
            "through additive or subtractive synthesis",
            font_size=24,
            color="#2aa198",
            line_spacing=1.5
        )
        
        synthesis_group = VGroup(synthesis_title, synthesis_desc).arrange(DOWN, aligned_edge=LEFT)
        synthesis_group.next_to(wave_group, DOWN * 2)
        
        # Animations
        self.play(Write(title))
        self.wait(1)
        
        self.play(Write(modeling_title))
        self.play(Write(modeling_desc))
        
        self.play(Create(axes))
        for wave in waves:
            self.play(Create(wave))
        
        self.play(Create(sum_wave))
        
        self.play(Write(synthesis_title))
        self.play(Write(synthesis_desc))
        
        self.wait(2)

class ImageIntroduction(Scene):
    def construct(self):
        self.camera.background_color = "#fdf6e3"
        
        # Create title and main text
        title = Text("Image Processing", font_size=48, color="#073642").to_edge(UP)
        
        description = Text(
            "Image refers to a visual representation of objects,\n" +
            "scenes, or patterns.",
            font_size=36,
            color="#2aa198",
            line_spacing=1.5
        ).next_to(title, DOWN)
        
        # Create components list
        components = VGroup(
            Text("Pixels", font_size=32, color="#268bd2"),
            Text("Resolution", font_size=32, color="#859900"),
            Text("Color Depth", font_size=32, color="#d33682"),
            Text("Image Formats", font_size=32, color="#cb4b16")
        ).arrange(DOWN, buff=0.8).to_edge(LEFT)
        
        # Create pixel grid demonstration
        pixel_grid = VGroup()
        colors = ["#073642", "#268bd2", "#859900", "#d33682"]
        for i in range(4):
            for j in range(4):
                pixel = Square(
                    side_length=0.3,
                    fill_opacity=0.7,
                    fill_color=colors[(i+j) % 4],
                    stroke_color="#073642"
                ).shift(RIGHT * j * 0.3 + DOWN * i * 0.3)
                pixel_grid.add(pixel)
        
        pixel_demo = VGroup(pixel_grid).next_to(components, RIGHT * 3)
        
        # Animations
        self.play(Write(title))
        self.play(Write(description))
        
        for component in components:
            self.play(Write(component))
        
        self.play(Create(pixel_grid))
        self.wait(2)

class LightAndEyeInteraction(Scene):
    def construct(self):
        self.camera.background_color = "#fdf6e3"
        
        # Create title
        title = Text(
            "Light and Human Eye Interaction",
            font_size=48,
            color="#073642"
        ).to_edge(UP)
        
        # Create eye components
        eye_outline = Circle(radius=1.5, color="#268bd2")
        iris = Circle(radius=0.8, color="#859900")
        pupil = Circle(radius=0.3, fill_color="#073642", fill_opacity=1)
        
        eye = VGroup(eye_outline, iris, pupil)
        
        # Create light rays
        rays = VGroup(*[
            Arrow(
                LEFT * 3,
                pupil.get_center(),
                color="#b58900",
                max_tip_length_to_length_ratio=0.1
            ).rotate(angle * DEGREES, about_point=pupil.get_center())
            for angle in range(-30, 31, 15)
        ])
        
        # Create labels
        labels = VGroup(
            Text("Cornea", font_size=24, color="#268bd2"),
            Text("Iris", font_size=24, color="#859900"),
            Text("Retina", font_size=24, color="#d33682"),
            Text("Optic Nerve", font_size=24, color="#cb4b16")
        ).arrange(DOWN, buff=0.5).to_edge(RIGHT)
        
        # Animations
        self.play(Write(title))
        self.play(Create(eye))
        self.play(Create(rays))
        
        for label in labels:
            self.play(Write(label))
            self.wait(0.5)
        
        # Animate light interaction
        self.play(
            rays.animate.set_opacity(0.5),
            rate_func=there_and_back,
            run_time=2
        )
        
        self.wait(2)

class DigitalImageProcessing(Scene):
    def construct(self):
        self.camera.background_color = "#fdf6e3"
        
        # Create title
        title = Text("Digital Image Processing", font_size=48, color="#073642").to_edge(UP)
        
        # Create steps
        steps = VGroup(
            Text("Sampling", color="#268bd2", font_size=36),
            Text("Quantization", color="#859900", font_size=36),
            Text("Encoding", color="#d33682", font_size=36)
        ).arrange(DOWN, buff=1).to_edge(LEFT)
        
        # Create grid demonstration
        grid = VGroup()
        n_pixels = 8
        pixel_size = 0.2
        
        for i in range(n_pixels):
            for j in range(n_pixels):
                # Create gradient effect
                intensity = (i + j) / (2 * n_pixels)
                pixel = Square(
                    side_length=pixel_size,
                    fill_opacity=1,
                    fill_color=color_gradient(["#073642", "#eee8d5"], intensity),
                    stroke_width=1,
                    stroke_color="#073642"
                ).move_to([j*pixel_size, -i*pixel_size, 0])
                grid.add(pixel)
        
        grid.scale(2).next_to(steps, RIGHT * 2)
        
        # Create bit depth demonstration
        bit_depths = VGroup(
            Text("1-bit", font_size=24, color="#268bd2"),
            Text("2-bit", font_size=24, color="#859900"),
            Text("4-bit", font_size=24, color="#d33682"),
            Text("8-bit", font_size=24, color="#cb4b16")
        ).arrange(DOWN, buff=0.5).next_to(grid, RIGHT * 2)
        
        # Animations
        self.play(Write(title))
        
        # Sampling demonstration
        self.play(Write(steps[0]))
        self.play(Create(grid))
        
        # Quantization demonstration
        self.play(Write(steps[1]))
        for bit_depth in bit_depths:
            self.play(Write(bit_depth))
        
        # Encoding demonstration
        self.play(Write(steps[2]))
        binary = Text(
            "10110101\n01101001\n11010110",
            font_size=24,
            color="#cb4b16"
        ).next_to(bit_depths, DOWN)
        self.play(Write(binary))
        
        self.wait(2)


class ImageModelingSynthesis(Scene):
    def construct(self):
        self.camera.background_color = "#fdf6e3"
        
        # Create title
        title = Text("Image Modeling & Synthesis", font_size=48, color="#073642").to_edge(UP)
        
        # Create modeling section
        modeling_title = Text("Modeling:", font_size=36, color="#268bd2")
        modeling_desc = Text(
            "Creating mathematical models using:\n" +
            "- Fourier Transform\n" +
            "- Wavelet Transform\n" +
            "- Pattern Recognition",
            font_size=24,
            color="#2aa198",
            line_spacing=1.5
        )
        
        modeling_group = VGroup(modeling_title, modeling_desc).arrange(DOWN, aligned_edge=LEFT)
        
        # Create synthesis section
        synthesis_title = Text("Synthesis:", font_size=36, color="#d33682")
        synthesis_desc = Text(
            "Generating images using:\n" +
            "- Texture Synthesis\n" +
            "- Pattern Generation\n" +
            "- Neural Networks",
            font_size=24,
            color="#2aa198",
            line_spacing=1.5
        )
        
        synthesis_group = VGroup(synthesis_title, synthesis_desc).arrange(DOWN, aligned_edge=LEFT)
        synthesis_group.next_to(modeling_group, DOWN * 2)
        
        # Create example visualization
        example = Square(
            side_length=2,
            fill_color="#268bd2",
            fill_opacity=0.3,
            stroke_color="#073642"
        ).to_edge(RIGHT)
        
        pattern = VGroup(*[
            Line(
                example.get_corner(UL) + RIGHT * i * 0.2,
                example.get_corner(DL) + RIGHT * i * 0.2,
                color="#859900"
            ) for i in range(11)
        ])
        
        # Animations
        self.play(Write(title))
        self.play(Write(modeling_group))
        self.play(Create(example))
        self.play(Create(pattern))
        self.play(Write(synthesis_group))
        
        # Transform pattern
        self.play(
            pattern.animate.rotate(PI/4),
            rate_func=there_and_back,
            run_time=2
        )
        
        self.wait(2)


class CompressionIntro(Scene):
    def construct(self):
        self.camera.background_color = "#fdf6e3"
        
        # Create title and description
        title = Text("Compression", font_size=48, color="#073642").to_edge(UP)
        description = Text(
            "Reducing data size while preserving essential information",
            font_size=32,
            color="#2aa198"
        ).next_to(title, DOWN)
        
        # Create compression types
        types_title = Text("Types:", font_size=36, color="#268bd2").to_edge(LEFT)
        
        lossless = VGroup(
            Text("Lossless Compression:", color="#859900", font_size=32),
            Text("• ZIP", color="#2aa198", font_size=24),
            Text("• PNG", color="#2aa198", font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT)
        
        lossy = VGroup(
            Text("Lossy Compression:", color="#d33682", font_size=32),
            Text("• JPEG", color="#cb4b16", font_size=24),
            Text("• MP3", color="#cb4b16", font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT)
        
        compression_types = VGroup(lossless, lossy).arrange(DOWN, buff=1)
        compression_types.next_to(types_title, DOWN)
        
        # Create visualization
        data_rect = Rectangle(
            height=3,
            width=5,
            color="#268bd2",
            fill_opacity=0.3
        ).to_edge(RIGHT)
        
        compressed_rect = Rectangle(
            height=1.5,
            width=2.5,
            color="#d33682",
            fill_opacity=0.3
        ).next_to(data_rect, DOWN, buff=0.5)
        
        arrow = Arrow(
            data_rect.get_bottom(),
            compressed_rect.get_top(),
            color="#b58900"
        )
        
        # Animations
        self.play(Write(title))
        self.play(Write(description))
        self.play(Write(types_title))
        
        self.play(Write(lossless))
        self.play(Write(lossy))
        
        self.play(
            Create(data_rect),
            Create(arrow),
            Create(compressed_rect)
        )
        
        self.wait(2)

class JPEGCompression(Scene):
    def construct(self):
        self.camera.background_color = "#fdf6e3"
        
        # Create title
        title = Text("JPEG Compression Process", font_size=48, color="#073642").to_edge(UP)
        
        # Create steps
        steps = VGroup(
            Text("1. Color Space Conversion", color="#268bd2", font_size=32),
            Text("2. Downsampling", color="#859900", font_size=32),
            Text("3. DCT Transform", color="#d33682", font_size=32),
            Text("4. Quantization", color="#cb4b16", font_size=32),
            Text("5. Entropy Encoding", color="#b58900", font_size=32)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        
        steps.next_to(title, DOWN)
        
        # Create block visualization
        block = VGroup()
        for i in range(8):
            for j in range(8):
                pixel = Square(
                    side_length=0.2,
                    fill_opacity=0.5,
                    fill_color=color_gradient(["#073642", "#eee8d5"], (i+j)/14),
                    stroke_width=1,
                    stroke_color="#073642"
                ).move_to([j*0.2, -i*0.2, 0])
                block.add(pixel)
        
        block.scale(2).to_edge(RIGHT)
        
        # Animations
        self.play(Write(title))
        
        for step in steps:
            self.play(Write(step))
            if step == steps[2]:  # During DCT Transform
                self.play(Create(block))
            elif step == steps[3]:  # During Quantization
                self.play(
                    block.animate.set_opacity(0.3),
                    run_time=2
                )
        
        self.wait(2)


class MJPEGCompression(Scene):
    def construct(self):
        self.camera.background_color = "#fdf6e3"
        
        # Create title
        title = Text("MJPEG & Motion Compression", font_size=48, color="#073642").to_edge(UP)
        
        # Create MJPEG description
        mjpeg_title = Text("MJPEG (Motion JPEG):", font_size=36, color="#268bd2")
        mjpeg_desc = Text(
            "Compresses each frame independently as a JPEG image",
            font_size=24,
            color="#2aa198"
        )
        
        mjpeg_group = VGroup(mjpeg_title, mjpeg_desc).arrange(DOWN, aligned_edge=LEFT)
        
        # Create frame sequence visualization
        frames = VGroup()
        for i in range(4):
            frame = Rectangle(
                height=2,
                width=1.5,
                color="#859900",
                fill_opacity=0.2
            ).shift(RIGHT * i * 2)
            
            jpeg_text = Text(
                "JPEG",
                font_size=20,
                color="#d33682"
            ).move_to(frame)
            
            frames.add(VGroup(frame, jpeg_text))
        
        frames.next_to(mjpeg_group, DOWN)
        
        # Create arrows between frames
        arrows = VGroup()
        for i in range(3):
            arrow = Arrow(
                frames[i].get_right(),
                frames[i+1].get_left(),
                color="#b58900",
                buff=0.2
            )
            arrows.add(arrow)
        
        # Create storage/transmission section
        storage_title = Text(
            "Frame Storage/Transmission:",
            font_size=36,
            color="#268bd2"
        )
        
        storage_desc = Text(
            "Compressed frames are stored or transmitted\n"
            "sequentially to create a video stream",
            font_size=24,
            color="#2aa198",
            line_spacing=1.5
        )
        
        storage_group = VGroup(storage_title, storage_desc).arrange(DOWN, aligned_edge=LEFT)
        storage_group.next_to(frames, DOWN * 2)
        
        # Create data flow visualization
        data_flow = Rectangle(
            height=0.5,
            width=6,
            color="#cb4b16",
            fill_opacity=0.3
        ).next_to(storage_group, DOWN)
        
        flow_arrows = VGroup(*[
            Arrow(
                LEFT * 2 + RIGHT * i,
                LEFT * 2 + RIGHT * (i + 0.5),
                color="#b58900",
                buff=0.1
            ) for i in range(0, 4, 0.5)
        ]).next_to(storage_group, DOWN)
        
        # Animations
        self.play(Write(title))
        self.play(Write(mjpeg_group))
        
        # Animate frame sequence
        for frame in frames:
            self.play(Create(frame))
        
        for arrow in arrows:
            self.play(GrowArrow(arrow))
        
        self.play(Write(storage_group))
        self.play(
            Create(data_flow),
            *[GrowArrow(arrow) for arrow in flow_arrows]
        )
        
        # Animate data flow
        self.play(
            *[
                arrow.animate.shift(RIGHT * 2)
                for arrow in flow_arrows
            ],
            rate_func=linear,
            run_time=2
        )
        
        self.wait(2)


class FinalQuote(Scene):
    def construct(self):
        self.camera.background_color = "#fdf6e3"
        
        # Create quote text
        quote = Text(
            '"Be a voice, not an echo."',
            font_size=48,
            color="#073642"
        )
        
        # Add wave effect to visualize sound/voice
        waves = VGroup(*[
            Circle(
                radius=i*0.5,
                stroke_width=2,
                stroke_opacity=1-i/8,
                color="#268bd2"
            ) for i in range(1, 6)
        ])
        
        # Position elements
        quote.move_to(ORIGIN)
        waves.move_to(LEFT * 3)
        
        # Animations
        self.play(Write(quote))
        
        # Animate expanding waves
        def wave_animation(mob, dt):
            for wave in waves:
                wave.scale(1.02)
                wave.move_to(LEFT * 3)  # Keep waves centered
                if wave.get_width() > 5:
                    wave.scale(0.5)  # Reset size when too large
        
        waves.add_updater(wave_animation)
        self.play(Create(waves))
        
        self.play(
            quote.animate.scale(1.1),
            rate_func=there_and_back,
            run_time=2
        )
        
        self.wait(3)
        
        # Remove updater before fading out
        waves.clear_updaters()
        
        # Fade out
        self.play(
            FadeOut(quote),
            FadeOut(waves)
        )
        
        self.wait(1)