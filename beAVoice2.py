from manim import *

class AddNewQuote(Scene):
    def construct(self):
        self.camera.background_color = "#fdf6e3"
        
        # Recreate the initial quote (as it was at the end of FinalQuote)
        quote = Text(
            '"Be a voice, not an echo."',
            font_size=48,
            color="#073642"
        )
        quote.move_to(ORIGIN)  # Start at the same position as the end of FinalQuote
        
        # Add the quote to the scene
        self.add(quote)
        
        # Move the quote up slightly
        self.play(quote.animate.shift(UP * 1.5))
        self.wait(1)
        
        # Create the new quote
        new_quote = Text(
            "Be a lighter, not a laughter.",
            font_size=48,
            color="#073642"
        )
        new_quote.next_to(quote, DOWN, buff=0.5)  # Position below the original quote
        
        # Animate the new quote appearing
        self.play(FadeIn(new_quote, shift=UP))
        self.wait(2)
        
        # Optional: Emphasize "lighter" and "laughter" with color changes
        lighter_word = new_quote[3:11]  # "lighter"
        laughter_word = new_quote[15:23]  # "laughter"

        voice_word = quote[4:9]  # "voice"
        echo_word = quote[15:19]  # "echo"
        
        self.play(
            lighter_word.animate.set_color("#b58900"),  # Yellowish
            laughter_word.animate.set_color("#2aa198"),  # Cyan
            voice_word.animate.set_color("#b58900"),  # Yellowish
            echo_word.animate.set_color("#2aa198"),  # Cyan
        )
        self.wait(2)