import tkinter as tk

root = tk.Tk()

c = tk.Canvas(root)
c.pack()

class Player:
    def __init__(self):
        self.x = 50
        self.y = 50
        self.vx = 0
        self.vy = 0
        self.speed = 5

    def draw(self):
        c.create_oval(self.x-15, self.y-15, self.x+15, self.y+15)

    def move(self):
        self.x += self.vx
        self.y += self.vy

plr = Player()

def loop():
    global x, y
    c.delete('all')

    plr.move()
    plr.draw()

    c.update_idletasks()
    c.update()
    c.after(16, loop)

def keydown(e):
    code = e.keycode
    if code == 37:
        plr.vx = -plr.speed
    elif code == 38 :
        plr.vy = plr.speed
    elif code == 39:
        plr.vx = plr.speed

root.bind('<KeyPress>', keydown)

c.after(0, loop)
root.focus_set()
root.mainloop()
