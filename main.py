#Main code for SDOptimizer
import time
import argparse
import cv2
import numpy
import os
from tqdm import tqdm


from exposure import *
from fileOperations import *
from motion_blur import *

from console_resources import *






consoleSetup(True, True, True, True) 


ap = argparse.ArgumentParser()
ap.add_argument("-r", "--directory", required=False,
	help="Directory of SD Card")
ap.add_argument("-t", "--threshold", type=float, default=50.0,
	help="focus measures that fall below this value will be considered 'blurry'")

SDdir = vars(ap.parse_args())["directory"]
blurThreshold =  vars(ap.parse_args())["threshold"]


if(SDdir == None):
	print("Please drag and drop your SD card onto the console, and press enter.")
	print("You may type in the PATH to a folder as well")
	SDdir = input("PATH=")
	if(SDdir[-1]==" "):
		SDdir = SDdir[:-1]


try:
	jobFile = open("CANON_DC.log", "x")
	console("Jobfile created.", "ok")
except:
	os.remove("CANON_DC.log")
	jobFile = open("CANON_DC.log", "x")
	console("Jobfile already exists. Overwriting...", "warning")


jobFile = open("CANON_DC.log", "a")

print("\n")

console("SDOptimizer v1.1", "info")


print("\n")







#print("Exposure task is estimated to take ", int(exposureTaskPredictionDir(speed)), " seconds.")
console("Please wait, indexing files...", "info")
images = omitFileExtensions(indexFiles(SDdir))
filesRemaining = getNumberOfFiles(images)
console("Files indexed succesfully.", "ok")

console("Processing Images, please wait...", "info")

imagesProcessed = 0
imagesDestroyed = []

console("Test 1: Exposure", "info")

for image in tqdm(images):
	# if filesRemaining%5==0:
	# 	print(filesRemaining," photos left, ", speed*filesRemaining, " seconds left.")

	filesRemaining -= 1
	if(exposureTest(image)):
		pass

	else:
		imagesProcessed += 1
		jobFile.write(image+"\n")
		imagesDestroyed.append(image)

		

console("Test 1 completed.", "ok")

console("Test 2: Motion Blur", "info")
for image in tqdm(images):
	if image in imagesDestroyed:
		pass
	else:
		filesRemaining -= 1
		if(motionBlurTest(image, blurThreshold)):

			pass
		else:
			imagesProcessed += 1

			jobFile.write(image+"\n")
			imagesDestroyed.append(image)


jobFile.close()

console("Scanning completed. Purging images...", "info")
print("\n")
if imagesProcessed != 0:
	purgePhotos()	
send2trash("CANON_DC.log")
console("Job completed. Make sure to view what was removed in your system trash.", "ok")
console("Do not forget to empty the trash as well.", "info")
console("Exiting. Thank you for using SDOptimizer!", "info")


