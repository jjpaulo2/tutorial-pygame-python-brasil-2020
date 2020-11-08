import pygame
pygame.init()

largura = 800
altura = 500

tela = pygame.display.set_mode([largura, altura])
pygame.display.set_caption("Minha janela")

clock = pygame.time.Clock()

quadrado1_cor = (255, 0, 0)
quadrado1_top = 10
quadrado1_left = 10
quadrado1_largura = 100
quadrado1_altura = 100
quadrado1 = pygame.Rect(quadrado1_left, quadrado1_top, quadrado1_largura, quadrado1_altura)

quadrado2_cor = (0, 255, 0)
quadrado2_top = 10
quadrado2_left = 300
quadrado2_largura = 100
quadrado2_altura = 100
quadrado2 = pygame.Rect(quadrado2_left, quadrado2_top, quadrado2_largura, quadrado2_altura)

executando = True
while executando:
    
    eventos = pygame.event.get()
    for evento in eventos:
        if evento.type == pygame.QUIT:
            executando = False

    pygame.draw.rect(tela, quadrado1_cor, quadrado1)
    pygame.draw.rect(tela, quadrado2_cor, quadrado2)

    clock.tick(30)
    pygame.display.update()

pygame.quit()