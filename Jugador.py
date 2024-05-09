import pygame

from Constants import Constants
from ObjetoEscenario import ObjetoEscenario


class Jugador(ObjetoEscenario):
    def __init__(self, posX, posY, width, height, color):
        super().__init__(posX, posY, color)
        self.width = width
        self.height = height
        self.velocidad = 5
        self.puntos = 0

    def Pinta(self, superficie):
        pygame.draw.rect(superficie, self.color, (self.posX, self.posY, self.width, self.height))

    def MoureAmunt(self):
        self.posY -= self.velocidad
        # Asegurarse de que el jugador no salga del campo de juego
        self.posY = max(Constants.Dimensions.MARGIN_TOP, self.posY)

    def MoureAvall(self):
        self.posY += self.velocidad
        # Asegurarse de que el jugador no salga del campo de juego
        self.posY = min(Constants.Dimensions.HEIGHT - Constants.Dimensions.MARGIN_BOTTOM - self.height, self.posY)
