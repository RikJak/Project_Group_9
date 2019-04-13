import os
import sys
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(f"{FILE_DIR}/../integration")
from flask import Flask, render_template, Response, request, abort
from camera_pi import Camera
# Raspberry Pi camera module (requires picamera package)

PORT = 8000
number_of_args=len(sys.argv)

app = Flask(__name__)
@app.before_request
def limit_remote_addr():
    if  number_of_args >1:
        client_ip = sys.argv[1]
        PORT = sys.argv[2]

    if request.remote_addr != client_ip:
         abort(403)

@app.route('/')

      

def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed', methods = ['POST', 'GET'])
def request_handler():
   if request.method == 'POST':
      res_x = request.form.get('resolution_x')
      res_y = request.form.get('resolution_y')
      camera= Camera(res_x,res_y)
      video_feed(camera)
      return json.dumps{'msg':resolution changed}
    self.video_feed()
def video_feed(camera=None):
    if camera is None:
        camera = Camera(640,480)
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(camera), mimetype='multipart/x-mixed-replace; boundary=frame')

# @app.route('/settings', methods = ['POST'])
# def request_handler():
#    if request.method == 'POST':
#       res_x = request.form.get('resolution_x')
#       res_y = request.form.get('resolution_y')
#       camera= Camera(res_x,res_y)
#       return video_feed(camera)

      


if __name__ == '__main__':
    app.run(host='130.237.215.167', port =PORT, debug=True, threaded=True)
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