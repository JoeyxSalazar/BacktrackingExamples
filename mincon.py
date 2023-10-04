import random 

class mc:
    def __init__(self, ind):
        self.i = ind
        pass

    def min_conflicts(self, max_iterations, num_mutate):
      for j in range(max_iterations):
          conflicts = self.get_conflicts()
          if conflicts == 0:
              return True  # Solution found
          variable = self.select_variable_with_conflicts(conflicts)
          value = self.select_value_minimizing_conflicts(variable)
          self.i.genome[variable] = value
          self.i.updateFitness()
          if j % num_mutate == 0: #Exit local minima
              self.i.mutate()
      return False  # No solution found within the max_iterations

    def get_conflicts(self):
        conflicts = 0
        for border in self.i.map.borders:
            s1 = self.i.genome[self.i.map.states[border.index1]]
            s2 = self.i.genome[self.i.map.states[border.index2]]
            if s1 == s2:
                conflicts += 1
        return conflicts
    
    def has_conflicts(self, state):
        state_idx = self.i.map.states.index(state)
        for border in self.i.map.borders:
            if state_idx == border.index1 or state_idx == border.index2:
                s1 = self.i.genome[self.i.map.states[border.index1]]
                s2 = self.i.genome[self.i.map.states[border.index2]]
                if s1 == s2:
                    return True
        return False

    def select_variable_with_conflicts(self, conflicts):
        conflicted_variables = [state for state in self.i.map.states if self.has_conflicts(state)]
        return random.choice(conflicted_variables)

    def select_value_minimizing_conflicts(self, variable):
        current_color = self.i.genome[variable]
        neighbor_colors = set(self.i.genome[state] for state in self.i.map.neighbors[variable])
        neighbor_colors.discard(current_color)

        best_color = current_color
        best_conflicts = self.get_conflicts()

        for color in neighbor_colors:
            self.i.genome[variable] = color
            conflicts = self.get_conflicts()

            # update best
            if conflicts < best_conflicts:
                best_color = color
                best_conflicts = conflicts

        # Restore
        self.i.genome[variable] = current_color
        return best_color
 