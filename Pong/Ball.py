import pygame
import random


class Ball: 
    
    tamanho_bola = 10

    # Velocidade aleatória da bola
    velocidade_bola_x = random.randint(2,5)
    velocidade_bola_y = random.randint(2,5)
