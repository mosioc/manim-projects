from manim import *
import numpy as np
import random

class EnhancedIrisAnimation(Scene):
    def construct(self):
        self.camera.background_color = "#fdf6e3"
        
        # Enhanced configuration
        
        num_lines = 300  # Increased number of lines
        radius = 3
        pupil_radius = 1
        
        # Create the background circle
        circle = Circle(radius=radius, color="#fdf6e3").set_fill("#fdf6e3", opacity=1)
        
        # Create the pupil
        pupil = Circle(radius=pupil_radius, color=BLACK).set_fill(BLACK, opacity=1)
        
        # Create detailed iris patterns
        outer_lines = VGroup()
        inner_lines = VGroup()
        texture_dots = VGroup()
        
        # Create two sets of lines for more detail
        for i in range(num_lines):
            angle = i * TAU / num_lines
            
            # Outer pattern (longer, wavier lines)
            points_outer = []
            num_points = 30
            for t in range(num_points):
                t_val = t / (num_points - 1)
                # Complex wave pattern
                wave_amplitude = 0.15 * np.sin(t_val * PI * 3) * np.cos(angle * 2)
                r = pupil_radius + (radius - pupil_radius) * t_val
                theta = angle + wave_amplitude
                points_outer.append([r * np.cos(theta), r * np.sin(theta), 0])
            
            line_outer = VMobject()
            line_outer.set_points_smoothly(points_outer)
            outer_lines.add(line_outer)
            
            # Inner pattern (shorter, finer details)
            if i % 2 == 0:  # Add inner lines to every other position for variety
                points_inner = []
                for t in range(15):
                    t_val = t / 14
                    wave_amplitude = 0.08 * np.sin(t_val * PI * 4)
                    r = pupil_radius + (radius - pupil_radius) * 0.7 * t_val
                    theta = angle + wave_amplitude
                    points_inner.append([r * np.cos(theta), r * np.sin(theta), 0])
                
                line_inner = VMobject()
                line_inner.set_points_smoothly(points_inner)
                inner_lines.add(line_inner)
        
        # Add texture dots for more detail
        for _ in range(200):
            angle = random.uniform(0, TAU)
            dist = random.uniform(pupil_radius + 0.2, radius - 0.2)
            dot = Dot(
                point=[dist * np.cos(angle), dist * np.sin(angle), 0],
                radius=0.02
            )
            texture_dots.add(dot)
        
        # Create detailed color gradients
        outer_colors = [
            "#87CEEB",  # Light blue
            "#E8E8E8",  # Light gray
            "#CD853F",  # Peru (orange-brown)
            "#8B4513"   # Saddle brown
        ]
        inner_colors = [
            "#A9A9A9",  # Dark gray
            "#F5F5F5",  # White smoke
            "#DEB887"   # Burlywood
        ]
        
        outer_lines.set_color_by_gradient(*outer_colors)
        inner_lines.set_color_by_gradient(*inner_colors)
        texture_dots.set_color_by_gradient(*outer_colors)
        
        # Enhanced animation sequence
        self.play(
            Create(circle),
            run_time=1
        )
        
        # Animate outer lines with stagger effect
        for i in range(0, len(outer_lines), 10):
            self.play(
                *[Create(outer_lines[j]) for j in range(i, min(i + 10, len(outer_lines)))],
                run_time=0.3,
            )
        
        # Animate inner lines
        self.play(
            Create(inner_lines),
            run_time=2
        )
        
        # Add texture dots with fade effect
        self.play(
            FadeIn(texture_dots, lag_ratio=0.05),
            run_time=2
        )
        
        # Create pupil with spiral effect
        pupil_spiral = Circle(radius=pupil_radius, color=BLACK)
        self.play(
            Create(pupil_spiral, run_time=1.5),
            pupil_spiral.animate.set_fill(BLACK, opacity=1),
            run_time=1
        )
        
        # Add dynamic movement animations
        animations = []
        
        # Subtle pulsing of the iris
        for i in range(len(outer_lines)):
            if i % 3 == 0:  # Animate every third line for efficiency
                animations.append(
                    outer_lines[i].animate.shift(0.05 * np.sin(i) * RIGHT + 0.03 * np.cos(i) * UP)
                )
        
        # Subtle rotation of inner lines
        animations.append(inner_lines.animate.rotate(0.1))
        
        # Subtle movement of texture dots
        for dot in texture_dots:
            animations.append(
                dot.animate.shift(0.05 * random.uniform(-1, 1) * RIGHT + 
                                0.05 * random.uniform(-1, 1) * UP)
            )
        
        # Play all animations together
        self.play(
            *animations,
            run_time=3,
            rate_func=there_and_back_with_pause
        )
        
        # Final subtle pulse animation
        self.play(
            outer_lines.animate.scale(1.02),
            inner_lines.animate.scale(1.01),
            texture_dots.animate.scale(1.02),
            run_time=2,
            rate_func=there_and_back
        )
        
        self.wait(1)

if __name__ == "__main__":
    config.pixel_height = 1080
    config.pixel_width = 1080
    config.frame_height = 8
    config.frame_width = 8
    with tempconfig({"quality": "high_quality", "preview": True}):
        scene = EnhancedIrisAnimation()
        scene.render()