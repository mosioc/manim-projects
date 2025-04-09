from manim import *


class SquareFunction(Scene):
    def construct(self):

        self.camera.background_color = "#fdf6e3"  # Solarized Light background

        axes = Axes(
            x_range=[-5, 5.1, 1],
            y_range=[-1.5, 1.5, 1],
            x_length=2 * TAU,
            axis_config={"color": GREEN},
            tips=False,
        )

        def squareWave(x):
            if int(x) % 2 == 0:
                return 1 * x // abs(x)
            else:
                return -1 * x // abs(x)

        def Sinn(x, n):
            result = 0
            for i in range(1, n + 1, 2):
                result += (2 / (i * np.pi)) * (2) * np.sin(i * x * np.pi)
            return result

        def SINN(x, i):
            return (2 / (i * np.pi)) * (2) * np.sin(i * x * np.pi)

        # Change the color of the square wave to RED
        square_graph = axes.plot(
            squareWave,
            x_range=(-4.9, 4.9, 0.01),
            color=RED,
            **{"discontinuities": [x for x in range(-5, 6)]},
        )

        values = [0]
        values1 = [0]
        index = 1
        for i in range(1, 31, 2):
            # Change the color of the intermediate waves to DARK_BROWN
            values.append(
                axes.plot(
                    lambda x: SINN(x, i), x_range=(-4.9, 4.9, 0.1), color=DARK_BROWN
                )
            )
            values1.append(
                axes.plot(lambda x: Sinn(x, i), x_range=(-4.9, 4.9, 0.1), color=BLUE)
            )
        self.play(FadeIn(axes), FadeIn(square_graph), FadeIn(values[1]))
        self.play(ReplacementTransform(values[1], values1[1]))
        for i in range(2, 15):
            self.play(Create(values[i]))
            self.wait(1)
            self.play(
                ReplacementTransform(values[i], values1[i]),
                ReplacementTransform(values1[i - 1], values1[i]),
            )
