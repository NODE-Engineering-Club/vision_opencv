import cv2
img = cv2.imread('buoy jpegs/NODE buoy.jpg', 0) #0 because we wanna screen it gray, -1 colored
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

#img = cv2.rotate(img, cv2.cv2.ROTATE_90_CLOCKWISE) # if you need rotation


cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#blue, green, red

# Change first 100 rows to random pixels
for i in range(100):
	for j in range(img.shape[1]):
		img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
		
# Copy part of image
tag = img[500:700, 600:900] #copy from row 500 to 700 coloum 600 to 900
img[100:300, 650:950] = tag #random position to paste

