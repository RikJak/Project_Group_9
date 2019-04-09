import os
import sys
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(f"{FILE_DIR}/../integration")
from flask import Flask, render_template, Response, request, abort
from camera_pi import Camera


from flask import Flask, render_template, Response

# Raspberry Pi camera module (requires picamera package)
from camera_pi import Camera

app = Flask(__name__)


@app.route('/')
# def index():
#     """Video streaming home page."""
#     return render_template('index.html')


def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='130.237.215.167', port =8000, debug=True, threaded=True)
# # def start_stream(client_ip,port):
# PORT = 8000
# SERVER_IP = '130.237.215.167'
# app = Flask(__name__)
#     # app.run(host=SERVER_IP, port = PORT, debug=True, threaded=True)
#     # @app.before_request
#     # def limit_remote_addr():
#     #         if request.remote_addr != client_ip:
#     #             abort(403)
# @app.route('/')
#         # def index():
#         #     """Video streaming home page."""
#         #     return render_template('index.html')
# def gen(camera):
#     """Video streaming generator function."""
#     while True:
#         frame = camera.get_frame()
#         yield (b'--frame\r\n'+b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
# @app.route('/video_feed')
# def video_feed():
#         """Video streaming route. Put this in the src attribute of an img tag."""
#         return Response(gen(Camera()), mimetype='multipart/x-mixed-replace; boundary=frame')
# if __name__ == '__main__':
#   app.run(host=SERVER_IP, port = PORT, debug=True, threaded=True)