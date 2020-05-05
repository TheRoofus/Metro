import sys
import pygame

w = 0
s = 1
g = 2
f = 3

blue = (0, 0, 255)
sandayyllow = (194, 178, 128)
grassgreen = (124, 252, 0)
forestgreen = (0, 100, 0)

tileColour = {w: blue,
              s: sandayyllow,
              g: grassgreen,
              f: forestgreen
              }

map1 = [
       [f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f],
       [w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w],
       [w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w],
       [w, w, s, w, w, w, s, w, w, w, w, s, w, w, w, s, w, w, w, w, s, w, w, w, s, w, w, w, w, s, w, w, w, s, w, w],
       [w, s, g, s, w, s, g, s, w, w, s, g, s, w, s, g, s, w, w, s, g, s, w, s, g, s, w, w, s, g, s, w, s, g, s, w],
       [w, w, s, w, w, w, s, w, w, w, w, s, w, w, w, s, w, w, w, w, s, w, w, w, s, w, w, w, w, s, w, w, w, s, w, w],
       [w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w],
       [w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w],
       [f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f]
       ]

tileSize = 40
mapWidth = 36
mapHeight = 9

pygame.init()
display = pygame.display.set_mode((mapWidth * tileSize, mapHeight * tileSize))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    for row in range(mapHeight):
        for col in range(mapWidth):
            pygame.draw.rect(display, tileColour[map1[row][col]], (col*tileSize, row*tileSize, tileSize, tileSize))
    pygame.display.update()

