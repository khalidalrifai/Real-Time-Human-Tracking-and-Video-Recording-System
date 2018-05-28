import cv2
import serial
import helpers


try:
    # change to the corresponding usb output
    serial = serial.Serial('/dev/ttyACM0', 9600)
except Exception as e:
    print(e)

detector = cv2.CascadeClassifier('haar-frontface.xml')  # import the classifier
videoCapture = cv2.VideoCapture(0)
videoWriter = None
outputVideoName = "output"
pause = False
frameCounter = 0
margin = 25

while(True):

    captured, image = videoCapture.read()
    if not captured:
        break

    image = cv2.resize(image, None, fx=0.25, fy=0.25)
    image = cv2.flip(image, 1)

    # initialize the video writer
    if videoWriter is None:
        videoWriter = helpers.initializeVideoWriter(
            image, videoCapture, outputVideoName)

    # convert to gray scale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # detect all faces
    detected = detector.detectMultiScale(
        gray, scaleFactor=1.1, minNeighbors=5, minSize=(10, 10))

    # loop over the faces and draw a rect. and label for each one
    for (x, y, w, h) in detected:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 255, 0), 2)

    # check for multiple faces and pause for one second(30 frames) if more than one face is detected
    faces = len(detected)
    if faces > 1:
        pause = True
        frameCounter = 0

    if pause is True:
        frameCounter += 1

    if frameCounter > 30:
        pause = False

    # get the image center
    imageCenter = image.shape[1] / 2
    # check if there are
    if faces != 0 and pause is False:
        (x, y, w, h) = detected[0]
        detectionCenter = x + w / 2
        # get direction
        direction = helpers.getDirection(imageCenter, margin, detectionCenter)
        # write direction on the screen
        cv2.putText(image, direction, (50, 0 + 50), 5, 2.0, (0, 0, 255), 2)
        # send serial
        serial.write(str(direction).encode())

    # draw lines
    image = helpers.drawLines(image, imageCenter, margin)

    # write video frames into a video
    videoWriter.write(cv2.flip(image, 1))
    # resize and output the video to the screen
    image = cv2.resize(image, None, fx=2.0, fy=2.0)
    cv2.imshow('frame', image)
    # exit loop if command q is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# close all the running operations
videoCapture.release()
if videoWriter != None:
    videoWriter.release()
cv2.destroyAllWindows()
