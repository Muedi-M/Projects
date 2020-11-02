# RUN THIS CODE FIRST.
# WHAT IT DOES IS CAPTURE THE BACKGROUND THAT WILL BE USED . SO WHEN THE WEBCAM IS ON JUST MOVE AND CAPTURE THE BACKGROUND BY PRESSING "Q"

import cv2

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, back = cap.read()  # THIS READS THE WEBCAM
    if ret:
        # back is what the camera is reading
        cv2.imshow("image", back)
        if cv2.waitKey(5) == ord('q'):
            # save the image
            cv2.imwrite('image.jpg', back)
            break

cap.release()
cv2.destroyAllWindows()
