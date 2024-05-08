import pygame
from pygame import locals
from sys import exit

pygame.init()

tela = pygame.display.set_mode((800,600))
pygame.display.set_caption('Jogo')
while True:
    for event in pygame.event.get():
        if event.type == quit:
            pygame.quit()
            exit()
    pygame.display.update()