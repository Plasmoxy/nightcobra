from pyglet.gl import *

# Direct OpenGL commands to this window.
window = pyglet.window.Window(resizable=True)

@window.event
def on_resize(width, height):
    pass


@window.event
def on_draw():

    glClear(GL_COLOR_BUFFER_BIT or GL_DEPTH_BUFFER_BIT)
    glViewport(0, 0, window.width, window.height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, window.width/window.height, 0.1, 100)

    glColor3f(1, 0, 0)
    glTranslatef(0, 0, -10)

    glBegin(GL_POLYGON)
    glVertex3f(0, 0, 0)
    glVertex3f(20, 0, 0)
    glVertex3f(20, 20, 0)
    glVertex3f(0, 20, 0)
    glEnd()

glClearColor(0, 0, 0, 1)
glClearDepth(1)
glEnable(GL_DEPTH_TEST)
glDepthFunc(GL_LEQUAL)
glShadeModel(GL_SMOOTH)

pyglet.app.run()