import random

class Individual:
	# Updates the fitness value based on the genom and the map.
    def updateFitness(self):
        #TODO implement fitness function
        #how many violations?
        num = 0
        for border in self.map.borders:
            s1 = self.genome[self.map.states[border.index1]] #color 1
            s2 = self.genome[self.map.states[border.index2]] #color 2
            if s1 != s2:
                num += 1
        self.fitness=num 

    def random_individual(self):
        # TODO implement random generation of an individual
        self.genome = {state: random.randint(1, 4) for state in self.map.states}  # Assuming 4 colors

    def updateDomains(self):
        for state in self.map.states:
            if self.genome[state] == 0:
                self.domains[state] = [1, 2, 3, 4]  # All colors are possible by default
            else:
                self.domains[state] = [self.genome[state]]  # Assigned color is the only choice

    def __init__(self,map):
        self.map=map# the map
        self.fitness=0
        self.domains = {}  # Domain for each state (possible color choices)
        self.variables = [1,2,3,4]
        self.constraints = [(state_A, state_B) for state_A in self.map.states for state_B in self.map.neighbors[state_A]]
        # TODO some representation of the genome of the individual
        # TODO implement random generation of an individual
        self.random_individual()
        self.updateFitness()
        self.updateDomains()

    def set_zero(self):
        for key in self.genome.keys():
            self.genome[key] = 0

    def backtrack(self):
        if self.isGoal() and all(self.genome[key] != 0 for key in self.genome.keys()):
            print('Goal')
            return True

        state = self.selectUnassignedState()
        if state is None:
                return True # All states are assigned colors

        for color in self.domains[state]:
            if self.isColorValid(state, color):
                prev_color = self.genome[state]
                self.genome[state] = color
                self.updateDomains()
                self.updateFitness()

                if self.backtrack():
                    return True

                self.genome[state] = prev_color  # Backtrack
                self.updateDomains()

        return False
    
    def forwardCheck(self):
        for state in self.map.states:
            if self.genome[state] == 0:
                for neighbor in self.map.neighbors[state]:
                    if self.genome[neighbor] == self.genome[state]:
                        if self.genome[state] in self.domains[state]:
                            self.domains[state].remove(self.genome[state])  # Remove the color from the domain
                if not self.domains[state]:  # If the domain is empty, no valid colors remain
                    return False
        return True

    
    def FWDbacktrack(self):
        if self.isGoal():
            return True

        state = self.selectUnassignedState()
        if state is None:
            return True  # All states are assigned colors

        for color in self.domains[state]:
            if self.isColorValid(state, color):
                self.genome[state] = color  # Assign a valid color to the state
                self.updateDomains()
                self.updateFitness()

                if self.forwardCheck():  # Check if forward checking leads to a valid solution
                    if self.backtrack():  # Recursively backtrack
                        return True

                self.genome[state] = 0  # Backtrack by resetting the color to 0 (unassigned)
                self.updateDomains()

        return False
    
    def selectUnassignedState(self):
        for state in self.map.states:
            if self.genome[state] == 0:
                return state
        return None  # All states are assigned colors
    
    def isColorValid(self, state, color):
        for neighbor in self.map.neighbors[state]:
            if self.genome[neighbor] == color:
                return False  # Invalid color assignment due to neighbors
        return True
        

    # Reproduces a child randomly from two individuals (see textbook).
	# x The first parent.
	# y The second parent.
	# return The child created from the two individuals.
    def reproduce(self, x, y):
        child = Individual(x.map)
        # TODO: Implement the reproduction process to create a child from parents x and y.
        # For example, you can perform one-point crossover.
        crossover_point = random.randint(1, len(self.map.states) - 1)
        for i, state in enumerate(self.map.states):
            if i < crossover_point:
                child.genome[state] = x.genome[state]
            else:
                child.genome[state] = y.genome[state]
        child.updateFitness()
        return child

	# Randomly mutates the individual.
    def mutate(self):
        # TODO implement random mutation of the individual
        state_to_mutate = random.choice(list(self.map.states))
        new_color = random.randint(1, 4)  # Assuming 4 colors
        self.genome[state_to_mutate] = new_color
        self.updateFitness()

	# Checks whether the individual represents a valid goal state.
	# return Whether the individual represents a valid goal state.
    def isGoal(self):
        return self.fitness == len(self.map.borders)

    def printresult(self):
        # TODO implement printing the individual in the following format:
        # fitness: 15
        # North Carolina: 0
        # South Carolina: 2
        # ...
        dict = {
            0:'N/A',
            1:'Red',
            2:'Blue',
            3:'Yellow',
            4:'Green'
        }
        print("Your result:")
        print("Fitness Rating: ", self.fitness)
        for key, value in self.genome.items():
            print(key, ": ", dict[value])

