import pygame
import sys
from MecMovimento import MovendoTexto
# Acima, a classe 'Game' herda a classe 'MovendoTexto'.

class Game:
    # A função abaixo é utilizada para construir a classe game. Não há atributos no construtor pois a classe 'Game' herda os atributos da classe 'MovendoTexto'.
    def __init__(self): 
        pygame.init()
        self.largura = 800 # Determina a largua da tela.
        self.altura = 600  # Determina a altura da tela. 
        self.tela = pygame.display.set_mode((self.largura, self.altura)) # Função utilizada para criar a tela do jogo.
        pygame.display.set_caption("Bate-Bate") # Determina o nome da tela.
        self.clock = pygame.time.Clock() # Define o objeto clock que determina a quantidade de quadros (FPS).
        self.MovendoTexto = MovendoTexto("DVD", 50, self.largura, self.altura) # Cria o objeto, com altura e largura própria, que ficará 'batendo' pela tela. 
        
    # Função utilizada para rodar o jogo. Ela é disparada ao se criar um objeto do tipo Game no main.
    def run(self):
        rodando = True
        while rodando: 
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    rodando = False

            self.MovendoTexto.move() # Move o objeto puxando a função 'move' da classe MecMovimento.
            self.tela.fill((0, 0, 0)) # Determina que a cor de fundo da tela.
            self.tela.blit(self.MovendoTexto.texto_surf, self.MovendoTexto.rect) # A função 'blit' atualiza a tela. 
            pygame.display.flip() # A funçao 'flip' renderiza a tela. 
            self.clock.tick(120) # Determina o tempo de tick da tela, que impactará a velocidade do objeto (FPS).
        pygame.quit()
        sys.exit()
    