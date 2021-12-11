from manim import *

class v3t1(VectorScene):
    def construct(self):
        plane = self.add_plane(animate=True)
        self.play(plane.animate.add_coordinates())
        vector = self.add_vector([-3,-2],color=YELLOW)
        self.vector_to_coords(vector=vector)

        basis=self.get_basis_vectors()
        self.add(basis)
        self.wait()

class Matrix(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            leave_ghost_vectors=True,
            show_basis_vectors=True
        )
    def construc(self):
        
        matrix = [[1, 2], [2, 1]]

        matrix_tex = (
            MathTex("A = \\begin{bmatrix} 1 & 2 \\\ 2 & 1 \\end{bmatrix}")
            .to_edge(UL)
            .add_background_rectangle()
        )

