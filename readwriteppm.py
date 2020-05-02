## @file readwriteppm.py
#  @author Sida Wang
#  @date May 1st 2020



#  @brief This a method library that stores the methods for file I/O methods.
class readwriteppm():
    ## @brief This function reads a PPM file and gives a abstract PPM data type as return.
    #  @param filename The name of the file to be read.
    #  @return The abstract type of the PPM that is to be processed.
    def readPPM(fileName):
        file = open(fileName, 'r')
        format = file.readline().strip()
        if(format != "P3"):
            raise Exception("This file is not of PPM P3 Type")
        secondLine = file.readline().strip()
        dimension = secondLine.split(' ')
        width = int(dimension[0])
        height = int(dimension[1])
        thirdLine = file.readline().strip()
        maxC = int(thirdLine)
        pixels = []
        for i in range(height):
            rgbs = file.readline().strip()
            rgbL = rgbs.split('  ')
            for j in range(width):
                rgb = rgbL[j].split(' ')
                pixel = {'r' : int(rgb[0]),
                'g' : int(rgb[1]),
                'b' : int(rgb[2])
                }
                pixels.append(pixel)
        file.close()
        return {'pixels' : pixels, 'width' : width, 'height' : height, 'maxColor' : maxC}
    ## @brief This function exports the abstract PPM to a given text file.
    #  @param filename The name of the file to be written to.
    #  @ppm filename The abstract PPM.
    def writePPM(fileName, ppm):
        file = open(fileName, 'w')
        file.write("P3\n")
        file.write(str(ppm['width']) + ' ' + str(ppm['height']) + '\n')
        file.write(ppm['maxColor']+ '\n')
        pixels = ppm['pixels']
        for i in range(len(pixels)):
            file.write(str(pixels[i]['r']) + ' ' + str(pixels[i]['g']) + ' ' + str(pixels[i]['b']) + '  ')
            if i % len(pixels) == 0:
                file.write('\n')
        file.close()
