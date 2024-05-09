import sys
import pygame
import math
import time
import random
from Constants import Constants
from Jugador import Jugador
from Pilota import Pilota


pygame.init()
pygame.font.init()

fontText = pygame.font.SysFont("monospace", 35)

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
pilota = Pilota(jugador1, jugador2)
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

    # Preparar el texto con los puntos de cada jugador
    textJugador1 = "Jugador 1: " + str(jugador1.puntos)
    textJugador2 = "Jugador 2: " + str(jugador2.puntos)

    # Renderizar y mostrar los puntos utilizando antialiasing y el color adecuado
    etiquetaJugador1 = fontText.render(textJugador1, 1, Constants.Colors.JUGADOR1_COLOR)
    etiquetaJugador2 = fontText.render(textJugador2, 1, Constants.Colors.JUGADOR2_COLOR)

    # Situar las etiquetas en la pantalla
    finestraJoc.blit(etiquetaJugador1, (10, 10))  # Posición arriba a la izquierda para el Jugador 1
    finestraJoc.blit(etiquetaJugador2, (Constants.Dimensions.WIDTH - etiquetaJugador2.get_width() - 10,
                                        10))  # Posición arriba a la derecha para el Jugador 2

    if pilota.paused:
        elapsed_time = (pygame.time.get_ticks() - pilota.pause_start_time) / 1000
        remaining_time = max(0, pilota.pause_duration - int(elapsed_time))
        countdown_text = fontText.render(str(remaining_time), True, (0, 0, 0))  # Cambio a color negro para visibilidad
        text_rect = countdown_text.get_rect(center=(Constants.Dimensions.WIDTH / 2, Constants.Dimensions.HEIGHT / 2))
        finestraJoc.blit(countdown_text, text_rect)


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
    pilota.update_after_pause()
    if not pilota.paused:
        pilota.MovimientoPilota()
    rellotge.tick(60)
    pygame.display.update()
