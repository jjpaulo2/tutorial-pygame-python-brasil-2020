#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SOLUÇÃO DO DESAFIO 4
---
Adicione um pouco de movimento ao 
desafio 2. Implemente uma classe de 
sprites e dê vida ao seu personagem
"""

import pygame
from pathlib import Path

DIRETORIO_ATUAL = str(Path(__file__).parent.absolute())

def carregar_imagem(imagem: str):
    return pygame.image.load(DIRETORIO_ATUAL + '/src/sprites/' + imagem)

class Sonic(pygame.sprite.Sprite):
    
    def __init__(self, x=100, y=350):
        super().__init__()

        self.velocidade_x = 0
        self.velocidade_y = 0
        self.x = x
        self.y = y

        self.images = [
            carregar_imagem('sonic-correndo-esquerda-3.png'),
            carregar_imagem('sonic-correndo-esquerda-2.png'),
            carregar_imagem('sonic-correndo-esquerda-1.png'),
            carregar_imagem('sonic-stop-esquerda.png'),
            carregar_imagem('sonic-stop.png'),
            carregar_imagem('sonic-correndo-direita-1.png'),
            carregar_imagem('sonic-correndo-direita-2.png'),
            carregar_imagem('sonic-correndo-direita-3.png'),
        ]

        self.index = 4
        self.image = self.images[self.index]
        self.rect = pygame.Rect(self.x, self.y, 100, 107)

    def update(self):
        self.rect.move_ip(self.velocidade_x, self.velocidade_y)

        if self.velocidade_x > 0:
            self.index += 1
            if self.index >= 8:
                self.index = 4
        elif self.velocidade_x < 0:
            self.index -= 1
            if self.index <= 0:
                self.index = 3

        self.image = self.images[self.index]

    def stop(self):
        if self.velocidade_x > 0:
            self.index = 4
        elif self.velocidade_x < 0:
            self.index = 3
        self.velocidade_x = 0
        self.update()


tela = pygame.display.set_mode([800, 600])
clock = pygame.time.Clock()

sonic = Sonic()
grupo_sprites = pygame.sprite.Group(sonic)

fundo = pygame.image.load(DIRETORIO_ATUAL + '/src/green-hills.png')

executando = True
while executando:

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False
        
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                sonic.velocidade_x = -20
            if evento.key == pygame.K_RIGHT:
                sonic.velocidade_x = 20
        
        if evento.type == pygame.KEYUP:
            sonic.stop()
    
    grupo_sprites.update()
    
    tela.blit(fundo, [0, 0])
    tela.blit(sonic.image, sonic.rect)

    clock.tick(30)
    pygame.display.update()

pygame.quit()
