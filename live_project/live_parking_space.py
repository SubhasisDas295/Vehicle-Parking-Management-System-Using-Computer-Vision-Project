import pickle
import cv2
 
width, height = 48, 80   #Ultimate height and width of parking lot
 
try:
    with open('CarParkPos', 'rb') as f:
        #for Loading
        posList = pickle.load(f)
except:
    posList = []
 
 
def mouseClick(events, x, y, flags, params):
    #When we use leftbutton
    if events == cv2.EVENT_LBUTTONDOWN:
        posList.append((x, y))

    #When we use rightbutton    
    if events == cv2.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(posList):
            x1, y1 = pos
            if x1 < x < x1 + width and y1 < y < y1 + height:
                posList.pop(i)
 
    with open('CarParkPos', 'wb') as f:
        #To dump the position
        pickle.dump(posList, f)
 
 
while True:
    #To read image from system
    img = cv2.imread('car_parking_live_demo.jpg')

    for pos in posList:
        #To make a rectangle for detection

        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), (255, 0, 255), 2)
 
    cv2.imshow("Image", img)       #To show the image on system

    #To callback the mouseclick function 
    cv2.setMouseCallback("Image", mouseClick) 

    cv2.waitKey(1) #To show image fastly
