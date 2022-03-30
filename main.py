import cv2

def snapShot():
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frames = videoCaptureObject.read()
        cv2.imwrite("image.jpg", frames)
        result = False
    videoCaptureObject.release()
    cv2.destroyAllWindows()
snapShot()