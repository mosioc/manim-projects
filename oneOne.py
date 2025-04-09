from manim import *

class TextTransition(Scene):
    def construct(self):
        # 1. Display the initial text
        self.camera.background_color = "#fdf6e3"  # Solarized Light background
        
        title = Text("Manim", font_size=72, color="#268bd2")  # Solarized Blue for text
        subtitle = Text("Mehdi Maleki", font_size=48, color="#2aa198")  # Solarized Cyan for text
        year = Text("2025", font_size=36, color="#859900")  # Solarized Green for text
        # Positioning the text
        title.to_edge(UP)
        subtitle.next_to(title, DOWN)
        year.next_to(subtitle, DOWN)
        
        self.add(title, subtitle, year)
        self.wait(1)

        # 1.1. Transition "Manim Mehdi Maleki 2025" to "M + Anim: Mathematical Animation"
        new_text = VGroup(Text("M + Anim:"), Text("Mathematical Animation"))
        new_text.arrange(DOWN, aligned_edge=LEFT)
        new_text.move_to(ORIGIN)

        self.play(Transform(title, new_text[0]), Transform(subtitle, new_text[1]))

        # Change color and boldness for 'M' and 'Anim'
        self.play(
            title[0][0].animate.set_color("#d33682").set_bold(True),  # Change color and bold 'M'
            subtitle[0][0:4].animate.set_color("#d33682").set_bold(True),  # Change color and bold 'Anim'
        )

        # Fade out the year 2025
        self.play(FadeOut(year))
        self.wait(1)
