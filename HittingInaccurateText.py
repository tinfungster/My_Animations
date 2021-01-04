# How to Hit Inaccurate Text with a Vector (Arrow) !

from manimlib.imports import *

class HittingInaccurateText(Scene):
    def construct(self):
        vector = Vector(3 * RIGHT)
        runtime = 5
        parts = 300
        part = 0

        theta = 0

        while part <= parts:
            self.play(Rotating(vector, radians=TAU/parts, about_point=ORIGIN), run_time=5/300)
            text = TexMobject("e^{i" + str(theta) + "}")
            text.add_updater(lambda t: t.next_to(vector, RIGHT, buff=0.05))
            self.add(text)
            part += 1

        self.wait()

# This is a failed attempt of code for rotating circles and arrows for my Fourier Series Explanation video.
