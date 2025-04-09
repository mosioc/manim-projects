from manim import *

class TexTransformExample(Scene):
    def construct(self):
        # Set Solarized Light background
        self.camera.background_color = "#fdf6e3"
        # Define the equations with proper LaTeX formatting
        lines = VGroup(
            MathTex("A^2", "+", "B^2", "=", "C^2"),
            MathTex("A^2", "=", "C^2", "-", "B^2"),
            MathTex("A^2", "=", "(C + B)(C - B)"),
            MathTex("A", "=", "\\sqrt{(C + B)(C - B)}"),
        )
        lines.arrange(DOWN, buff=LARGE_BUFF)

        # Set colors using the correct method
        for line in lines:
            line.set_color_by_tex_to_color_map(
                {
                    "A": BLUE,
                    "B": TEAL,
                    "C": GREEN,
                    "=": BLACK,
                    "+": BLACK,
                    "-": BLACK,
                }
            )

        play_kw = {"run_time": 2}
        self.add(lines[0])

        # First transformation
        self.play(
            TransformMatchingTex(
                lines[0].copy(),
                lines[1],
                path_arc=90 * DEGREES,
            ),
            **play_kw,
        )
        self.wait()

        # Second transformation
        self.play(
            TransformMatchingTex(
                lines[1].copy(),
                lines[2],
                key_map={
                    "C^2": "C",
                    "B^2": "B",
                },
            ),
            **play_kw,
        )
        self.wait()

        # Final transformation with square root
        new_line2 = MathTex("A^2", "=", "(C + B)(C - B)")
        new_line2.replace(lines[2])
        new_line2.match_style(lines[2])

        self.play(
            TransformMatchingTex(
                new_line2,
                lines[3],
                transform_mismatches=True,
            ),
            **play_kw,
        )
        self.wait(3)
        self.play(FadeOut(lines))

        # Text transformation
        source = Text("the morse code", height=1, color=BLACK)
        target = Text("here come dots", height=1, color=BLACK)

        self.play(Write(source))
        self.wait()
        kw = {"run_time": 3, "path_arc": PI / 2}
        self.play(TransformMatchingShapes(source, target, **kw))
        self.wait()
        self.play(TransformMatchingShapes(target, source, **kw))
        self.play(Wait(4))
        self.play(FadeOut(source))
