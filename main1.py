import cv2
import time
import dropbox
import random

start_time = time.time()

def snapShot():
    number = random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret, frames = videoCaptureObject.read()
        img_name = "img" + str(number) + ".png"
        cv2.imwrite(img_name,frames)
        start_time = time.time
        result = False
    return img_name
    print("SnapShot taken!")
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def upload_file(img_name):
    access_token = "sl.BEwPpe8fIdCvKYjHt0k_-kFjGrBFenApMlDWu-Tl3QL7LtLSsVWkwYu_MalCpsrHw2hgl4EVfNcT4XnIhvbfZPycmwP9ZIvaHKv35eA19_ldEaWkceUg0MGvOJtv_AtnjZu28hzQuARa"
    file = img_name
    file_from = file
    file_to = "/Project102/" + (img_name)
    dbx = dropbox.Dropbox(access_token)
    with open(file_from,'rb') as f:
        dbx.files_upload(f.read(),file_to,mode = dropbox.files.WriteMode.overwrite)
        print("Files Uploaded")

def main():
    while(True):
        if((time.time()-start_time)>=300):
            name = snapShot()
            upload_file(name)
main()