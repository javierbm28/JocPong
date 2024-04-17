import sys
import pygame
from Constants import Constants
from Jugador import Jugador

pygame.init()

finestraJoc = pygame.display.set_mode((Constants.Dimensions.WIDTH, Constants.Dimensions.HEIGHT))
rellotge = pygame.time.Clock()

gameOver = False


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


def PintaObjetec():
    finestraJoc.fill(Constants.Colors.BACKGROUND)
    pygame.draw.rect(finestraJoc, Constants.Colors.RECTANGLE, (
    Constants.Dimensions.MARGIN_TOP, Constants.Dimensions.MARGIN_TOP,
    Constants.Dimensions.WIDTH - Constants.Dimensions.MARGIN_TOP - Constants.Dimensions.MARGIN_BOTTOM,
    Constants.Dimensions.HEIGHT - Constants.Dimensions.MARGIN_TOP - Constants.Dimensions.MARGIN_BOTTOM))

    # Pintar jugadores
    pygame.draw.rect(finestraJoc, jugador1.color, (jugador1.posX, jugador1.posY, jugador1.width, jugador1.height))
    pygame.draw.rect(finestraJoc, jugador2.color, (jugador2.posX, jugador2.posY, jugador2.width, jugador2.height))


def DetectaEvents():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


    teclas = pygame.key.get_pressed()


    if teclas[pygame.K_w]:
        jugador1.posY -= jugador1.velocidad
    if teclas[pygame.K_s]:
        jugador1.posY += jugador1.velocidad


    if teclas[pygame.K_UP]:
        jugador2.posY -= jugador2.velocidad
    if teclas[pygame.K_DOWN]:
        jugador2.posY += jugador2.velocidad


    jugador1.posY = max(Constants.Dimensions.MARGIN_TOP, min(jugador1.posY, Constants.Dimensions.HEIGHT - Constants.Dimensions.MARGIN_BOTTOM - jugador1.height))
    jugador2.posY = max(Constants.Dimensions.MARGIN_TOP, min(jugador2.posY, Constants.Dimensions.HEIGHT - Constants.Dimensions.MARGIN_BOTTOM - jugador2.height))


while not gameOver:
    PintaObjetec()
    DetectaEvents()

    rellotge.tick(60)
    pygame.display.update()

