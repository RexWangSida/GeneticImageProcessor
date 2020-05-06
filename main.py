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
    ppm = readwriteppm.readPPM(inputFile)
    print("\n" + "File: " + inputFile + ", " + str(ppm['width']) +"X"+ str(ppm['height']) + ", max color: " + str(ppm['maxColor']) + str(mutateRate/100 * ppm['width'] * ppm['height']) + " pixels to mutate.")
    ##perform operations on the image
    newPPM = population.evolve_image(ppm, genNum, populationSize, mutateRate)
    ##write new image
    readwriteppm.writePPM(outputFile, newPPM)
if __name__ == '__main__':
    main()
