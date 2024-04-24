import sys
import pygame
import math
import time
import random
from Constants import Constants
from Jugador import Jugador
from Pilota import Pilota

pygame.init()

finestraJoc = pygame.display.set_mode((Constants.Dimensions.WIDTH, Constants.Dimensions.HEIGHT))
rellotge = pygame.time.Clock()

gameOver = False

# Crear jugadores
jugador1 = Jugador(Constants.Dimensions.MARGIN_TOP,
                   (Constants.Dimensions.HEIGHT - Constants.Dimensions.MARGIN_TOP - Constants.Dimensions.MARGIN_BOTTOM) / 2 - Constants.Dimensions.JUGADOR_HEIGHT / 2,
                   Constants.Dimensions.JUGADOR_WIDTH,
                   Constants.Dimensions.JUGADOR_HEIGHT,
                   Constants.Colors.JUGADOR1_COLOR)

jugador2 = Jugador(Constants.Dimensions.WIDTH - Constants.Dimensions.MARGIN_BOTTOM - Constants.Dimensions.JUGADOR_WIDTH,
                   (Constants.Dimensions.HEIGHT - Constants.Dimensions.MARGIN_TOP - Constants.Dimensions.MARGIN_BOTTOM) / 2 - Constants.Dimensions.JUGADOR_HEIGHT / 2,
                   Constants.Dimensions.JUGADOR_WIDTH,
                   Constants.Dimensions.JUGADOR_HEIGHT,
                   Constants.Colors.JUGADOR2_COLOR)

# Crear pilota
pilota = Pilota()
pilota.random_direction()  # Comenzar con una dirección aleatoria

def PintaObjetec():
    finestraJoc.fill(Constants.Colors.BACKGROUND)
    pygame.draw.rect(finestraJoc, Constants.Colors.RECTANGLE, (
    Constants.Dimensions.MARGIN_TOP, Constants.Dimensions.MARGIN_TOP,
    Constants.Dimensions.WIDTH - Constants.Dimensions.MARGIN_TOP - Constants.Dimensions.MARGIN_BOTTOM,
    Constants.Dimensions.HEIGHT - Constants.Dimensions.MARGIN_TOP - Constants.Dimensions.MARGIN_BOTTOM))

    # Pintar jugadores
    pygame.draw.rect(finestraJoc, jugador1.color, (jugador1.posX, jugador1.posY, jugador1.width, jugador1.height))
    pygame.draw.rect(finestraJoc, jugador2.color, (jugador2.posX, jugador2.posY, jugador2.width, jugador2.height))

    # Pintar pilota
    pygame.draw.circle(finestraJoc, pilota.color, (int(pilota.posX), int(pilota.posY)), Constants.Dimensions.PILOTA_SIZE)


def DetectaEvents():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    teclas = pygame.key.get_pressed()

    MueveJugador(jugador1, teclas, pygame.K_w, pygame.K_s)
    MueveJugador(jugador2, teclas, pygame.K_UP, pygame.K_DOWN)

def MueveJugador(jugador, teclas, tecla_arriba, tecla_abajo):
    if teclas[tecla_arriba]:
        jugador.posY -= jugador.velocidad
    if teclas[tecla_abajo]:
        jugador.posY += jugador.velocidad

    jugador.posY = max(Constants.Dimensions.MARGIN_TOP, min(jugador.posY, Constants.Dimensions.HEIGHT - Constants.Dimensions.MARGIN_BOTTOM - jugador.height))

def DetectaColisiones():
    # Colisión con el borde superior e inferior
    if pilota.posY <= Constants.Dimensions.MARGIN_TOP or pilota.posY >= Constants.Dimensions.HEIGHT - Constants.Dimensions.MARGIN_BOTTOM:
        pilota.velY = -pilota.velY

        # Si la pelota sale del margen azul, reaparece en el centro y se mueve en dirección opuesta
        if pilota.posX <= Constants.Dimensions.MARGIN_TOP or pilota.posX >= Constants.Dimensions.WIDTH - Constants.Dimensions.MARGIN_BOTTOM:
            pilota.reset()
            pilota.random_direction()
            pilota.velX = -pilota.velX

    # Colisión con los jugadores
    if (jugador1.posX < pilota.posX + Constants.Dimensions.PILOTA_SIZE and
            jugador1.posX + Constants.Dimensions.JUGADOR_WIDTH > pilota.posX and
            jugador1.posY < pilota.posY + Constants.Dimensions.PILOTA_SIZE and
            jugador1.posY + Constants.Dimensions.JUGADOR_HEIGHT > pilota.posY):
        pilota.velX = -pilota.velX
        pilota.increase_speed()

    if (jugador2.posX < pilota.posX + Constants.Dimensions.PILOTA_SIZE and
            jugador2.posX + Constants.Dimensions.JUGADOR_WIDTH > pilota.posX and
            jugador2.posY < pilota.posY + Constants.Dimensions.PILOTA_SIZE and
            jugador2.posY + Constants.Dimensions.JUGADOR_HEIGHT > pilota.posY):
        pilota.velX = -pilota.velX
        pilota.increase_speed()

while not gameOver:
    PintaObjetec()
    DetectaEvents()
    DetectaColisiones()
    pilota.move()
    rellotge.tick(60)
    pygame.display.update()
