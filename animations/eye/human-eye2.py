from manim import *

class HumanEyeAnatomy(Scene):
    def construct(self):
        # Set Solarized Light background
        self.camera.background_color = "#FDF6E3"
        
        # Create a group to hold all elements
        eye_group = VGroup()
        
        # Create the basic eye structure
        eye_center = ORIGIN
        eye_radius = 2.5
        
        eye_outline = Circle(radius=eye_radius, color="#073642").move_to(eye_center)
        
        # Define positions relative to eye center
        front_of_eye = eye_center + LEFT * eye_radius * 0.7
        back_of_eye = eye_center + RIGHT * eye_radius * 0.7
        
        # Inner structures
        iris = Circle(radius=0.8, color="#268BD2", fill_opacity=0.2).move_to(front_of_eye)
        cornea = Arc(radius=1.1, angle=PI/2, color="#839496", stroke_width=3).rotate(PI).move_to(front_of_eye + UP * 0.2)
        lens = Ellipse(width=0.6, height=1.0, color="#832496", fill_opacity=0.3).move_to(front_of_eye + RIGHT * 0.5)
        retina = Arc(radius=eye_radius-0.2, angle=TAU * 0.7, color="#B58900", fill_opacity=0.1).move_to(eye_center).shift(RIGHT * 0.2)
        optic_nerve = Rectangle(height=0.7, width=1.5, color="#D33682", fill_opacity=0.7).move_to(eye_center + RIGHT * eye_radius + RIGHT * 0.2)
        
        # Add eye parts to the group
        eye_parts = VGroup(eye_outline, retina, lens, iris, cornea, optic_nerve)
        eye_group.add(eye_parts)
        
        # Center the entire eye structure
        eye_group.move_to(ORIGIN)
        
        # Labels
        labels = VGroup()
        
        def create_label(text, target, direction, offset=ORIGIN, line_offset=ORIGIN):
            label = Text(text, font_size=20, color="#586E75")
            label.next_to(target, direction, buff=0.7)
            label.shift(offset)
            
            line_start = label.get_edge_center(DOWN) if UP in direction else label.get_edge_center(UP)
            line_end = target.get_center() + line_offset
            
            line = Line(line_start, line_end, buff=0.1, color="#073642")
            return VGroup(label, line)
        
        # Create labels for the selected parts
        cornea_label = create_label("Cornea", cornea, UP+LEFT, UP*0.3+LEFT*0.5, UP*0.2)
        iris_label = create_label("Iris", iris, LEFT, LEFT*0.5, UP*0.2)
        lens_label = create_label("Lens", lens, DOWN, DOWN*0.5)
        retina_label = create_label("Retina", retina, UP+RIGHT, UP*0.5+RIGHT*0.5, UP*0.4+RIGHT*0.3)
        optic_nerve_label = create_label("Optic nerve", optic_nerve, UP, UP*0.3+RIGHT*0.5)
        
        labels.add(cornea_label, iris_label, lens_label, retina_label, optic_nerve_label)
        
        # Animation sequence
        self.play(Create(eye_outline))
        self.wait(0.3)
        
        self.play(FadeIn(retina))
        self.play(Write(retina_label))
        self.wait(0.3)
        
        self.play(FadeIn(lens))
        self.play(Write(lens_label))
        self.wait(0.3)
        
        self.play(FadeIn(iris))
        self.play(Write(iris_label))
        self.wait(0.3)
        
        self.play(Create(cornea))
        self.play(Write(cornea_label))
        self.wait(0.3)
        
        self.play(FadeIn(optic_nerve))
        self.play(Write(optic_nerve_label))
        self.wait(0.3)
        
        self.wait(1)
        
        # Highlight animation
        highlight = Circle(radius=0.5, color="#CB4B16", stroke_width=5, fill_opacity=0)
        
        highlight_points = {
            "Cornea": cornea.get_center() + UP * 0.1,
            "Iris": iris.get_center(),
            "Lens": lens.get_center(),
            "Retina": retina.get_center() + UP * 0.7,
            "Optic nerve": optic_nerve.get_center()
        }
        
        label_dict = {label_group[0].get_text(): label_group[0] for label_group in labels}
        
        for name, point in highlight_points.items():
            self.play(highlight.animate.move_to(point), run_time=0.5)
            if name in label_dict:
                self.play(label_dict[name].animate.set_color("#CB4B16"), run_time=0.3)
                self.wait(0.5)
                self.play(label_dict[name].animate.set_color("#586E75"), run_time=0.3)
        
        self.play(FadeOut(highlight))
        
        final_text = Text("Understanding the Human Eye", font_size=36, color="#586E75")
        final_text.to_edge(DOWN)
        self.play(Write(final_text))
        
        self.wait(2)
        
        all_objects = VGroup(eye_group, labels, final_text)
        
