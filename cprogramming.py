from big_ol_pile_of_manim_imports import *

class TitleScene(Scene):
    def construct(self):
        title = TextMobject("\\begin{minipage}{2.3cm}\\begin{flushleft}Introduction to the \phantom{C} Programming Language\\end{flushleft}\\end{minipage}")
        c = TextMobject("\\begin{minipage}{2.3cm}\\begin{flushleft}\phantom{Introduction} \phantom{to} \phantom{the} C \phantom{Programming} \phantom{Language}\\end{flushleft}\\end{minipage}")
        title.set_color(SRCERY_BRIGHT_WHITE)
        c.set_color(SRCERY_GREEN)
        title.scale(2.5)
        title.shift(3*LEFT)
        c.scale(10)
         
        self.add(c)
        self.wait(2)
        self.play(ScaleInPlace(c, 0.25))
        self.play(ApplyMethod(c.shift, 2.82*LEFT+0.85*UP))
        self.play(ShowCreation(title))
        self.wait(2)
        title.add(c)
        self.remove(c)
        self.play(FadeOut(title))
        self.wait(2)

class ComputerScene(Scene):
    def construct(self):
        computer = Computer()
        #self.add(computer)
        self.play(FadeIn(computer))
        self.wait(2)
        self.play(ScaleInPlace(computer, 3))
        self.wait(2)

class Computer(SVGMobject):
    CONFIG = {
        "file_name": "apple-01.svg"
    }

    def __init__(self, **kwargs):
        SVGMobject.__init__(self, **kwargs)
        self[0].set_fill("#A6A6AD", 1)
        self[1].set_fill("#3E3E42", 1) # frame
        self[2].set_fill("#000000", 0.1)
        self[3].set_fill("#D2D2D6", 1)
        self[4].set_fill("#57575E", 1)
        self[5].set_fill("#A6A6AD", 1)
        self[6].set_fill("#D2D2D6", 1)

