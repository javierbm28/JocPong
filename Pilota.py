import random
import math
from Constants import Constants

class Pilota:
    def __init__(self):
        self.posX = Constants.Dimensions.WIDTH // 2
        self.posY = Constants.Dimensions.HEIGHT // 2
        self.velX = 0
        self.velY = 0
        self.color = Constants.Colors.PILOTA_COLOR
        self.velocitat_inicial = 5

    def reset(self):
        self.posX = Constants.Dimensions.WIDTH // 2
        self.posY = Constants.Dimensions.HEIGHT // 2
        self.velX = 5
        self.velY = 5

    def random_direction(self):
        angles = [45, 135, 225, 315]  # Ángulos para las cuatro direcciones diagonales
        angle = random.choice(angles)
        self.velX = self.velocitat_inicial * round(math.cos(math.radians(angle)))
        self.velY = self.velocitat_inicial * round(math.sin(math.radians(angle)))

    def move(self):
        self.posX += self.velX
        self.posY += self.velY

    def check_collision(self):
        # Comprobar colisión con los bordes superior e inferior
        if self.posY <= Constants.Dimensions.MARGIN_TOP or self.posY >= Constants.Dimensions.HEIGHT - Constants.Dimensions.MARGIN_BOTTOM:
            self.velY = -self.velY

        # Comprobar colisión con los bordes izquierdo y derecho
        if self.posX <= Constants.Dimensions.MARGIN_TOP or self.posX >= Constants.Dimensions.WIDTH - Constants.Dimensions.MARGIN_BOTTOM:
            self.reset()  # Resetear la posición y velocidad cuando sale del margen azul

    def increase_speed(self):
        # Aumentar la velocidad en 1 unidad cada vez que se llama a este método
        self.velX = math.copysign(abs(self.velX) + 0.5, self.velX)
        self.velY = math.copysign(abs(self.velY) + 0.5, self.velY)
