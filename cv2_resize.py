import cv2
import numpy as np

bird = cv2.imread('Indian_Pitta.jpg')


cv2.imshow('Indian Pitta', bird)
cv2.waitKey(0)

print('Image dimensions:', bird.shape)
height, width = bird.shape[:2]
small = cv2.resize(bird,(int(width/4), int(height/4)))

cv2.imshow('Smaller Image', small)
cv2.waitKey(0)

roi = bird[100:200, 100:200]

bird[100:200, 100:200] = np.ones([100, 100, 3])
cv2.imshow('Indian Pitta', bird)
cv2.waitKey(0)

bird[100:200, 100:200] = np.ones([100, 100, 3])*255
cv2.imshow('Indian Pitta', bird)
cv2.waitKey(0)

cv2.destroyAllWindows()
