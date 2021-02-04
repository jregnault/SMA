from core.Agent import Agent


class ParticleAgent(Agent):
    """A simple bouncing particle"""

    def __init__(self, agent_id, environment, step_x=0, step_y=0):
        super().__init__(agent_id, environment, color=(150, 150, 150, 255))
        self.stepX = step_x
        self.stepY = step_y
