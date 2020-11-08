#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SOLUÇÃO DO DESAFIO 3
---
Construa um jogo com dois retângulos na tela.
Cada um deve tocar uma música específica ao
ser clicado.
"""

import pygame

pygame.mixer.pre_init(44100, 16, 2, 1024)
pygame.init()

tela = pygame.display.set_mode([130, 70])
clock = pygame.time.Clock()

quadro1 = pygame.Rect(10, 10, 50, 50)
quadro2 = pygame.Rect(70, 10, 50, 50)

musicas = [
    "/home/jjpaulo2/musica1.wav",
    "/home/jjpaulo2/musica2.wav"
]

executando = True
while executando:

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False

        if evento.type == pygame.MOUSEBUTTONDOWN:

            if quadro1.collidepoint(pygame.mouse.get_pos()):
                pygame.mixer.music.stop()
                pygame.mixer.music.load(musicas[0])
                pygame.mixer.music.set_volume(0.5)
                pygame.mixer.music.play()

            elif quadro2.collidepoint(pygame.mouse.get_pos()):
                pygame.mixer.music.stop()
                pygame.mixer.music.load(musicas[1])
                pygame.mixer.music.set_volume(0.5)
                pygame.mixer.music.play()

    pygame.draw.rect(tela, (255, 0, 0), quadro1)
    pygame.draw.rect(tela, (0, 255, 0), quadro2)
    clock.tick(30)
    pygame.display.update()

pygame.quit()
