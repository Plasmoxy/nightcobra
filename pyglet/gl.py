from pyglet.gl import *
from random import random

window = pyglet.window.Window(resizable=True)

counter = 0.0

def tick(dt):
    global counter
    print(counter)
    counter += dt


@window.event
def on_draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    glColor3f(random(), random(), random())

    w = window.width
    h = window.height

    glBegin(GL_TRIANGLES)
    glVertex2f(w*random(), h*random())
    glVertex2f(w*random(), h*random())
    glVertex2f(w*random(), h*random())
    glEnd()
    
    

pyglet.clock.schedule_interval(tick, 1/5)
pyglet.app.run()