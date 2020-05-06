## @file evolve.py
#  @author Bryan Chang
#  @date May 1st 2020

from population import *
from fitness import *
from crossover import *
from mutation import *

#  @brief This class contains the function which is the skeleton of the genertic
#  algorithm
class evolve():
    ## @brief This function will generate population with size N and mutate for X
    #  generations with mutate rate of Z and output the final result
    #  @param imageIn PPM file, the target image for the evolution
    #  @param numGenerations int, the number of generation for the evolution
    #  @param populationSize int, the total number of the population
    #  @param mutateRate float, the percent of pixel that will be mutated for the image
    #  @return imageOut the image that is most similiar to imageIn
    def evolve_image(imageIn, numGenerations, populationSize, mutateRate):

        p = population.generatePopulation(populationSize, imageIn["width"], imageIn["height"], imageIn["maxColor"])

        fitness.compFitnessPopulation(imageIn["pixels"], p, populationSize)

        ## python's built in sorting algorithm
        sorted(p, key = lambda Individual: Individual["fitness"])

        for i in range(numGenerations):
            p = fitness.compFitnessPopulation(imageIn, mutation.mutatePopulation(CrossOver.crossover(p, populationSize), populationSize, mutateRate), populationSize)
            sorted(p, key = lambda Individual: Individual["fitness"])

        ## creating the output image
        ImageOut = {
            "pixels": p[0]["image"]["pixels"],
            "width": p[0]["image"]["width"],
            "height": p[0]["image"]["height"],
            "maxColor": p[0]["image"]["maxColor"]
        }

        return ImageOut
