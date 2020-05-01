## @file readwriteppm.py
#  @author Sida Wang
#  @date May 1st 2020


from PPMImage import PPMImage
#  @brief This a method library that stores the methods for file I/O methods.
class readwriteppm():
    ## @brief This function reads a PPM file and gives a abstract PPM data type as return.
    #  @param filename The name of the file to be read.
    #  @return The abstract type of the PPM that is to be processed.
    def readPPM(fileName):
        file = open(fileName, 'r')
        format = file.readline()
        if(format != "P3"):
            raise exception("This file is not of PPM P3 Type")
        secondLine = file.readline()
        dimension = secondLine.split(' ')
        width = dimension[0]
        height = dimension[1]
        thirdLine = file.readline()
        maxC = thirdLine
        pixels = []
        for i in range(height):
            rgbs = file.readline()
            rgbL = rgbs.split('  ')
            for j in range(width):
                rgb = rgbL[j].split(' ')
                pixel = dict{'r' : rgb[0],
                'g' : rgb[1],
                'b' : rgb[2]
                }
                pixels.append(pixel)
        file.close()
        return PPMImage(pixels, width, height, maxC)
    ## @brief This function exports the abstract PPM to a given text file.
    #  @param filename The name of the file to be written to.
    #  @ppm filename The abstract PPM.
    def writePPM(fileName, ppm):
        file = open(fileName, 'w')
        file.write("P3\n")
        file.write(ppm.getWidth() + ' ' + ppm.getHeight() + '\n')
        file.write(ppm.getMaxColor()+ '\n')
        pixels = ppm.getPixels()
        for i in range(len(pixels)):
            file.write(pixels[0]['r'] + ' ' + pixels[0]['g'] + ' ' pixels[0]['r'] + '  ')
            if i % len(pixels) == 0:
                file.write('\n')
        file.close()
