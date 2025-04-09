from manim import *

# Define a custom peach color
PEACH = "#FFE5B4"

class HeterochromiaIridum(Scene):
    def construct(self):
        # Define eye colors
        left_eye_color = BLUE
        right_eye_color = GREEN

        # Create the face
        face = Circle(color=WHITE, fill_opacity=1, radius=2.5)
        face.set_fill(PEACH)  # Use the custom peach color

        # Rest of the code remains the same
        left_eye = Circle(color=left_eye_color, fill_opacity=1, radius=0.5)
        right_eye = Circle(color=right_eye_color, fill_opacity=1, radius=0.5)
        left_eye.move_to(LEFT * 1.5)
        right_eye.move_to(RIGHT * 1.5)

        left_pupil = Circle(color=BLACK, fill_opacity=1, radius=0.2)
        right_pupil = Circle(color=BLACK, fill_opacity=1, radius=0.2)
        left_pupil.move_to(left_eye.get_center())
        right_pupil.move_to(right_eye.get_center())

        eyes = VGroup(left_eye, right_eye, left_pupil, right_pupil)

        left_eyebrow = ArcBetweenPoints(
            start=LEFT * 2 + UP * 1.5,
            end=LEFT * 1 + UP * 1.5,
            angle=-PI / 4,
            color=BLACK
        )
        right_eyebrow = ArcBetweenPoints(
            start=RIGHT * 1 + UP * 1.5,
            end=RIGHT * 2 + UP * 1.5,
            angle=PI / 4,
            color=BLACK
        )

        mouth = ArcBetweenPoints(
            start=LEFT * 1 + DOWN * 1.5,
            end=RIGHT * 1 + DOWN * 1.5,
            angle=PI / 2,
            color=BLACK
        )

        face_group = VGroup(face, eyes, left_eyebrow, right_eyebrow, mouth)

        self.play(FadeIn(face_group))
        self.wait(1)

        self.play(
            left_eye.animate.scale(0.8, about_point=left_eye.get_center()),
            right_eye.animate.scale(0.8, about_point=right_eye.get_center()),
            rate_func=there_and_back,
            run_time=1
        )
        self.wait(1)

        description = Text("Heterochromia Iridum: Two Different Colored Eyes", font_size=24)
        description.to_edge(DOWN)
        self.play(Write(description))
        self.wait(3)

        self.play(FadeOut(face_group), FadeOut(description))