from core.Agent import Agent


class ParticleAgent(Agent):
    """A simple bouncing particle"""

    def __init__(self, agent_id, environment, step_x=0, step_y=0):
        super().__init__(agent_id, environment, color=(150, 150, 150, 255))
        self.stepX = step_x
        self.stepY = step_y

    def decide(self, environment):
        (x, y) = environment.get_agent_position(self.agentId)
        next_x, next_y = x + self.stepX, y + self.stepY

        if environment.get_position(next_x, next_y) is None:
            environment.move_to(self, next_x, next_y)