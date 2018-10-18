import cv2
import time

class VideoCamera(object):

    def __init__(self, videoPath = "./static/final-run/sample2.mp4"):
        self.video = cv2.VideoCapture(videoPath)
    
    def __del__(self):
        self.video.release()

    def get_frame(self):
        time.sleep(0.2)
        success, image = self.video.read()
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()
