## @file population.py
#  @author Deuce Cao
#  @date May 2nd 2020

#  @brief This file contains the methods of generationg random images

from random import randint

class population():
	## This method generates image with certificated size and randomized color each pixel
	def __generateRandomImage(width, height, maxColor):
	    randomSize = height * width

	    pixels = []

	    for i in range(0, randomSize):
	        pixels.append({'r':randint(0, maxColor),
	                       'g':randint(0, maxColor),
	                       'b':randint(0, maxColor)})
	    return pixels

	## @brief This method generates a population with certificated size and contains multiple image
	#  @param populationSize, the size of population
	#  @param width, the width of each image
	#  @param height, the height of each image
	#  @param maxColor, the maximum value of each RGB color in each image
	#  @return population, a list of all individuals as dictionary with image
	def generatePopulation(populationSize, width, height, maxColor):
	    population = []

	    for i in range(0, populationSize):
	        population.append({'image':{'width':width,
	                                    'height':height,
	                                    'maxColor':maxColor,
	                                    'pixels':generateRandomImage(width, height, maxColor)},
	                           'fitness':100000000})
	    return population
