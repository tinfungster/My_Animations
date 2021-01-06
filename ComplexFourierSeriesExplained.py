# I am not a master at Manim, so my code is quite simple. In fact, I only
# started using Manim 2 weeks ago. My Complex Fourier Series video was the
# first video I made using Manim. I hope you enjoyed it!

# The other animations were either made by 3Blue1Brown or Theorem of Beethoven.

# The python files that were made by 3Blue1Brown are in:
# from_3b1b/active/diffyq/part4

# I mainly used the fourier_series_scenes.py and long_fourier_scenes.py.

# Theorem of Beethoven's code is in this website:
# https://pastebin.com/eeQ4mbLj

# This uses the newest version of Manim. If you use the Feb 3 version of
# Manim, change the manimlib.imports to big_ol_pile_of_manim_imports.

# I seperated all of the code from ComplexRotations.py from this file.
# This is becuase the code there is horribly messy and it would look less
# intimidating if I seperated it. Check lines number 356 - 381 to understand
# why I did that.

# All of my code is underneath this comment!

# Top Tip: check out the end of this file. I have a list of all the animations
# in this file over there!

from manimlib.imports import *
from My_Code.ComplexRotations import Complex_Rotations 

class Intro(Scene):
    def construct(self):
        text = TextMobject("How to Draw Images with Spinning Arrows and Circles!\\\\(Fourier Series)"
                           , run_time=10)
        self.play(text.set_color_by_gradient, GREEN_C, RED)
        self.wait(3)
        self.play(FadeOut(text), run_time=1.5)

class Agenda(Scene):
    def construct(self):
        text = TextMobject("1. What is Complex Fourier Series?")
        self.play(Write(text), run_time=5)
        self.wait(2)
        text2 = TextMobject("2. How to draw Images with\\\\Complex Fourier Series?")
        text2.next_to(text, DOWN)
        self.play(Write(text2), run_time=7)
        self.wait(15)
        self.play(FadeOut(text))
        self.play(FadeOut(text2))

class ComplexFourierSeries(Scene):
    # I surrounded the text with a yellow rectangle.

    def construct(self):
        text = TextMobject("Complex Fourier Series")
        text.scale(2)
        self.play(Write(text))
        self.wait(2)

        text2 = TextMobject("Complex")
        text2.scale(2)
        rect = SurroundingRectangle(text2)
        rect.set_stroke(YELLOW, 5)
        rect.to_edge(LEFT, buff=1.95)
        self.play(ShowCreation(rect))
        self.wait(20)
        self.play(FadeOut(rect))
        self.wait()

class ComplexNumbers101(Scene):
    def construct(self):
        text = TextMobject("Complex Numbers 101")
        text.scale(2)
        self.play(Write(text))
        self.wait()
        self.play(FadeOut(text))

class Complex_Numbers_Recap(Scene):
    def construct(self):
        plane = ComplexPlane()
        plane.add_coordinates()
        self.play(ShowCreation(plane), run_time=5)
        text = TextMobject("Complex Plane")
        text.to_corner(UL)
        self.play(Write(text))
        self.wait(2)
        self.play(FadeOut(text))

        # Rectangular form animations
        text2 = TextMobject("Rectangular Form")
        text2.to_corner(UL)
        self.play(Write(text2))

        y_line = Line(np.array([3, 0, 0]), np.array([3, 2, 0]))
        y_line.set_color(RED)

        point = Dot()

        self.play(point.move_to, np.array([3, 2, 0]))
        self.wait()
        x_line = Line(np.array([0, 0, 0]), np.array([3, 0, 0]))
        x_line.set_color(GREEN)
        self.play(ShowCreation(x_line), ShowCreation(y_line))
        x_brace = Brace(x_line, DOWN, buff=0.25)
        y_brace = Brace(y_line, RIGHT, buff=0.25)
        self.play(GrowFromCenter(x_brace), GrowFromCenter(y_brace), run_time=2)
        x_text = TexMobject("x")
        x_text.next_to(x_brace, DOWN)
        x_text.set_color(GREEN)
        y_text = TexMobject("y")
        y_text.next_to(y_brace, RIGHT)
        y_text.set_color(RED)
        self.play(FadeIn(x_text), FadeIn(y_text))
        complextext = TexMobject("x + y")
        complextext.next_to(point, RIGHT, buff=0.75)
        complextext2 = TexMobject("i").next_to(complextext, RIGHT, buff=0.05)
        self.play(Write(complextext))
        self.play(Write(complextext2))
        self.wait(3)
        self.play(FadeOut(x_text), FadeOut(y_text), FadeOut(x_brace), FadeOut(y_brace), FadeOut(x_line), FadeOut(y_line))
        self.wait()
        self.play(FadeOut(complextext), FadeOut(complextext2))

        # real_component
        real_component = DecimalNumber(
            0,
            num_decimal_places=2,
            include_sign=False,
            unit=None,
        )

        # imaginary_component
        imaginary_component = DecimalNumber(
            0,
            num_decimal_places=2,
            include_sign=True,
            unit=None,
        )

        imaginary_number = TexMobject("i").next_to(imaginary_component, RIGHT, buff=0.05)
        self.add(imaginary_number)

        # Updating the real component.
        real_component.add_updater(lambda r: r.next_to(point, RIGHT))
        real_component.add_updater(lambda r: r.set_value(point.get_center()[0]))

        # Updating the imaginary_component
        imaginary_component.add_updater(lambda i: i.next_to(real_component, RIGHT, buff=0.1))
        imaginary_component.add_updater(lambda i: i.set_value(point.get_center()[1]))

        # Updating the i next to the imaginary_component
        imaginary_number.add_updater(lambda i: i.next_to(imaginary_component, RIGHT, buff=0.05))

        self.add(real_component, imaginary_component, imaginary_number)

        # Moving the point around

        self.play(point.move_to, np.array([3, 2, 0]))
        self.wait()

        self.play(point.move_to, np.array([-3, 2, 0]))
        self.wait()

        self.play(point.move_to, np.array([-3, -2, 0]))
        self.wait()

        self.play(point.move_to, np.array([3, -2, 0]))
        self.wait()

        self.play(point.move_to, np.array([3, 2, 0]))
        self.wait()

        real_component.clear_updaters()
        imaginary_component.clear_updaters()
        imaginary_number.clear_updaters()
        self.play(FadeOut(real_component), FadeOut(imaginary_component), FadeOut(imaginary_number))

        self.play(FadeOut(point), FadeOut(text2))

        # Polar Form animations

        text3 = TextMobject("Polar Form")
        text3.to_corner(UL)
        self.play(Write(text3))
        self.wait()

        point2 = Dot()
        point2.move_to(np.array([3, 2, 0]))
        self.play(ShowCreation(point2))

        uselessline = Line(np.array([0, 0, 0]), np.array([math.sqrt(3 ** 2 + 2 ** 2), 0, 0]))
        origintopoint = Line(np.array([0, 0, 0]), np.array([3, 2, 0]))
        origintopoint.set_color(PINK)
        self.play(ShowCreation(origintopoint))

        r_brace = Brace(uselessline, UP, buff=0.01)
        r_brace.rotate(np.arctan(2/3))
        r_brace.shift(np.array([-0.45, 1.10, 0]))
        self.play(ShowCreation(r_brace))

        angle = np.arctan(2/3)
        arc =  Arc(radius=0.5,angle=angle)
        arc.set_color(YELLOW)
        self.play(ShowCreation(arc))

        distance = TexMobject("r")
        distance.move_to(np.array([1.2, 1.45, 0]))
        distance.set_color(PINK)
        theta = TexMobject("\\theta")
        theta.move_to(np.array([0.75, 0.25, 0]))
        theta.set_color(YELLOW)

        self.play(Write(distance), Write(theta))
        self.wait()
        self.play(ShowCreation(x_line), ShowCreation(y_line))
        self.wait()

        overlap_point = Dot()
        overlap_point.move_to(np.array([3, 2, 0]))
        self.add(overlap_point)

        self.play(GrowFromCenter(x_brace), GrowFromCenter(y_brace), run_time=2)
        self.wait()
        self.play(FadeIn(x_text), FadeIn(y_text))
        self.wait(3)

        x_text_2 = TexMobject("rcos(\\theta)")
        x_text_2.set_color(GREEN)
        x_text_2.next_to(x_brace, DOWN, buff=0)
        y_text_2 = TexMobject("rsin(\\theta)")
        y_text_2.set_color(RED)
        y_text_2.next_to(y_brace, RIGHT)

        self.play(Transform(x_text, x_text_2))
        self.wait(5)
        self.play(Transform(y_text, y_text_2))
        self.wait()

        complextext3 = TexMobject("rcos(\\theta) + rsin(\\theta)i")
        complextext3.move_to(np.array([5, 2.25, 0]))
        self.play(Write(complextext3))
        self.wait(3)

        complextext4 = TexMobject("r(cos(\\theta) + sin(\\theta)i)")
        complextext4.move_to(np.array([5, 2.25, 0]))
        self.play(Transform(complextext3, complextext4))

        self.play(text3.shift, 11 * RIGHT)
        self.wait()

        # THE MOST BEAUTIFUL EQUATION IN THE WORLD!!!

        Euler_Text = TextMobject("Euler's Formula")
        Euler_Text.move_to(np.array([-4.25, 3.325, 0]))
        EULERS_FORMULA = TexMobject("e^{i\\theta} = cos(\\theta) + sin(\\theta)i")
        EULERS_FORMULA.next_to(Euler_Text, DOWN)
        self.play(Write(Euler_Text))
        self.play(Write(EULERS_FORMULA))

        rect = SurroundingRectangle(EULERS_FORMULA)
        rect.set_stroke(YELLOW, 5)
        rect.to_edge(LEFT, buff=0.425)
        self.play(ShowCreation(rect))
        self.wait()

        Euler_Identities = TextMobject("Euler Identities")
        Euler_Identities.next_to(Euler_Text, DOWN, buff=1.35)
        self.play(Write(Euler_Identities))
        Euler_Identity_1 = TexMobject("e^{i\\tau} = 0")
        Euler_Identity_1.next_to(EULERS_FORMULA, DOWN, buff=1.05)
        self.play(Write(Euler_Identity_1))
        Euler_Identity_2 = TexMobject("e^{i\\pi} + 1 = 0")
        Euler_Identity_2.next_to(Euler_Identity_1, DOWN, buff=0.20)
        self.play(Write(Euler_Identity_2))
        self.wait()

        complextext5 = TexMobject("re^{i\\theta}")
        complextext5.move_to(np.array([3.6, 2.4, 0]))
        self.play(Transform(complextext3, complextext5))
        self.wait()

        rect2 = SurroundingRectangle(complextext3)
        rect2.set_stroke(YELLOW, 5)
        rect2.to_edge(RIGHT, buff=3.025)
        self.play(ShowCreation(rect2))
        self.wait(3)

        # Get rid of the surrounding rectangle.
        self.play(FadeOut(rect), FadeOut(rect2))

        complextext6 = TexMobject("3.61e^{33.69i}")
        complextext6.move_to(np.array([4, 2.4, 0]))
        self.play(Transform(complextext3, complextext6))
        self.wait(5)

        # Radians!
        complextext7 = TexMobject("3.61e^{0.59i}")
        complextext7.move_to(np.array([4, 2.4, 0]))
        self.play(Transform(complextext3, complextext7))
        self.wait(5)

        # Everything will disappear!
        self.play(FadeOut(complextext3), FadeOut(Euler_Text), FadeOut(EULERS_FORMULA), FadeOut(Euler_Identities), FadeOut(Euler_Identity_1), FadeOut(Euler_Identity_2), FadeOut(text3), FadeOut(x_brace), FadeOut(y_brace), FadeOut(r_brace), FadeOut(arc), FadeOut(origintopoint), FadeOut(x_line), FadeOut(y_line), FadeOut(point2), FadeOut(overlap_point), FadeOut(theta), FadeOut(distance), FadeOut(x_text), FadeOut(y_text))
        self.wait()

class FewThingsToSay(Scene):
    def construct(self):
        plane = ComplexPlane()
        self.add(plane)
        plane.add_coordinates()

        point = Dot()
        self.play(ShowCreation(point))
        self.wait()
        self.play(point.shift, np.array([3, 2, 0]))
        self.play(point.shift, np.array([-6, 0, 0]))
        self.play(point.shift, np.array([0, -4, 0]))
        self.play(point.shift, np.array([6, 0, 0]))
        self.play(point.shift, np.array([0, 4, 0]))
        self.wait()

        cross = Cross(point, stroke_color = RED, stroke_width = 3)
        self.play(ShowCreation(cross))
        self.wait(3)

        vector = Vector(3 * RIGHT + 2 * UP)
        vector.set_color(BLUE_B)
        self.play(FadeOut(cross), FadeOut(point), GrowFromCenter(vector))
        self.wait(3)
        self.play(FadeOut(vector))

        vector2 = Vector(3 * RIGHT)
        vector2.set_color(BLUE_B)

        point.move_to(np.array([3, 0, 0]))
        self.add(point)

        circle = Circle()
        circle.set_color(TEAL)
        circle.scale(3)

        self.play(Rotating(point, radians=TAU, about_point=ORIGIN), run_time=5)
        self.wait()
        self.play(FadeOut(point))

        self.play(ShowCreation(vector2))
        self.wait()

        self.play(Rotating(vector2, radians=TAU, about_point=ORIGIN), run_time=5)
        self.play(FadeIn(circle))
        self.play(Rotating(vector2, radians=TAU, about_point=ORIGIN), run_time=5)
        self.wait()
        self.play(FadeOut(vector2), FadeOut(circle))
        self.wait()

class Learn_Complex_Rotations(Complex_Rotations):
    # Here are the parameters that you can tweak. Sort of.

    # The code in the ComplexRotations.py file is not fully
    # autonomous which means it does not automatically update
    # everything in this scene after changing the CONFIG parameters.
    # It automatically updates the rotating_speed and size parameters
    # , but not the angle. You need to manually change the code in
    # the ComplexRotations.py file.

    # The code over there had "some" (a lot, seriously) problems and bugs.
    # I could have analysed 3Blue1Brown's code that he used in staging.py,
    # but there was over a thousand lines of code and I barely understood
    # 2 % of his code, so I resorted to the easy way (Grant Sanderson's
    # code is definitely better than mine.) :

    # I calculated the time by calculating the angle.
    # time = distance / speed. distance is the angle and speed is seconds
    # per revolution.
    # I calculated the angle by using arctan because arcsin and arccos did
    # not work.

    # However, arctan has a range (not domain) between tau/4 and -tau/4
    # which caused a lot of problems. I wanted to fix the problems by using
    # a while loop, but that did not work, by that I mean, it failed horribly.
    # I had no choice but to copy and paste the code for every tau/4 rotations
    # which was a nightmare.

    CONFIG = {
        # The angle will be in radians. This angle is how much you want the
        # vector (arrow) to rotate.
        "angle": np.array([TAU / 4]),

        # Seconds per revolution. I will use this for the run_time for the
        # animation.
        "rotating_speed": np.array([TAU]),

        # This is the size of the circles and arrows based on the scaled up
        # Complex Plane.
        "size": np.array([1]),
    }
