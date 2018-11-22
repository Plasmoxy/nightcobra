import turtle

screen = turtle.Screen()
t = turtle.Turtle()
t.speed(200)

# zakladne body
xa = 50
ya = 0

def polkruznica(x, y, r):
    t.pu()
    t.setx(x)
    t.sety(y)
    t.pd()
    t.circle(r, 180)
    t.lt(180)

def kresli_pyramidu(r, poschodia):

    t.lt(90)

    for p in range(poschodia, 0, -1):
        for k in range(0, p):
            if (p % 2 == 0):
                t.color("black")
            else:
                t.color("red")
            # dx = -k*2r, dy = -k*2r
            polkruznica(xa - p*r + k*2*r, ya - p*r, r)

    screen.mainloop()

kresli_pyramidu(10, 20)