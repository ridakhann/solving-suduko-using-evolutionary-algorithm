from copy import deepcopy
from random import random, shuffle, randint, sample, choice
import numpy as np
import random as random
import time as time
from sudoko import *
# global a


class Chromosome:
    def __init__(self, changeable, grid) -> None:
        self.changeable = changeable
        self.grid = grid
        self.fitness = 0

    def createChromosome(self):
        individual = deepcopy(self.grid)
        row_index = 0

        for row in individual:

            # Find the remaining numbers to fill in this row.
            remaining = {1, 2, 3, 4, 5, 6, 7, 8, 9} - set(row)
            remaining = list(remaining)
            # Shuffle them randomly.
            shuffle(remaining)

            # Add them in this random order to the non-fixed row locations.
            for index in self.changeable[row_index]:
                # if (len(remaining) != 0):
                row[index] = remaining.pop()

            assert len(remaining) == 0
            row_index += 1
        self.grid = individual

    def fitnessCalculator(self):
        conflicts = 0

        # Count subgrid conflicts.
        for i in range(0, 8, 3):
            conflicts += (9 -
                          len(set(self.grid[i][:3] + self.grid[i+1][:3] + self.grid[i+2][:3])))
            conflicts += (9 -
                          len(set(self.grid[i][3:6] + self.grid[i+1][3:6] + self.grid[i+2][3:6])))
            conflicts += (9 -
                          len(set(self.grid[i][6:9] + self.grid[i+1][6:9] + self.grid[i+2][6:9])))

        # Count row conflicts.
        for row in self.grid:
            conflicts += (9 - len(set(row)))

        # Count column conflicts.
        for col_index in range(9):
            col = []
            for row in self.grid:
                col.append(row[col_index])
            conflicts += (9 - len(set(col)))

        self.fitness = conflicts


class Population:
    def __init__(self, size, grid, changeable):
        self.populationSize = size
        self.changeable = changeable
        self.grid = grid
        self.population = []

    def createPopulation(self, size):
        for i in range(size):
            individual = Chromosome(self.changeable, self.grid)
            individual.createChromosome()
            individual.fitnessCalculator()
            self.population.append((individual, individual.fitness))


class Evolution:
    def __init__(self, pop: Population, mRate, generations, iterations, numOffspring):
        self.population = pop
        self.populationSize = pop.populationSize
        self.mutationRate = mRate
        self.numGenerations = generations
        self.iterations = iterations
        self.numOffspring = numOffspring
        self.best = []
        self.average = []

    def fitnessProp(self):
        sums = 0
        normalized = []
        for i in range(self.populationSize):
            sums += 1/(self.population.population[i][1])
        for i in range(self.populationSize-1):
            normalized.append((1/self.population.population[i][1])/sums)
        cumulative = normalized.copy()
        for i in range(1, len(normalized)):
            cumulative[i] = cumulative[i] + cumulative[i-1]
        rand = np.random.uniform()
        for i in range(len(cumulative)):
            if(rand < cumulative[i]):
                return self.population.population[i]
        return self.population.population[-1]

    def RBS(self):
        new = sorted(self.population.population,
                     key=lambda x: x[1], reverse=True)
        sums_c = 0
        x = []
        for i in range(len(new)):
            x.append(i+1)
            sums_c += i+1
        for i in range(len(new)):
            x[i] = x[i]/sums_c
        for i in range(1, len(new)):
            x[i] = x[i] + x[i-1]

        rand = np.random.uniform()

        for i in range(len(x)):
            if(rand < x[i]):
                return new[i]

    def truncation(self, n):
        new = sorted(self.population.population,
                     key=lambda x: x[1], reverse=False)
        top = []
        for i in range(n):
            top.append(new[i])
        return top

    def randomSelection(self):
        rand = random.randint(0, len(self.population.population)-1)
        return self.population.population[rand]

    def binaryTournament(self):
        rand1 = np.random.choice((range(0, len(self.population.population)-1)))
        rand2 = np.random.choice((range(0, len(self.population.population)-1)))
        lst = [self.population.population[rand1],
               self.population.population[rand2]]
        return min(lst, key=lambda t: t[1])

    def parentSelection(self):
        selectedParents = []
        # selectedParents = self.truncation(2)
        for i in range(2):
            selectedParents.append(self.randomSelection())
        return selectedParents

    def mutation(self, parent: Chromosome):
        for n in range(9):
            if len(parent.changeable[n]) > 1:
                # Get the indices of the two elements to swap.
                swap = sample(parent.changeable[n], 2)
                # Swap their places.
                parent.grid[n][swap[0]], parent.grid[n][swap[1]
                                                        ] = parent.grid[n][swap[1]], parent.grid[n][swap[0]]
        parent.fitnessCalculator()
        return parent

    def superMutation(self):
        for indv in self.population.population:
            self.mutation(indv)

    def evaluate_pop(self):
        lst = []
        for individual in self.population.population:
            individual[0].fitnessCalculator()
            lst.append(individual[0].fitness)
        return lst

    def crossover_individuals(self, parent1: Chromosome, parent2: Chromosome):
        crossover_point1 = randint(1, 8)
        crossover_point2 = randint(1, 8)
        return deepcopy(parent1.grid[:crossover_point1]) + deepcopy(parent2.grid[crossover_point1:]), deepcopy(parent2.grid[:crossover_point2]) + deepcopy(parent1.grid[crossover_point2:])
        # offspring1 = Chromosome(parent1.changeable, parent1.grid)
        # offspring2 = Chromosome(parent1.changeable, parent1.grid)

        # offspring1.grid = deepcopy(
        #     parent1.grid[:crossover_point]) + deepcopy(parent2.grid[crossover_point:])

        # offspring2.grid = deepcopy(
        #     parent2.grid[:crossover_point]) + deepcopy(parent1.grid[crossover_point:])

        # offspring1.fitnessCalculator()
        # offspring2.fitnessCalculator()

        # return offspring1, offspring2

    def generation(self):
        for i in range(self.numOffspring//2):
            parents = self.parentSelection()
            rand = np.random.uniform()
            rand1 = np.random.uniform()
            offspring1 = Chromosome(
                parents[0][0].changeable, parents[0][0].grid)
            offspring2 = Chromosome(
                parents[0][0].changeable, parents[0][0].grid)
            if parents[0] and parents[1] != None:
                offspring1.grid, offspring2.grid = self.crossover_individuals(
                    parents[0][0], parents[1][0])
                if (rand < self.mutationRate):
                    if (rand1 < 0.5):
                        offspring1 = self.mutation(offspring1)
                    else:
                        offspring2 = self.mutation(offspring2)
            offspring1.fitnessCalculator()
            offspring2.fitnessCalculator()
            self.population.population.append((offspring1, offspring1.fitness))
            self.population.population.append((offspring2, offspring2.fitness))
        new_pop = []
        new_pop = self.truncation(self.populationSize)
        # for i in range(self.populationSize):
        #     new_pop.append(self.binaryTournament())
        return new_pop

    def getBest(self):
        new = sorted(self.population.population,
                     key=lambda x: x[1], reverse=False)
        best = self.population.population[0][1]
        for i in range(self.populationSize):
            if self.population.population[i][1] < best:
                best = self.population.population[i][1]
                # a = self.population.population[i]
        return best

    def getAverage(self):
        sum = 0
        for i in range(self.populationSize):
            sum += self.population.population[i][1]
        return sum/self.populationSize


    def bestPopulation(self):
        lst = self.evaluate_pop()
        return sorted(zip(self.population.population, lst), key=lambda ind_fit: ind_fit[1])[0]

    def evolve(self, grid):
        lastBest = 100
        bestKnown = [[], 100, 0]
        avg = []
        best = []
        generations = []
        localCounter = 0
        timeEnd = 0
        win = pygame.display.set_mode((540, 600))
        start = time.time()
        for i in range(self.numGenerations):
            count = i
            generations.append(i)
            self.population.population = self.generation()
            if localCounter > 50:
                self.superMutation()
            avg.append(self.getAverage())
            bestInd, bestFit = self.bestPopulation()
            best.append(bestFit)
            if bestFit < bestKnown[1]:
                bestKnown[0], bestKnown[1], bestKnown[2] = bestInd, bestFit, i
            print("Generation #", i, "Best fit: ", bestFit)
            board = Grid(9, 9, 540, 540, win, bestInd[0].grid)
            redraw_window(win, board, grid)
            pygame.display.update()
            if bestFit == 0:
                timeEnd = time.time() - start
        if timeEnd == 0:
            timeEnd = time.time() - start
        self.best = best
        self.average = avg
        if bestFit in range(lastBest-20, lastBest+20+1):
            localCounter += 1
        else:
            lastBest = bestFit
            localCounter = 0
        print("\nBest found fitness: ", bestKnown[1])
        return bestInd, timeEnd
