# python 2.7
import os
import ctypes
import tkFileDialog
import re
import ICIfunctions as ICI

# name of text file to write pixel-level contents
oFile = "data/processed/metaFromImage.txt"
# x Pixel (origin = 0 at "top left" of image)
xPix = ctypes.c_int(333)
# y pixel (origin = 0 at "top left" of image)
yPix = ctypes.c_int(461)
if os._exists(oFile):
    os.remove(oFile)

# interactive image load
imgFileNames = tkFileDialog.askopenfilenames()

with open(oFile, 'w') as f:
    for imgFileName in imgFileNames:

        print(imgFileName)
        if not re.search(".jpg", imgFileName):
            continue

        creationTime = os.path.getctime(imgFileName)
        print(creationTime)
        # get the "ihandle" image handle
        ihandle = ICI.ImgLoad(imgFileName)

        FPAbuff = ctypes.c_float()
        LENSbuff = ctypes.c_float()

        a = ICI.sensReadings(ihandle, LENSbuff, FPAbuff)

        print("LENS: " + str(LENSbuff.value))
        print("FPA: " + str(FPAbuff.value))

        buff = ctypes.c_float()

        res = ICI.ImgGetPixelTemperature(ihandle, buff, xPix, yPix)
        print("pxTemp: " + str(buff.value))

        ICI.delImgHandle(ihandle)
        strOut = str(creationTime) + " " + str(LENSbuff.value) + " " + str(FPAbuff.value) + " " + str(buff.value)
        f.write("%s\n" % strOut)
