from manim import *

class IntegralSolution(Scene):
    def construct(self):
        
        title = Tex("Integration of \(e^x \sin(x)\) with respect to \(x\)")

        equation1 = MathTex(r"\int e^x \sin(x) \, dx = -e^x \cos(x) - \int -e^x \cos(x) \, dx")
        equation2 = MathTex(r"\int e^x \cos(x) \, dx = e^x \sin(x) - \int e^x \sin(x) \, dx")
        equation3 = MathTex(r"I = e^x \sin(x) - \int e^x \sin(x) \, dx")
        equation4 = MathTex(r"2I = -e^x \cos(x) + e^x \sin(x)")
        equation5 = MathTex(r"I = \frac{-e^x \cos(x) + e^x \sin(x)}{2} + C")

        equations = VGroup(equation1, equation2, equation3, equation4, equation5)
        equations.arrange(DOWN, buff=0.5)

        self.play(Write(title))
        temp = title
        self.wait(1)

        for equation in equations:
            self.play(Transform(temp, equation))
            self.wait(1.5)
            temp = equation

        self.wait(1)


class IntegralSolution2(Scene):
    
    def animate_equation(self, equation, colors):
        """Helper function to animate the writing and coloring of equations."""
        for text, color in zip(equation, colors):
            text.set_fill(color=color)
            self.play(Write(text), run_time=0.75)
            # self.wait(0.1)
    
    def animate_substitution(self, equation, color):
        """Helper function to animate the writing and coloring of equations."""
        equation.set_fill(color=color)
        self.play(Write(equation), run_time=1)
        # self.wait(0.1)

    def draw_substitution_dictionary(self): 
        # Define the substitution equations
        u_eq = MathTex(r"u =", r"x")
        v_eq = MathTex(r"v =", r"\sin(x)")
        du_eq = MathTex(r"du =", r"dx")
        dv_eq = MathTex(r"dv =", r"\cos(x) dx")

        # Arrange the equations in a 2x2 grid
        substitutions = VGroup(u_eq, v_eq, du_eq, dv_eq).arrange_in_grid(rows=2, cols=2, buff=0.25)

        # Draw a surrounding rectangle
        rect = SurroundingRectangle(substitutions, color=WHITE, buff=0.25)
        
        # Position the box at the bottom left
        substitutions.next_to(ORIGIN, DOWN + LEFT, buff=1.5)
        rect.move_to(substitutions)

        # Animate the equations and rectangle
        self.play(Write(rect))
        self.animate_substitution(u_eq, RED)
        self.animate_substitution(v_eq, GREEN)
        self.animate_substitution(du_eq, BLUE)
        self.animate_substitution(dv_eq, YELLOW)

    def construct(self):
        # Define the equations
        eq_integral = MathTex(r"\int", r"x", r"\cos(x) \, dx")
        eq_parts = MathTex(r"\, =", r"\text{u} ", r"\text{v} ", r"- \int", r"\text{v}", r"\, \text{du}")
        eq_integral_solution_1 = MathTex(r"\, =", r"x", r"\sin(x)", r"- \int", r"\sin(x)", r"\, \text{dx}")
        eq_integral_solution_2 = MathTex(r"\, =", r"x", r"\sin(x)", r"+ \cos(x) + \text{C}")
        
        # Align equations on the same line
        top_equations = VGroup(eq_integral, eq_parts).arrange(RIGHT, buff=0.5)
        # Position the top equations at the top of the screen
        top_equations.to_edge(UP, buff=1)

        # Align eq_integral_solution_1 with eq_parts and position eq_integral_solution_2 next to it
        eq_integral_solution_1.next_to(eq_integral, DOWN, buff=0.5).align_to(eq_parts[0], LEFT)
        eq_integral_solution_2.next_to(eq_integral_solution_1, DOWN, buff=0.5).align_to(eq_integral_solution_1, LEFT)

        # Position the top equations at the top of the screen
        top_equations.to_edge(UP, buff=1)

        # Animate the equations
        self.animate_equation(eq_integral, [WHITE, RED, YELLOW])
        self.draw_substitution_dictionary()
        self.animate_equation(eq_parts, [WHITE, RED, GREEN, WHITE, GREEN, BLUE])
        self.animate_equation(eq_integral_solution_1, [WHITE, RED, GREEN, WHITE, GREEN, BLUE])
        self.animate_equation(eq_integral_solution_2, [WHITE, RED, GREEN, WHITE])


