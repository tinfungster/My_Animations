# There is a reason I seperated all of this code from the
# ComplexFourierSeriesExplained.py file. The code here is
# horribly messy and it would look less intimidating 

from manimlib.imports import *

class Complex_Rotations(Scene):
    def construct(self):

        # Setting up the parameters
        angle = self.angle
        rotating_speed = self.rotating_speed
        size = self.size

        # Animations
        plane = ComplexPlane()
        plane.scale(2.5)
        self.add(plane)
        plane.add_coordinates()
        self.wait()

        # 0 indexed.
        circle = Circle()
        circle.set_color(TEAL)
        circle.scale(2.5 * size[0])

        vector = Vector(2.5 * size[0] * RIGHT)
        vector.set_color(BLUE)

        self.play(ShowCreation(circle))
        self.wait()
        self.play(ShowCreation(vector))
        self.wait()

        invisiblepoint = Dot()
        invisiblepoint.scale(0.01)
        invisiblepoint.move_to(np.array([2.95, 0, 0]))
        self.add(invisiblepoint)

        # Label
        label = TexMobject("e^{it}")
        self.play(Write(label))
        label.scale(2)
        label[2].set_color(BLUE_B)
        label.to_corner(UP + LEFT)

        # t (time) is based on how big the angle is. It is how much the
        # angle increases divided by rotating speed

        # We will use arctan to calculate the angle.

        # Since arctan has a range between TAU/4 and  -TAU/4, we will
        # make several time variables.

        text = TexMobject("e^{i}")
        text.scale(1.5)
        text.move_to(np.array([invisiblepoint.get_center()[0], invisiblepoint.get_center()[1], 0]))

        time_1 = DecimalNumber(
            0,
            num_decimal_places=2,
            include_sign=False,
            unit=None,
        )

        time_1.set_color(BLUE_B)

        text.add_updater(lambda t: t.move_to(np.array([invisiblepoint.get_center()[0], invisiblepoint.get_center()[1], 0])))
        time_1.add_updater(lambda t: t.set_value(float(abs(np.arctan(vector.get_center()[1] / vector.get_center()[0])))))
        time_1.add_updater(lambda t: t.move_to(np.array([invisiblepoint.get_center()[0] + 0.75, invisiblepoint.get_center()[1] + 0.175, 0])))

        self.add(text, time_1)

        self.play(Rotating(vector, radians=TAU / 4, about_point=ORIGIN), Rotating(invisiblepoint, radians=TAU / 4, about_point=ORIGIN), run_time=rotating_speed[0] / 4)

        self.wait()
