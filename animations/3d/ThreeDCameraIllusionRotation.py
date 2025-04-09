from manim import *

class ThreeDCameraIllusionRotation(ThreeDScene):
    def construct(self):
        self.camera.background_color = "#fdf6e3"
        
        axes = ThreeDAxes().set_color(LOGO_BLACK)
        circle=Circle()
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        self.add(circle,axes)
        self.begin_3dillusion_camera_rotation(rate=2)
        self.wait(PI/2)
        self.begin_3dillusion_camera_rotation(rate=6)
        self.wait(PI/2)
        self.begin_3dillusion_camera_rotation(rate=2)
        self.stop_3dillusion_camera_rotation()
        self.play(Wait(5))