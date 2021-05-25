from itertools import count
import pygame
from random import random, shuffle, randint, sample, choice
from copy import deepcopy
from time import time
import sys
from EA import Chromosome, Population, Evolution
from sudoko import *
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
    # print(grid)


process_file("grid2.txt")

numIterations = 2
numGenerations = 100
populationSize = 500
numOfOffsprings = 100
mutationRate = 0.6
b = []
a = []


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


fitness = []
win = pygame.display.set_mode((540, 600))
pygame.display.set_caption("Sudoku Visualizer")
board = Grid(9, 9, 540, 540, win, grid)
redraw_window(win, board, grid)
pygame.display.update()

generations = []
timeList = []
for i in range(numIterations):

    population = Population(populationSize, grid, changeable)
    population.createPopulation(populationSize)
    evo = Evolution(population, mutationRate,
                    numGenerations, numIterations, numOfOffsprings)
    solution, timeend = evo.evolve(grid)
    timeList.append(timeend)
    b.append(evo.best)
    a.append(evo.average)
    fitness.append(solution[1])
    print(solution[1])


print(timeList)
# averageTime = sum(timeList)

best = averageBSF(b)
aver = averageAFSF(a)
generations = range(numGenerations)
# print(len(aver), len(best), len(gen))
plt.plot(generations, aver)
plt.plot(generations, best)
plt.legend(["Average Fitness", "Best Fitness"])
plt.title('Fitness Vs Generations')
plt.xlabel('Generations')
plt.ylabel('Fitness')
plt.show()
pygame.quit()
