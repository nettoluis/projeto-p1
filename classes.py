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
        self.cor = (255, 255, 255)
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
        self.image = pygame.image.load('assets/mobDir.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.rect = self.image.get_rect(center=(x, y))

    def draw(self, screen):
        screen.blit(self.image, self.rect)


    def move(self, alvo):
        dx, dy = alvo.rect.x - self.rect.x, alvo.rect.y - self.rect.y
        dist = (dx ** 2 + dy ** 2) ** 0.5
        if dist > 0:
            self.rect.x += self.velocidade * dx / dist
            self.rect.y += self.velocidade * dy / dist
