import cv2 as cv

#Photos
# mg = cv.imread('Resources/Photos/cat_large.jpg')

# cv.imshow('Cat', mg)

# cv.waitKey(0)

#Videos
capture = cv.VideoCapture(0) # 0 is the default camera, 1 is the next camera, and so on. use the path of the video file to read a video file

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width, height):
    # Live video
    capture.set(3, width)
    capture.set(4, height)

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()