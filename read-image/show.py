import cv2

img = cv2.imread('image.png')
img = cv2.resize(img, (300,300))
cv2.imshow('New Profile', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
    
    