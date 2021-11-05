import os
import time
import cv2
import numpy
from send2trash import send2trash
from tqdm import tqdm


print("File Operations Imported.")


def indexFiles(path):
	imagePaths = []
	subFolders = os.listdir(path+"/DCIM")
	try:
		subFolders.remove(".DS_Store") #for macOS
	except:
		pass
	rawWarned = False

	

	for folder in range(len(subFolders)):
		workingDirectory = subFolders[folder]

		imagePath = os.listdir(path+"/DCIM/"+workingDirectory+"")
		try:
			imagePath.remove(".DS_Store")
		except:
			pass


		for picture in range(len(imagePath)):
			if ((imagePath[picture])[-4:] == ".CR2") and not rawWarned:
				warnAboutRAW()
				rawWarned = True
			if (imagePath[picture])[-4:] == ".JPG" or (imagePath[picture])[-4:] == ".jpg":
				imagePaths.append(path+"/DCIM/"+workingDirectory+"/"+imagePath[picture])
			else:
				pass


			
	return imagePaths



def warnAboutRAW():
	print("\n")
	print("\n")
	print("\n")
	print("*****************")
	print("Warning! RAW files have been found on the selected SD card. The program currently does not support checking RAW files.")
	print("If a JPEG is flagged for removal then the RAW files associated with it will be removed as well.")
	print("A future release will scan RAW files as well, but for the time being please shoot in JPEG+RAW mode on the camera.")
	print("*****************")
	print("\n")
	print("\n")
	print("\n")
	time.sleep(10)


def omitFileExtensions(pathArray):
	imageCount = 0
	for path in pathArray:
		if(path[-4:] == ".JPG" or path[-4:] == ".jpg"):
			imageCount += 1
		if(path[-4:] != ".JPG" and path[-4:] != ".jpg"):
			#ignore non jpeg files
			pathArray.remove(path)
	return pathArray


def getNumberOfFiles(filesArray):
	return len(filesArray)




def purgePhotos():

	f = open("CANON_DC.log", "r")
	todel = f.read()
	imagesToDelete = todel.splitlines()
	print("Deleting flagged pictures...")
	time.sleep(1)

	for image in tqdm(imagesToDelete):

		send2trash(image)
	time.sleep(2)
	print("\n")
	print("\n")

	print("Checking for RAW files and deleting them...")
	for raw in tqdm(imagesToDelete):
		try:
			send2trash(raw[:len(raw)-4]+".CR2")
		except:
			pass

	time.sleep(2)




	f.close()

