## @file population.py
#  @author Deuce Cao
#  @date May 2nd 2020

#  @brief This file contains the methods of generationg random images

from random import randint

## @brief This method generates image with certificated size and randomized color each pixel
#  @param width, the width of image
#  @param height, the height of image
#  @param max_color, the maximum value of each RGB color
#  @return L, a list of all pixels as dictionary with RGB color
def generate_random_image(width, height, max_color):
    random_size = height * width

    pixels = []

    for i in range(0, random_size):
        pixels.append({'r':randint(0, max_color),
                       'g':randint(0, max_color),
                       'b':randint(0, max_color)})
    return pixels;

## @brief This method generates a population with certificated size and contains multiple image
#  @param population_size, the size of population
#  @param width, the width of each image
#  @param height, the height of each image
#  @param max_color, the maximum value of each RGB color in each image
#  @return population, a list of all individuals as dictionary with image
def generate_population(population_size, width, height, max_color):
    population = []

    for i in range(0, population_size):
        population.append({'image':{'width':width,
                                    'height':height,
                                    'max_color':max_color,
                                    'pixels':generate_random_image(width, height, max_color)},
                           'fitness':100000000})
    return population;
