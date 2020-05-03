## @file fitness.py
#  @author Deuce Cao
#  @date May 2nd 2020

#  @brief This file contains the methods of calculationg fitness

from math import sqrt

## @brief This method calculate the sum of RGB color distance pixel by pixel between two images
#  @param A, the pixels of 1st image
#  @param B, the pixels of 2nd image
#  @param image_size, the size of images
#  @return distance, the distance of two images
def comp_distance(A, B, image_size):
    sum = 0
    reminder = image_size %2
    if(reminder == 0):
        for i in range(0, image_size, 2):
            r = A[i]['r'] - B[i]['r']
            g = A[i]['g'] - B[i]['g']
            b = A[i]['b'] - B[i]['b']
            sum += r*r + g*g + b*b
            r = A[i+1]['r'] - B[i+1]['r']
            g = A[i+1]['g'] - B[i+1]['g']
            b = A[i+1]['b'] - B[i+1]['b']
            sum += r*r + g*g + b*b
    elif(image_size == 1):
        r = A[-1]['r'] - B[-1]['r']
        g = A[-1]['g'] - B[-1]['g']
        b = A[-1]['b'] - B[-1]['b']
        sum += r*r + g*g + b*b
    elif(reminder == 1):
        for i in range(0, image_size, 2):
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

## @brief This method calculate fitness between each individual in a population and the input image
#  @param image, the pixels of input image
#  @param population, the population of all individuals
#  @param population_size, the size of population
#  @detail save the fitness to each individual
def comp_fitness_population(image, population, population_size):
    size = population[0]['image']['width'] * population[0]['image']['height']

    for i in range(0, population_size):
        population[i]['fitness'] = comp_distance(population[i]['image']['pixels'], image, size)
