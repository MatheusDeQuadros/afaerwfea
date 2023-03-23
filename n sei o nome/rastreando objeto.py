import cv2

video = cv2.VideoCapture("bb3.mp4")

tracker = cv2.TrackerCSTR_create()

returned,img = video.read()

tracker.int(img,bbox)

print(bbox)

def drawBox(img,bbox):
 x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
 cv2.rectangle(img,(x,y),((x+w),(y+h)),(255,0,255),3,1)
 cv2.putText(img,"Rastreando.....",(75,90),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2)

def gol_track(img,bbox):
 x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])

while True:
 check,img = video.read()
 sucees,bbox = tracker.update(img)

 if sucees:
  drawBox(img,bbox)
 else:
  cv2.putText(img,"Falhou",(75,90),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2)
  cv2.imshow(img,bbox)
  tecla = cv2.waitKey(25)
  if tecla == 32:
   print("parando o video")
   break

video.released()
cv2.destroyAllWindows()