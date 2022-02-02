import random

from particles.Particle import Particle


class ParticleSMA:
    def __init__(self, environment, view, nb_particles, scheduling, trace=False):
        self.environment = environment
        self.view = view
        self.scheduling = scheduling
        self.trace = trace

        self.agentList = []
        self.observers = []

        for i in range(0, nb_particles):
            step_x = 0
            step_y = 0
            while step_x == 0 and step_y == 0:
                step_x = random.randint(-1, 1)
                step_y = random.randint(-1, 1)
            self.agentList.append(
                Particle(
                    i,
                    environment,
                    random.randint(0, environment.width - 1),
                    random.randint(0, environment.height - 1),
                    step_x,
                    step_y)
            )
    
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
