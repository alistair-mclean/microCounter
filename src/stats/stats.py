import cv2
import numpy as np
import matplotlib.pyplot as plt



def histogramImage(image):
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	blue, green, red = cv2.split(image)

#	print('Green',green)
	histr1 = cv2.calcHist([gray],[0], None, [256],[1,256])
	histr2 = cv2.calcHist([red],[0], None, [256],[1,256])
	histr3 = cv2.calcHist([green],[0], None, [256],[1,256])
	histr4 = cv2.calcHist([blue],[0], None, [256],[1,256])


	plt.subplot(2,2,1),plt.imshow(image,cmap='gray')
	plt.title('Original'), plt.xticks([]), plt.yticks([])
	plt.subplot(2,2,2),plt.imshow(histr2,cmap='gray')
	plt.title('Red Pixel Values'), plt.xticks([]), plt.yticks([])
	plt.subplot(2,2,3),plt.imshow(histr3,cmap='gray')
	plt.title('Green Pixel Values'), plt.xticks([]), plt.yticks([])
	plt.subplot(2,2,4),plt.imshow(histr4,cmap='gray')
	plt.title('Blue Pixel Values'), plt.xticks([]), plt.yticks([])
	
	# FIrst thing that needs to be considered is the fact that we have most pixels turned off.
	# If the value is not within the 
	plt.hist(gray.ravel(), bins=256, range=(10, 155), fc='k', ec='k')
	plt.show()
	plt.plot(histr1)
	plt.show()


testImg = cv2.imread('../../samples/Mix_Well1_2Steel_new.tif')
histogramImage(testImg)
