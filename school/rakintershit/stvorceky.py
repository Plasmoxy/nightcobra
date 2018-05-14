from tkinter import Canvas

active = True

c = Canvas(width=1000, height=600)
c.pack()

t = 0

def stvorec(x, y):
    c.create_rectangle(x, y, x + 10, y + 10)


def riadok(x, y, pocet):
    for i in range(0, pocet):
        stvorec(x + 20*i, y)

def stvorecStvorcov(x, y, dx, dy):
    for i in range(0, dy):
        riadok(x, y + 20 * i, dx)

def mindfuck(amt):
    for i in range(0, 20):
        stvorecStvorcov(i * amt, i * amt, i, i)

def loop():
    global t, c
    c.delete('all')

    mindfuck(t)

    if t > 20:
        t = 0
    else:
        t += 1

    c.update_idletasks()
    c.update()
    c.after(0, loop)

c.after(0, loop)
c.mainloop()