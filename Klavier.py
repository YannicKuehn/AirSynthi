import numpy as np
import cv2
import rtmidi
import mido
import time

print("Midi output ports: ", mido.get_output_names())
midiOutput = mido.open_output("LoopBe Internal MIDI 1") #hier ändern falls MAC

# cap = cv2.VideoCapture('./img/klavier_PS_2.mp4')
cap = cv2.VideoCapture(0)

cv2.namedWindow('Video1')

def nothing (x):
    pass

#lower keys
cv2.createTrackbar('thresholdH', 'Video1', 20, 180, nothing)
cv2.createTrackbar('thresholdS', 'Video1', 30, 255, nothing)
cv2.createTrackbar('thresholdV', 'Video1', 30, 255, nothing)

#upper keys
cv2.createTrackbar('thresholdH2', 'Video1', 20, 180, nothing)
cv2.createTrackbar('thresholdS2', 'Video1', 30, 255, nothing)
cv2.createTrackbar('thresholdV2', 'Video1', 30, 255, nothing)

#marker
cv2.createTrackbar('thresholdH3', 'Video1', 40, 180, nothing)
cv2.createTrackbar('thresholdS3', 'Video1', 40, 255, nothing)
cv2.createTrackbar('thresholdV3', 'Video1', 40, 255, nothing)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
dEkernel = np.ones((3,3), np.uint8)

def mouseCallback(event, x, y, flags, param):
    print('h: ' + str(h[y][x]))
    print('s: ' + str(s[y][x]))
    print('v: ' + str(v[y][x]))

upperKeyStates = [False, False, False, False, False, False]
lowerKeyStates = [False, False, False, False, False, False, False, False, False]

def keyDetect(marker, contours, contours2 , r, g, b):
    upperKeyBuffer = []
    lowerKeyBuffer = []
    for cnt in contours:
        x,y,width,height = cv2.boundingRect(cnt)
        if height > 50 and width > 20:
            cv2.rectangle(frame,(x,y),(x+width,y+height),(b, g, r),2)
            lowerKeyBuffer.append((x, y, width, height))
            if (marker[0] > x and marker[0] < x + width and marker[1] > y and marker[1] < y + height):
                lowerKeyManager(len(lowerKeyBuffer))
            else: 
                lowerOff(len(lowerKeyBuffer))          
    for cnt in contours2:
        x,y,width,height = cv2.boundingRect(cnt)
        if height > 50 and width > 20:
            cv2.rectangle(frame,(x,y),(x+width,y+height),(b, r, g),2)
            upperKeyBuffer.append((x, y, width, height))
            if (marker[0] > x and marker[0] < x + width and marker[1] > y and marker[1] < y + height):
                upperKeyManager(len(upperKeyBuffer))
            else:
                upperOff(len(upperKeyBuffer))                                      
  
def upperKeyManager(index):
    if(index == 1 and not upperKeyStates[0]):
        sendMidiOn(73, 100)
        upperKeyStates[0] = True
        print("note " + str(73) + " on!")
    elif(index == 2 and not upperKeyStates[1]):
        sendMidiOn(70, 100)
        upperKeyStates[1] = True
        print("note " + str(70) + " on!")
    elif(index == 3 and not upperKeyStates[2]):
        sendMidiOn(68, 100)
        upperKeyStates[2] = True
        print("note " + str(68) + " on!")
    elif(index == 4 and not upperKeyStates[3]):
        sendMidiOn(66, 100)
        upperKeyStates[3] = True
        print("note " + str(66) + " on!")
    elif(index == 5 and not upperKeyStates[4]):
        sendMidiOn(63, 100)
        upperKeyStates[4] = True
        print("note " + str(63) + " on!")
    elif(index == 6 and not upperKeyStates[5]):
        sendMidiOn(61, 100)
        upperKeyStates[5] = True
        print("note " + str(61) + " on!")

def lowerKeyManager(index):
    if(index == 1 and not lowerKeyStates[0]):
        sendMidiOn(74, 100)
        lowerKeyStates[0] = True
        print("note " + str(74) + " on!")
    elif(index == 2 and not lowerKeyStates[1]):
        sendMidiOn(72, 100)
        lowerKeyStates[1] = True
        print("note " + str(72) + " on!")
    elif(index == 3 and not lowerKeyStates[2]):
        sendMidiOn(71, 100)
        lowerKeyStates[2] = True
        print("note " + str(71) + " on!")
    elif(index == 4 and not lowerKeyStates[3]):
        sendMidiOn(69, 100)
        lowerKeyStates[3] = True
        print("note " + str(69) + " on!")
    elif(index == 5 and not lowerKeyStates[4]):
        sendMidiOn(67, 100)
        lowerKeyStates[4] = True
        print("note " + str(67) + " on!")
    elif(index == 6 and not lowerKeyStates[5]):
        sendMidiOn(65, 100)
        lowerKeyStates[5] = True
        print("note " + str(65) + " on!")
    elif(index == 7 and not lowerKeyStates[6]):
        sendMidiOn(64, 100)
        lowerKeyStates[6] = True
        print("note " + str(64) + " on!")
    elif(index == 8 and not lowerKeyStates[7]):
        sendMidiOn(62, 100)
        lowerKeyStates[7] = True
        print("note " + str(62) + " on!")
    elif(index == 9 and not lowerKeyStates[8]):
        lowerKeyStates[8] = True
        sendMidiOn(60, 100)
        print("note " + str(60) + " on!")

def lowerOff(index):
    if(lowerKeyStates[0] and index == 1):
        sendMidiOff(74, 0)
        lowerKeyStates[0] = False
    if(lowerKeyStates[1] and index == 2):
        sendMidiOff(72, 0)
        lowerKeyStates[1] = False
    if(lowerKeyStates[2] and index == 3):
        sendMidiOff(71, 0)
        lowerKeyStates[2] = False
    if(lowerKeyStates[3] and index == 4):
        sendMidiOff(69, 0)
        lowerKeyStates[3] = False
    if(lowerKeyStates[4] and index == 5):
        sendMidiOff(67, 0)
        lowerKeyStates[4] = False
    if(lowerKeyStates[5] and index == 6):
        sendMidiOff(65, 0)
        lowerKeyStates[5] = False
    if(lowerKeyStates[6] and index == 7):
        sendMidiOff(64, 0)
        lowerKeyStates[6] = False
    if(lowerKeyStates[7] and index == 8):
        sendMidiOff(62, 0)
        lowerKeyStates[7] = False
    if(lowerKeyStates[8] and index == 9):
        sendMidiOff(60, 0)
        lowerKeyStates[8] = False

def upperOff(index):    
    if(upperKeyStates[0] and index == 1):
        sendMidiOff(73, 0)
        upperKeyStates[0] = False
    if(upperKeyStates[1] and index == 2):
        sendMidiOff(70, 0)
        upperKeyStates[1] = False
    if(upperKeyStates[2] and index == 3):
        sendMidiOff(68, 0)
        upperKeyStates[2] = False
    if(upperKeyStates[3] and index == 4):
        sendMidiOff(66, 0)
        upperKeyStates[3] = False
    if(upperKeyStates[4] and index == 5):
        sendMidiOff(63, 0)
        upperKeyStates[4] = False
    if(upperKeyStates[5] and index == 6):
        sendMidiOff(61, 0)
        upperKeyStates[5] = False

def sendMidiOn(note, velocity):
    message = mido.Message('note_on', note=note, velocity=velocity)
    midiOutput.send(message)

def sendMidiOff(note, velocity):
    message = mido.Message('note_off', note=note, velocity=velocity)
    midiOutput.send(message)

def sendMidiControlChange(control, value):
    message = mido.Message('control_change', control=control, value=value)
    midiOutput.send(message)
       
while cap.isOpened():
    ret, frame = cap.read()

    cv2.setMouseCallback("Video", mouseCallback)

    #Aufteilen des Frames in h,s,v chnnels
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)

    #lower keys
    typicalH, typicalS , typicalV = 120, 250, 240
    #typicalH, typicalS , typicalV = 80, 80, 150

    #upper keys
    typicalH2, typicalS2 , typicalV2 = 60, 245, 255
    #typicalH2, typicalS2 , typicalV2 = 110, 150, 150 

    #marker
    typicalH3, typicalS3 , typicalV3 = 0, 240, 234
    #typicalH3, typicalS3 , typicalV3 = 180, 70, 210 

    #lower keys
    lowerH = typicalH - cv2.getTrackbarPos('thresholdH', 'Video1')
    lowerS = typicalS - cv2.getTrackbarPos('thresholdS', 'Video1')
    lowerV = typicalV - cv2.getTrackbarPos('thresholdV', 'Video1')

    upperH = typicalH + cv2.getTrackbarPos('thresholdH', 'Video1')
    upperS = typicalS + cv2.getTrackbarPos('thresholdS', 'Video1')
    upperV = typicalV + cv2.getTrackbarPos('thresholdV', 'Video1')

    #upper keys
    lowerH2 = typicalH2 - cv2.getTrackbarPos('thresholdH2', 'Video1')
    lowerS2 = typicalS2 - cv2.getTrackbarPos('thresholdS2', 'Video1')
    lowerV2 = typicalV2 - cv2.getTrackbarPos('thresholdV2', 'Video1')

    upperH2 = typicalH2 + cv2.getTrackbarPos('thresholdH2', 'Video1')
    upperS2 = typicalS2 + cv2.getTrackbarPos('thresholdS2', 'Video1')
    upperV2 = typicalV2 + cv2.getTrackbarPos('thresholdV2', 'Video1')

    #marker
    lowerH3 = typicalH3 - cv2.getTrackbarPos('thresholdH3', 'Video1')
    lowerS3 = typicalS3 - cv2.getTrackbarPos('thresholdS3', 'Video1')
    lowerV3 = typicalV3 - cv2.getTrackbarPos('thresholdV3', 'Video1')

    upperH3 = typicalH3 + cv2.getTrackbarPos('thresholdH3', 'Video1')
    upperS3 = typicalS3 + cv2.getTrackbarPos('thresholdS3', 'Video1')
    upperV3 = typicalV3 + cv2.getTrackbarPos('thresholdV3', 'Video1')


    # lower keys
    maskh = cv2.inRange(h, lowerH, upperH, 180)
    masks = cv2.inRange(s, lowerS, upperS, 255)
    maskv = cv2.inRange(v, lowerV, upperV, 255)

    # upper keys
    maskh2 = cv2.inRange(h, lowerH2, upperH2, 180)
    masks2 = cv2.inRange(s, lowerS2, upperS2, 255)
    maskv2 = cv2.inRange(v, lowerV2, upperV2, 255)

    #marker
    maskh3 = cv2.inRange(h, lowerH3, upperH3, 180)
    masks3 = cv2.inRange(s, lowerS3, upperS3, 255)
    maskv3 = cv2.inRange(v, lowerV3, upperV3, 255)

    # lower keys
    mask = maskh * masks * maskv

    # upper keys
    mask2 = maskh2 * masks2 * maskv2

    # marker
    mask3 = maskh3 * masks3 * maskv3


    # lower keys
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)
    dilation = cv2.dilate(closing, dEkernel, iterations=1)

    # upper keys
    opening2 = cv2.morphologyEx(mask2, cv2.MORPH_OPEN, kernel)
    closing2 = cv2.morphologyEx(opening2, cv2.MORPH_CLOSE, kernel)
    dilation2 = cv2.dilate(closing2, dEkernel, iterations=1)

    #marker
    closing3 = cv2.morphologyEx(mask3, cv2.MORPH_CLOSE, kernel)
    dilation3 = cv2.dilate(closing3, dEkernel, iterations=3)

    ret, thresh = cv2.threshold(dilation,127,255,0)
    ret2, thresh2 = cv2.threshold(dilation2,127,255,0)
    ret3, thresh3 = cv2.threshold(dilation3,127,255,0)
    contours,hierarchy = cv2.findContours(thresh, 1, 2)
    contours2,hierarchy2 = cv2.findContours(thresh2, 1, 2)
    contours3,hierarchy3 = cv2.findContours(thresh3, 1, 2)
    
    # Blob code
    M = cv2.moments(thresh3)

    if M["m00"] != 0:
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
    else:
        cX, cY = 0, 0

    cv2.circle(frame, (cX,cY), 2, (255, 255, 255), -1)

    #detect Keys
    keyDetect((cX, cY), contours, contours2, 0, 255, 0)

    # Masken
    cv2.imshow('Video1', dilation)
    cv2.imshow('Video2', dilation2)
    cv2.imshow('Video3', dilation3)

    cv2.imshow('Video', frame)

    if cv2.waitKey(25) != -1:
        break

cap.release()
cv2.destroyAllWindows()