import pygame
import random

class MovendoTexto:
    def __init__(self, texto, fonte_tamanho, largura, altura):
        self.font = pygame.font.SysFont(None, fonte_tamanho)
        self.texto = texto
        self.largura = largura
        self.altura = altura
        self.texto_surf = self.font.render(texto, True, (255, 255, 255))
        self.rect = self.texto_surf.get_rect(center=(largura/2, altura/2))
        
        self.velocidade_x = self.gerar_numero_nao_zero()
        self.velocidade_y = self.gerar_numero_nao_zero()
        
    def gerar_numero_nao_zero(self):
        numero = 0
        while numero == 0: 
            numero = random.randint(-1, 1)
        return numero
    
    def move(self):
        self.rect.x += self.velocidade_x
        self.rect.y += self.velocidade_y
         
        # Lado Esquerdo:
        if self.rect.left <= 0:
            self.velocidade_x = random.randint(0, 1)
            self.velocidade_y = random.randint(-1, 1)
            self.change_color()
            
        # Lado Direito: 
        if self.rect.right >= self.largura:
            self.velocidade_x = random.randint(-1, 0)
            self.velocidade_y = random.randint(-1, 1)
            self.change_color()
            
        # Lado Inferior:
        if self.rect.bottom <= 0:
            self.velocidade_x = random.randint(-1, 1)
            self.velocidade_y = random.randint(-1, 0)
            self.change_color()
            
        # Lado Superior:
        if self.rect.top >= self.altura: 
            self.velocidade_x = random.randint(-1, 1)
            self.velocidade_y = random.randint(0, 1)
            self.change_color()
            
    def change_color(self):
        cor_texto = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                
        self.texto_surf = self.font.render(self.texto, True, cor_texto)
        
    def draw(self, tela):
        tela.blit(self.texto_surf, self.rect)