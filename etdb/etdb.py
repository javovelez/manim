from manim import *

class escena1(Scene):
    def construct(self):
        punto = Dot()
        punto.to_edge(UP)
        self.add(punto)
        self.wait()

class Fuentes(Scene):
	def construct(self):
		textoNormal = TextMobject("{Texto normal 012.\\#!?} Texto normal")
		textoItalica = TextMobject("\\textit{Texto en itálicas 012.\\#!?} Texto normal")
		textoMaquina = TextMobject("\\texttt{Texto en máquina 012.\\#!?} Texto normal")
		textoNegritas = TextMobject("\\textbf{Texto en negritas 012.\\#!?} Texto normal")
		textoSL = TextMobject("\\textsl{Texto en sl 012.\\#!?} Texto normal")
		textoSC = TextMobject("\\textsc{Texto en sc 012.\\#!?} Texto normal")
		textoNormal.to_edge(UP)
		textoItalica.next_to(textoNormal,DOWN,buff=.5)
		textoMaquina.next_to(textoItalica,DOWN,buff=.5)
		textoNegritas.next_to(textoMaquina,DOWN,buff=.5)
		textoSL.next_to(textoNegritas,DOWN,buff=.5)
		textoSC.next_to(textoSL,DOWN,buff=.5)
		self.add(textoNormal,textoItalica,textoMaquina,textoNegritas,textoSL,textoSC)
		self.wait(3)