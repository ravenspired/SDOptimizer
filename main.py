#Main code for SDOptimizer
import time
import argparse
import cv2
import numpy
import os

ap = argparse.ArgumentParser()
ap.add_argument("-r", "--directory", required=True,
	help="Directory of SD Card")
SDdir = vars(ap.parse_args())["directory"]





def exposureBenchmark(imageDir):
	image = cv2.imread(imageDir)
	image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	# compute a grayscale histogram
	hist = cv2.calcHist([image], [0], None, [256], [0, 256])
	#print("this image has an exposure value of: ",numpy.mean(image))

	if (numpy.mean(image)>=-1):
		return True


def getNumberOfFiles():
	numberOfFiles = 0
	chapterDirs = os.listdir(SDdir+"/DCIM")
	try:
		chapterDirs.remove(".DS_Store")
	except:
		pass
	for folder in range(len(chapterDirs)):
		workingDirectory = chapterDirs[folder]
		# print("Analyzing: " + workingDirectory)
		JPG = os.listdir(SDdir+"/DCIM/"+workingDirectory+"")
		try:
			JPG.remove(".DS_Store")
		except:
			pass
		for picture in range(len(JPG)):
			numberOfFiles = numberOfFiles + 1
	
	return numberOfFiles






def exposureTaskPredictionDir(speed):
	numberOfFiles = 0
	chapterDirs = os.listdir(SDdir+"/DCIM")
	try:
		chapterDirs.remove(".DS_Store")
	except:
		pass
	for folder in range(len(chapterDirs)):
		workingDirectory = chapterDirs[folder]
		# print("Analyzing: " + workingDirectory)
		JPG = os.listdir(SDdir+"/DCIM/"+workingDirectory+"")
		try:
			JPG.remove(".DS_Store")
		except:
			pass
		for picture in range(len(JPG)):
			numberOfFiles = numberOfFiles + 1
	print("There are ", numberOfFiles, " images to check.")
	return speed*numberOfFiles


def exposureTaskPrediction(speed, numberOfFiles):
	return speed*numberOfFiles	


print("SDOptimizer v1")

print("Test 1: Exposure")

print("Please wait, running benchmarks...")
start = time.time()
for i in range(30):
	if exposureBenchmark("/Users/anton/Desktop/SDOptimizer/sample.JPG"):
		pass
end = time.time()
speed = (end-start)/30
print("raw speed", speed)
print("Benchmarking completed. Speed is roughly ", 1/speed, "images/sec")		





print("Exposure task is estimated to take ", int(exposureTaskPredictionDir(speed)), " seconds.")
print("Preparing for exposure task...")
time.sleep(7)




chapterDirs = os.listdir(SDdir+"/DCIM")
try:
	chapterDirs.remove(".DS_Store")
except:
	pass
# print(chapterDirs)

def exposureTest(imageDir):
	image = cv2.imread(imageDir)
	image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	# compute a grayscale histogram
	hist = cv2.calcHist([image], [0], None, [256], [0, 256])




	if (numpy.mean(image)<=30):

		return False
	elif (numpy.mean(image)>=200):

		return False
	else:

		return True




numberOfFiles = getNumberOfFiles()

for folder in range(len(chapterDirs)):
	workingDirectory = chapterDirs[folder]
	# print("Analyzing: " + workingDirectory)
	JPG = os.listdir(SDdir+"/DCIM/"+workingDirectory+"")
	try:
		JPG.remove(".DS_Store")
	except:
		pass
	for picture in range(len(JPG)):
		picturePath = SDdir+"/DCIM/"+workingDirectory+"/"+JPG[picture]
		if (numberOfFiles % 10) == 0:
			print("\n")
			print("\n")
			print("\n")
			print("There are ", numberOfFiles, " images remaining.")
			print("Approximate time left: ", int(exposureTaskPrediction(speed, numberOfFiles)), " seconds.")

		numberOfFiles = numberOfFiles - 1


		if exposureTest(picturePath):
			pass



