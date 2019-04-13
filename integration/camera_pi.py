import time
import io
import threading
import picamera
RES_X=640
RES_Y=480
CUR_RES_X = RES_X
CUR_RES_Y = RES_Y
class Camera(object):
    thread = None  # background thread that reads frames from camera
    frame = None  # current frame is stored here by background thread
    last_access = 0  # time of last client access to the camera

    def __init__(self,res_x, res_y):
        RES_X = res_x
        RES_Y = res_y
        print(res_x)

    def set_resolution(self,res_x,res_y):
        RES_X = res_x
        RES_Y = res_y
    def get_res(self):
        return RES_X
    def changed_resolution(self):
        if CUR_RES_X != RES_X or CUR_RES_Y != RES_Y:
            return True
        return False

    def initialize(self):
        if Camera.thread is None:
            # start background frame thread
            Camera.thread = threading.Thread(target=self._thread)
            Camera.thread.start()

            # wait until frames start to be available
            while self.frame is None:
                time.sleep(0)

    def get_frame(self):
        Camera.last_access = time.time()
        self.initialize()
        return self.frame

    @classmethod
    def _thread(self):
        with picamera.PiCamera() as camera:
            # camera setup
            camera.resolution = (RES_X, RES_Y)
            camera.hflip = True
            camera.vflip = True

            # let camera warm up
            camera.start_preview()
            time.sleep(2)

            stream = io.BytesIO()
            for foo in camera.capture_continuous(stream, 'jpeg',
                                                 use_video_port=True):
                # store frame
                # if self.changed_resolution():
                #     camera.resolution(RES_X,RES_Y)
                #     CUR_RES_X = RES_X
                #     CUR_RES_Y = RES_Y

                stream.seek(0)
                self.frame = stream.read()

                # reset stream for next frame
                stream.seek(0)
                stream.truncate()

                # if there hasn't been any clients asking for frames in
                # the last 10 seconds stop the thread
                if time.time() - self.last_access > 10:
                    break
        self.thread = None
