import sys
import pygame
import random

pygame.init()

# Configuração da tela: 
largura = 800
altura = 600

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Pygame")

PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
AZUL_CLARO = (0, 85, 255)
AZUL_ESCURO = (0, 32, 95)
ROSA = (255, 0, 208)
AMARELO = (237, 255, 0)
VERDE = (38, 255, 0)
VERMELHO = (255, 0, 0)

COR_FUNDO = (0, 30, 95)

tamanho_fonte = 50
fonte = pygame.font.SysFont(None,  tamanho_fonte)

texto = fonte.render("DVD", True, BRANCO)

texto_rect1 = texto.get_rect(center=(400, 300))      # Centro

texto_rect2 = texto.get_rect()        # Canto-Superior-Esquerdo
texto_rect2.left = 0
texto_rect2.top = 0

texto_rect3 = texto.get_rect()       # Canto-Superior-Direito
texto_rect3.right = 800
texto_rect3.top = 0

texto_rect4 = texto.get_rect()       # Canto-Inferior-Esquerdo
texto_rect4.left = 0
texto_rect4.bottom = 600

texto_rect5 = texto.get_rect()      # Canto-Inferior-Direito
texto_rect5.right = 800
texto_rect5.bottom = 600

texto_rect = texto.get_rect(center=(largura/2, altura/2))
#velocidade_x = 1
#velocidade_y = 1

velocidade_x = random.randint(-1, 1)
velocidade_y = random.randint(-1, 1)

while velocidade_x == 0:
    velocidade_x = random.randint(-1, 1)

while velocidade_y == 0:
    velocidade_y = random.randint(-1, 1)

v_x = 0
v_y = 0

r = 0
g = 0
b = 0

clock = pygame.time.Clock()

# Loop Principal:
while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    texto_rect.x += velocidade_x
    texto_rect.y += velocidade_y

    # Lado Direito (x): 
    if  texto_rect.right >= largura:
        velocidade_x = random.randint(-1, 1)
        velocidade_y = random.randint(-1, 1)
        v_x = velocidade_x 
        v_y = velocidade_y

        while velocidade_x == 1 and v_x == velocidade_x:
            velocidade_x = random.randint(-1, 1)

        while velocidade_y == 0 and v_y == velocidade_y:
            velocidade_y = random.randint(-1, 1)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)

        COR = (r, g, b)

        if COR == COR_FUNDO:
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)

            COR = (r, g, b)

        texto = fonte.render("DVD", True, COR)


    # Lado Esquerdo (x): 
    if texto_rect.left <= 0:
        velocidade_x = random.randint(-1, 1)
        velocidade_y = random.randint(-1, 1)
        v_x = velocidade_x
        v_y = velocidade_y

        while velocidade_x == -1 and v_x == velocidade_x:
            velocidade_x = random.randint(-1, 1)

        while velocidade_y == 0 and v_y == velocidade_y:
            velocidade_y = random.randint(-1, 1)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)

        COR = (r, g, b)

        if COR == COR_FUNDO:
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)

            COR = (r, g, b)

        texto = fonte.render("DVD", True, COR)

    # Lado Superior (y): 
    if texto_rect.top >= altura:
        velocidade_x = random.randint(-1, 1)
        velocidade_y = random.randint(-1, 1)
        v_x = velocidade_x
        v_y = velocidade_y

        while velocidade_x == 0 and v_x == velocidade_x:
            velocidade_x = random.randint(-1, 1)

        while velocidade_y == 1 and v_y == velocidade_y:
            velocidade_y = random.randint(-1, 1)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)

        COR = (r, g, b)

        if COR == COR_FUNDO:
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)

            COR = (r, g, b)
            
        texto = fonte.render("DVD", True, COR)

    # Lado Inferior (y):
    if texto_rect.bottom <= 0:
        velocidade_x = random.randint(-1, 1)
        velocidade_y = random.randint(-1, 1)
        v_x = velocidade_x
        v_y = velocidade_y

        while velocidade_x == 0 and v_x == velocidade_x:
            velocidade_x = random.randint(-1, 1)

        while velocidade_y == -1 and v_y == velocidade_y:
            velocidade_y = random.randint(-1, 1)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)

        COR = (r, g, b)
        
        if COR == COR_FUNDO:
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)

            COR = (r, g, b)
            
        texto = fonte.render("DVD", True, COR)
    
    clock.tick(250)
    tela.fill(COR_FUNDO)
    tela.blit(texto, texto_rect)
    pygame.display.flip()