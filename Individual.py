class Individual(object):
    def _init_(image, fitness):
        self.image = image ##image is an instance of PPMImage
        self.fitness = fitness ##fitness is the difference between the given image and the new generated image
