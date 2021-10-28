import os
import time
import cv2
import numpy
from send2trash import send2trash







def indexFiles(path):
	imagePaths = []
	subFolders = os.listdir(path+"/DCIM")
	try:
		subFolders.remove(".DS_Store") #for macOS
	except:
		pass

	for folder in range(len(subFolders)):
		workingDirectory = subFolders[folder]

		imagePath = os.listdir(path+"/DCIM/"+workingDirectory+"")
		try:
			imagePath.remove(".DS_Store")
			#insert interrupt for files other than jpegs
		except:
			pass

		for picture in range(len(imagePath)):
			imagePaths.append(path+"/DCIM/"+workingDirectory+"/"+imagePath[picture])
	return imagePaths

def omitFileExtensions(pathArray):
	imageCount = 0
	for path in pathArray:
		if(path[-4:] == ".JPG"):
			imageCount += 1
		if(path[-4:] != ".JPG"):
			#ignore non jpeg files
			pathArray.remove(path)
	return pathArray


def getNumberOfFiles(filesArray):
	return len(filesArray)




def purgePhotos():

	f = open("CANON_DC.log", "r")
	todel = f.read()
	imagesToDelete = todel.splitlines()

	for image in imagesToDelete:
		# print("deleting: "+image)
		send2trash(image)



	f.close()

