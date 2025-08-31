import pygame
from classes import Jogador
from classes import Inimigo


def criarJanela():
    pygame.init()

    largura, altura = 1080, 720
    screen = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("The Big Arrow")

    cor_fundo = (127, 127, 255)

    jogador = Jogador(largura / 2, altura / 2)
    inimigo1 = Inimigo(largura / 108, altura / 2)

    projeteis = []
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        jogador.move(keys)
        inimigo1.move(jogador)
        screen.fill(cor_fundo)
        jogador.draw(screen)
        inimigo1.draw(screen)
        pygame.display.flip()

    pygame.quit()

criarJanela()
