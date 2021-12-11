from manim import *

class Ejemplo1(Scene):
    def construct(self):
        circle=Circle()
        square=Square()
        self.add(circle)
        self.wait(0.1)
        self.remove(circle)
        self.add(square)
        self.wait(0.1)

class Ejemplo2(Scene):
    def construct(self):
        square=Square()
        triangle=Triangle()
        circle=Circle()
        square.shift(UP)
        triangle.shift(RIGHT)
        circle.shift(LEFT)
        self.add(square,circle,triangle)

        self.add(square)

class Ejemplo3(Scene):
    def construct(self):
        circle=Circle()
        square=Square()
        triangle=Triangle()

        circle.shift(LEFT*2)
        square.next_to(circle,LEFT)
        triangle.align_to(circle,LEFT)
        self.add(circle,square,triangle)

class Ejemplo4(Scene):
    def construct(self):
        triangle = Triangle()
        circle=Circle()
        square=Square()

        square.shift(UP).set_fill(YELLOW, opacity=1.0)
        circle.shift(LEFT).set_stroke(color=GREEN, width=20)
        triangle.shift(RIGHT).set_fill(color=RED, opacity=0.5)

        self.add(circle,square,triangle)

class Ejemplo5(Scene):
    def construct(self):
        square=Square()
        self.play(FadeIn(square))
        self.play(Rotate(square,PI/4))

class Ejemplo6(Scene):
    def construct(self):
        square=Square()
        square.set_fill(RED, opacity=1.0)
        self.add(square)
        self.play(square.animate.set_fill(WHITE, opacity=1.0))
        self.wait(1)
        self.play(square.animate.rotate(PI/4).shift(UP))
        self.wait(1)

class Count(Animation):
    def __init__(self, number: DecimalNumber, start: float, end: float, **kwargs) -> None:
        super().__init__(number,**kwargs)
        self.start=start
        self.end=end
    
    def interpolate_mobject(self, alpha: float) -> None:
        value=self.start+(alpha * (self.end-self.start))
        self.mobject.set_value(value)

class Ejemplo7(Scene):
    def construct(self):
        number=DecimalNumber().set_color(WHITE).scale(5)
        number.add_updater(lambda number: number.move_to(ORIGIN))
        self.add(number)
        self.wait()

        self.play(Count(number, 0, 100), run_time=4, rate_func=linear)
        self.wait()



