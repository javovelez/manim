from manim import *
from pathlib import Path
import os
## flags
FLAGS= f'-pqm'
SCENE="perro"



class xLength(Scene):
    def construct(self):

        xr=ValueTracker(1)
        p=always_redraw(lambda: NumberPlane(x_range=[-7,7],x_length=xr.get_value(), y_range=[-4,4]))
        self.add(p)
        self.play(xr.animate.set_value(14),run_time=3, func_rate=linear)
        self.play(xr.animate.set_value(0.1),run_time=3)
        self.wait(10)
        

class perro(Scene):
    def construct(self):
        circ=Circle()
        self.play(Create(circ),run_time=3)
        
if __name__=='__main__':
    script_name = f'{Path(__file__).resolve()}'.replace('OneDrive - docentes.frm.utn.edu.ar\Apuntes y repos','\\"OneDrive - docentes.frm.utn.edu.ar\Apuntes y repos"')
    print(script_name)
    os.system(f'manim {script_name} {SCENE} {FLAGS }')