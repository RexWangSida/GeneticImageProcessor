## @file fitness.py
#  @author Deuce Cao
#  @date May 2nd 2020

#  @brief This file contains the methods of calculationg fitness

## @brief This method calculate the sum of RGB color distance pixel by pixel between two images
#  @param A, the pixels of 1st image
#  @param B, the pixels of 2nd image
#  @param image_size, the size of images
#  @return distance, the distance of two images
def comp_distance(A, B, image_size):
	sum = 0
	reminder = image_size %2
	last = image_size - 1
	if(reminder == 0):
		for i in range(0, image_size, 2):
			r = A[i]['r'] - B[i].['r']
            g = A[i]['g'] - B[i].['g']
            b = A[i]['b'] - B[i].['b']
			r_2 = r*r
			g_2 = g*g
			b_2 = b*b
			sum += r_2 + g_2 + b_2
			r = A[i+1]['r'] - B[i+1]['r']
			g = A[i+1]['g'] - B[i+1]['g']
			b = A[i+1]['b'] - B[i+1]['b']
			r_2 = r*r
			g_2 = g*g
			b_2 = b*b
			sum += r_2 + g_2 + b_2
	elif(image_size == 1):
		r = A[last]['r'] - B[last]['r']
		g = A[last]['g'] - B[last]['g']
		b = A[last]['b'] - B[last]['b']
		r_2 = r*r
		g_2 = g*g
		b_2 = b*b
		sum += r_2 + g_2 + b_2
	elif(reminder == 1):
		for i in range(0, image_size, 2):
			r = A[i]['r'] - B[i]['r']
			g = A[i]['g'] - B[i]['g']
			b = A[i]['b'] - B[i]['b']
			r_2 = r*r
			g_2 = g*g
			b_2 = b*b
			sum += r_2 + g_2 + b_2
			r = A[i+1]['r'] - B[i+1]['r']
			g = A[i+1]['g'] - B[i+1]['g']
			b = A[i+1]['b'] - B[i+1]['b']
			r_2 = r*r
			g_2 = g*g
			b_2 = b*b
			sum += r_2 + g_2 + b_2

		r = A[last]['r'] - B[last]['r']
		g = A[last]['g'] - B[last]['g']
		b = A[last]['b'] - B[last]['b']
		r_2 = r*r
		g_2 = g*g
		b_2 = b*b
		sum += r_2 + g_2 + b_2

	distance = sqrt(sum)
	return distance

## @brief This method calculate fitness between each individual in a population and the input image
#  @param image, the pixels of input image
#  @param individual, the individuals in the population
#  @param population_size, the size of population
#  @detail save the fitness to each individual
def comp_fitness_population(image, individual, population_size):
	size = individual[0]['image']['width'] * individual[0]['image']['height']

	for i in range(0, population_size):
		individual[i]['fitness'] = comp_distance(individual[i]['image']['data'], image, size)
