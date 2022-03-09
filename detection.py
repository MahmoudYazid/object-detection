import cv2
import numpy as np

# define a video capture object
vid = cv2.VideoCapture(0)
vid.set(900,900)
kernel= np.ones((5,5))

while(True):
    
    # Capture the video frame
    # by frame
    ret, frame = vid.read()

    #get feature
    frame1=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame2=cv2.Canny(frame1, 50, 50)
    frame3=cv2.dilate(frame2, kernel,3)
    feature,s= cv2.findContours(
        frame3, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_TC89_KCOS)
    for f in feature:
       
        arc=cv2.arcLength(f, True)
        edges=cv2.approxPolyDP(f, .01*arc, False)
        #---
        x,y,w,h=cv2.boundingRect(edges)
        
        cv2.circle(frame, (x+w,y+h), 100, (0,255,0))
    
        
    # Display the resulting frame
    
    cv2.imshow('frame1', frame)
    
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop release the cap object
vid.release()

# Destroy all the windows

cv2.destroyAllWindows()