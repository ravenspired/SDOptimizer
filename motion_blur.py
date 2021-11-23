import cv2







def variance_of_laplacian(image):
	# compute the Laplacian of the image and then return the focus
	# measure, which is simply the variance of the Laplacian
	return cv2.Laplacian(image, cv2.CV_64F).var()


def motionBlurTest(imageDir, threshold):
	image = cv2.imread(imageDir)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	fm = (variance_of_laplacian(gray))
	if int(fm) >= int(threshold):

		return True
	else:

		return False



