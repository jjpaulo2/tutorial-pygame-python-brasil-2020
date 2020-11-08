import pygame, pathlib
pygame.init()

largura = 800
altura = 300

tela = pygame.display.set_mode([largura, altura])
pygame.display.set_caption("Sprites do Sonic")

clock = pygame.time.Clock()

DIRETORIO_ATUAL = str(pathlib.Path(__file__).parent.absolute())

class Sonic(pygame.sprite.Sprite):
    def __init__(self):
        self.posicao = [50, 100]
        self.velocidade = (0, 0)

        self.images = [
            DIRETORIO_ATUAL + '/src/sonic1.png',
            DIRETORIO_ATUAL + '/src/sonic2.png',
            DIRETORIO_ATUAL + '/src/sonic3.png',
        ]
        self.index = 0
        self.__set_image()
        self.rect = self.image.get_rect()
        self.rect.left = self.posicao[0]
        self.rect.top = self.posicao[1]

    def __set_image(self):
        self.image = pygame.image.load(self.images[self.index])

    def update(self):
        self.rect.move_ip(self.velocidade[0], self.velocidade[1])

        if self.velocidade[0] != 0:
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
            self.image = pygame.image.load(self.images[self.index])

sonic = Sonic()

executando = True
while executando:
    
    eventos = pygame.event.get()
    for evento in eventos:
        if evento.type == pygame.QUIT:
            executando = False

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RIGHT:
                sonic.velocidade = (20, 0)

            if evento.key == pygame.K_LEFT:
                sonic.velocidade = (-20, 0)

            if evento.key == pygame.K_DOWN:
                sonic.velocidade = (0, 20)

            if evento.key == pygame.K_UP:
                sonic.velocidade = (0, -20)

        if evento.type == pygame.KEYUP:
            sonic.velocidade = (0, 0)

    tela.fill((0,0,0))
    sonic.update()
    tela.blit(sonic.image, sonic.rect)

    clock.tick(30)
    pygame.display.update()

pygame.quit()