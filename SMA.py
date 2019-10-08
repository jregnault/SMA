import pygame
from pygame.locals import *
from configparser import ConfigParser
import random
import time

import View
import Agent
import Environment

class ParticlesSMA:
    def __init__(self, environment, view, nbParticles, scheduling):
        self.observers = []
        self.environment = environment
        self.view = view
        self.scheduling = scheduling
        self.agentList = []
        for _ in range(0,nbParticles):
            self.agentList.append(
                Agent.Agent(
                    self.environment,
                    random.randint(0,self.environment.width-1),
                    random.randint(0,self.environment.height-1),
                    random.randint(-1,1),
                    random.randint(-1,1)
                )
            )

    def register(self,observer):
        self.observers.append(observer)

    def notify(self):
        for o in self.observers:
            o.update(self)
    
    def run(self, config):
        self.notify()
        nbTours = config.getint("simulation","nbticks")
        delay = config.getfloat("simulation","delay")
        refresh = config.getint("simulation","refresh")
        stay_alive = False
        tick = 0
        if nbTours == 0:
            stay_alive = True
        while stay_alive or tick < nbTours:
            self.runTurn()
            tick += 1
            print("Tick;" + str(tick))

            for event in pygame.event.get():
                if event.type == QUIT:
                    stay_alive = False
                    
            time.sleep(delay)
            if (tick % refresh == 0):
                self.notify()
    
    def runTurn(self):
        if self.scheduling == "fair":
            random.shuffle(self.agentList)
            for a in self.agentList:
                a.decide()
        elif self.scheduling == "sequential":
            for a in self.agentList:
                a.decide()
        elif self.scheduling == "random":
            a = random.choice(self.agentList)
            a.decide()

if __name__ == "__main__":
    config = ConfigParser()
    config.read("config.ini")

    gridSizeX = config.getint("environment","gridSizeX")
    gridSizeY = config.getint("environment","gridSizeY")

    environment = Environment.Environment(
        gridSizeX,
        gridSizeY,
        config.getboolean("environment","torus")
    )

    grid = config.getboolean("view","grid")
    boxSize = config.getint("view","boxsize")
    canvasSizeX = gridSizeX * boxSize
    canvasSizeY = gridSizeY * boxSize
    if grid:
        canvasSizeX += gridSizeX + 1
        canvasSizeY += gridSizeY + 1
    

    view = View.View(
        environment,
        canvasSizeX,
        canvasSizeY,
        boxSize,
        grid
    )

    seed = config.getint("simulation","seed")
    if seed != 0:
        random.seed(seed)

    sma = ParticlesSMA(environment,view,config.getint("particules","nbparticles"), config.get("simulation","scheduling"))
    sma.register(view)
    sma.run(config)
    