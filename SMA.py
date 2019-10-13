import pygame
from pygame.locals import *
from configparser import ConfigParser
import random
import time
import logging

from core.Environment import Environment
from core.View import View

from particles.ParticleSMA import ParticleSMA
    
def run(sma, config):
    sma.notify()
    nbTours = config.getint("simulation","nbticks")
    delay = config.getfloat("simulation","delay")
    refresh = config.getint("simulation","refresh")
    stay_alive = False
    tick = 0
    if nbTours == 0:
        stay_alive = True
    while stay_alive or tick < nbTours:
        sma.runTurn()
        tick += 1
        print("Tick;" + str(tick))

        for event in pygame.event.get():
            if event.type == QUIT:
                stay_alive = False
                    
        time.sleep(delay)
        if (tick % refresh == 0):
            sma.notify()

if __name__ == "__main__":
    LOG_FORMAT = "[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s"
    LOG_LEVEL = logging.DEBUG
    logging.basicConfig(format=LOG_FORMAT, level=LOG_LEVEL)

    config = ConfigParser()
    config.read("config.ini")

    gridSizeX = config.getint("environment","gridSizeX")
    gridSizeY = config.getint("environment","gridSizeY")

    environment = Environment(
        gridSizeX,
        gridSizeY,
        config.getboolean("environment","torus")
    )

    grid = config.getboolean("view","grid")
    boxSize = config.getint("view","boxsize")

    view = View(
        environment,
        boxSize,
        grid
    )

    seed = config.getint("simulation","seed")
    if seed != 0:
        random.seed(seed)

    sma = ParticleSMA(environment,view,config.getint("particles","nbparticles"), config.get("simulation","scheduling"), config.getboolean("simulation","trace"))
    sma.register(view)
    run(sma, config)
    