from manim import *
import numpy as np

class FourierTransformVisualization(Scene):
    def construct(self):
        # Create a layout with better spacing
        # Title with more space
        title = Text("Fourier Transform Visualization", font_size=40)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        
        # Set up the axes for the time domain - position further left with more space
        time_axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-1.5, 1.5, 0.5],
            axis_config={"color": BLUE},
            x_length=5,
            y_length=3,
        ).to_corner(DL, buff=1)
        
        # Add axis labels for time domain with better positioning
        time_x_label = Text("Time", font_size=20).next_to(time_axes.x_axis, DOWN, buff=0.25)
        time_y_label = Text("Amplitude", font_size=20).next_to(time_axes.y_axis, LEFT, buff=0.25)
        
        time_label = Text("Time Domain", font_size=24, color=BLUE)
        time_label.next_to(time_axes, UP, buff=0.25)
        
        # Set up the axes for the frequency domain - position further right with more space
        freq_axes = Axes(
            x_range=[0, 4, 1],
            y_range=[0, 1.5, 0.5],
            axis_config={"color": RED},
            x_length=5,
            y_length=3,
        ).to_corner(DR, buff=1)
        
        # Add axis labels for frequency domain with better positioning
        freq_x_label = Text("Frequency", font_size=20).next_to(freq_axes.x_axis, DOWN, buff=0.25)
        freq_y_label = Text("Magnitude", font_size=20).next_to(freq_axes.y_axis, LEFT, buff=0.25)
        
        freq_label = Text("Frequency Domain", font_size=24, color=RED)
        freq_label.next_to(freq_axes, UP, buff=0.25)
        
        self.play(
            Create(time_axes),
            Write(time_label),
            Write(time_x_label),
            Write(time_y_label),
            Create(freq_axes),
            Write(freq_label),
            Write(freq_x_label),
            Write(freq_y_label)
        )
        
        # Define a simple signal (sum of two sine waves)
        def signal_func(x):
            return 0.5 * np.sin(2 * PI * 1 * x) + 0.3 * np.sin(2 * PI * 2 * x)
        
        # Create the signal graph
        signal_graph = time_axes.plot(signal_func, color=BLUE)
        signal_label = Text("f(t) = 0.5sin(2πt) + 0.3sin(4πt)", font_size=16, color=BLUE)
        signal_label.next_to(time_axes, DOWN, buff=0.5)
        
        self.play(
            Create(signal_graph),
            Write(signal_label)
        )
        
        # Create the frequency domain representation with proper positioning
        freq_values = [1, 2]
        amplitudes = [0.5, 0.3]
        
        # Create bars for the frequency components
        bars = VGroup()
        
        for freq, amp in zip(freq_values, amplitudes):
            bar = Rectangle(
                height=amp * freq_axes.y_length / 1.5,  # Scale height to match axes
                width=0.2,
                fill_opacity=0.8,
                color=RED
            )
            # Position bars properly on the frequency axis
            bar.move_to(freq_axes.c2p(freq, amp/2), aligned_edge=DOWN)
            bars.add(bar)
            
            # Add magnitude labels with better positioning
            mag_label = Text(f"{amp}", font_size=16, color=RED)
            mag_label.next_to(bar, UP, buff=0.1)
            bars.add(mag_label)
            
            # Add frequency labels with better positioning
            freq_label = Text(f"{freq} Hz", font_size=16, color=RED)
            freq_label.next_to(bar, DOWN, buff=0.1)
            bars.add(freq_label)
        
        # Animation showing the transformation
        self.play(
            TransformFromCopy(signal_graph, bars, run_time=2.5)
        )
        
        # Add centered arrow between the domains
        arrow_start = time_axes.get_right() + RIGHT * 0.5
        arrow_end = freq_axes.get_left() + LEFT * 0.5
        
        arrow = Arrow(
            arrow_start,
            arrow_end,
            buff=0.3,
            color=YELLOW,
            max_tip_length_to_length_ratio=0.15
        )
        
        fourier_text = Text("Fourier Transform", font_size=24, color=YELLOW)
        fourier_text.move_to((arrow_start + arrow_end) / 2 + UP * 0.5)
        
        self.play(
            Create(arrow),
            Write(fourier_text)
        )
        
        # Add explanation with better positioning
        explanation = VGroup(
            Text("The Fourier Transform decomposes a signal", font_size=20),
            Text("from time domain into its frequency components", font_size=20)
        ).arrange(DOWN, buff=0.2)
        explanation.to_edge(DOWN, buff=0.8)
        
        self.play(Write(explanation))
        self.wait(2)
        
        # Create a vertical line in time domain to represent current time
        time_indicator = Line(
            time_axes.c2p(-3, -1.5),
            time_axes.c2p(-3, 1.5),
            color=YELLOW
        )
        
        self.play(Create(time_indicator))
        
        # Instead of animating each small step individually,
        # use a single animation with ValueTracker for smoother performance
        time_tracker = ValueTracker(-3)
        
        def update_time_indicator(line):
            t = time_tracker.get_value()
            new_line = Line(
                time_axes.c2p(t, -1.5),
                time_axes.c2p(t, 1.5),
                color=YELLOW
            )
            line.become(new_line)
        
        time_indicator.add_updater(update_time_indicator)
        self.add(time_indicator)
        
        # Single animation to sweep through the time domain
        self.play(
            time_tracker.animate.set_value(3),
            run_time=3,
            rate_func=linear
        )
        
        time_indicator.clear_updaters()
        self.wait(1)
        
        # Final note with better positioning
        final_note = Text("The spikes in frequency domain show the frequencies\npresent in our original signal", font_size=20)
        final_note.move_to(explanation.get_center())
        
        self.play(
            FadeOut(explanation),
            Write(final_note)
        )
        
        self.wait(2)