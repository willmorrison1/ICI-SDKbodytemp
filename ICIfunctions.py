# python 2.7
import ctypes
import os

# load the cpp functions from the .dll
# PROPRIETARY - DO NOT REDISTRIBUTE ICI.dll
os.chdir("lib")
lib = ctypes.WinDLL('ICI.dll')
os.chdir("../")

# define the C input/output ("arg"/"res") types (i.e. "ctypes") for each function used
sensReadings = lib.ImgGetSensorReadings
sensReadings.argtypes = [ctypes.POINTER(ctypes.c_long),
                         ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float)]

sensReadings.restype = ctypes.c_int

ImgLoad = lib.ImgLoad
ImgLoad.argtypes = [ctypes.c_char_p]
ImgLoad.restype = ctypes.POINTER(ctypes.c_long)

delImgHandle = lib.ImgDeleteHandle

ImgGetPixelTemperature = lib.ImgGetPixelTemperature
ImgGetPixelTemperature.argtypes = [ctypes.POINTER(ctypes.c_long),
                                   ctypes.POINTER(ctypes.c_float),
                                   ctypes.c_int,
                                   ctypes.c_int]
