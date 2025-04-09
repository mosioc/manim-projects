from manim import *

class ThreeDCameraRotation(ThreeDScene):
    def construct(self):

        self.camera.background_color = "#fdf6e3"

        axes = ThreeDAxes().set_color(LOGO_BLACK)
        circle=Circle()
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        self.play(Create(circle), Create(axes))
        self.begin_ambient_camera_rotation(rate=0.1)
        self.wait()
        self.begin_ambient_camera_rotation(rate=0.8)
        self.wait()
        self.begin_ambient_camera_rotation(rate=0.5)
        self.wait()
        self.begin_ambient_camera_rotation(rate=0.8)
        self.stop_ambient_camera_rotation()
        self.move_camera(phi=75 * DEGREES, theta=30 * DEGREES)
        self.play(Wait(5))