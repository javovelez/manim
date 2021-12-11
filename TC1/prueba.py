from manim import *

class TikzMobject(TextMobject):
    CONFIG = {
        "stroke_width": 2,
        "fill_opacity": 0,
        "stroke_opacity": 1,
    }

class VoltageFollower(Scene):
    def construct(self):
        circuit = TikzMobject("""
        \\begin{circuitikz}[american]
        \draw (0,0) node[op amp](OpAmp){};
        \draw ++(OpAmp.out) -- ++(0,1.5) -- (OpAmp.- |- ++(0,1.5) -- (OpAmp.-);
        \draw (OpAmp.out) to[short, -*](2,0) node[right](V_o){$V_o$};
        \draw (OpAmp.+) to[R, l=$Rs$]++(-3,0) to[sV, l=$V_s$]++(0,-1.5) node[ground]{};
        \end{circuitikz}""")
        self.play(FadeIn(circuit))
        self.wait()