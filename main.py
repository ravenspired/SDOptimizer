#Main code for SDOptimizer
import time
import argparse
import cv2
import numpy
import os
from tqdm import tqdm


from exposure import *
from fileOperations import *


ap = argparse.ArgumentParser()
ap.add_argument("-r", "--directory", required=False,
	help="Directory of SD Card")
SDdir = vars(ap.parse_args())["directory"]

if(SDdir == None):
	print("Please drag and drop your SD card onto the console, and press enter.")
	print("You may type in the PATH to a folder as well")
	SDdir = input("PATH=")
	if(SDdir[-1]==" "):
		SDdir = SDdir[:-1]


try:
	jobFile = open("CANON_DC.log", "x")
	print("Jobfile created.")
except:
	os.remove("CANON_DC.log")
	jobFile = open("CANON_DC.log", "x")
	print("Jobfile already exists. Overwriting...")


jobFile = open("CANON_DC.log", "a")

print("\n")

print("SDOptimizer v1")


print("\n")







#print("Exposure task is estimated to take ", int(exposureTaskPredictionDir(speed)), " seconds.")
print("Please wait, indexing files...")
images = omitFileExtensions(indexFiles(SDdir))
filesRemaining = getNumberOfFiles(images)


print("Processing Images, please wait...")

imagesProcessed = 0

for image in tqdm(images):
	# if filesRemaining%5==0:
	# 	print(filesRemaining," photos left, ", speed*filesRemaining, " seconds left.")

	filesRemaining -= 1
	if(exposureTest(image)):
		pass

	else:
		imagesProcessed += 1
		jobFile.write(image+"\n")
		
jobFile.close()
print("\n")
print("\n")
print("Scanning Completed. Moving ",imagesProcessed, "images to the trash.")
print("\n")
if imagesProcessed != 0:
	purgePhotos()	
send2trash("CANON_DC.log")
print("\n")
print("\n")
print("Job completed. Make sure to view what was removed in your system trash.")
print("Do not forget to empty the trash as well.")
print("Exiting. Thank you for using SDOptimizer!")


