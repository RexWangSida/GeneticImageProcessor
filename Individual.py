## @file Individual.py
#  @author Sida Wang
#  @date May 1st 2020

#  @brief This a template module that gives a abstract representation of an individual image, with its difference to the given image.
class Individual(object):
    ## @brief This is constructor of the Individual template.
    #  @param image The PPM image that it represents.
    #  @param fitness A value that shows how similar it is compared to the given image. The better fitness it has, the more similar it is compared to the given image.
    def _init_(image, fitness):
        self.image = image ##image is an instance of PPMImage
        self.fitness = fitness ##fitness is the difference between the given image and the new generated image
