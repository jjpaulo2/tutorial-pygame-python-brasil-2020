#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SOLUÇÃO DO DESAFIO 1
---
Construa um jogo com dois retângulos na
tela. Você deverá controlar um deles e
assim que ele colidir com o segundo, este
deverá mudar sua posição na tela.
"""

import pygame
from random import randint

tela = pygame.display.set_mode([300, 300])
clock = pygame.time.Clock()

quadro1 = pygame.Rect(10, 10, 30, 30)
quadro2 = pygame.Rect(100, 100, 50, 50)

direcao = (0, 0)

executando = True
while executando:

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False
        
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_UP:
                direcao = (0, -20)
            if evento.key == pygame.K_DOWN:
                direcao = (0, 20)
            if evento.key == pygame.K_LEFT:
                direcao = (-20, 0)
            if evento.key == pygame.K_RIGHT:
                direcao = (20, 0)
        
        if evento.type == pygame.KEYUP:
            direcao = (0, 0)

    quadro1.move_ip(direcao)
    if quadro1.colliderect(quadro2):
        quadro2.x = randint(0, 250)
        quadro2.y = randint(0, 250)

    tela.fill((255, 255, 255))
    pygame.draw.rect(tela, (255, 0, 0), quadro2)
    pygame.draw.rect(tela, (0, 0, 0), quadro1)
    clock.tick(30)
    pygame.display.update()

pygame.quit()
