import tkinter as tk
c = tk.Canvas(width=700, height=500)
c.pack()


class Ball:
    def __init__(self, canv, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        self.c = canv

    def draw(self):
        self.c.create_oval(self.x, self.y, self.x + 2*self.r, self.y + 2*self.r)

    def move(self):
        self.x += 1

active = True

b = Ball(c, 30, 30, 30)

def draw():
    global active, b
    c.delete('all')

    b.move()
    b.draw()

    c.update_idletasks()
    c.update()
    if (active):
        c.after(16, draw) # 60fps

c.after(50, draw)
c.mainloop()
