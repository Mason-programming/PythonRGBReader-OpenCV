import cv2

class RGBreader:
    def __init__(self, photo):
        self.photo = photo

    def readPhoto(self):
        img = cv2.imread(self.photo)
        cv2.imshow('photo',img)
        color = (img[300,300])
        print(color)
        cv2.waitKey(0)

