import cv2
from rgbreader import RGBreader

class Camera:
    def turnOn(self):
        C1 = cv2.VideoCapture(0)

        while (True):
            # Capture frame-by-frame
            ret, frame = C1.read()
            # Display the resulting frame
            cv2.imshow('frame', frame)
            if cv2.waitKey(0) & 0xFF == ord('q'):
                cv2.imwrite('imgs.png', frame)
                break

        r1 = RGBreader("/Users/masonkirby/rgb_reader/imgs.png")
        r1.readPhoto()

        # When everything done, release the capture
        C1.release()
        cv2.destroyAllWindows()


