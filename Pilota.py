import random
import math
import pygame
from Constants import Constants
from ObjetoEscenario import ObjetoEscenario

class Pilota(ObjetoEscenario):
    def __init__(self):
        super().__init__(Constants.Dimensions.WIDTH // 2, Constants.Dimensions.HEIGHT // 2, Constants.Colors.PILOTA_COLOR)
        self.velX = 0
        self.velY = 0
        self.size = Constants.Dimensions.PILOTA_SIZE
        self.velocitat_inicial = 5
        self.max_speed = 8
        self.random_direction()

    def random_direction(self):
        angles = [45, 135, 225, 315]
        angle = random.choice(angles)
        self.velX = self.velocitat_inicial * round(math.cos(math.radians(angle)))
        self.velY = self.velocitat_inicial * round(math.sin(math.radians(angle)))

    def Pinta(self, superficie):
        pygame.draw.circle(superficie, self.color, (int(self.posX), int(self.posY)), self.size)

    def reset(self):
        self.posX = Constants.Dimensions.WIDTH // 2
        self.posY = Constants.Dimensions.HEIGHT // 2
        self.random_direction()

    def MovimientoPilota(self):
        self.posX += self.velX
        self.posY += self.velY
        self.check_collision()

    def check_collision(self):
        # Colisión con los bordes superior e inferior
        if self.posY - self.size <= Constants.Dimensions.MARGIN_TOP or self.posY + self.size >= Constants.Dimensions.HEIGHT - Constants.Dimensions.MARGIN_BOTTOM:
            self.velY = -self.velY

        # Colisión con los bordes izquierdo y derecho
        if self.posX - self.size <= Constants.Dimensions.MARGIN_TOP or self.posX + self.size >= Constants.Dimensions.WIDTH - Constants.Dimensions.MARGIN_BOTTOM:
            self.reset()

    def increase_speed(self):
        # Aumentar la velocidad en 0.5 unidades cada vez que se llama a este método, hasta un máximo de 8
        if abs(self.velX) < self.max_speed:
            self.velX = math.copysign(abs(self.velX) + 0.5, self.velX)
        if abs(self.velY) < self.max_speed:
            self.velY = math.copysign(abs(self.velY) + 0.5, self.velY)
