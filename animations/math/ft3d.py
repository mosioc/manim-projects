from manim import *
import numpy as np

class FourierTransform3D(ThreeDScene):
    def construct(self):
        # Configure the scene
        self.set_camera_orientation(phi=75 * DEGREES, theta=-30 * DEGREES)
        self.camera.set_zoom(0.75)
        
        # Title
        title = Text("3D Fourier Transform Visualization", font_size=36)
        title.to_corner(UL)
        self.add_fixed_in_frame_mobjects(title)
        self.play(Write(title))
        
        # Create 3D axes for time domain
        time_axes = ThreeDAxes(
            x_range=[-4, 4, 1],
            y_range=[-1.5, 1.5, 0.5],
            z_range=[0, 1, 0.25],
            x_length=8,
            y_length=3,
            z_length=2,
            axis_config={"color": BLUE},
        ).shift(LEFT * 3)
        
        # Axes labels for time domain
        x_label_t = Text("Time", font_size=24, color=BLUE)
        y_label_t = Text("Amplitude", font_size=24, color=BLUE)
        z_label_t = Text("Signal", font_size=24, color=BLUE)
        
        x_label_t.next_to(time_axes.get_x_axis(), DOWN, buff=0.5)
        y_label_t.next_to(time_axes.get_y_axis(), LEFT, buff=0.5)
        z_label_t.next_to(time_axes.get_z_axis(), OUT, buff=0.5)
        
        self.add_fixed_in_frame_mobjects(x_label_t, y_label_t, z_label_t)
        
        # Create 3D axes for frequency domain
        freq_axes = ThreeDAxes(
            x_range=[0, 4, 1],
            y_range=[0, 1.5, 0.5],
            z_range=[0, 1, 0.25],
            x_length=6,
            y_length=3,
            z_length=2,
            axis_config={"color": RED},
        ).shift(RIGHT * 3)
        
        # Axes labels for frequency domain
        x_label_f = Text("Frequency", font_size=24, color=RED)
        y_label_f = Text("Magnitude", font_size=24, color=RED)
        z_label_f = Text("Components", font_size=24, color=RED)
        
        x_label_f.next_to(freq_axes.get_x_axis(), DOWN, buff=0.5)
        y_label_f.next_to(freq_axes.get_y_axis(), LEFT, buff=0.5)
        z_label_f.next_to(freq_axes.get_z_axis(), OUT, buff=0.5)
        
        self.add_fixed_in_frame_mobjects(x_label_f, y_label_f, z_label_f)
        
        # Create the scene
        self.play(
            Create(time_axes),
            Create(freq_axes),
        )
        self.wait(1)
        
        # Create a signal in time domain (sum of two sine waves with different frequencies)
        def signal_func(x):
            return 0.5 * np.sin(2 * PI * 1 * x) + 0.3 * np.sin(2 * PI * 2 * x)
        
        # Plot the signal as a parametric 3D curve
        t_range = np.linspace(-3, 3, 100)
        time_curve_points = []
        
        for t in t_range:
            time_curve_points.append(time_axes.c2p(t, signal_func(t), 0))
        
        time_curve = VMobject()
        time_curve.set_points_as_corners(time_curve_points)
        time_curve.set_color(BLUE)
        time_curve.set_stroke(width=3)
        
        # Add text label for the signal function
        signal_eq = MathTex(r"f(t) = 0.5\sin(2\pi t) + 0.3\sin(4\pi t)", font_size=24, color=BLUE)
        signal_eq.next_to(time_axes, UP, buff=0.5)
        self.add_fixed_in_frame_mobjects(signal_eq)
        
        # Animate creating the signal
        self.play(Create(time_curve), Write(signal_eq))
        self.wait(1)
        
        # Create 3D surface for the signal over time (for better visualization)
        surface_z_range = np.linspace(0, 1, 20)
        signal_surface_points = []
        
        for z_val in surface_z_range:
            z_points = []
            for t in t_range:
                z_points.append(time_axes.c2p(t, signal_func(t), z_val))
            signal_surface_points.append(z_points)
        
        # Create a surface from the points
        signal_surface = Surface(
            lambda u, v: np.array([
                time_axes.c2p(
                    -3 + 6 * u,
                    signal_func(-3 + 6 * u),
                    v
                )
            ])[0],
            u_range=[0, 1],
            v_range=[0, 1],
            resolution=(50, 20),
            fill_opacity=0.6,
            stroke_width=0,
            fill_color=BLUE_D,
            should_make_jagged=True,
        )
        
        self.play(Create(signal_surface))
        self.wait(1)
        
        # Frequency domain representation
        freq_values = [1, 2]
        amplitudes = [0.5, 0.3]
        
        # Create 3D bars for frequency components
        bars = VGroup()
        freq_surface_points = []
        
        for i, (freq, amp) in enumerate(zip(freq_values, amplitudes)):
            # Create 3D bars
            bar = Prism(
                dimensions=[0.2, amp, 0.2],
                fill_color=RED,
                fill_opacity=0.8,
                stroke_width=2
            )
            
            # Position at the correct frequency
            bar.move_to(freq_axes.c2p(freq, amp/2, 0.1), aligned_edge=DOWN)
            
            # Create frequency labels
            freq_label = Text(f"{freq} Hz", font_size=16, color=RED)
            mag_label = Text(f"{amp}", font_size=16, color=RED)
            
            freq_label.next_to(bar, DOWN, buff=0.2)
            mag_label.next_to(bar, UP, buff=0.2)
            
            self.add_fixed_in_frame_mobjects(freq_label, mag_label)
            
            bars.add(bar)
            
            # Generate points for a surface along the z-axis for each frequency
            bar_z_points = []
            for z in surface_z_range:
                bar_z_points.append(freq_axes.c2p(freq, amp, z))
            freq_surface_points.append(bar_z_points)
        
        # Create frequency domain prisms/bars
        self.play(TransformFromCopy(signal_surface, bars, run_time=2.5))
        self.wait(1)
        
        # Add an arrow to show the transformation
        arrow = Arrow3D(
            start=time_axes.get_origin() + RIGHT * 2,
            end=freq_axes.get_origin() + LEFT * 2,
            color=YELLOW
        )
        
        fourier_text = Text("Fourier Transform", font_size=28, color=YELLOW)
        fourier_text.move_to(arrow.get_center() + UP * 1.5)
        self.add_fixed_in_frame_mobjects(fourier_text)
        
        self.play(
            Create(arrow),
            Write(fourier_text)
        )
        self.wait(1)
        
        # Create a frequency domain surface to better visualize
        for i, points in enumerate(freq_surface_points):
            freq, amp = freq_values[i], amplitudes[i]
            
            freq_bar_surface = Surface(
                lambda u, v: np.array([
                    freq_axes.c2p(
                        freq,
                        amp * u,
                        v
                    )
                ])[0],
                u_range=[0, 1],
                v_range=[0, 1],
                resolution=(20, 20),
                fill_opacity=0.6,
                stroke_width=0,
                fill_color=RED_D,
            )
            
            self.play(Create(freq_bar_surface))
        
        # Add explanation text
        explanation = Text(
            "The Fourier Transform decomposes a complex signal\ninto its constituent frequency components", 
            font_size=24, 
            line_spacing=1.5
        )
        explanation.to_edge(DOWN, buff=0.5)
        self.add_fixed_in_frame_mobjects(explanation)
        
        self.play(Write(explanation))
        self.wait(1)
        
        # Move camera to show different perspectives of the 3D representation
        self.move_camera(
            phi=45 * DEGREES,
            theta=60 * DEGREES,
            run_time=3
        )
        self.wait(1)
        
        self.move_camera(
            phi=60 * DEGREES,
            theta=-45 * DEGREES,
            run_time=3
        )
        self.wait(1)
        
        # Return to original view
        self.move_camera(
            phi=75 * DEGREES,
            theta=-30 * DEGREES,
            run_time=2
        )
        
        # Final note
        final_note = Text(
            "In 3D, we can visualize how each frequency component\ncontributes to the original signal across time", 
            font_size=24,
            line_spacing=1.5
        )
        final_note.to_edge(DOWN, buff=0.5)
        self.add_fixed_in_frame_mobjects(final_note)
        
        self.play(
            FadeOut(explanation),
            Write(final_note)
        )
        
        self.wait(2)