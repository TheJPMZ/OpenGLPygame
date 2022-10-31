'''
Renderizador con OpenGl y pygame.
Por Jose Pablo Monzon
Basado en el codigo visto en clase y en el repositorio de CHURLY92 (El profesor)
https://github.com/churly92/RendererOpenGL_2022
'''
import pygame
from pygame.locals import *

from shaders import *

from gl import Renderer, Model

width = 960
height = 540

deltaTime = 0.0

pygame.init()

screen = pygame.display.set_mode((width, height), pygame.OPENGL | pygame.DOUBLEBUF)
clock = pygame.time.Clock()

rend = Renderer(screen)

rend.setShaders(vertex_shader, fragment_shader)

rend.target.z = -2

# * Modelo

model = Model("pumpkin.obj", "pumpkin.bmp")

model.position.z -= 2
model.position.y -= 0.1
model.scale.x = 1
model.scale.y = 1
model.scale.z = 1

rend.scene.append( model )

# * Fin Modelo

zoom_level = 50
y_level = 180
x_level = 180

running = True

while running:

    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # * Camera movement

    if keys[K_LEFT]:
        if x_level > 0:
            rend.camPosition.x -= 10 * deltaTime
            x_level -= 10

    elif keys[K_RIGHT]:
        if x_level <= 360:
            rend.camPosition.x += 10 * deltaTime
            x_level += 10
    
    elif keys[K_UP]:
        if y_level <= 360:
            rend.camPosition.y += 10 * deltaTime
            y_level += 10
    
    elif keys[K_DOWN]:
        if y_level > 0:
            rend.camPosition.y -= 10 * deltaTime
            y_level -= 10

    # * Zoom

    if keys[K_RSHIFT]:
        if zoom_level <= 100:
            rend.camPosition.z -= 10  * deltaTime
            zoom_level += 10
    elif keys[K_RCTRL]:
        if zoom_level > 0:
            rend.camPosition.z += 10 * deltaTime
            zoom_level -= 10

    deltaTime = clock.tick(60) / 1000
    rend.time += deltaTime

    rend.update()
    rend.render()
    pygame.display.flip()

pygame.quit()
