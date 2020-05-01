## @file crossover.py
#  @author Bryan Chang
#  @date May 1st, 2020
import Individual.py
import random

#  @brief This is the file responsible for generating new children through
#  cross over

## @brief This function will generate two children based on the two parents
#  @param parent1 Individual as first parent that will be used to generate children
#  @param parent2 Individual as second parent that will be used to generate children
#  @param child1 Individual as first child that will be generated based on two parents
#  @param child2 Individual as second child that will be generated based on two parents
def recombine(parent1, parent2, child1, child2):
	parent1Image = parent1.getImage()
	parent2Image = parent2.getImage()
	child1Image = child1.getImage()
	child2Image = child2.getImage()
	width, height = parent1.getImage().size
	crossoverwidth = random.randint(0, width)
	crossoverheight = random.randint(0, height)

	## The following two for loops will copy parent1,2 to child1,2 from [0,0] to
	## [crossoverwidth, crossoverheight]
	for i in range(0,crossoverheight - 1):
		for j in range(0, width):
			child1Image[j,i] = parent1Image[j,i]
			child2Image[j,i] = parent2Image[j,i]

	for i in range(0, crossoverwidth):
			child1Image[i,crossoverheight] = parent1Image[i,crossoverheight]
			child2Image[i,crossoverheight] = parent2Image[i,crossoverheight]

	## The following two for loops will copy parent1,2 to child2,1 from
	## [crossoverwidth, crossoverheight] to [width - 1, height - 1]
	for i in range(crossoverwidth, width):
		child1Image[i,crossoverheight] = parent2Image[i,crossoverheight]
		child2Image[i,crossoverheight] = parent1Image[i,crossoverheight]

	for i in range(crossoverheight + 1,height):
		for j in range(0, width):
			child1Image[j,i] = parent1Image[j,i]
			child2Image[j,i] = parent2Image[j,i]

	##upload new gnerated image to child1 and child 2
	child1.changeImage(child1Image)
	child2.changeImage(child2Image)

	return none

## @brief This function will generate the second half of the population based
#  on the first half of the population
#  @param population the list for the Individuals that will be modified
#  @param populationSize the length of the population
def crossover(population, populationSize):

	for i in range(0, populationSize // 2, 2):
		## parent i and i+1 produce children population_size/2+i and
		## population_size/2+i+1.
		recombine(population[i], population[i + 1], population[i + populationSize // 2], population[i + populationSize // 2] + 1)




