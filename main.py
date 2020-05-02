from readwriteppm import *

ppm = readwriteppm.readPPM('night.ppm')
readwriteppm.writePPM('night2.ppm', ppm)
