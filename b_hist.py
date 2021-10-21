

# import the necessary packages
from matplotlib import pyplot as plt
import argparse
import cv2
import numpy

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to the image")
args = vars(ap.parse_args())
# load the input image and convert it to grayscale
image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# compute a grayscale histogram
hist = cv2.calcHist([image], [0], None, [256], [0, 256])
print("image '"+ args["image"]+"' has a mean bin value of ",numpy.mean(image))


if (numpy.mean(image)<=30):
	print("this image appears to be underexposed.")
elif (numpy.mean(image)>=230):
	print("this image appears to be overexposed.")
else:
	print("this image passes the exposure test.")