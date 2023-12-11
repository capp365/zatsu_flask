from flask import Flask, render_template
from flask_socketio import SocketIO
import threading
import time
from llms import *

app = Flask(__name__)
socketio = SocketIO(app)

def background_task():
    while True:
        time.sleep(10)
        text = get_response()
        socketio.emit('my response', {'data': text})

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    thread = threading.Thread(target=background_task)
    thread.daemon = True
    thread.start()

    socketio.run(app, debug=True, use_reloader=False)
