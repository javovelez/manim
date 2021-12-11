from manim import *
config["tex_template"].add_to_preamble("\\usepackage{tikz}")
config["tex_template"].add_to_preamble("\\usepackage{circuitikz}")

class v2t1(Scene):
    def construct(self):
        ax = Axes(x_range=[0, 5], y_range=[0,3], x_length=5,y_length=3,
            axis_config={   }).add_coordinates()
        ax.to_edge(UR)
        axis_label=ax.get_axis_labels(x_label='x',y_label='f(x)')

        func=ax.get_graph(lambda x: x**0.5,x_range=[0,4],color=YELLOW)

        gr= VGroup(ax, func, axis_label)

        self.play(DrawBorderThenFill(ax),Write(axis_label))
        self.play(Create(func))
        self.play(gr.animate.shift(DOWN*4))
        self.play(ax.animate.shift(LEFT*3),run_time=3)

class v2t2(Scene):
    def construct(self):

        pl=NumberPlane(x_range=[-6,6,2], y_range=[-10,10,2], x_length=5, y_length=5)
        pl.add_coordinates()
        pl.shift(RIGHT*3)


        fc = pl.get_graph(lambda x: 0.1*x*(x-5)*(x+5),x_range=[-6,6],color=GREEN_B)

        area = pl.get_area(graph=fc,x_range=[-5,5],color=[BLUE,YELLOW] ,opacity=1)

        tx = MathTex('\sin(x)')
        tx.to_edge(LEFT)

        self.play(Create(pl),run_time=3)
        self.play(Create(fc),run_time=3)
        self.play(FadeIn(area),run_time=3)
        self.play(Transform(area,tx))

class v2t3(Scene):
    def construct(self):
        pl=NumberPlane(x_range = [-4,4,1], x_length=4 , y_range = [0,20,5], y_length = 4).add_coordinates()
        pl.shift(LEFT*3+DOWN*1.5)
        #pl.coordinate_labels.shift(LEFT*0.3)
        f1=pl.get_graph(lambda x: x**2, x_range=[-4,4], color=GREEN)
        a1=pl.get_riemann_rectangles(graph=f1, x_range=[-2,2], color=[BLUE,GREEN], dx=0.05)



        ax =Axes(x_range=[-4,4], y_range=[-20,20,5],x_length=4,y_length=4,axis_config={"include_tip": True, "numbers_to_exclude": [0]})
        ax.add_coordinates()
        ax.shift(RIGHT*3+DOWN*1.5)
        f2 = ax.get_graph(lambda x: 2*x, x_range=[-4,4], color=YELLOW)
        v_lines=ax.get_vertical_lines_to_graph(graph=f2, x_range=[-3,3], num_lines=12)

        self.play(Write(pl),Create(f1),Create(a1))
        self.wait(1)
        self.play(Create(ax),Create(f2))
        self.add(v_lines)
        self.wait(1)

class v2t4(Scene):
    def construct(self):
        
        var = ValueTracker(0.01)
        
        pplane=PolarPlane(radius_max=3).add_coordinates()
        pplane.shift(LEFT*2)
        f1=always_redraw(lambda: ParametricFunction(lambda t: pplane.polar_to_point(2*np.sin(3*t), t), t_range= [0 , var.get_value()] , color=GREEN))

        dot1=always_redraw(lambda: Dot(fill_color= GREEN,fill_opacity=0.8).scale(0.5).move_to(f1.get_end()))


        ax=Axes(x_range=[0,4], x_length=3 ,y_range=[-3,3], y_length=3).shift(RIGHT*4)
        ax.add_coordinates()

        f2=always_redraw(lambda: ax.get_graph(lambda x: 2*np.sin(3*x), x_range=[0, var.get_value()],color=GREEN ))
        dot2=always_redraw(lambda: Dot(fill_color= GREEN,fill_opacity=0.8).scale(0.5).move_to(f2.get_end()))

        title =MathTex(r'f(\theta)=2 \sin(3\theta)',color=GREEN)
        title.next_to(ax,UP,buff=0.2)

        self.play(LaggedStart(Create(pplane), Create(ax),Create(title), lag_ratio=0.5))
        self.add(f1,dot1,f2,dot2)

        self.play(var.animate.set_value(PI), run_time=10, rate_func=linear)




class circ(Scene):
    def construct(self):
        # Circuit content
        circuit = MathTex(r"""
            \begin{circuitikz} \draw
            (0,0) to[battery] (0,4)
              to[ammeter] (4,4) -- (4,0)
              to[lamp] (0,0)
            ;
            \end{circuitikz}
            """
            ,stroke_width=2,fill_opacity=0
            )

        d=Dot()

        self.play(Write(circuit))
        self.play(MoveAlongPath(d,circuit))
        self.wait()

class circ2(Scene):
    def construct(self):
        # Circuit content
        circuit = MathTex("\n",
            r"\begin{circuitikz} \draw","\\"
            r"(0,0) to[battery] (0,4)","\\",
            r"  to[ammeter] (4,4) -- (4,0)","\\",
            r"  to[lamp] (0,0)","\\",
            ";","\\",
            r"\end{circuitikz}"
            ,stroke_width=2,fill_opacity=0
            )
        self.play(Write(circuit))
        self.wait()

class TextAlignement(MovingCameraScene):
    def construct(self):
        # Create RF networok
        rf_network = Rectangle(height=2.75, width=4.5).set_fill(ORANGE, opacity=0.6)
        rf_network.set_stroke(color=WHITE, width=3)
 
        # Show RF network
        self.play(FadeIn(rf_network))
 
        # Create ports
        # Port 1
        port1 = Rectangle(height=0.7, width=0.3).set_fill(MAROON, opacity=0.6)
        port1.set_stroke(color=WHITE, width=2)
        port1.move_to(LEFT * 2.41)
 
        # Numbering
        port1_num=MathTex("1")
        port1_num.move_to(LEFT * 2.42)
        port1_num.shift(UP * 0.57)
        port1_num.scale(0.8)
 
        # Port 2
        port2 = Rectangle(height=0.7, width=0.3).set_fill(MAROON, opacity=0.6)
        port2.set_stroke(color=WHITE, width=2)
        port2.move_to(RIGHT * 2.41)
 
        self.play(FadeIn(port1), FadeIn(port2))
 
        # Numbering
        port2_num=MathTex("2")
        port2_num.move_to(RIGHT * 2.42)
        port2_num.shift(UP * 0.57)
        port2_num.scale(0.8)
 
        self.play(Write(port1_num),Write(port2_num))
 
        # Change color
        self.wait(2)
        self.play(ApplyMethod(rf_network.set_fill, DARK_GREY, opacity=0.3))
 
        # Circuit content
        circuit="""\\begin{circuitikz}[american]
                    \\draw[ultra thin](-2.64,0) to [R] (0,0) to [cute inductor] (2.64,-0);
                    \\draw[ultra thin](0,0) to [capacitor,l^] (0,-1) to (0,-0.8) node[ground]{};;
                    \\end{circuitikz}"""
        circuit=Tex(circuit,stroke_width=2,fill_opacity=0)
        circuit.shift(DOWN * 0.5)
        circuit.scale(0.6)
 
        self.play(Write(circuit), run_time=3)
        self.wait(1)
        self.play(FadeOut(circuit))
        self.play(ApplyMethod(rf_network.set_fill, RED, opacity=0.3))
 
        # Questionmark
        questionmark=MathTex("?")
        questionmark.scale(3)
 
        self.play(Write(questionmark))
        self.wait(1)
        self.play(FadeOut(questionmark))