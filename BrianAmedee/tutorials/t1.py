from manim import *

class v1t1(Scene):
    def construct(self):
        plane = NumberPlane(x_range=[-7,7,1], y_range=[-4,4,1])
        plane.add_coordinates()
        box = Rectangle(stroke_color = GREEN_C, stroke_opacity=0.7, fill_color = RED_B, fill_opacity = 0.5, height=1, width=1)
        dot = always_redraw(lambda : Dot().move_to(box.get_center()))

        self.play(FadeIn(plane, run_time=3))
        self.add(box,dot)
        self.play(box.animate.shift(RIGHT*2), run_time=3)
        self.play(box.animate.shift(UP*2), run_time=3)

class v1t2(Scene):
    def construct(self):
        plane = NumberPlane(x_range=[-7,7,1], y_range=[-4,4,1])
        plane.add_coordinates()
        
        axes = Axes(x_range=[-3,3,1], y_range=[-3,3,1], x_length = 6, y_length=6)
        #axes.to_edge(LEFT,buff=0)
        axes.move_to([-3. , 0., 0.])
        
        circ = Circle(radius=1., stroke_color=YELLOW, stroke_opacity=0.7,fill_color=RED, fill_opacity=0.5)
        #circ.shift(DOWN*3+RIGHT*6)
        circ.to_edge(DR,buff=0)

        tri=Triangle(stroke_color=ORANGE, stroke_width=10).set_height(2)
        tri.shift(RIGHT*3+DOWN*3)
        self.play(FadeIn(plane),run_time=3)
        self.play(FadeIn(axes),run_time=1)
        self.play(DrawBorderThenFill(circ),run_time=1)
        self.play(circ.animate.set_width(1),run_time=3)
        self.wait()
        self.play(Transform(circ,tri))

class v1t3(Scene):
    def construct(self):

        rec=RoundedRectangle(stroke_width=8, stroke_color=WHITE,fill_color=BLUE_B, width=4.5, height=2 ).shift(UP*3+LEFT*4)
        
        frac=MathTex(r'\frac{1}{2}=0.5',).set_color_by_gradient(PINK,GREEN).set_height(1.5)
        frac.move_to(rec.get_center()) 
        frac.add_updater(lambda x: x.move_to(rec.get_center()))

        self.play(FadeIn(rec))
        self.play(Write(frac),run_time=2)

        self.play(rec.animate.move_to(DOWN*2+LEFT*1), run_time=3)
        self.wait()

        frac.clear_updaters()

        self.play(rec.animate.move_to(LEFT*3+DOWN*1), run_time=2)

class v1t4(Scene):
    def construct(self):
        
        r = ValueTracker(0.5)
        
        circ = always_redraw(lambda:
             Circle(radius=r.get_value(), stroke_color = YELLOW, stroke_width=5))

        line_radius=always_redraw(lambda: 
            Line(start=circ.get_center(),end=circ.get_bottom(), stroke_color=RED_B,stroke_width=10 ))

        line_diametro=always_redraw(lambda: Line(stroke_color=YELLOW, stroke_width=5,
            ).set_length(2*r.get_value()*PI).next_to(circ,DOWN,buff=0.2))

        tri=always_redraw(lambda: Polygon(circ.get_left(), circ.get_top(),circ.get_right() , stroke_color=GREEN_C))  

        # self.play(Create(circ))
        # self.play(Create(line_radius))
        # self.play(line_radius.animate.set_stroke(width=20))
        # self.play(Create(tri))
        # self.play(tri.animate.set_stroke(width=20))

        self.play(LaggedStart(Create(circ),DrawBorderThenFill(line_radius), DrawBorderThenFill(tri), run_time=4, lag_ratio=0.75))
        self.play(ReplacementTransform(circ.copy(),line_diametro), run_time=2)
        self.play(r.animate.set_value(2), run_time = 5)


        

class Count(Animation):
    def __init__(self, number: DecimalNumber, start: float, end: float, **kwargs) -> None:
        # Pass number as the mobject of the animation
        super().__init__(number,  **kwargs)
        # Set start and end
        self.start = start
        self.end = end

    def interpolate_mobject(self, alpha: float) -> None:
        # Set value of DecimalNumber according to alpha
        value = self.start + (alpha * (self.end - self.start))
        self.mobject.set_value(value)


class CountingScene(Scene):
    def construct(self):
        # Create Decimal Number and add it to scene
        number = DecimalNumber().set_color(WHITE).scale(5)
        # Add an updater to keep the DecimalNumber centered as its value changes
        number.add_updater(lambda number: number.move_to(ORIGIN))



        # Play the Count Animation to count from 0 to 100 in 4 seconds
        self.play(Count(number, 0, 100), run_time=4)

        self.wait()