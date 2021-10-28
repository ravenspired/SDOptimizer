#Main code for SDOptimizer
import time
import cv2
import numpy
import os





def exposureBenchmark(imageDir):
	image = cv2.imread(imageDir)
	image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	# compute a grayscale histogram
	hist = cv2.calcHist([image], [0], None, [256], [0, 256])
	#print("this image has an exposure value of: ",numpy.mean(image))

	if (numpy.mean(image)>=-1):
		return True






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



def benchmarkExposure():

	start = time.time()
	for i in range(30):
		if exposureBenchmark("sample.JPG"):
			pass
	end = time.time()
	speed = (end-start)/30
	return speed
