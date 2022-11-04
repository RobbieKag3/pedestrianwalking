import cv2
bodyclassifier=cv2.CascadeClassifier("PRO-106-ProjectTemplate-main/haarcascade_fullbody.xml")
cap = cv2.VideoCapture('PRO-106-ProjectTemplate-main/walking.avi')
while True:
    ret,frame=cap.read()
    grey=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    bodies=bodyclassifier.detectMultiScale(grey,1.2,3)
    for(x,y,w,h) in bodies:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)
        cv2.imshow("people walking",frame)
    if cv2.waitKey(1)==32:
        break



cap.release()
cv2.destroyAllWindows()
