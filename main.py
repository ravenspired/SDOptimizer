#Main code for SDOptimizer
import time
import argparse
import cv2
import numpy
import os

from exposure import *
from fileOperations import *


ap = argparse.ArgumentParser()
ap.add_argument("-r", "--directory", required=True,
	help="Directory of SD Card")
SDdir = vars(ap.parse_args())["directory"]


try:
	jobFile = open("CANON_DC.log", "x")
	print("file created.")
except:
	print("job file already exists.")

jobFile = open("CANON_DC.log", "a")



print("SDOptimizer v1")

print("Test 1: Exposure")


print("Please wait, running benchmarks...")
speed = benchmarkExposure()
print("Benchmarking completed. Speed is roughly ", 1/speed, "images/sec")		





#print("Exposure task is estimated to take ", int(exposureTaskPredictionDir(speed)), " seconds.")
print("Please wait, indexing files...")
images = omitFileExtensions(indexFiles(SDdir))
filesRemaining = getNumberOfFiles(images)


print("Beginning processing.")

imagesProcessed = 0

for image in images:
	if filesRemaining%5==0:
		print(filesRemaining," photos left, ", speed*filesRemaining, " seconds left.")

	filesRemaining -= 1
	if(exposureTest(image)):
		pass

	else:
		imagesProcessed += 1
		jobFile.write(image+"\n")
		
jobFile.close()
if imagesProcessed != 0:
	purgePhotos()	
send2trash("CANON_DC.log")


