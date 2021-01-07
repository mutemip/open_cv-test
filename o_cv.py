#computer vision ....deals with getting and processing images
#done using open cv library
#glob library is used to search for file paths at a given patterns
import cv2
import glob

images = glob.glob("*.jpg")

for image in images:
    img = cv2.imread(image, 0)
    resized_img = cv2.resize(img, (150, 150))
    cv2.imshow("Galaxy", resized_img)
    #cv2.imwrite("Galaxy_resized.jpg", resized_img)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()
    cv2.imwrite("resized_"+image, resized_img)