# ICI_SDKbodytemp
Quick set of functions and example of grabbing body and FPA temperature from ICI camera radiometric images. You need the ICI SDK, which is proprietary and not available in this repository for that reason. Put that file (ICI.dll) in [lib](lib).

Examples:
1) Wrapping python around the SDK .dll functions (c++) is demonstrated in ICIfunctions.py
2) metaFromImage.py applies these wrappers to get meta data from ICI images

