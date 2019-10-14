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
    
    def runTurn(self):
        if self.scheduling == "random":
            a = random.choice(self.agentList)
            a.decide(self)
        else:
            if self.scheduling == "fair":
                random.shuffle(self.agentList)
            for a in self.agentList:
                a.decide(self)
        deathNote = []
        nbFishes = 0
        nbSharks = 0
        for a in self.agentList:
            a.update(self)
            if a.isAlive == False:
                deathNote.append(a)
            else:
                if type(a) == Fish:
                    nbFishes += 1
                else:
                    nbSharks += 1
        for a in deathNote:
            self.agentList.remove(a)
        for a in self.birthList:
            a.update(self)
            if a.isAlive:
                self.agentList.append(a)
        self.birthList = []
        print("Tick;" + str(nbFishes) + ";" + str(nbSharks))