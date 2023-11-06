import cv2

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*"MP4V")
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (640,480))

while cap.isOpened():
    ret,frame = cap.read()
    if ret == True:
        out.write(frame)
        cv2.imshow('Spy Cam', frame)
        if cv2.waitKey(1) & 0XFF == ord('q'):
            break
    else:
        print('No Capture Device')
        break

cap.release()
out.release()
cv2.destroyAllWindows()