import cv2

video = cv2.VideoCapture('./videos/demo.mp4')

numberPlateCascade = cv2.CascadeClassifier('./haarcascades/haarcascade_russian_plate_number.xml')

counter = 0

while True:
    ret, frame = video.read()
    frame = cv2.resize(frame, (640, 480))

    if not ret:
        break

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    number_plate = numberPlateCascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=10)
    print("enter this block")
    print("number plate:", number_plate)
    print("number plate length:", len(number_plate))
    for (x, y, w, h) in number_plate:
        print(x, y, w, h)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, "Number Plate", (x, y - 10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 255), 2)

        # crop the number plate
        frameROI = frame[y:y + h, x:x + w]

    cv2.imshow('frame', frame)
    cv2.imshow('numberPlate', frameROI)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
