import pygame

class Jogador:
    def __init__(self, x, y):
        self.vida = 20
        self.x = x
        self.y = y  
        self.dano = 5
        self.velocidade = 1
        
        self.largura = 32
        self.altura = 32
        self.cor = (255, 141, 161)
        self.rect = pygame.Rect(self.x, self.y, self.largura, self.altura)

    
    def draw(self, screen):
        self.rect.topleft = (self.x, self.y)
        pygame.draw.rect(screen, self.cor, self.rect)

    def move(self, keys):
        pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.x -= self.velocidade
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.x += self.velocidade
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.y -= self.velocidade
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.y += self.velocidade


class Inimigo:
    def __init__(self, x, y,):
        self.vida = 5
        self.x = x
        self.y = y
        self.dano = 20
        self.velocidade = 0.6

        self.largura = 32
        self.altura = 32
        self.cor = (255, 255, 255)
        self.rect = pygame.Rect(self.x, self.y, self.largura, self.altura)


    def draw(self, screen):
        self.rect.topleft = (self.x, self.y)
        pygame.draw.rect(screen, self.cor, self.rect)


    def move(self, alvo):
        if alvo.x > self.x:
            self.x += self.velocidade
        if alvo.y > self.y:
            self.y += self.velocidade
        if alvo.x < self.x:
            self.x -= self.velocidade
        if alvo.y < self.y:
            self.y -= self.velocidade


