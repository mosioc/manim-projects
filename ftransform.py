from manim import *
import numpy as np
from scipy.fft import fft

class AdvancedFourierTransform3D(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=30 * DEGREES)

        # تعریف سیگنال ترکیبی
        t_vals = np.linspace(0, 4 * np.pi, 200)
        signal = 0.5 * np.sin(t_vals) + 0.3 * np.sin(2 * t_vals) + 0.1 * np.sin(3 * t_vals)

        # محاسبه تبدیل فوریه
        freq_data = np.abs(fft(signal))
        amplitudes = freq_data[:len(freq_data) // 2] / len(signal)  # نرمال‌سازی دامنه

        # ایجاد محورهای سه‌بعدی
        axes = ThreeDAxes(
            x_range=[0, 4 * np.pi, np.pi],
            y_range=[-1.5, 1.5, 0.5],
            z_range=[0, 5, 1],
            axis_config={"color": BLUE},
        ).add_coordinates()

        # نمایش سیگنال زمانی
        time_signal = ParametricFunction(
            lambda t: [t, signal[min(int(t / (4 * np.pi) * len(signal)), len(signal) - 1)], 0],
            t_range=[0, 4 * np.pi],
            color=RED
        )

        # نمایش مؤلفه‌های فرکانسی
        freq_components = []
        for i in range(1, min(len(amplitudes), 4)):  # حداکثر 3 مؤلفه اصلی فرکانس
            amplitude = amplitudes[i]
            freq_component = ParametricFunction(
                lambda t, n=i, amp=amplitude: [t, amp * np.sin(n * t), n],
                t_range=[0, 4 * np.pi],
                color=[PURPLE, PINK, YELLOW][i-1]
            )
            freq_components.append(freq_component)

        # نمایش طیف فرکانس
        frequency_spectrum = VGroup()
        bar_width = 0.1
        for i, amp in enumerate(amplitudes[:20]):
            bar = Rectangle(
                width=bar_width,
                height=amp * 2,
                fill_color=BLUE,
                fill_opacity=0.7,
                stroke_width=0
            ).move_to([i * bar_width * 1.5, 0, 4])
            frequency_spectrum.add(bar)


        # انیمیشن‌ها
        self.play(Create(axes))
        self.play(Create(time_signal), run_time=2)
        self.play(Create(frequency_spectrum), run_time=2)
        self.wait(1)

        # ایجاد انیمیشن برای مؤلفه‌های فرکانسی
        self.play(AnimationGroup(*[Create(component) for component in freq_components]), run_time=3)


        # بازسازی سیگنال از مؤلفه‌های فرکانسی
        combined_signal = ParametricFunction(
            lambda t: [t, sum(amp * np.sin(n * t) for n, amp in enumerate(amplitudes[1:4], 1)), 0],
            t_range=[0, 4 * np.pi],
            color=GREEN
        )
        self.play(Transform(time_signal, combined_signal), run_time=2)

        # چرخش دوربین
        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait(5)

if __name__ == "__main__":
    scene = AdvancedFourierTransform3D()
    scene.render()
