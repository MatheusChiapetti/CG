import pygame
import random

# Observa-se que a classe 'MovendoTexto' não importa nenhuma outra classe do projeto.

class MovendoTexto:
    # Função para construir a classe 'MovendoTexto'.
    def __init__(self, texto, fonte_tamanho, largura, altura): # Os atributos da classe são: self, texto, fonte_tamanho, largura e altura. 
        self.font = pygame.font.SysFont(None, fonte_tamanho) # Atribui à fonte o tamanho informado pelo usuário.
        self.texto = texto # Atribui o texto informado pelo usuário.
        self.largura = largura # Atribui à tela a largura informada pelo usuário.
        self.altura = altura # Atribui à tela a altura informada pelo usuário.
        self.texto_surf = self.font.render(texto, True, (255, 255, 255))
        self.rect = self.texto_surf.get_rect(center=(largura/2, altura/2))
        
        self.velocidade_x = self.gerar_numero_nao_zero()
        self.velocidade_y = self.gerar_numero_nao_zero()
        
    # Função para gerar um número que não seja 0.
    def gerar_numero_nao_zero(self):
        numero = 0

        # Enquanto a variável 'numero' foi igual a 0, o sistema irá sorter um número inteiro entre -1 e 1. O código sairá do loop apenas quando a variável 'numero' for diferente de 0.
        while numero == 0: 
            numero = random.randint(-1, 1)
        return numero
    
    def move(self):
        # Abaixo, soma-se +1 aos valores das velocidades do objeto nos eixos x e y.
        self.rect.x += self.velocidade_x
        self.rect.y += self.velocidade_y
         
        # Lado Esquerdo:
        if self.rect.left <= 0: 
            # Caso o valor do lado esquerdo seja menor ou igual a 0, o sistema sorteará um novo valor para as velocidades em x e y. 
            # O valor de x, nesse caso, não pode ser -1. Se for -1, o texto sairá da tela. 
            self.velocidade_x = random.randint(0, 1) 
            self.velocidade_y = random.randint(-1, 1)
            self.change_color()
            
        # Lado Direito: 
        if self.rect.right >= self.largura:
            # Caso o valor do lado esquerdo seja menor ou igual a largura da tela, o sistema sorteará um novo valor para as velocidades em x e y. 
            # O valor de x, nesse caso, não pode ser 1. Se for 1, o texto sairá da tela. 
            self.velocidade_x = random.randint(-1, 0)
            self.velocidade_y = random.randint(-1, 1)
            self.change_color()
            
        # Lado Inferior:
        if self.rect.bottom >= self.altura:
            # Caso o valor do lado inferior seja menor ou igual a altura da tela, o sistema sorteará um novo valor para as velocidades em x e y. 
            # O valor de y, nesse caso, não pode ser 1. Se for 1, o texto sairá da tela. 
            self.velocidade_x = random.randint(-1, 1)
            self.velocidade_y = random.randint(-1, 0)
            self.change_color()
            
        # Lado Superior:
        if self.rect.top <= 0: 
            # Caso o valor do lado superior seja menor ou igual a 0, o sistema sorteará um novo valor para as velocidades em x e y. 
            # O valor de y, nesse caso, não pode ser -1. Se for -1, o texto sairá da tela. 
            self.velocidade_x = random.randint(-1, 1)
            self.velocidade_y = random.randint(0, 1)
            self.change_color()
            
    # A função abaixo sorteia uma nova cor para o objeto dentro do expectro RGB toda vez que ele se choca com uma das paredes da tela (Superior, Inferior, Esquerda ou Direita).
    def change_color(self):

        # Os valores são sorteados dentro do intervalo de 0 até 255, e uma nova cor é montada.
        cor_texto = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                
        self.texto_surf = self.font.render(self.texto, True, cor_texto)
        
    # A função 
    def draw(self, tela):
        tela.blit(self.texto_surf, self.rect) # # A função 'blit' atualiza (desenha) a variável. 