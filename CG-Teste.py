import sys
import pygame

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

tamanho_fonte = 50
fonte = pygame.font.SysFont(None,  tamanho_fonte)

texto = fonte.render("Matheus", True, BRANCO)
texto_rect1 = texto.get_rect(center=(400, 300))      # Centro
texto_rect2 = texto.get_rect(center=(400, 25))       # Centro-Superior
texto_rect3 = texto.get_rect(center=(400, 575))      # Centro-Inferior
texto_rect4 = texto.get_rect(center=(720, 300))      # Centro-Direita
texto_rect5 = texto.get_rect(center=(80, 300))       # Centro-Esquerda
texto_rect6 = texto.get_rect(center=(80, 25))        # Canto-Superior-Esquerdo
texto_rect7 = texto.get_rect(center=(720, 25))       # Canto-Superior-Direito
texto_rect8 = texto.get_rect(center=(80, 575))       # Canto-Inferior-Esquerdo
texto_rect9 = texto.get_rect(center=(720, 575))      # Canto-Inferior-Direito

# Loop Principal:
while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    tela.fill(AZUL_ESCURO)
    tela.blit(texto, texto_rect1)
    tela.blit(texto, texto_rect2)
    tela.blit(texto, texto_rect3)
    tela.blit(texto, texto_rect4)
    tela.blit(texto, texto_rect5)
    tela.blit(texto, texto_rect6)
    tela.blit(texto, texto_rect7)
    tela.blit(texto, texto_rect8)
    tela.blit(texto, texto_rect9)
    pygame.display.flip()