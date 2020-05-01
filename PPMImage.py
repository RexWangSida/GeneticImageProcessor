## @file PPMImage.py
#  @author Sida Wang
#  @date May 1st 2020

#  @brief This a template module that gives a template of an PPM Image for processing.
class PPMImage(object):
    ## @brief This is constructor of the PPM Image template.
    #  @param pixels A list of dictionaries, each dictionary represents an individual pixel.
    #  @param width The width of the PPM Image.
    #  @param height The height of the PPM Image.
    #  @param maxColor The maximum number of the r,g,b of the pixels in the image.
    def _init_(pixels, width, height, maxColor):
        self.pixels = pixels ##pixel is a list of dictionaries with r,g,b
        self.width = width
        self.height = height
        self.maxColor = maxColor

    ## @brief This is accessor of the pixel
    def getPixel():
        return self.pixel

    ## @brief This is accessor of the width
    def getWidth():
        return self.width

    ## @brief This is accessor of the height
    def getHeight():
        return self.height

    ## @brief This is accessor of the maxColor
    def getMaxColor():
        return self.maxColor
