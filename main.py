from random import random, shuffle, randint, sample, choice
from copy import deepcopy
from time import time
import sys
from EA import Chromosome, Population, Evolution
from matplotlib import pyplot as plt

grid = []   # Holds rows of base grid
changeable = []   # Holds indices per row in 'grid' that are not fixed

"""
Processes a file and formulates a base grid, and keeps track of changeable indices.
Parameters
    file_path: Path to the file to be processed
"""


def process_file(file_path):

    with open(file_path, "r") as grid_file:
        grid_data = grid_file.readlines()

        for line in grid_data:
            current_row = []  # holds current row with empty spaces replaced with 0
            current_changeable = []  # hold indices of positions not fixed in a row
            index = 0

            # Ignore divider row.
            if line[0] == '-':
                continue

            for ch in line:
                # If number is not fixed, add a '0' placeholder & record index.
                if ch == '.':
                    current_row.append(0)
                    current_changeable.append(index)
                    index += 1

                elif ch != '\n' and ch != '!':
                    # If number is fixed, add to the base grid.
                    current_row.append(int(ch))
                    index += 1

            grid.append(current_row)
            changeable.append(current_changeable)
    # for i in grid:
    #     print(i)
    # print(changeable)
    # print(grid)


process_file("grid1.txt")

numIterations = 1
numGenerations = 10000
populationSize = 100
numOfOffsprings = 80
mutationRate = 0.5
b = []
a = []
# p = Population(4, grid, changeable)
# p.createPopulation(4)
# print(p.population)


def averageBSF(best):
    best2 = []
    for i in range(len(best[0])):  # for each generation
        sum = 0
        for g in best:  # for each iteration
            sum += g[i]
        best2.append(sum/len(best))
    return best2


def averageAFSF(avg):
    best2 = []
    for i in range(len(avg[0])):  # for each generation
        sum = 0
        for g in avg:  # for each iteration
            sum += g[i]
        best2.append(sum/len(avg))
    return best2


for i in range(numIterations):
    population = Population(populationSize, grid, changeable)
    population.createPopulation(populationSize)
    evo = Evolution(population, mutationRate,
                    numGenerations, numIterations, numOfOffsprings)
    evo.evolve()
    b.append(evo.best)
    a.append(evo.average)
best = averageBSF(b)
aver = averageAFSF(a)
print(best[-1])
print(aver[-1])
generations = range(numGenerations)
plt.plot(generations, aver)
plt.plot(generations, best)
plt.legend(["Average Fitness", "Best Fitness"])
plt.title('Fitness Vs Generations')
plt.xlabel('Generations')
plt.ylabel('Fitness')
plt.show()

