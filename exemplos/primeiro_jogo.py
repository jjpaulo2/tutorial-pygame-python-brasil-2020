# IMPORTANDO A BIBLIOTECA
import pygame

# INICIALIZANDO O PYGAME
pygame.init()

# CRIANDO NOSSA JANELA
tela = pygame.display.set_mode([600, 800])

# DEFININDO O RELÓGIO QUE VAI CONTAR OS FRAMES POR SEGUNDO
clock = pygame.time.Clock()

# CRIANDO UM QUADRADO QUE SERÁ EXIBIDO NA TELA
quadrado = pygame.Rect(100,  100,  50,  50)

# LOOP PRINCIPAL DO JOGO
executando = True
while executando:

	# VERIFICANDO EVENTOS
	for evento in pygame.event.get():

		# EVENTO DE FECHAR A TELA
		if evento.type == pygame.QUIT:
			executando = False

		# EVENTOS DE TECLA PRESSIONADA
		if evento.type == pygame.KEYDOWN:
			if evento.key == pygame.K_DOWN:
				quadrado.move_ip([0, 20])
			if evento.key == pygame.K_UP:
				quadrado.move_ip([0, -20])
			if evento.key == pygame.K_LEFT:
				quadrado.move_ip([-20, 0])
			if evento.key == pygame.K_RIGHT:
				quadrado.move_ip([20, 0])

	# ELEMENTOS DA TELA
	pygame.draw.rect(tela, (255, 0, 0), quadrado)

	# CONFIGURAÇÃO DE QUADROS
	clock.tick(27)
	pygame.display.update()

pygame.quit()