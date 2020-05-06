from random import randint
from math import sqrt
import random

class population():
    def __generateRandomImage(width, height, maxColor):
        randomSize = height*width
        pixels = []
        for i in range(0,randomSize):
            pixels.append({'r':randint(0,maxColor),
                            'g': randint(0,maxColor),
                            'b': randint(0,maxColor)})
        return pixels


    def generatePopulation(populationSize, width, height, maxColor):
        population = []

        for i in range(0, populationSize):
            population.append({
                'image':{
                    'width': width,
                    'height': height,
                    'maxColor':maxColor,
                    'pixels': self.__generateRandomImage(width, height, maxColor),
                },
                'fitness' : 1000000
            })
        return population

class population:

    def __init__(self):
        self.population = []

    def generatePopulation(self, populationSize, width, height, maxColor):

        for i in range(0, populationSize):
            self.population.append({
                'image':{
                    'width': width,
                    'height': height,
                    'maxColor':maxColor,
                    'pixels': self.__generateRandomImage(width, height, maxColor),
                },
                'fitness' : 1000000
            })

    def __generateRandomImage(self, width, height, maxColor):
        randomSize = height*width
        pixels = []
        for i in range(0,randomSize):
            pixels.append({'r':randint(0,maxColor),
                            'g': randint(0,maxColor),
                            'b': randint(0,maxColor)})
        return pixels

    def __compFitnessPopulation(self, image, populationSize):
        size = self.population[0]['image']['width'] * self.population[0]['image']['height']

        for i in range(0, populationSize):
            self.population[i]['fitness'] = self.__compDistance(self.population[i]['image']['pixels'], image, size)

    def __compDistance(self, A, B, imageSize):
        sum = 0
        reminder = imageSize %2
        if(reminder == 0):
            for i in range(0, imageSize, 2):
                r = A[i]['r'] - B[i]['r']
                g = A[i]['g'] - B[i]['g']
                b = A[i]['b'] - B[i]['b']
                sum += r*r + g*g + b*b
                r = A[i+1]['r'] - B[i+1]['r']
                g = A[i+1]['g'] - B[i+1]['g']
                b = A[i+1]['b'] - B[i+1]['b']
                sum += r*r + g*g + b*b
        elif(imageSize == 1):
            r = A[-1]['r'] - B[-1]['r']
            g = A[-1]['g'] - B[-1]['g']
            b = A[-1]['b'] - B[-1]['b']
            sum += r*r + g*g + b*b
        elif(reminder == 1):
            for i in range(0, imageSize, 2):
                r = A[i]['r'] - B[i]['r']
                g = A[i]['g'] - B[i]['g']
                b = A[i]['b'] - B[i]['b']
                sum += r*r + g*g + b*b
                r = A[i+1]['r'] - B[i+1]['r']
                g = A[i+1]['g'] - B[i+1]['g']
                b = A[i+1]['b'] - B[i+1]['b']
                sum += r*r + g*g + b*b

                r = A[-1]['r'] - B[-1]['r']
                g = A[-1]['g'] - B[-1]['g']
                b = A[-1]['b'] - B[-1]['b']
                sum += r*r + g*g + b*b

        distance = sqrt(sum)
        return distance

    def __crossover(self, populationSize):

        for i in range(0, populationSize // 2, 2):
    ## parent i and i+1 produce children population_size/2+i and
    ## population_size/2+i+1.
            totalPixel = len(self.population[i]["image"]["pixels"])
            crossoverPoint = random.randint(0,totalPixel)

    ## The following for loop will copy parent1,2 to child1,2 from [0] to
    ## [crossoverPoint]
            for i in range(0, crossoverPoint):
                self.population[i + populationSize // 2]["image"]["pixels"][i] = self.population[i]["image"]["pixels"][i]
                self.population[i + populationSize // 2 + 1]["image"]["pixels"][i] = self.population[i + 1]["image"]["pixels"][i]
    ## The following for loop will copy parent1,2 to child2,1 from
    ## [crossoverPoint] to [totalPixel - 1]
            for i in range(crossoverPoint, totalPixel):
                self.population[i + populationSize // 2 + 1]["image"]["pixels"][i] = self.population[i]["image"]["pixels"][i]
                self.population[i + populationSize // 2]["image"]["pixels"][i] = self.population[i + 1]["image"]["pixels"][i]

    def __mutate(Individual, rate):
        imageSize = Individual['image']['width'] * Individual['image']['height']
        mutateRate = int(rate/100 * imageSize)
        maxColor = Individual['image']['maxColor'] + 1
        for i in range(mutateRate):
            index = randint(0,imageSize)
            Individual['image']['pixels'][index]['r'] = randint(0,maxColor)
            Individual['image']['pixels'][index]['g'] = randint(0,maxColor)
            Individual['image']['pixels'][index]['b'] = randint(0,maxColor)
        return Individual


    def __mutatePopulation(self, populationSize, rate):
        index = populationSize/4
        for i in range(index, populationSize):
            individual = mutate(self.population[i], rate)
            self.population[i] = individual


    def evolve_image(self, imageIn, numGenerations, populationSize, mutateRate):

        self.__generatePopulation(populationSize, imageIn["width"], imageIn["height"], imageIn["maxColor"])

        self.__compFitnessPopulation(imageIn["pixels"], populationSize)

        ## python's built in sorting algorithm
        sorted(self.population, key = lambda Individual: Individual["fitness"])

        for i in range(numGenerations):
            self.__crossover(populationSize)
            self.__mutatePopulation(populationSize, mutateRate)
            self.__compFitnessPopulation(imageIn["pixels"], populationSize)
            sorted(self.population, key = lambda Individual: Individual["fitness"])

        ## creating the output image
        ImageOut = {
            "pixels": p[0]["image"]["pixels"],
            "width": p[0]["image"]["width"],
            "height": p[0]["image"]["height"],
            "maxColor": p[0]["image"]["maxColor"]
        }

        return ImageOut
