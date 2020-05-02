## @file mutation.py
#  @author Sida Wang
#  @date May 1st 2020

from random import randint

#  @brief This a method library that stores the methods supporting the image mutations.
class mutation():
    ## This function performs mutation on one individual image.
    def __mutate(allIndividuals, rate):
        imageSize = allIndividuals.getImage().getWidth() * allIndividuals.getImage().getHeight()
        mutateRate = int(rate/100 * imageSize)
        maxColor = image.getMaxColor() + 1
        for i in range(mutateRate):
            index = randint(0,imageSize)
            allIndividuals.getImage().getPixel()[index]['r'] = randint(0,maxColor)
            allIndividuals.getImage().getPixel()[index]['g'] = randint(0,maxColor)
            allIndividuals.getImage().getPixel()[index]['b'] = randint(0,maxColor)

    ## @brief This function performs mutations on the whole population.
    #  @param allIndividuals All the images.
    #  @param populationSize The number of the population(all images).
    #  @param rate The mutation rate.
    def mutatePopulation(allIndividuals, populationSize, rate):
        index = populationSize/4
        for i in range(populationSize):
            mutate(allIndividuals + i, rate)
