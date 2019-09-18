import pygame
from pygame.locals import *
import argparse

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
    parser = argparse.ArgumentParser()
    # Config
    parser.add_argument("agents", help="the amount of agents to create. default to 10", default=10, type=int)
    parser.add_argument("--resolution", help="the resolution of the windows in the format <width>x<height>. default to 800x600.", default="800x600")
    parser.add_argument("--isToric", help="If activated, the agents will teleport to the opposite border when reaching one.", action="store_true")

    parser.parse_args()
    width = 800
    height = 600
    isToric = False

    sma = SMA()
    view = View.View()
    env = Environment.Environment(width,height,isToric)
    sma.register(view)

    stay_alive = True
    while stay_alive:
        for event in pygame.event.get():
            if event.type == QUIT:
                stay_alive = False