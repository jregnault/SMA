class Environment:

    def __init__(self, width=100, height=100, isToric=False):
        self.width = width
        self.height = height
        self.isToric = isToric
        self.agents = []
    
    