import cv2

#https://github.com/opencv/opencv/tree/master/data/haarcascades
f_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
img = cv2.imread("news.jpg")

gc_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = f_cascade.detectMultiScale(gc_image, scaleFactor=1.05, minNeighbors=5)
for x, y, w, h in faces:
    img=cv2.rectangle(img,(x,y), (x+w, y+h), (0,255, 0),3)
print(type(faces))
print(faces)
resize = cv2.resize(img, (int(img.shape[1]/3), int(img.shape[0]/3)))
cv2.imshow("test", resize)
cv2.waitKey(0)
cv2.destroyAllWindows()