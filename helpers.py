import cv2
from picamera.array import PiRGBArray
from picamera import PiCamera


def initializePICamera():
    # initialize the camera and grab a reference to the raw camera capture
    camera = PiCamera()
    camera.resolution = (640, 480)
    camera.framerate = 32
    rawCapture = PiRGBArray(camera, size=(640, 480))

    return camera, rawCapture


def initializeVideoWriter(frame, video, outputVideoName, fps=None):

    if fps is not None:
        fps = int(fps)

    opencvVersion = cv2.__version__.split('.')

    fourcc = None
    if int(opencvVersion[0]) is 2:
        fourcc = cv2.cv.CV_FOURCC(*'MJPG')

    elif int(opencvVersion[0]) is 3:
        fourcc = cv2.VideoWriter_fourcc(*"XVID")  # MJPG XVID

    (h, w) = frame.shape[:2]

    if fps is None:
        if int(opencvVersion[0]) is 2:
            fps = video.get(cv2.cv.CV_CAP_PROP_FPS)
            # print "first condition"

        elif int(opencvVersion[0]) is 3:

            fps = video.get(cv2.CAP_PROP_FPS)
            # print "second condition"

    if repr(fps) == 'nan' or fps is None or int(fps) <= 0:
        fps = 30
    print "fps: ", fps

    videoWriter = cv2.VideoWriter(
        str(outputVideoName) + ".avi",
        fourcc, 10, (w, h), True)  # int(fps)

    return videoWriter


def drawLines(image, imageCenter, margin):

        # cv2.line(image, (imageCenter, 0), (imageCenter,
        # image.shape[0]), (0, 255, 0), thickness=1)

    cv2.line(image, (imageCenter + margin, 0), (imageCenter + margin,
                                                image.shape[0]), (0, 255, 0), thickness=1)

    cv2.line(image, (imageCenter - margin, 0), (imageCenter - margin,
                                                image.shape[0]), (0, 255, 0), thickness=1)

    return image


def getDirection(imageCenter, margin, detectionCenter):

    if detectionCenter < imageCenter + margin or detectionCenter > imageCenter - margin:  # center
        direction = "C"

    if detectionCenter < imageCenter - margin:  # left
        direction = "L"

    elif detectionCenter > imageCenter + margin:  # right
        direction = "R"

    return direction
