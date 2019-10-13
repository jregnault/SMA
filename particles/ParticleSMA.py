import random

from particles.Particle import Particle

class ParticleSMA:
    def __init__(self, environment, view, nbParticles, scheduling):
        self.environment = environment
        self.view = view
        self.scheduling = scheduling

        self.agentList = []
        self.observers = []

        for i in range(0,nbParticles):
            stepX = 0
            stepY = 0
            while stepX == 0 and stepY == 0:
                stepX = random.randint(-1,1)
                stepY = random.randint(-1,1)
            self.agentList.append(
                Particle(
                    environment,
                    random.randint(0,environment.width - 1),
                    random.randint(0,environment.height - 1),
                    (stepX,stepY))
            )
    
    def register(self, observer):
        self.observers.append(observer)