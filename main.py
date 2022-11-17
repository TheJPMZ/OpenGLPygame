'''
Renderizador con OpenGl y pygame.
Por Jose Pablo Monzon
Basado en el codigo visto en clase y en el repositorio de CHURLY92 (El profesor)
https://github.com/churly92/RendererOpenGL_2022
'''
import pygame
from pygame.locals import *
import glm 

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

model1 = Model("pumpkin/pumpkin.obj", "pumpkin/pumpkin.bmp")
model1.position = (0, -0.3, -2)
model1.scale = (1, 1, 1)
model2 = Model("school/school.obj", "school/school.bmp")
model2.position = (0, -0.7, -2)
model2.scale = (0.3, 0.3, 0.3)
model3 = Model("carro/carro.obj", "carro/carro.bmp")
model3.position = (0, 0, -2)
model3.scale = (0.05, 0.05, 0.05)
model4 = Model("burunya/burunya.obj", "burunya/burunya.bmp")
model4.position = (0, -0.6, -2)
model4.rotation = glm.vec3(0, -90, 0)
model4.scale = (0.5, 0.5, 0.5)
model5 = Model("female/female.obj", "female/female.bmp")
model5.position = (0, -1, -2)
model5.scale = (0.01, 0.01, 0.01)



rend.scene.append( model1 )

# * Fin Modelo

zoom_level = 50
y_level = 180
x_level = 180

running = True

neco = pygame.mixer.Sound("sounds/neco-arc.mp3")
switch = pygame.mixer.Sound("sounds/switch-sound.mp3")
wow = pygame.mixer.Sound("sounds/wow.mp3")
boom = pygame.mixer.Sound("sounds/boom.mp3")

pygame.mixer.music.load("sounds/marketmusic.mp3")
pygame.mixer.music.play(-1)


while running:
    
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            
            elif event.key == pygame.K_1:
                pygame.mixer.Sound.play(wow)
                rend.setShaders(vertex_shader, fragment_shader)
            elif event.key == pygame.K_2:
                pygame.mixer.Sound.play(wow)
                rend.setShaders(vertex_shader, toon_shader)
            elif event.key == pygame.K_3:
                pygame.mixer.Sound.play(wow)
                rend.setShaders(vertex_shader, glow_shader)
            elif event.key == pygame.K_4:
                pygame.mixer.Sound.play(wow)
                rend.setShaders(vertex_shader, glownt_shader)
            elif event.key == pygame.K_5:
                pygame.mixer.Sound.play(wow)
                rend.setShaders(vertex_shader, toon_glow_shader)
            elif event.key == pygame.K_m:
                pygame.mixer.Sound.play(boom)
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else: 
                    pygame.mixer.music.unpause()
                
            elif event.key == pygame.K_q:
                # School
                rend.pointLight = glm.vec3(0,0,0)
                rend.scene[0] = model2
                pygame.mixer.Sound.play(switch)
            elif event.key == pygame.K_w:
                # Car
                rend.pointLight = glm.vec3(0,0,0)
                rend.scene[0] = model3
                pygame.mixer.Sound.play(switch)
            elif event.key == pygame.K_e:
                # Neco Arc
                rend.pointLight = glm.vec3(2,0,-2)
                rend.scene[0] = model4
                pygame.mixer.Sound.play(neco)
            elif event.key == pygame.K_r:
                # Female
                rend.pointLight = glm.vec3(0,0,0)
                rend.scene[0] = model5
                pygame.mixer.Sound.play(switch)
            elif event.key == pygame.K_t:
                # Pumpkin
                rend.pointLight = glm.vec3(0,0,0)
                rend.scene[0] = model1
                pygame.mixer.Sound.play(switch)
        
        if event.type == pygame.MOUSEWHEEL:
            if event.y > 0:
                if zoom_level <= 100:
                    rend.camPosition.z -= 10  * deltaTime
                    zoom_level += 10
            elif event.y < 0:
                if zoom_level > 0:
                    rend.camPosition.z += 10 * deltaTime
                    zoom_level -= 10
                    
        if event.type == pygame.MOUSEMOTION:
            if event.rel[0] != 0:
                if x_level <= 350 and event.rel[0] >= 0 or x_level >= 10 and event.rel[0] <= 0:
                    rend.camPosition.x += 10 * deltaTime * (event.rel[0]/abs(event.rel[0]))
                    x_level += 10 * (event.rel[0]/abs(event.rel[0]))
            if event.rel[1] != 0:
                if y_level <= 350 and event.rel[1] >= 0 or y_level >= 10 and event.rel[1] <= 0:
                    rend.camPosition.y += 10 * deltaTime * (event.rel[1]/abs(event.rel[1]))
                    y_level += 10 * (event.rel[1]/abs(event.rel[1]))
  
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

    rend.update()
    rend.render()
    pygame.display.flip()

pygame.quit()
