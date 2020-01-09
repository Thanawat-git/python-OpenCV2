#open Camera
import cv2

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    features = classifier.detectMultiScale(gray, scaleFactor, minNeighbors) #detect ใบหน้า
    coords = [] # use to keep x,y possition ของใบหน้า
    for (x, y, w, h) in features:
        cv2.rectangle(img, (x,y), (x+w, y+h), color, 2) #วาดสี่เหลี่ยมผืนผ้า เลย 2 คือความหน้าของเส้น
        cv2.putText(img, text, (x+10,y-10), cv2.FONT_HERSHEY_DUPLEX, 0.8, color, 1) #ใส่ข้อความลงไปในภาพตรงที่เราตรวจจับได้
    return img

def detect(img, faceCascade): #เรียกใช้งาน draw_boundary
    img = draw_boundary(img, faceCascade, 1.1, 10, (255,0,0), "It,s Me!")
    return img

cap = cv2.VideoCapture(0) #เปิดกล้อง เลข 0 คือค่า index ของกล้อง ถ้ามีตัวเดียวก็คือ ตัวที่ 0
#ถ้าต้องการให้เปิด video ให้ทำการเปลี่ยนเลข 0 เป็นชื่อ video 
while True: #loop เพื่อเปิดกล้องเรื่อยๆ
    ret, frame = cap.read() #อ่านค่าภาพจากกล้องละ frame by .read
    frame = detect(frame, faceCascade)
    cv2.imshow('frame', frame) #แสดงผลทีละ frame
    if(cv2.waitKey(1) & 0xFF== ord('q')): #เช็คเงื่อนไขเพื่อปิดกล้อง หรือ ออกจาก loop
        break

cap.release() #คืนทรัพยากรให้แก่เครื่อง
cv2.destroyAllWindows() #ปิดหน้าจอ
