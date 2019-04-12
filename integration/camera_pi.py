import time
import io
import threading
import picamera


class Camera(object):
    thread = None  # background thread that reads frames from camera
    frame = None  # current frame is stored here by background thread
    last_access = 0  # time of last client access to the camera
    camera =picamera.PiCamera() 

    def initialize(self):
        if Camera.thread is None:
            # start background frame thread
            Camera.thread = threading.Thread(target=self._thread(self))
            Camera.thread.start()

            # wait until frames start to be available
            while self.frame is None:
                time.sleep(0)

    def get_frame(self):
        Camera.last_access = time.time()
        self.initialize()
        return self.frame
    def set_resolution(self,res_x,res_y):
        self.camera.resolution(res_x,res_y)
    @classmethod
    def _thread(self,cls):
       # with as camera:
            # camera setup
            self.camera.resolution = (640, 480)
            self.camera.hflip = True
            self.camera.vflip = True

            # let camera warm up
            self.camera.start_preview()
            time.sleep(2)

            stream = io.BytesIO()
            for foo in self.camera.capture_continuous(stream, 'jpeg',
                                                 use_video_port=True):
                # store frame
                stream.seek(0)
                cls.frame = stream.read()

                # reset stream for next frame
                stream.seek(0)
                stream.truncate()

                # if there hasn't been any clients asking for frames in
                # the last 10 seconds stop the thread
                if time.time() - cls.last_access > 10:
                    break
            cls.thread = None
