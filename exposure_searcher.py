

# import the necessary packages
from matplotlib import pyplot as plt
import argparse
import cv2
import numpy
import os

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-r", "--directory", required=True,
	help="Directory of SD Card")
SDdir = vars(ap.parse_args())["directory"]

print(SDdir)
chapterDirs = os.listdir(SDdir+"/DCIM")
try:
	chapterDirs.remove(".DS_Store")
except:
	print("dsstorenotfound. (2)")
print(chapterDirs)




def exposureTest(imageDir):
	image = cv2.imread(imageDir)
	image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	# compute a grayscale histogram
	hist = cv2.calcHist([image], [0], None, [256], [0, 256])
	print("this image has an exposure value of: ",numpy.mean(image))



	if (numpy.mean(image)<=30):
		print("this image appears to be underexposed.")
		return False
	elif (numpy.mean(image)>=200):
		print("this image appears to be overexposed.")
		return False
	else:
		print("this image passes the exposure test.")
		return True















for folder in range(len(chapterDirs)):
	workingDirectory = chapterDirs[folder]
	print("Analyzing: " + workingDirectory)
	JPG = os.listdir(SDdir+"/DCIM/"+workingDirectory+"")
	try:
		JPG.remove(".DS_Store")
	except:
		print("dsstorenotfound. (2)")
	for picture in range(len(JPG)):
		picturePath = SDdir+"/DCIM/"+workingDirectory+"/"+JPG[picture]
		print("testing: "+picturePath)
		if exposureTest(picturePath):
			pass



