from readwriteppm import *
import sys
from population import *
##sys.argv[1] ----> given PPM image
##sys.argv[2] ----> produced new PPM image
##sys.argv[3] ----> No. Generations
##sys.argv[4] ----> population size
##sys.argv[5] ----> mutation rate
def main():
    if len(sys.argv) != 6:
        raise Exception("Invalid number of command line args!")
    ##read args
    inputFile = sys.argv[1]
    outputFile = sys.argv[2]
    genNum = int(sys.argv[3])
    populationSize = int(sys.argv[4])
    mutateRate = float(sys.argv[5])
    ##read image
    ppm = readwriteppm.readPPM(outputFile)
    print("\n" + "File: " + inputFile + ", " + str(ppm['width']) +"X"+ str(ppm['height']) + ", max color: " + str(ppm['maxColor']) + str(mutateRate/100 * ppm['width'] * ppm['height']) + " pixels to mutate.")
    ##generate population
    allImages = population()
    allImages.generatePopulation(populationSize, ppm['width'], ppm['height'], ppm['maxColor'])
    ##perform operations on the image
    newPPM = allImages.evolve_image(ppm, genNum, populationSize, mutateRate)
    ##write new image
    print("Image successfully processed!")
    readwriteppm.writePPM(outputFile, newPPM)
if __name__ == '__main__':
    main()
