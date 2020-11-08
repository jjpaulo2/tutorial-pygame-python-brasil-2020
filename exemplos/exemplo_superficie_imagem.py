import pygame, pathlib
pygame.init()

largura = 800
altura = 500

tela = pygame.display.set_mode([largura, altura])
pygame.display.set_caption("Minha janela")

clock = pygame.time.Clock()

DIRETORIO_ATUAL = str(pathlib.Path(__file__).parent.absolute())
mario = pygame.image.load(DIRETORIO_ATUAL + '/src/mario.png')
mario_pos = [10, 10]
mario_vel = [0, 0]

executando = True
while executando:
    
    eventos = pygame.event.get()
    for evento in eventos:
        if evento.type == pygame.QUIT:
            executando = False

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RIGHT:
                mario_vel[0] = 10

            if evento.key == pygame.K_LEFT:
                mario_vel[0] = -10

            if evento.key == pygame.K_DOWN:
                mario_vel[1] = 10

            if evento.key == pygame.K_UP:
                mario_vel[1] = -10

        if evento.type == pygame.KEYUP:
            mario_vel = [0, 0]

    tela.fill((0,0,0))

    mario_pos[0] += mario_vel[0]
    mario_pos[1] += mario_vel[1]
    tela.blit(mario, mario_pos)

    clock.tick(30)
    pygame.display.update()

pygame.quit()