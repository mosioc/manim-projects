from manim import *
from manim.utils.rate_functions import ease_in_out_sine
from manim.utils.rate_functions import ease_in_elastic
from manim.utils.rate_functions import ease_out_elastic
from manim.utils.rate_functions import ease_in_out_cubic

class CP(Scene):
    def construct(self):
        self.camera.background_color = "#fdf6e3"  # Solarized Light background
        
        # --- SECTION 1: Initial Title ---
        title = Text("Manim", font_size=102, color="#073642")  # Darker Solarized base02
        subtitle = Text("Mehdi Maleki", font_size=48, color="#2aa198")  # Solarized Cyan for text
        year = Text("2025", font_size=36, color="#859900")  # Solarized Green for text
        
        title.move_to(ORIGIN, DOWN * 0.1)
        subtitle.next_to(title, DOWN * 0.8)
        year.next_to(subtitle, DOWN)
        
        self.play(Write(title), Write(subtitle), Write(year))
        self.wait(1)
        
        # --- SECTION 1.1: Transform to M + Anim ---
        self.play(FadeOut(year))
        
        new_title = Text("M + Anim:", font_size=72, color="#073642")
        
        math_text = "Mathematical Animation"
        math_animation = Text(math_text, font_size=48, color="#073642")
        
        m_index = 0
        anim_start = math_text.find("Anim")
        
        math_animation[m_index].set_color("#d3003f").set_weight(BOLD)
        
        if anim_start != -1:
            for i in range(anim_start, anim_start + 4):
                math_animation[i].set_color("#d3003f").set_weight(BOLD)
        
        new_text = VGroup(new_title, math_animation)
        new_text.arrange(DOWN, aligned_edge=LEFT)
        new_text.move_to(ORIGIN)
        
        self.play(
            Transform(title, new_title),
            Transform(subtitle, math_animation)
        )
        
        emphasis_animations = [math_animation[m_index].animate.scale(1.2)]
        if anim_start != -1:
            for i in range(anim_start, anim_start + 4):
                emphasis_animations.append(math_animation[i].animate.scale(1.2))
        
        self.play(*emphasis_animations)
        self.wait(2)
        
        # --- SECTION 1.2: Fade Out All Text ---
        all_text = VGroup(title, subtitle)
        self.play(
            FadeOut(all_text, shift=UP*0.5, scale=0.8),
            rate_func=smooth
        )
        self.wait(0.5)
        
        # --- SECTION 1.3: Abstract Engine Animation ---
        # Create an abstract engine shape
        engine_parts = VGroup()
        
        # Main body (circle)
        main_body = Circle(radius=2, color="#073642").set_fill("#268bd2", opacity=0.4)
        
        # Gears inside the engine
        gear1 = RegularPolygon(n=8, color="#b58900", fill_opacity=0.6).scale(0.5).move_to(main_body.get_center())
        gear2 = RegularPolygon(n=8, color="#cb4b16", fill_opacity=0.6).scale(0.8).move_to(main_body.get_center())
        
        # Add some connecting rods
        rod1 = Line(main_body.get_left(), main_body.get_right(), color="#d33682").set_stroke(width=4)
        rod2 = Line(main_body.get_top(), main_body.get_bottom(), color="#d33682").set_stroke(width=4)
        
        # Add decorative elements
        for angle in np.linspace(0, 2*PI, 6, endpoint=False):
            point = main_body.point_at_angle(angle)
            connector = Circle(radius=0.3, color="#6c71c4").set_fill("#dc322f", opacity=0.7)
            connector.move_to(point)
            engine_parts.add(connector)
        
        engine_parts.add(gear2, rod1, rod2, gear1, main_body)
        
        # Animate the engine appearing
        self.play(
            FadeIn(engine_parts, scale=1.5),
            rate_func=ease_out_elastic
        )
        
        # Rotation animations
        self.play(
            Rotate(gear1, angle=2*PI, rate_func=linear),
            Rotate(gear2, angle=-2*PI, rate_func=linear),
            Rotate(engine_parts, angle=PI/2, rate_func=smooth),
            run_time=3
        )
        
        self.play(
            Rotate(gear1, angle=PI, rate_func=linear),
            Rotate(gear2, angle=-PI, rate_func=linear),
            Rotate(engine_parts, angle=-PI/4, rate_func=ease_in_out_sine),
            run_time=2
        )
        
        self.wait(0.5)
        
        # --- SECTION 1.4: Fade Out Engine ---
        self.play(
            FadeOut(engine_parts, shift=DOWN*1.5, scale=0.7),
            rate_func=ease_in_out_cubic,
            run_time=1.5
        )
        self.wait(0.5)
        
        # --- SECTION 1.5: Animation Engine Text ---
        title_engine = Text("Animation Engine:", font_size=72, color="#073642")
        subtitle_engine = Text("An engine for precise programmatic animations.", 
                              font_size=36, color="#586e75")
        
        title_engine.to_edge(UP, buff=1.5)
        subtitle_engine.next_to(title_engine, DOWN, buff=0.8)
        
        engine_text_group = VGroup(title_engine, subtitle_engine)
        
        # Animate in with typewriter effect
        self.play(AddTextLetterByLetter(title_engine), run_time=1.5)
        self.play(AddTextLetterByLetter(subtitle_engine), run_time=2)
        
        self.wait(1.5)
        
        # --- SECTION 1.6: Fade Out Engine Text ---
        self.play(
            FadeOut(engine_text_group, shift=RIGHT*0.7),
            rate_func=smooth,
            run_time=1.2
        )
        self.wait(0.5)
        
        # --- SECTION 1.7: 3Blue1Brown Reference ---
        main_title = Text("Heterochromia Iridum", font_size=64, color="#073642")
        creator = Text("3Blue 1Brown", font_size=48, color="#268bd2")
        byline = Text("- by Grant Sanderson", font_size=36, color="#586e75")
        
        main_title.to_edge(UP, buff=1.5)
        creator.next_to(main_title, DOWN, buff=0.8)
        byline.next_to(creator, DOWN, buff=0.5)
        
        grant_text_group = VGroup(main_title, creator, byline)
        
        # Color the "3Blue" in blue and "1Brown" in brown
        creator[0:5].set_color("#268bd2")  # 3Blue in blue
        creator[6:].set_color("#b58900")   # 1Brown in brown
        
        # Create a reveal animation with growing circles
        self.play(
            GrowFromCenter(main_title),
            run_time=1.2
        )
        
        self.play(
            FadeIn(creator, shift=UP*0.5),
            run_time=1
        )
        
        self.play(
            Write(byline),
            run_time=1
        )
        
        self.wait(1.5)
        
        # --- SECTION 1.8: Final Fade Out ---
        self.play(
            FadeOut(grant_text_group, shift=DOWN*0.5, scale=0.9),
            rate_func=ease_in_out_sine,
            run_time=1.5
        )
        
        self.wait(1)