import random
import time
from Border import Border
from Individual import Individual
from Map import Map
from Population import Population
from mincon import mc
from supp import make_lists10, make_lists
from ac3backtrack import ac3bt
import networkx as nx
import matplotlib.pyplot as plt



# Author Fan Zhang
def init51(map):
    map.states.append("AK")
    map.states.append("AL")
    map.states.append("AR")
    map.states.append("AZ")
    map.states.append("CA")
    map.states.append("CO")
    map.states.append("CT")
    map.states.append("DC")
    map.states.append("DE")
    map.states.append("FL")
    map.states.append("GA")
    map.states.append("HI")
    map.states.append("IA")
    map.states.append("ID")
    map.states.append("IL")
    map.states.append("IN")
    map.states.append("KS")
    map.states.append("KY")
    map.states.append("LA")
    map.states.append("MA")
    map.states.append("MD")
    map.states.append("ME")
    map.states.append("MI")
    map.states.append("MN")
    map.states.append("MO")
    map.states.append("MS")
    map.states.append("MT")
    map.states.append("NC")
    map.states.append("ND")
    map.states.append("NE")
    map.states.append("NH")
    map.states.append("NJ")
    map.states.append("NM")
    map.states.append("NV")
    map.states.append("NY")
    map.states.append("OH")
    map.states.append("OK")
    map.states.append("OR")
    map.states.append("PA")
    map.states.append("RI")
    map.states.append("SC")
    map.states.append("SD")
    map.states.append("TN")
    map.states.append("TX")
    map.states.append("UT")
    map.states.append("VA")
    map.states.append("VT")
    map.states.append("WA")
    map.states.append("WI")
    map.states.append("WV")
    map.states.append("WY")

    map.borders.append(Border(0, 47))
    map.borders.append(Border(1, 42))
    map.borders.append(Border(1, 10))
    map.borders.append(Border(1, 9))
    map.borders.append(Border(1, 25))
    map.borders.append(Border(2, 24))
    map.borders.append(Border(2, 42))
    map.borders.append(Border(2, 25))
    map.borders.append(Border(2, 18))
    map.borders.append(Border(2, 43))
    map.borders.append(Border(2, 36))
    map.borders.append(Border(3, 44))
    map.borders.append(Border(3, 5))
    map.borders.append(Border(3, 32))
    map.borders.append(Border(3, 4))
    map.borders.append(Border(3, 33))
    map.borders.append(Border(4, 37))
    map.borders.append(Border(4, 33))
    map.borders.append(Border(4, 3))
    map.borders.append(Border(4, 11))
    map.borders.append(Border(5, 50))
    map.borders.append(Border(5, 29))
    map.borders.append(Border(5, 16))
    map.borders.append(Border(5, 36))
    map.borders.append(Border(5, 32))
    map.borders.append(Border(5, 3))
    map.borders.append(Border(5, 44))
    map.borders.append(Border(6, 19))
    map.borders.append(Border(6, 39))
    map.borders.append(Border(6, 34))
    map.borders.append(Border(7, 20))
    map.borders.append(Border(7, 45))
    map.borders.append(Border(8, 38))
    map.borders.append(Border(8, 31))
    map.borders.append(Border(8, 20))
    map.borders.append(Border(9, 10))
    map.borders.append(Border(9, 1))
    map.borders.append(Border(10, 27))
    map.borders.append(Border(10, 40))
    map.borders.append(Border(10, 9))
    map.borders.append(Border(10, 1))
    map.borders.append(Border(10, 42))
    map.borders.append(Border(11, 4))
    map.borders.append(Border(12, 23))
    map.borders.append(Border(12, 48))
    map.borders.append(Border(12, 14))
    map.borders.append(Border(12, 24))
    map.borders.append(Border(12, 29))
    map.borders.append(Border(12, 41))
    map.borders.append(Border(13, 26))
    map.borders.append(Border(13, 50))
    map.borders.append(Border(13, 44))
    map.borders.append(Border(13, 33))
    map.borders.append(Border(13, 37))
    map.borders.append(Border(13, 47))
    map.borders.append(Border(14, 15))
    map.borders.append(Border(14, 17))
    map.borders.append(Border(14, 24))
    map.borders.append(Border(14, 12))
    map.borders.append(Border(14, 48))
    map.borders.append(Border(15, 22))
    map.borders.append(Border(15, 35))
    map.borders.append(Border(15, 17))
    map.borders.append(Border(15, 14))
    map.borders.append(Border(16, 29))
    map.borders.append(Border(16, 24))
    map.borders.append(Border(16, 36))
    map.borders.append(Border(16, 5))
    map.borders.append(Border(17, 35))
    map.borders.append(Border(17, 49))
    map.borders.append(Border(17, 45))
    map.borders.append(Border(17, 42))
    map.borders.append(Border(17, 24))
    map.borders.append(Border(17, 14))
    map.borders.append(Border(17, 15))
    map.borders.append(Border(18, 2))
    map.borders.append(Border(18, 25))
    map.borders.append(Border(18, 43))
    map.borders.append(Border(19, 30))
    map.borders.append(Border(19, 39))
    map.borders.append(Border(19, 6))
    map.borders.append(Border(19, 34))
    map.borders.append(Border(19, 46))
    map.borders.append(Border(20, 38))
    map.borders.append(Border(20, 8))
    map.borders.append(Border(20, 7))
    map.borders.append(Border(20, 45))
    map.borders.append(Border(20, 49))
    map.borders.append(Border(21, 30))
    map.borders.append(Border(22, 35))
    map.borders.append(Border(22, 15))
    map.borders.append(Border(22, 48))
    map.borders.append(Border(23, 48))
    map.borders.append(Border(23, 12))
    map.borders.append(Border(23, 41))
    map.borders.append(Border(23, 28))
    map.borders.append(Border(24, 12))
    map.borders.append(Border(24, 14))
    map.borders.append(Border(24, 17))
    map.borders.append(Border(24, 42))
    map.borders.append(Border(24, 2))
    map.borders.append(Border(24, 36))
    map.borders.append(Border(24, 16))
    map.borders.append(Border(24, 29))
    map.borders.append(Border(25, 42))
    map.borders.append(Border(25, 1))
    map.borders.append(Border(25, 18))
    map.borders.append(Border(25, 2))
    map.borders.append(Border(26, 28))
    map.borders.append(Border(26, 41))
    map.borders.append(Border(26, 50))
    map.borders.append(Border(26, 13))
    map.borders.append(Border(27, 45))
    map.borders.append(Border(27, 40))
    map.borders.append(Border(27, 10))
    map.borders.append(Border(27, 42))
    map.borders.append(Border(28, 23))
    map.borders.append(Border(28, 41))
    map.borders.append(Border(28, 26))
    map.borders.append(Border(29, 41))
    map.borders.append(Border(29, 12))
    map.borders.append(Border(29, 24))
    map.borders.append(Border(29, 16))
    map.borders.append(Border(29, 5))
    map.borders.append(Border(29, 50))
    map.borders.append(Border(30, 21))
    map.borders.append(Border(30, 19))
    map.borders.append(Border(30, 46))
    map.borders.append(Border(31, 34))
    map.borders.append(Border(31, 6))
    map.borders.append(Border(31, 8))
    map.borders.append(Border(31, 38))
    map.borders.append(Border(32, 5))
    map.borders.append(Border(32, 36))
    map.borders.append(Border(32, 43))
    map.borders.append(Border(32, 3))
    map.borders.append(Border(32, 44))
    map.borders.append(Border(33, 13))
    map.borders.append(Border(33, 44))
    map.borders.append(Border(33, 3))
    map.borders.append(Border(33, 4))
    map.borders.append(Border(33, 37))
    map.borders.append(Border(34, 46))
    map.borders.append(Border(34, 19))
    map.borders.append(Border(34, 6))
    map.borders.append(Border(34, 31))
    map.borders.append(Border(34, 38))
    map.borders.append(Border(35, 38))
    map.borders.append(Border(35, 49))
    map.borders.append(Border(35, 17))
    map.borders.append(Border(35, 15))
    map.borders.append(Border(35, 22))
    map.borders.append(Border(36, 16))
    map.borders.append(Border(36, 24))
    map.borders.append(Border(36, 2))
    map.borders.append(Border(36, 43))
    map.borders.append(Border(36, 32))
    map.borders.append(Border(36, 5))
    map.borders.append(Border(37, 47))
    map.borders.append(Border(37, 13))
    map.borders.append(Border(37, 33))
    map.borders.append(Border(37, 4))
    map.borders.append(Border(38, 34))
    map.borders.append(Border(38, 31))
    map.borders.append(Border(38, 8))
    map.borders.append(Border(38, 20))
    map.borders.append(Border(38, 49))
    map.borders.append(Border(38, 35))
    map.borders.append(Border(39, 19))
    map.borders.append(Border(39, 6))
    map.borders.append(Border(40, 27))
    map.borders.append(Border(40, 10))
    map.borders.append(Border(41, 28))
    map.borders.append(Border(41, 23))
    map.borders.append(Border(41, 12))
    map.borders.append(Border(41, 29))
    map.borders.append(Border(41, 50))
    map.borders.append(Border(41, 26))
    map.borders.append(Border(42, 17))
    map.borders.append(Border(42, 45))
    map.borders.append(Border(42, 27))
    map.borders.append(Border(42, 10))
    map.borders.append(Border(42, 1))
    map.borders.append(Border(42, 25))
    map.borders.append(Border(42, 2))
    map.borders.append(Border(42, 24))
    map.borders.append(Border(43, 36))
    map.borders.append(Border(43, 2))
    map.borders.append(Border(43, 18))
    map.borders.append(Border(43, 32))
    map.borders.append(Border(44, 13))
    map.borders.append(Border(44, 50))
    map.borders.append(Border(44, 5))
    map.borders.append(Border(44, 32))
    map.borders.append(Border(44, 3))
    map.borders.append(Border(44, 33))
    map.borders.append(Border(45, 20))
    map.borders.append(Border(45, 7))
    map.borders.append(Border(45, 27))
    map.borders.append(Border(45, 42))
    map.borders.append(Border(45, 17))
    map.borders.append(Border(45, 49))
    map.borders.append(Border(46, 30))
    map.borders.append(Border(46, 19))
    map.borders.append(Border(46, 34))
    map.borders.append(Border(47, 0))
    map.borders.append(Border(47, 13))
    map.borders.append(Border(47, 37))
    map.borders.append(Border(48, 22))
    map.borders.append(Border(48, 14))
    map.borders.append(Border(48, 12))
    map.borders.append(Border(48, 23))
    map.borders.append(Border(49, 38))
    map.borders.append(Border(49, 20))
    map.borders.append(Border(49, 45))
    map.borders.append(Border(49, 17))
    map.borders.append(Border(49, 35))
    map.borders.append(Border(50, 26))
    map.borders.append(Border(50, 41))
    map.borders.append(Border(50, 29))
    map.borders.append(Border(50, 5))
    map.borders.append(Border(50, 44))
    map.borders.append(Border(50, 13))
    pass

def initMap(map):
    map.states.append("NC")
    map.states.append("SC")
    map.states.append("VA")
    map.states.append("TN")
    map.states.append("KY")
    map.states.append("WV")
    map.states.append("GA")
    map.states.append("AL")
    map.states.append("MS")
    map.states.append("FL")

    map.borders.append(Border(0, 1))
    map.borders.append(Border(0, 2))
    map.borders.append(Border(0, 3))
    map.borders.append(Border(0, 6))
    map.borders.append(Border(1, 6))
    map.borders.append(Border(2, 3))
    map.borders.append(Border(2, 4))
    map.borders.append(Border(2, 5))
    map.borders.append(Border(3, 4))
    map.borders.append(Border(3, 6))
    map.borders.append(Border(3, 7))
    map.borders.append(Border(3, 8))
    map.borders.append(Border(4, 5))
    map.borders.append(Border(6, 7))
    map.borders.append(Border(6, 9))
    map.borders.append(Border(7, 8))
    map.borders.append(Border(7, 9))  

def showmap(indiv):
    dict = {
            1:'Red',
            2:'Blue',
            3:'Yellow',
            4:'Green'
        }
    G = nx.Graph()
    for i, s in enumerate(indiv.map.states):
        color = indiv.genome[s]
        G.add_node(s, color=dict[color])
    if len(indiv.map.states) < 50:
        conns, states = make_lists10()
    else:
        conns, states = make_lists()
    for key, value in conns.items():
        idx = states.index(key)
        for vals in value:
            idx2 = states.index(vals)
            G.add_edge(states[idx], states[idx2])
    
    node_colors = [data["color"] for _, data in G.nodes(data=True)]
    nx.draw(G, with_labels=True, node_color=node_colors)

    # Display the graph
    plt.show()
    pass

def south_genetic():
    map = Map()
    initMap(map)
    populationSize = 50 # TODO find reasonable value
    population = Population(map, populationSize)

    maxIterations = 40 # TODO find reasonable value
    currentIteration = 0
    goalFound = False
    bestIndividual = Individual(map) # to hold the individual representing the goal, if any
    while currentIteration < maxIterations and goalFound==False:
        newPopulation = Population(map,0)
        for i in range(populationSize):
            x= population.randomSelection()
            y = population.randomSelection()
            child = Individual.reproduce(x, x, y)
            if random.random() < 0.1 :# TODO use small probability instead
                child.mutate()
            if child.isGoal():
                goalFound = True
                bestIndividual = child
            newPopulation.vector.append(child)
        currentIteration += 1
        population = newPopulation


    if goalFound :
        print("Found a solution after ",currentIteration," iterations" )
        bestIndividual.printresult()
    else:
        print("Did not find a solution after ",currentIteration," iterations")
    showmap(bestIndividual)
    pass  

def all_genetic():
    map = Map()
    init51(map)
    populationSize = 275 # TODO find reasonable value
    population = Population(map, populationSize)

    maxIterations = 5000 # TODO find reasonable value
    currentIteration = 0
    goalFound = False
    bestIndividual = Individual(map) # to hold the individual representing the goal, if any
    while currentIteration < maxIterations and goalFound==False:
        newPopulation = Population(map,0)
        for i in range(populationSize):
            x= population.randomSelection()
            y = population.randomSelection()
            child = Individual.reproduce(x, x, y)
            if random.random() < 0.1 :# TODO use small probability instead
                child.mutate()
            if child.isGoal():
                goalFound = True
                bestIndividual = child
            newPopulation.vector.append(child)
        currentIteration += 1
        population = newPopulation
    
    if goalFound :
        print("Found a solution after ",currentIteration," iterations" )
        bestIndividual.printresult()
    else:
        print("Did not find a solution after ",currentIteration," iterations")

    showmap(bestIndividual)
    pass  

def print_time(one, two):
    print("Process took ", two - one, " seconds long")

def btrack():
    map = Map()
    initMap(map)
    map.updateNeighbors()
    start_individ = Individual(map)
    start_individ.set_zero()
    s = time.time()
    result = start_individ.backtrack()
    e = time.time()
    print_time(s, e)

    if result == True:
        print("Solution found:")
        start_individ.printresult()
        #showmap(start_individ)
        return e-s
    else:
        print("No solution found.")

def fwdbtrack():
    map = Map()
    initMap(map)
    map.updateNeighbors()
    start_individ = Individual(map)
    start_individ.set_zero()
    s = time.time()
    result = start_individ.FWDbacktrack()
    e = time.time()
    print_time(s,e)

    if result == True:
        print("Solution found:")
        start_individ.printresult()
        return e-s
        #showmap(start_individ)
    else:
        print("No solution found.")

def ac3btrack():
    map = Map()
    initMap(map)
    map.updateNeighbors()
    start_individ = Individual(map)
    start_individ.set_zero()
    sol = ac3bt(start_individ)
    s = time.time()
    result = sol.backtrack()
    e = time.time()
    print_time(s,e)
    if result == True:
            print("Solution found:")
            start_individ.printresult()
            return e-s
            #showmap(start_individ)
    else:
        print("No solution found.")
        start_individ.printresult()
    pass

def mincons(i, m):
    map = Map()
    initMap(map)
    map.updateNeighbors()
    start_individ = Individual(map)
    solve = mc(start_individ)
    s = time.time()
    h = solve.min_conflicts(i, m)
    e = time.time()
    print_time(s,e)
    if h == True:
        print("Solution found:")
        start_individ.printresult()
        return e-s
        #showmap(start_individ)
    else:
        print("No solution found.")
        start_individ.printresult()
        #showmap(start_individ)
    pass


if __name__ == '__main__':
    m = input("1: South Genetic, 2: All Genetic, 3: For all backtracks and min-con\nEnter: ")
    
    if m == '1':
        print("Southern States: ")
        south_genetic()
    elif m == '2':
        print("All States:")
        all_genetic()
    elif m == '3':
        bt = 0
        fwd = 0
        ac3 = 0
        minc = 0
        for i in range(1, 11):
            print("Backtracking Normal")
            bt += btrack()
            print("Backtracking w/ FWD Checking")
            fwd += fwdbtrack()
            print("AC3 Backtracking:")
            ac3 += ac3btrack()
            print("MinConflicts")
            minc += mincons(1000000, 200)
        print("\nAverage Times (run 10 Times):")
        print("Backtrack: ", bt/10)
        print("Backtrack w/ Forward: ", fwd/10)
        print("Backtrack w/ AC3: ", ac3/10)
        print("Min-Conflicts: ", minc/10)
    else:
        print("MinConflicts")
        mincons(1000000, 200)
        pass
    
        