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

    # Pintar jugadores y pelota usando el método Pinta
    jugador1.Pinta(finestraJoc)
    jugador2.Pinta(finestraJoc)
    pilota.Pinta(finestraJoc)


def DetectaEvents():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_w]:
        jugador1.MoureAmunt()
    if teclas[pygame.K_s]:
        jugador1.MoureAvall()
    if teclas[pygame.K_UP]:
        jugador2.MoureAmunt()
    if teclas[pygame.K_DOWN]:
        jugador2.MoureAvall()


def DetectaColisiones():
    # Colisión con el jugador1
    if (jugador1.posX < pilota.posX + Constants.Dimensions.PILOTA_SIZE and
        jugador1.posX + Constants.Dimensions.JUGADOR_WIDTH > pilota.posX - Constants.Dimensions.PILOTA_SIZE and
        jugador1.posY < pilota.posY + Constants.Dimensions.PILOTA_SIZE and
        jugador1.posY + Constants.Dimensions.JUGADOR_HEIGHT > pilota.posY - Constants.Dimensions.PILOTA_SIZE):
        pilota.velX = -pilota.velX
        pilota.increase_speed()

    # Colisión con el jugador2
    if (jugador2.posX < pilota.posX + Constants.Dimensions.PILOTA_SIZE and
        jugador2.posX + Constants.Dimensions.JUGADOR_WIDTH > pilota.posX - Constants.Dimensions.PILOTA_SIZE and
        jugador2.posY < pilota.posY + Constants.Dimensions.PILOTA_SIZE and
        jugador2.posY + Constants.Dimensions.JUGADOR_HEIGHT > pilota.posY - Constants.Dimensions.PILOTA_SIZE):
        pilota.velX = -pilota.velX
        pilota.increase_speed()


while not gameOver:
    PintaObjetec()
    DetectaEvents()
    DetectaColisiones()
    pilota.MovimientoPilota()
    rellotge.tick(60)
    pygame.display.update()
