from manim import *

class EscherInspiredScene(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        
        # Set background color to Solarized Light
        self.camera.background_color = "#fdf6e3"
        self.renderer.background_color = "#fdf6e3"
        
        
        # Create multiple concentric spheres
        spheres = VGroup(*[Sphere(radius=r, color="#073642", fill_opacity=0.05)
                           for r in [1, 1.5, 2, 2.5, 3]])
        
        # Create intersecting circular arcs
        arcs = VGroup(*[Circle(radius=2.5, stroke_width=2, stroke_color="#073642", stroke_opacity=0.6).rotate(angle, axis=axis)
                        for angle, axis in [(PI/2, RIGHT), (PI/2, UP), (PI/4, OUT)]])
        
        # Create a tetrahedral framework
        tetrahedron = VGroup()
        edges = [(0,1), (1,2), (2,0), (0,3), (1,3), (2,3)]
        vertices = [np.array(v) for v in [(1,1,1), (-1,-1,1), (-1,1,-1), (1,-1,-1)]]
        for edge in edges:
            tetrahedron.add(Line(vertices[edge[0]], vertices[edge[1]], color="#073642", stroke_width=2))
        
        # Animation
        self.add(spheres, arcs, tetrahedron)
        self.play(Rotate(spheres, angle=PI, axis=UP, run_time=4),
                  Rotate(arcs, angle=PI, axis=RIGHT, run_time=4),
                  Rotate(tetrahedron, angle=PI, axis=OUT, run_time=4))
        self.wait(2)
