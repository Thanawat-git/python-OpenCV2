import cv2
img = cv2.imread("cat2.jpg",1)
img = cv2.line(img, (0,0), (255,255), (255,0,255), 5) #เส้นตรง
img = cv2.arrowedLine(img, (0,0), (200,200), (255,0,0), 5) #ลูกศร
img = cv2.rectangle(img, (100,0), (0,100), (0,0,255), 5) #สี่เหลี่ยมผืนผ้า
img = cv2.circle(img, (277,55), 63, (0,255,0), -1) #วงกลม
cv2.imshow("cat",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

