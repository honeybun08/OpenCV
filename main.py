import cv2

img = cv2.imread('test.jpg')  # считываем картиночку

# img = cv2.resize(img, (500, 500))

cv2.imshow('Result', img) # result это название окна где покажется картинка

cv2.waitKey(0)

