from manim import *
import numpy as np
import itertools as it
import operator as op
from functools import reduce
import pickle
import os.path

class presentacion(Scene):
    def construct(self):
        self.camera.background_color=WHITE
        logo = SVGMobject(file_name="logoUTN.svg",color=BLACK)
        ASyS = Text("Análisis de Señales y Sistemas", color=BLACK)
        ASyS.shift(UP*3)
        logo.next_to(ASyS,DOWN)
        ie = Text("Ingeniería Electrónica" ,color=BLACK).next_to(logo, DOWN)
        utn = Text("Universidad Tecnológica Nacional", color=BLACK).next_to(ie, DOWN)
        frm = Text("Facultad Regional Mendoza",  color=BLACK).next_to(utn, DOWN)
        texto = VGroup(logo,ie,utn,frm)

        self.play(DrawBorderThenFill(ASyS))
        self.play(Write(texto),run_time=2)

        self.wait(2)



class VectorExample(Scene):
    def construct(self):
        plane = NumberPlane()
        vector_1 = Vector(RIGHT)

        self.add(plane, vector_1)


class utnLogo(Scene):

    def construct(self):

        self.colors = [     
            BLUE_D,
            BLUE_C,
            BLUE_E,
            GREY_BROWN,
        ]

        self.circle_style = {"stroke_width": 2} 
        self.vector_config = {                          
            "buff": 0,
            "max_tip_length_to_length_ratio": 0.08,
            "tip_length": 0.8,
            "max_stroke_width_to_length_ratio": 1,
            "stroke_width": 1.7,
        }
        
        self.circle_config = {                             
            "stroke_width": 1,
            "stroke_opacity": 0.9,
        }
        
        self.center_point = ORIGIN
        self.parametric_function_step_size = 0.001
        self.drawn_path_color = YELLOW   
        self.drawn_path_stroke_width = 2  
    
        self.n_cycles = 1
        self.max_circle_stroke_width = 1

        self.file_name = "logoUTN.svg"
        self.n_vectors = 101
        self.start_drawn = False
        self.height = 7.5
        


        self.add_vectors_circles_path()
        for n in range(self.n_cycles):
            self.run_one_cycle()


    def setup(self):
        self.slow_factor = 0.2
        self.slow_factor_tracker = ValueTracker(
            self.slow_factor
        )
        self.vector_clock = ValueTracker(0)
        self.vector_clock.add_updater(
            lambda m, dt: m.increment_value(
                self.get_slow_factor() * dt
            )
        )
        self.add(self.vector_clock)


    def add_vectors_circles_path(self):
        path = self.get_path()
        coefs = self.get_coefficients_of_path(path)

        for freq, coef in zip(self.get_freqs(), coefs):
            print(freq, "\t", coef)

        vectors = self.get_rotating_vectors(coefficients=coefs)
        circles = self.get_circles(vectors)
        self.set_decreasing_stroke_widths(circles)
        drawn_path = self.get_drawn_path(vectors)
        if self.start_drawn:
            self.vector_clock.increment_value(1)

        self.add(path)
        self.add(vectors)
        self.add(circles)
        self.add(drawn_path)

        self.vectors = vectors
        self.circles = circles
        self.path = path
        self.drawn_path = drawn_path

    def get_path(self):
        shape = self.get_shape()
        path = shape.family_members_with_points()[0]
        path.height=self.height
        path.set_fill(opacity=0)
        path.set_stroke(WHITE, 0)
        return path

    def get_shape(self):
        shape = SVGMobject(self.file_name)
        return shape


    # Computing Fourier series
    # i.e. where all the math happens
    def get_coefficients_of_path(self, path, n_samples=10000, freqs=None):
        if freqs is None:
            freqs = self.get_freqs()
        dt = 1 / n_samples
        ts = np.arange(0, 1, dt)
        samples_file_name='samples'+str(self.n_vectors)+'.pickle'
        if os.path.isfile('./' + samples_file_name):
            print("Se cargan las samples de pickle")
            infile = open(samples_file_name,'rb') 
            complex_samples = pickle.load(infile)
            infile.close()
        else:
            print("Se calculan las samples")
            samples = np.array([
                path.point_from_proportion(t)
                for t in ts
            ])
            samples -= self.center_point
            print(self.centerpoint)
            complex_samples = samples[:, 0] + 1j * samples[:, 1]
            outfile = open(samples_file_name,'wb') 
            pickle.dump(complex_samples, outfile)
            outfile.close()
        result = []
        file_name = str(self.n_vectors)+'.pickle'
        if os.path.isfile('./' + file_name):
            print("Se cargan coeficientes de pickle")
            infile = open(file_name,'rb') 
            result = pickle.load(infile)
            infile.close()
        else:
            print("Se calculan coeficientes")
            for freq in freqs:
                riemann_sum = np.array([
                    np.exp(-TAU * 1j * freq * t) * cs
                    for t, cs in zip(ts, complex_samples)
                ]).sum() * dt
                result.append(riemann_sum)
            outfile = open(file_name,'wb') 
            pickle.dump(result, outfile)
            outfile.close()
        print('Listos los coeficientes')
        return result

    def get_freqs(self):
        n = self.n_vectors
        all_freqs = list(range(n // 2, -n // 2, -1))
        all_freqs.sort(key=abs)
        return all_freqs

    def get_rotating_vectors(self, freqs=None, coefficients=None):
        vectors = VGroup()
        self.center_tracker = VectorizedPoint(self.center_point)
        

        if freqs is None:
            freqs = self.get_freqs()
        if coefficients is None:
            coefficients = self.get_coefficients()
        last_vector = None
        for freq, coefficient in zip(freqs, coefficients):
            if last_vector is not None:
                center_func = last_vector.get_end
            else:
                center_func = self.center_tracker.get_location

            
            vector = self.get_rotating_vector(
                coefficient=coefficient,
                freq=freq,
                center_func=center_func
            )
            vectors.add(vector)
            last_vector = vector
        return vectors

    def get_rotating_vector(self, coefficient, freq, center_func):
        vector = Vector(RIGHT, **self.vector_config)

        vector.scale(abs(coefficient), scale_tips = True)#
        if abs(coefficient) == 0:
            phase = 0
        else:
            phase = np.log(coefficient).imag
        vector.rotate(phase, about_point=ORIGIN)
        vector.freq = freq
        if vector.freq==0:
            print(vector.get_start())
        vector.coefficient = coefficient
        vector.center_func = center_func
        vector.shift(vector.center_func() - vector.get_start())
        vector.add_updater(self.update_vector)
        return vector

    def update_vector(self, vector, dt):
        time = self.get_vector_time()
        coef = vector.coefficient
        freq = vector.freq
        phase = np.log(coef).imag

        # vector.set_length(abs(coef))
        vector.set_angle(phase + time * freq * TAU)
        vector.shift(vector.center_func() - vector.get_start())
        return vector

    def get_vector_time(self):
        return self.vector_clock.get_value()

    def set_decreasing_stroke_widths(self, circles):
        mcsw = self.max_circle_stroke_width
        for k, circle in zip(it.count(1), circles):
            circle.set_stroke(width=max(
                # mcsw / np.sqrt(k),
                mcsw / k,
                mcsw,
            ))
        return circles
        
    def get_circles(self, vectors):
        return VGroup(*[
            self.get_circle(
                vector,
                color=color
            )
            for vector, color in zip(
                vectors,
                self.get_color_iterator()
            )
        ])

    def get_circle(self, vector, color=RED):
        circle = Circle(color=color, **self.circle_config)
        circle.center_func = vector.get_start
        circle.radius_func = vector.get_length
        circle.add_updater(self.update_circle)
        return circle

    def update_circle(self, circle):
        circle.width=2 * circle.radius_func()
        circle.move_to(circle.center_func())
        return circle
        
    def get_drawn_path(self, vectors, stroke_width=None, **kwargs):
        if stroke_width is None:
            stroke_width = self.drawn_path_stroke_width
        path = self.get_vector_sum_path(vectors, **kwargs)
        broken_path = CurvesAsSubmobjects(path)
        broken_path.curr_time = 0

        def update_path(path, dt):
            alpha = self.get_drawn_path_alpha() # obtiene el tiempo transcurrido para dibujar el path hasta ese momento
            n_curves = len(path)
            for a, sp in zip(np.linspace(0, 1, n_curves), path):
                b = alpha - a
                if b < 0:
                    width = 0
                else:
                    width = stroke_width * (1 - (b % 1))
                sp.set_stroke(width=width)
            path.curr_time += dt
            return path

        broken_path.set_color(self.drawn_path_color)
        broken_path.add_updater(update_path)
        return broken_path






    def get_vector_sum_path(self, vectors, color=YELLOW):
        coefs = [v.coefficient for v in vectors]
        freqs = [v.freq for v in vectors]
        center = vectors[0].center_func() #.get_start()
        # center=ORIGIN
        path = ParametricFunction(
            lambda t: center + reduce(op.add, [
                complex_to_R3(coef * np.exp(TAU * 1j * freq * t))
                for coef, freq in zip(coefs, freqs)
            ]),
            color=color,
           dt=self.parametric_function_step_size,
        #    use_smoothing=True
        )
        return path


    def get_color_iterator(self):
        return it.cycle(self.colors)

    # TODO, this should be a general animated mobect
    def get_drawn_path_alpha(self):
        return self.get_vector_time()



    def get_slow_factor(self):
        return self.slow_factor_tracker.get_value()




    def run_one_cycle(self):
        time = 1 / self.slow_factor
        self.wait(time)



