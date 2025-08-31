import pygame

class Animacao(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.sheet = pygame.image.load('PNG/Swordsman_lvl3/With_shadow/Swordsman_lvl3_attack_with_shadow.png').convert_alpha()
        self.largura = 64
        self.altura = 64
        self.frame_attack = []
        self.atual = 0
        self.attack()

        self.image = self.frame_attack[self.atual]
        self.rect = self.image.get_rect()
        self.rect.topleft = (100, 100)

        self.contador = 0
        self.atacando = False
    def attack(self):
        for i in range(8):
            frame = self.sheet.subsurface((i * self.largura, 0, self.largura, self.altura))
            frame = pygame.transform.scale(frame, (self.largura * 4, self.altura * 4))
            self.frame_attack.append(frame)

    def atacar(self):
        self.atacando = True
        self.atual = 0

    def update(self):
        if self.atacando:
            self.contador += 1
            if self.contador % 5 == 0:
                self.atual += 1
                if self.atual >= len(self.frame_attack):
                    self.atual = 0
                    self.atacando = False
                self.image = self.frame_attack[self.atual]

class Jogador(Animacao):
    def __init__(self, x, y):
        super().__init__()
        self.vida = 20
        self.dano = 5
        self.velocidade = 10

        self.rect.topleft = (x, y)

    def acao(self, keys):
        esquerda, direita, cima, baixo = keys[pygame.K_LEFT] or keys[pygame.K_a],  keys[pygame.K_RIGHT] or keys[pygame.K_d],  keys[pygame.K_UP] or keys[pygame.K_w], keys[pygame.K_DOWN] or keys[pygame.K_s]
        if esquerda:
            self.rect.x -= self.velocidade
        if direita:
            self.rect.x += self.velocidade
        if cima:
            self.rect.y -= self.velocidade
        if baixo:
            self.rect.y += self.velocidade
        if keys[pygame.K_j]:
            self.atacar()
