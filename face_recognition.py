#Simple Face Recognition with opencv

#importing opencv
import cv2

#loading cascades
face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade=cv2.CascadeClassifier('haarcascade_eye.xml')

#detecting face with eyes
def detect(bw,org):   #bw-black n white image,org-original image
    faces=face_cascade.detectMultiScale(bw,1.3,5)   #scalarFactor=1.5,minNeighbors=5
    #faces = {x,y,w,h} x,y-coordinates w-width h-height
    #iteration through faces and find face and eyes
    for(x,y,w,h) in faces:
        cv2.rectangle(org,(x,y),(x+w,y+h),(255,0,0),2)
        #sun-zone of intrest for eyes in bw and orginal image
        bw_zone=bw[y:y+h,x:x+h]
        org_zone=org[y:y+h,x:x+h]
        eyes=eye_cascade.detectMultiScale(bw_zone,1.1,3) #similar to faces
        for(x1,y1,w1,h1) in eyes:
            #here two rectangles boxes for detecting 2 eyes
            cv2.rectangle(org_zone,(x1,y1),(x1+w1,y1+h1),(0,255,0),2)
    return org

#linking web-cam to detect the faces
#VideoCaputure class helps to take the frame from the video
video_capture=cv2.VideoCapture(0) #0-webCam,1-webcam from other hardware
while True:
    #read of videocaputure class return image as secound parameter
    _,image=video_capture.read()
    #make black and white image from orginal image
    #here cv2.COLOR_RGB2GRAY will make the image to black and white
    bw=cv2.cvtColor(image,cv2.COLOR_RGBA2GRAY)
    detected_face=detect(bw,image)
    #displaying as video
    cv2.imshow('video',detected_face)
    #inorder to stop the process if v press q it ll stop
    if cv2.waitKey(1)&0XFF==ord('q'):
        break
#stop the webcam and turn off windo
video_capture.release()
cv2.destroyAllWindows()  
               
    
