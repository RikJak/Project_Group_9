import os
import sys


FILE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(f"{FILE_DIR}/../controller")
SERVER_IP = '130.237.215.167'
from contr import Controller
from flask import Flask, redirect, url_for, request
app = Flask(__name__)
controller = Controller()
@app.route('/',methods = ['POST'])
def request_handler(self):
   if self.request.method == 'POST':
      print("found")
      user = request.form['user']
      api_key = request.form['api_key']
      client_ip = request.environ['REMOTE_ADDR']
      self.controller.set_up_stream(user,api_key,client_ip)  
      # return redirect(url_for('success',name = user))

if __name__ == '__main__':
   app.run(host = SERVER_IP)



# import io
# import socketserver
# from threading import Condition
# from http import server

# class StreamingServer(socketserver.ThreadingMixIn, server.HTTPServer):
#     allow_reuse_address = True
#     try:
#         address = ('', 8000)
#         server = StreamingServer(address, StreamingHandler)
#         server.serve_forever()

# class StreamingHandler(server.BaseHTTPRequestHandler):
#     def do_GET(self):
       
#         if self.path == '/':
#             self.send_response(200)
#             self.send_header('Age', 0)
#             self.send_header('Cache-Control', 'no-cache, private')
#             self.send_header('Pragma', 'no-cache')
#             self.send_header('Content-Type', 'multipart/x-mixed-replace; boundary=FRAME')
#             self.end_headers()
#             try:
#                 while True:
#                     with output.condition:
#                         output.condition.wait()
#                         frame = output.frame
#                     self.wfile.write(b'--FRAME\r\n')
#                     self.send_header('Content-Type', 'image/jpeg')
#                     self.send_header('Content-Length', len(frame))
#                     self.end_headers()
#                     self.wfile.write(frame)
#                     self.wfile.write(b'\r\n')
#             except Exception as e:
#                 logging.warning(
#                     'Removed streaming client %s: %s',
#                     self.client_address, str(e))
#         else:
#             self.send_error(404)
#             self.end_headers()
    
#     def do_POST(self):
#         if self.
