import cv2

img = cv2.imread('videos_to_cut/2019-05-11_06.31.53/2.jpg')
# print(img)
key=cv2.waitKey(100000000)
cv2.imshow('img',img)