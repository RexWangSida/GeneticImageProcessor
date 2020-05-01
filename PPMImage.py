class PPMImage(object):
    def _init_(pixel, width, height, maxColor):
        self.pixel = pixel ##pixel is a list of dictionaries with r,g,b
        self.width = width
        self.height = height
        self.maxColor = maxColor
