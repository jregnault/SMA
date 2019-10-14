import random

from wator.Fish import Fish
from wator.Shark import Shark

class WaTorSMA:
    def __init__(self, environment, view, scheduling, trace, nbFishes, fishBreedTime, nbSharks, sharkBreedTime, sharkStarveTime):
        self.environment = environment
        self.view = view
        self.scheduling = scheduling
        self.trace = trace

        self.agentList = []
        self.birthList = []
        self.observers = []

        self.nextAgentId = 0

        for _ in range(0, nbFishes):
            self.agentList.append(
                Fish(
                    self.nextAgentId,
                    environment,
                    random.randint(0,environment.width - 1),
                    random.randint(0,environment.height - 1),
                    (255,255,0,255),
                    fishBreedTime
                )
            )
            self.nextAgentId += 1
        
        for _ in range(0, nbSharks):
            self.agentList.append(
                Shark(
                    self.nextAgentId,
                    environment,
                    random.randint(0,environment.width - 1),
                    random.randint(0, environment.height - 1),
                    (253,108,158,255),
                    sharkBreedTime,
                    sharkStarveTime
                )
            )
            self.nextAgentId += 1
    
    def register(self, observer):
        self.observers.append(observer)
    
    def notify(self):
        for o in self.observers:
            o.update(self)
    
    