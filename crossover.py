## @file crossover.py
#  @author Bryan Chang
#  @date May 1st, 2020
import random

#  @brief This is the method library that stores the methods for corssover parent to generate children
class CrossOver():

	## @brief This function will generate two children based on the two parents
	#  @param parent1 Individual as first parent that will be used to generate children
	#  @param parent2 Individual as second parent that will be used to generate children
	#  @param child1 Individual as first child that will be generated based on two parents
	#  @param child2 Individual as second child that will be generated based on two parents
	def __init__(self):
		return None
	def __recombine(self, parent1, parent2, child1, child2):
		totalPixel = len(parent1["image"]["pixels"])
		crossoverPoint = random.randint(0,totalPixel)

		## The following for loop will copy parent1,2 to child1,2 from [0] to
		## [crossoverPoint]
		for i in range(0, crossoverPoint):
			child1["image"]["pixels"][i] = parent1["image"]["pixels"][i]
			child2["image"]["pixels"][i] = parent2["image"]["pixels"][i]
		## The following for loop will copy parent1,2 to child2,1 from
		## [crossoverPoint] to [totalPixel - 1]
		for i in range(crossoverPoint, totalPixel):
			child2["image"]["pixels"][i] = parent1["image"]["pixels"][i]
			child1["image"]["pixels"][i] = parent2["image"]["pixels"][i]

		return None

	## @brief This function will generate the second half of the population based
	#  on the first half of the population
	#  @param population the list for the Individuals that will be modified
	#  @param populationSize the length of the population
	def crossover(self, population, populationSize):

		for i in range(0, populationSize // 2, 2):
			## parent i and i+1 produce children population_size/2+i and
			## population_size/2+i+1.
			self.__recombine(population[i], population[i + 1], population[i + populationSize // 2], population[i + populationSize // 2] + 1)

			return None




