from manim import *

class LightAndVisionAnimation(Scene):
    def construct(self):
        # Set up the scene
        self.camera.background_color = "#1C1C1C"
        
        # Title
        title = Text("How Light Enters the Human Eye", font_size=40)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # Create a light source (sun)
        sun = Circle(radius=0.8, fill_opacity=1, color=YELLOW)
        sun.move_to([-5, 2, 0])
        
        # Add rays emanating from sun
        rays = VGroup()
        for angle in np.linspace(-PI/6, -PI/12, 8):
            ray = Line(
                sun.get_center(),
                sun.get_center() + 10 * np.array([np.cos(angle), np.sin(angle), 0]),
                stroke_width=2,
                color=YELLOW
            )
            rays.add(ray)
        
        # Create an object (tree)
        trunk = Rectangle(height=2, width=0.5, fill_opacity=1, color=DARK_BROWN)
        trunk.move_to([0, -1.5, 0])
        
        foliage = Circle(radius=1.2, fill_opacity=1, color=GREEN)
        foliage.move_to([0, 0.5, 0])
        
        tree = VGroup(trunk, foliage)
        
        # Create the eye
        eye_outline = Circle(radius=1.4, color=WHITE)
        eye_outline.move_to([5, 0, 0])
        
        # Create the cornea
        cornea = Arc(
            radius=1.4,
            angle=PI/2,
            start_angle=PI/4,
            color=BLUE_A,
            stroke_width=3
        )
        cornea.move_to(eye_outline.get_center())
        
        # Create the iris and pupil
        iris = Circle(radius=0.6, color=BLUE, fill_opacity=0.8)
        iris.move_to(eye_outline.get_center())
        
        pupil = Circle(radius=0.25, color=BLACK, fill_opacity=1)
        pupil.move_to(eye_outline.get_center())
        
        # Create the lens
        lens = Ellipse(width=0.5, height=0.8, fill_opacity=0.5, color=BLUE_A)
        lens.move_to(eye_outline.get_center())
        
        # Create the retina
        retina = Arc(
            radius=1.3,
            angle=PI,
            start_angle=PI,
            color=RED_A,
            stroke_width=5
        )
        retina.move_to(eye_outline.get_center())
        
        # Create the optic nerve
        optic_nerve = Line(
            eye_outline.get_center() + np.array([-1.2, -0.4, 0]),
            eye_outline.get_center() + np.array([-2.5, -1.2, 0]),
            stroke_width=10,
            color=WHITE
        )
        
        brain = SVGMobject("brain", height=1.5)
        brain.move_to(optic_nerve.get_end() + np.array([-1.5, 0, 0]))
        
        # Group all eye parts
        eye_parts = VGroup(eye_outline, cornea, iris, pupil, lens, retina, optic_nerve)
        
        # Labels
        cornea_label = Text("Cornea", font_size=20, color=BLUE_A)
        cornea_label.next_to(cornea, UP, buff=0.5)
        
        iris_label = Text("Iris", font_size=20, color=BLUE)
        iris_label.next_to(iris, UR, buff=0.7)
        
        pupil_label = Text("Pupil", font_size=20)
        pupil_label.next_to(pupil, RIGHT, buff=0.7)
        
        lens_label = Text("Lens", font_size=20, color=BLUE_A)
        lens_label.next_to(lens, DOWN, buff=0.5)
        
        retina_label = Text("Retina", font_size=20, color=RED_A)
        retina_label.next_to(retina, LEFT, buff=0.5)
        
        optic_nerve_label = Text("Optic Nerve", font_size=20)
        optic_nerve_label.next_to(optic_nerve, DOWN, buff=0.5)
        
        brain_label = Text("Brain", font_size=20)
        brain_label.next_to(brain, DOWN, buff=0.5)
        
        # Reflected light rays from object to eye
        reflected_rays = VGroup()
        start_points = [
            foliage.get_top(),
            foliage.get_center(),
            foliage.get_bottom(),
            trunk.get_top(),
            trunk.get_center()
        ]
        
        for point in start_points:
            ray = Line(
                point,
                pupil.get_center(),
                stroke_width=2,
                color=YELLOW
            )
            reflected_rays.add(ray)
        
        # Rays focusing inside eye
        focused_rays = VGroup()
        for ray in reflected_rays:
            # Create a path that bends at the lens and focuses on the retina
            start = pupil.get_center()
            end = eye_outline.get_center() + np.array([-1.2, (np.random.random() - 0.5) * 0.8, 0])
            
            focused_ray = ArcBetweenPoints(
                start,
                end,
                angle=-PI/8,
                color=YELLOW
            )
            focused_rays.add(focused_ray)
        
        # Neural signals to brain
        neural_signals = VGroup()
        for i in range(5):
            point = eye_outline.get_center() + np.array([-1.2, (np.random.random() - 0.5) * 0.8, 0])
            
            path = CubicBezier(
                point,
                point + np.array([-0.5, -0.2, 0]),
                optic_nerve.get_end() + np.array([0.3, 0.3, 0]),
                optic_nerve.get_end()
            )
            
            neural_signals.add(
                DashedVMobject(path, num_dashes=20, color=WHITE)
            )
        
        # Begin animation
        self.play(
            Create(sun),
            Write(Text("Light Source", font_size=24).next_to(sun, UP))
        )
        self.play(Create(rays))
        self.wait(1)
        
        self.play(
            FadeIn(tree),
            Write(Text("Object", font_size=24).next_to(tree, UP))
        )
        self.wait(1)
        
        # Explanation text
        explanation1 = Text("1. Light rays from the sun reach objects in our environment", 
                          font_size=24)
        explanation1.to_edge(DOWN, buff=0.5)
        self.play(Write(explanation1))
        self.wait(2)
        
        # Show reflection
        self.play(FadeOut(explanation1))
        explanation2 = Text("2. Objects reflect some light toward our eyes", 
                          font_size=24)
        explanation2.to_edge(DOWN, buff=0.5)
        self.play(Write(explanation2))
        self.play(Create(reflected_rays))
        self.wait(2)
        
        # Create the eye structure
        self.play(FadeOut(explanation2))
        explanation3 = Text("3. Light enters the eye through the cornea and pupil", 
                          font_size=24)
        explanation3.to_edge(DOWN, buff=0.5)
        self.play(
            Create(eye_outline),
            Write(Text("Human Eye", font_size=24).next_to(eye_outline, UP))
        )
        self.play(
            Create(cornea),
            Create(iris),
            Create(pupil),
            Write(explanation3)
        )
        self.play(
            Write(cornea_label),
            Write(iris_label),
            Write(pupil_label)
        )
        self.wait(2)
        
        # Show lens focusing light
        self.play(FadeOut(explanation3))
        explanation4 = Text("4. The lens focuses the light rays onto the retina", 
                          font_size=24)
        explanation4.to_edge(DOWN, buff=0.5)
        self.play(
            Create(lens),
            Write(lens_label),
            Write(explanation4)
        )
        self.wait(1)
        
        self.play(
            Create(retina),
            Write(retina_label)
        )
        self.play(Create(focused_rays))
        self.wait(2)
        
        # Show optic nerve and brain processing
        self.play(FadeOut(explanation4))
        explanation5 = Text("5. The retina converts light to neural signals sent to the brain", 
                          font_size=24)
        explanation5.to_edge(DOWN, buff=0.5)
        self.play(
            Create(optic_nerve),
            Write(optic_nerve_label),
            Write(explanation5)
        )
        self.wait(1)
        
        self.play(
            FadeIn(brain),
            Write(brain_label)
        )
        self.play(Create(neural_signals))
        self.wait(2)
        
        # Final explanation
        self.play(FadeOut(explanation5))
        explanation6 = Text("6. The brain interprets these signals as images", 
                          font_size=24)
        explanation6.to_edge(DOWN, buff=0.5)
        self.play(Write(explanation6))
        self.wait(1)
        
        # Add a thought bubble with the tree image
        thought = ThoughtBubble(height=2, width=3)
        thought.move_to(brain.get_center() + np.array([1.5, 1.5, 0]))
        
        small_tree = tree.copy().scale(0.3)
        small_tree.move_to(thought.get_bubble_center())
        
        self.play(
            Create(thought),
            FadeIn(small_tree)
        )
        self.wait(2)
        
        # Conclusion
        self.play(
            FadeOut(explanation6),
            FadeOut(title)
        )
        
        conclusion = Text(
            "Vision is a complex process that converts light into neural signals\n"
            "that our brain can interpret as the world around us.",
            font_size=32,
            line_spacing=1.5
        )
        conclusion.to_edge(DOWN, buff=1)
        self.play(Write(conclusion))
        self.wait(3)
        
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )