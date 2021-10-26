#Main code for SDOptimizer
import time
import argparse
import cv2
import numpy
import os

from exposure import *


ap = argparse.ArgumentParser()
ap.add_argument("-r", "--directory", required=True,
	help="Directory of SD Card")
SDdir = vars(ap.parse_args())["directory"]





print("SDOptimizer v1")

print("Test 1: Exposure")


# print("Please wait, running benchmarks...")
# speed = benchmarkExposure()
# print("Benchmarking completed. Speed is roughly ", 1/speed, "images/sec")		





#print("Exposure task is estimated to take ", int(exposureTaskPredictionDir(speed)), " seconds.")
print("Please wait, indexing files...")
time.sleep(1)




images = omitFileExtensions(indexFiles(SDdir))
filesRemaining = getNumberOfFiles(images)



for image in images:
	print(filesRemaining," photos left.")
	filesRemaining -= 1
	if(exposureTest(image)):
		pass
		# print("pass")
	else:
		# print("fail")
		pass



