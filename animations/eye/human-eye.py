from manim import *

class DetailedEyeAnatomy3D(ThreeDScene):
    def construct(self):
        # Set the background color to Solarized Light (#FDF6E3)
        self.camera.background_color = "#fdf6e3"

        # Set up the camera for 3D, initially facing the eye directly at eye level
        self.set_camera_orientation(phi=0 * DEGREES, theta=0 * DEGREES)  # Straight-on view, facing forward

        # Create the eyeball (white sclera) - a large sphere
        eyeball = Sphere(radius=1.5, resolution=(20, 20))
        eyeball.set_color(WHITE)
        eyeball.shift(OUT * 0.5)  # Move slightly forward for better visibility

        # Create the cornea (transparent layer over the iris) - a thin, transparent sphere
        cornea = Sphere(radius=1.6, resolution=(20, 20))
        cornea.set_color([255, 255, 255, 77])  # White with 30% opacity
        cornea.shift(OUT * 0.5)  # Position slightly in front of the eyeball

        # Create the iris (blue) - a smaller circle in front, facing the viewer
        iris = Circle(radius=0.6, color=BLUE, fill_opacity=1)
        iris.shift(OUT * 1.6)  # Position in front of the eyeball

        # Create the pupil (black) - a smaller circle inside the iris
        pupil = Circle(radius=0.2, color=BLACK, fill_opacity=1)
        pupil.move_to(iris.get_center())  # Center the pupil in the iris

        # Create the lens (simplified as a smaller transparent sphere behind the iris)
        lens = Sphere(radius=0.5, resolution=(20, 20))
        lens.set_color([128, 128, 128, 128])  # Gray with 50% opacity
        lens.shift(OUT * 1.0)  # Position behind the iris, inside the eyeball

        # Create the retina (inner layer with blood vessels) - a partial sphere
        retina = Sphere(radius=1.4, resolution=(20, 20))
        retina.set_color(RED_B)
        retina.shift(IN * 0.1)  # Position slightly inside the eyeball
        # Cut out the front part to simulate the opening for the iris
        retina = Intersection(retina, Cube(side_length=3).shift(IN * 1.5))

        # Create the optic nerve (simplified as a cylinder extending from the back of the eyeball)
        optic_nerve = Cylinder(radius=0.2, height=1.0, resolution=(20, 20))
        optic_nerve.set_color(YELLOW)
        optic_nerve.rotate(90 * DEGREES, axis=RIGHT)  # Orient vertically
        optic_nerve.shift(IN * 1.8 + DOWN * 0.5)  # Position at the back of the eyeball, slightly downward

        # Combine all eye parts
        eye = VGroup(eyeball, cornea, iris, pupil, lens, retina, optic_nerve)

        # Add detailed labels for each part (horizontal alignment)
        cornea_label = Text("Cornea", color=WHITE).next_to(cornea, RIGHT, buff=0.5)  # Horizontal (to the right)
        iris_label = Text("Iris", color=BLUE).next_to(iris, RIGHT, buff=0.5)  # Horizontal (to the right)
        lens_label = Text("Lens", color=GRAY).next_to(lens, RIGHT, buff=0.5)  # Horizontal (to the right)
        retina_label = Text("Retina", color=RED_B).next_to(retina, RIGHT, buff=0.5)  # Horizontal (to the right)
        optic_nerve_label = Text("Optic Nerve", color=YELLOW).next_to(optic_nerve, RIGHT, buff=0.5)  # Horizontal (to the right)

        # Add arrows to point labels to their corresponding parts
        cornea_arrow = Arrow(start=cornea_label.get_right(), end=cornea.get_center(), color=WHITE)
        iris_arrow = Arrow(start=iris_label.get_right(), end=iris.get_center(), color=BLUE)
        lens_arrow = Arrow(start=lens_label.get_right(), end=lens.get_center(), color=GRAY)
        retina_arrow = Arrow(start=retina_label.get_right(), end=retina.get_center(), color=RED_B)
        optic_nerve_arrow = Arrow(start=optic_nerve_label.get_right(), end=optic_nerve.get_center(), color=YELLOW)

        # Combine labels and arrows into groups for easier animation
        cornea_group = VGroup(cornea_label, cornea_arrow)
        iris_group = VGroup(iris_label, iris_arrow)
        lens_group = VGroup(lens_label, lens_arrow)
        retina_group = VGroup(retina_label, retina_arrow)
        optic_nerve_group = VGroup(optic_nerve_label, optic_nerve_arrow)

        # Animate the scene (create the eye and labels with arrows)
        self.play(Create(eyeball), run_time=2)
        self.play(Create(retina), Create(optic_nerve), run_time=2)
        self.play(Create(cornea), Create(iris), Create(pupil), Create(lens), run_time=2)
        self.play(
            FadeIn(cornea_group, iris_group, lens_group, retina_group, optic_nerve_group),
            run_time=1,
        )

        # Rotate the eye downward (around X-axis) by a smaller angle
        self.play(
            Rotate(eye, angle=TAU / 10, axis=X_AXIS),  # Rotate less than 36 degrees downward around X
            run_time=4,
        )  # Smooth rotation over 4 seconds

        # Stop at an isometric view facing directly toward the viewer
        self.move_camera(phi=35.264 * DEGREES, theta=0 * DEGREES)  # Isometric view, front-facing toward the viewer
        self.wait(2)  # Pause to show the isometric view

        # Ensure labels and arrows follow the eye during rotation (using always for dynamic positioning)
        cornea_group.add_updater(lambda m: m.next_to(eye, RIGHT, buff=0.5).shift(UP * 0.5))
        iris_group.add_updater(lambda m: m.next_to(eye, RIGHT, buff=0.5).shift(DOWN * 0.2))
        lens_group.add_updater(lambda m: m.next_to(eye, RIGHT, buff=0.5).shift(LEFT * 0.3))
        retina_group.add_updater(lambda m: m.next_to(eye, RIGHT, buff=0.5).shift(RIGHT * 0.3))
        optic_nerve_group.add_updater(lambda m: m.next_to(eye, RIGHT, buff=0.5).shift(DOWN * 0.7))

        self.wait(2)  # Additional pause to show updated labels

if __name__ == "__main__":
    scene = DetailedEyeAnatomy3D()
    scene.render()