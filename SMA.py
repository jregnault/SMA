import pygame
from pygame.locals import *
from configparser import ConfigParser
import random
import time

import View
import Agent
import Environment

class SMA:
    def __init__(self, env, view, nbParticles, scheduling):
        self.observers = []
        self.env = env
        self.view = view
        self.scheduling = scheduling
        self.agentList = []
        for _ in range(0,nbParticles):
            self.agentList.append(
                Agent.Agent(
                    self.env,
                    random.randint(0,self.env.width-1),
                    random.randint(0,self.env.height-1)
                )
            )

    def register(self,observer):
        self.observers.append(observer)

    def notify(self):
        for o in self.observers:
            o.update(self)
    
    def run(self, config):
        nbTours = config.getint("simulation","nbticks")
        delay = config.getfloat("simulation","delay")
        refresh = config.getint("simulation","refresh")
        stay_alive = False
        tick = 0
        if nbTours == 0:
            stay_alive = True
        while stay_alive or tick < nbTours:
            self.runTurn()
            for event in pygame.event.get():
                if event.type == QUIT:
                    stay_alive = False
            time.sleep(delay)
            if (tick % refresh == 0):
                self.notify()
    
    def runTurn(self):
        if self.scheduling == "fair":
            for a in sma.agentList:
                a.decide()

if __name__ == "__main__":
    config = ConfigParser()
    config.read("config.ini")

    gridSizeX = config.getint("env","gridSizeX")
    gridSizeY = config.getint("env","gridSizeY")

    env = Environment.Environment(
        gridSizeX,
        gridSizeY,
        config.getboolean("env","torus")
    )

    canvasSizeX = config.getint("view","canvassizex")
    canvasSizeY = config.getint("view","canvassizey")
    boxSize = (canvasSizeX/gridSizeX, canvasSizeY/gridSizeY)

    view = View.View(
        env,
        canvasSizeX,
        canvasSizeY,
        boxSize,
        config.getboolean("view","grid")
    )

    sma = SMA(env,view,config.getint("simulation","nbparticles"), config.get("simulation","scheduling"))
    sma.register(view)
    sma.run(config)
    