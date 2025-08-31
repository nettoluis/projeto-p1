import pygame
from jogador import Jogador

def criarJanela():
    pygame.init()

    largura, altura = 1080, 720
    screen = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("The Big Arrow")

    cor_fundo = (0, 0, 0)

    jogador = Jogador(largura / 2, altura / 2)
    all_sprites = pygame.sprite.Group(jogador)

    projeteis = []
    running = True
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        jogador.acao(keys)
        screen.fill(cor_fundo)
        all_sprites.update()
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

criarJanela()
