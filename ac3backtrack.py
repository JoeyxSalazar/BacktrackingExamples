import random

class ac3bt:
    def __init__(self, ind):
        self.i = ind
        
    
    def ac3(self):
        # Initialize a queue with all constraints
        queue = [(state_A, state_B) for state_A in self.i.map.states for state_B in self.i.map.neighbors[state_A]]
        while queue:
            state_X, state_Y = queue.pop(0)
            if self.revise(state_X, state_Y):
                if len(self.i.domains[state_X]) == 0:
                    return False  # Inconsistent assignment
                for neighbor in self.i.map.neighbors[state_X]:
                    if neighbor != state_Y:
                        queue.append((neighbor, state_X))
        return True  # domains are consistent

    def revise(self, state_X, state_Y):
        revised = False
        for color_X in self.i.domains[state_X][:]:
            if not any(self.i.isColorValid(state_Y, color_Y) for color_Y in self.i.domains[state_Y]):
                self.i.domains[state_X].remove(color_X)
                revised = True
        return revised

    def backtrack(self):
        if self.i.isGoal() and all(self.i.genome[key] != 0 for key in self.i.genome.keys()):
            print('Goal')
            return True

        state = self.i.selectUnassignedState()
        if state is None:
                return True # All states are assigned 

        for color in self.i.domains[state]:
            if self.i.isColorValid(state, color):
                prev_color = self.i.genome[state]
                self.i.genome[state] = color
                self.i.updateDomains()
                self.i.updateFitness()

                if self.ac3():  
                    if self.backtrack():  # Recursively backtrack
                        return True

                self.i.genome[state] = prev_color  # Backtrack
                self.i.updateDomains()

        return False
