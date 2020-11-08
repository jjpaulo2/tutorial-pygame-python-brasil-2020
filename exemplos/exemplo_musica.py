import pygame, pathlib

pygame.mixer.pre_init(44100, 16, 2, 1024)
pygame.init()

tela = pygame.display.set_mode([200, 200])
pygame.display.set_caption('Exemplo de música')

DIRETORIO_ATUAL = str(pathlib.Path(__file__).parent.absolute())

tocando = False

executando = True
while executando:

    if not tocando:
        pygame.mixer.music.load(DIRETORIO_ATUAL + '/src/musica1.wav')
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play()
        tocando = True

    for evento in pygame.event.get():
        
        if evento.type == pygame.QUIT:
            executando = False


pygame.quit()