import numpy as np
import cv2

# Load an color image in grayscale
#first argument is the path of the image
#Second argument is a flag which specifies the way image should be read
#img = cv2.imread('messi.jpg',0)
#img = cv2.imread('messi.jpg',-1)
img = cv2.imread('messi.jpg',1)
cv2.imshow('messi.jpg',img)
cv2.waitKey(0)
cv2.destroyAllWindows()





"""import numpy as np
import cv2

img = cv2.imread('messi5.jpg',0)
cv2.imshow('image',img)
k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('messigray.png',img)
    cv2.destroyAllWindows()
    """
