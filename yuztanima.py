#OpenCV'yi projemize ekliyoruz.
import cv2
#Yüz tanıma classımızı ekliyoruz.
face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_alt.xml')
#Webcam'den görüntü alıyoruz.
cap = cv2.VideoCapture(0)
#Bulunan yüzün etrafına eklenecek görselimizi içe aktarıyoruz.
imgsq=cv2.imread("./cerceve.jpg")
while(True):
    #Webcam'den bir frame alıyoruz.
    ret, frame = cap.read()
    #Yüzleri buluyoruz.
    faces = face_cascade.detectMultiScale(frame, 1.3, 5)
    #Bulunan yüzün etrafına çerçeve ve yazı ekliyoruz.
    for (x,y,w,h) in faces:
        rect=frame[y+h/2-100:y+h/2+100,x+w/2-100:x+w/2+100]
        cv2.addWeighted(rect,1,imgsq,1,0,rect)
        cv2.putText(frame,"YUZ",(x+h/4,y+w+40),cv2.FONT_HERSHEY_SIMPLEX,0.6,(255,255,255),2)
    #Son durumun çıktısını alıyoruz.
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
