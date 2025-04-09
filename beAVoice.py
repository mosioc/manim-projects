from manim import *

class BeAVoiceNotAnEcho(Scene):
    def construct(self):
        # Define the two sentences
        sentence1 = Text("Be a voice", font_size=48, font="Arial", color=WHITE)
        sentence2 = Text("Not an echo", font_size=48, font="Arial", color=WHITE)

        # Position sentence2 below sentence1
        sentence2.next_to(sentence1, DOWN)

        # Animate the first sentence appearing
        self.play(Write(sentence1))
        self.wait(1)

        # Animate the second sentence appearing with a fade-in effect
        self.play(FadeIn(sentence2, shift=UP))
        self.wait(1)

        # Emphasize "voice" and "echo" with color changes
        voice_word = sentence1[6:]  # "voice"
        echo_word = sentence2[4:]   # "echo"

        self.play(
            voice_word.animate.set_color(BLUE),
            echo_word.animate.set_color(RED),
        )
        self.wait(2)

        # Add a transformation effect to "echo"
        echo_copy = echo_word.copy()
        self.play(
            echo_copy.animate.scale(1.5).set_opacity(0.5).shift(DOWN * 0.5),
            rate_func=there_and_back,
            run_time=2
        )
        self.wait(1)

        # Fade out everything
        self.play(FadeOut(sentence1), FadeOut(sentence2))
        self.wait(1)