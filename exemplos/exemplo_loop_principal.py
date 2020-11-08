import pygame
pygame.init()

largura = 800
altura = 500

pygame.display.set_mode([largura, altura])
pygame.display.set_caption("Minha janela")

executando = True
while executando:
    
    eventos = pygame.event.get()
    for evento in eventos:
        if evento.type == pygame.QUIT:
            executando = False

pygame.quit()