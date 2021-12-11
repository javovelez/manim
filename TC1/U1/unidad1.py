from manim import *

class presentacion(Scene):
    def construct(self):
        materia = Tex('Teoría de los Circuitos 1')
        universidad = Tex('Universidad Tecnológia Nacional')
        regional = Tex('Facultad Regional Mendoza')
        Profesor = Tex('Mg. Ing. Javier Velez (JTP)')
        self.play(Create(materia.shift(UP)))
        self.play(Create(universidad.next_to(materia, DOWN)))
        self.play(Create(regional.next_to(universidad, DOWN)))
        self.play(Create(Profesor.next_to(regional,DOWN)))
        self.wait()

