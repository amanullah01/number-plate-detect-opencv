import cv2

video = cv2.VideoCapture('./videos/demo.mp4')

numberPlateCascade = cv2.CascadeClassifier('./haarcascades/haarcascade_frontalface_default.xml')

counter = 0

while True:
    ret, frame = video.read()

    if not ret:
        break

    cv2.imshow('frame', frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
