# Author Fan Zhang
class Map:
    def updateNeighbors(self):
        self.neighbors = {state: [] for state in self.states}

        for border in self.borders:
            state1 = self.states[border.index1]
            state2 = self.states[border.index2]

            # Add each state as a neighbor to the other
            self.neighbors[state1].append(state2)
            self.neighbors[state2].append(state1)
            

        pass
    def __init__(self):
        self.borders = []
        self.states = []
        self.neighbors = {}
        self.updateNeighbors()

    