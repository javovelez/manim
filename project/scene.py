from manim import *
class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()                    # create a circle
        circle.set_fill(PINK, opacity=0.5)   # set color and transparency

        square = Square()                    # create a square
        square.flip(RIGHT)                   # flip horizontally
        square.rotate(-3 * TAU / 8)          # rotate a certain amount

        self.play(Create(square))      # animate the creation of the square
        self.play(Transform(square, circle)) # interpolate the square into the circle
        self.play(FadeOut(square))           # fade out animation

class CreatingMobjects(Scene):
    def construct(self):
        circle = Circle()
        self.add(circle)
        self.wait(1)
        self.remove(circle)
        self.wait(1)

class Shapes(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        triangle = Triangle()

        circle.shift(LEFT)
        square.shift(UP)
        triangle.shift(RIGHT)

        self.add(circle, square, triangle)
        self.wait(1)

class MobjectPlacement(Scene):
    def construct(self):
        circle = Circle()
        square = Square() # podríamos haber ejecutado square.shift(LEFT) por ejemplo
        triangle = Triangle()

        # Coloca el círculo dos unidades a la izquierda del origen
        circle.move_to(LEFT * 2)
        # Coloca el cuadrado a la izquierda del círculo
        square.next_to(circle, LEFT)
        # Alinea el borde izquierdo del triángulo con el borde izquierdo del círculo
        triangle.align_to(circle, LEFT)

        self.add(circle, square, triangle)
        self.wait(1)

class MobjectStyling(Scene):
    def construct(self):
        circle = Circle().shift(LEFT)
        square = Square().shift(UP)
        triangle = Triangle().shift(RIGHT)

        circle.set_stroke(color=GREEN, width=20)
        square.set_fill(YELLOW, opacity=1.0)
        triangle.set_fill(PINK, opacity=0.5)

        self.add(circle, square, triangle)
        self.wait(1)

class SomeAnimations(Scene):
    def construct(self):
        square = Square()
        self.add(square)

        # some animations display mobjects, ...
        self.play(FadeIn(square))

        # ... some move or rotate mobjects around...
        self.play(Rotate(square, PI/4))

        # some animations remove mobjects from the screen
        self.play(FadeOut(square))

        self.wait(1)

class ApplyMethodExample(Scene):
    def construct(self):
        square = Square().set_fill(RED, opacity=1.0)
        self.add(square)

        # animate the change of color
        self.play(ApplyMethod(square.set_fill, WHITE))
        self.wait(1)

        # animate the change of position
        self.play(ApplyMethod(square.shift, UP))
        self.wait(1)


class TikzMobject(Tex):
    CONFIG = {
        "stroke_width": 3,
        "fill_opacity": 0,
        "stroke_opacity": 1,
    }

class ExampleTikz(Scene):
    def construct(self):
        circuit = TikzMobject(r"""
            \begin{circuitikz}[american voltages]
            \draw
              (0,0) to [short, *-] (6,0)
              to [V, l_=$\mathrm{j}{\omega}_m \underline{\psi}^s_R$] (6,2) 
              to [R, l_=$R_R$] (6,4) 
              to [short, i_=$\underline{i}^s_R$] (5,4) 
              (0,0) to [open,v^>=$\underline{u}^s_s$] (0,4) 
              to [short, *- ,i=$\underline{i}^s_s$] (1,4) 
              to [R, l=$R_s$] (3,4)
              to [L, l=$L_{\sigma}$] (5,4) 
              to [short, i_=$\underline{i}^s_M$] (5,3) 
              to [L, l_=$L_M$] (5,0); 
              \end{circuitikz}
            """
            )
        self.play(Write(circuit))
        self.wait()