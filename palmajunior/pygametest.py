import os

try :
    import pygame as pg
except ImportError:
    os.system("pip install pygame")
    import pygame as pg

BG = (0, 0, 0)
RED = (255, 0, 0)

size = (700, 500)
scr = pg.display.set_mode(size)
pg.display.set_caption("Fajv")

clock = pg.time.Clock()

done = False
while not done:
    mpos = pg.mouse.get_pos()
    mx = mpos[0]
    my = mpos[1]

    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
    
    scr.fill(BG)

    pg.draw.rect(scr, RED, [mx-10, my-10, 20, 20], 0)

    pg.display.flip()
    clock.tick(60)

pg.quit()