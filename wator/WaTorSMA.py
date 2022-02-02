import random

from wator.Fish import Fish
from wator.Shark import Shark


class WaTorSMA:
    def __init__(self, environment, view, scheduling, trace, nb_fishes, fish_breed_time, nb_sharks, shark_breed_time,
                 shark_starve_time):
        self.environment = environment
        self.view = view
        self.scheduling = scheduling
        self.trace = trace

        self.agentList = []
        self.birthList = []
        self.observers = []

        self.nextAgentId = 0

        for _ in range(0, nb_fishes):
            self.agentList.append(
                Fish(
                    self.nextAgentId,
                    environment,
                    random.randint(0, environment.width - 1),
                    random.randint(0, environment.height - 1),
                    (255, 255, 0, 255),
                    fish_breed_time
                )
            )
            self.nextAgentId += 1
        
        for _ in range(0, nb_sharks):
            self.agentList.append(
                Shark(
                    self.nextAgentId,
                    environment,
                    random.randint(0, environment.width - 1),
                    random.randint(0, environment.height - 1),
                    (253, 108, 158, 255),
                    shark_breed_time,
                    shark_starve_time
                )
            )
            self.nextAgentId += 1
    
    def register(self, observer):
        self.observers.append(observer)
    
    def notify(self):
        for o in self.observers:
            o.update(self)
    
    def run_turn(self):
        if self.scheduling == "random":
            a = random.choice(self.agentList)
            a.decide(self)
        else:
            if self.scheduling == "fair":
                random.shuffle(self.agentList)
            for a in self.agentList:
                a.decide(self)
        death_note = []
        nb_fishes = 0
        nb_sharks = 0
        for a in self.agentList:
            a.update(self)
            if not a.isAlive:
                death_note.append(a)
            else:
                if type(a) == Fish:
                    nb_fishes += 1
                else:
                    nb_sharks += 1
        for a in death_note:
            self.agentList.remove(a)
        for a in self.birthList:
            a.update(self)
            if a.isAlive:
                self.agentList.append(a)
        self.birthList = []
        print("Tick;" + str(nb_fishes) + ";" + str(nb_sharks))
