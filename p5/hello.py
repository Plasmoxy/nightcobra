from p5 import *

class Mover:
    def __init__(self, x, y):
        self.pos = Vector(x, y)
        self.vel = Vector(0, 0)

    def update(self):
        self.pos += self.vel

    def display(self):
        with push_matrix():
            fill(255, 0, 0)
            translate(self.pos.x, self.pos.y)
            ellipse((0,0), 20, 20)

a = Mover(50, 50)
a.vel.x = 1

def setup():
    size(800, 400)
    no_cursor()
def draw():
    global mouse_x, mouse_y
    mousev = Vector(mouse_x, mouse_y)


    a.vel = (mousev - a.pos)/20

    background(0)
    a.update()
    a.display()

    fill(200)
    ellipse(mousev, 10, 10)

run()