import pygame

class Projectile:
    def __init__(self, x, y, dano, velocidade):
        self.x = x
        self.y = y
        self.dano = 5
        self.velocidade = 1

        self.largura = 32
        self.altura = 32
        self.cor = (255, 255, 255)
        self.rect = pygame.Rect(self.x, self.y, self.largura, self.altura)


    def draw(self, screen):
        self.rect.topleft = (self.x, self.y)
        pygame.draw.rect(screen, self.cor, self.rect)


    def move(self, x, y):
        if esquerda:
            self.x -= self.velocidade
        if direita:
            self.x += self.velocidade
        if cima: 
            self.y -= self.velocidade
        if baixo:
            self.y += self.velocidade
        
