import os
import random
import pygame as pg
from vectormath import Vector2

BG = (0, 0, 0)
RED = (255, 0, 0)

size = (700, 500)
scr = pg.display.set_mode(size)
pg.display.set_caption("Fajv")

clock = pg.time.Clock()

class Kocka:

    def __init__(self, screen, x, y, a):
        self.pos = Vector2(x, y)
        self.vel = Vector2(0, 0)
        self.a = a
        self.screen = screen

    def update(self, dt):
        self.pos = self.pos + (self.vel * dt)

    def draw(self):
        x = self.pos.x-self.a
        y = self.pos.y-self.a
        w = self.a*2
        h = self.a*2
        pg.draw.rect(scr, RED, [x, y, w, h], 0)

k = Kocka(scr, 100, 100, 10)

done = False
while not done:
    dt = clock.get_time()/1000

    mparray = pg.mouse.get_pos()
    mpos = Vector2(mparray[0], mparray[1])

        
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
    
    scr.fill(BG)

    k.vel = (mpos - k.pos).normalize() * 200
    k.update(dt)    
    k.draw()

    pg.display.flip()
    clock.tick(60)

pg.quit()