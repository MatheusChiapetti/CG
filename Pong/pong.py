import pygame 
import sys

pygame.init()

# Criando as cores por meio do sistema RGB:
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)

# Define a altura e largura da tela:
largura = 800
altura = 600

screen = pygame.display.set_mode((largura, altura)) # Cria a tela com a largura e altura determinadas acima.
pygame.display.set_caption("Pong") # Define o nome da janela. 

# Definição da Raquete:
raquete_largura = 10 
raquete_altura = 60 # 10% da altura total da tela.

# Definição da Bola:
tamanho_bola = 10

# Posição das Raquetes (Player e PC) - Lembrar que o ponto de referência está no centro da raquete:
pc_x =  10 # É necessário levar em conta a largura da raquete.
pc_y = altura / 2 - raquete_altura / 2 # Aqui é necessário diminuir/desconsider a altura da raquete.
player_1_x = largura - 20 # Aqui é necessário levar em conta a distância entre a parede e a raquete (10), e a largura da raquete (10), logo 10 + 10 = 20.
player_1_y = altura / 2 - raquete_altura / 2

# Posição da Bola (Inicial) - Lembrar que o ponto de referência está no centro da bola:
bola_x = largura / 2 - tamanho_bola / 2 # É necessário levar em conta a largura da bola.
bola_y = altura / 2 - tamanho_bola / 2 # Aqui é necessário diminuir/desconsider a altura da bola.

raquete_altura_1_dy = 5
raquete_pc_dy = 5

clock = pygame.time.Clock()

rodando = True
# Loop para execução do código. 
while rodando:
    for event in pygame.event.get(): # Ao fechar a janela (pressionar o X), encerra a execução do código.
        if event.type == pygame.QUIT:
            rodando = False
    screen.fill(PRETO) # Define a cor do fundo (background).

    pygame.draw.ellipse(screen, BRANCO, (bola_x, bola_y, tamanho_bola, tamanho_bola)) 
    pygame.draw.rect(screen, BRANCO, (pc_x, pc_y, raquete_largura, raquete_altura)) # Função utilizada para criar a raquete do PC.
    pygame.draw.rect(screen, BRANCO, (player_1_x, player_1_y, raquete_largura, raquete_altura)) # Funçao utilizada para criar a raquete do Player.

    keys = pygame.key.get_pressed() # Função utilizada para ler as teclas do teclado.

    # Verifica se a tecla foi pressionada e se a altura está no mínimo da tela (0):
    if keys[pygame.K_UP] and player_1_y > 0:
        player_1_y -= raquete_altura_1_dy

    # Verifica se a tecla foi pressionada e se a altura está no máximo da tela (800):
    if keys[pygame.K_DOWN] and player_1_y < altura - raquete_altura:
        player_1_y += raquete_altura_1_dy

    pygame.display.flip() # A função 'flip' é usada para renderizar a tela. 
    clock.tick(120) # Define o FPS da tela.

pygame.quit()
sys.exit()