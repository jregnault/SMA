import pygame
from pygame.locals import *
from configparser import ConfigParser

import View
import Agent
import Environment

class SMA:
    def __init__(self):
        self.observers = []

    def register(self,observer):
        self.observers.append(observer)

    def notify(self):
        for o in self.observers:
            o.update()
    
    def init(self):
        pass
    
    def run(self, nbTours):
        pass

if __name__ == "__main__":
    config = ConfigParser()
    config.read("config.ini")
    torus = config.getboolean("settings","torus")
    gridSizeX = config.getint("settings","gridsizex")
    gridSizeY = config.getint("settings","gridsizey")
    canvasSizeX = config.getint("settings","canvassizex")
    canvasSizeY = config.getint("settings","canvassizey")
    boxSize = config.getint("settings","boxsize")
    delay = config.getint("settings","delay")
    scheduling = config.get("settings","scheduling")
    nbTicks = config.getint("settings","nbticks")
    grid = config.getboolean("settings","grid")
    trace = config.getboolean("settings","trace")
    seed = config.getint("settings","seed")
    refresh = config.getint("settings","refresh")
    nbParticles = config.getint("settings","nbparticles")
    
    sma = SMA()
    view = View.View()
    env = Environment.Environment(config.getint("settings","gridSizeX"), config.getint("settings","gridSizeY"), config.getboolean("settings","torus"))
    sma.register(view)

    stay_alive = True
    while stay_alive:
        for event in pygame.event.get():
            if event.type == QUIT:
                stay_alive = False