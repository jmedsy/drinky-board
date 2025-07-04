from flask import Flask, jsonify
from flask_cors import CORS
from routes import find_itsybitsy_ports
from routes.outputTests import output_tests_bp
import threading
import queue
import signal
import atexit
import time

app = Flask(__name__)
CORS(app, origins=["http://localhost:3000"])

# Register blueprints
app.register_blueprint(find_itsybitsy_ports.bp)
app.register_blueprint(output_tests_bp)

#region Drinky Board manager
##########################################################

command_queue = queue.Queue()
stop_event = threading.Event()

def drinky_manager():
    while not stop_event.is_set():
        try:
            cmd = command_queue.get(timeout=0.5)
        except queue.Empty:
            continue
        # Process command...
        time.sleep(0.2)
    # 🔄 Cleanup logic here
    print("Worker doing cleanup before exit")

def start_drinky_manager():
    thread = threading.Thread(target=drinky_manager, daemon=True)
    thread.start()
    return thread

def stop_drinky_manager():
    stop_event.set()
    print("Stopping Drinky Board manager...")

def drinky_shutdown_handler(signum, frame):
    print(f"\nReceived signal {signum}, shutting down...")
    stop_drinky_manager()
    # Force exit after a short delay to allow cleanup
    import os
    # import threading
    def force_exit():
        time.sleep(1)
        print("Force exiting...")
        os._exit(0)  # Force immediate exit
    threading.Thread(target=force_exit, daemon=True).start()

atexit.register(stop_drinky_manager)
signal.signal(signal.SIGINT, drinky_shutdown_handler)
signal.signal(signal.SIGTERM, drinky_shutdown_handler)

drinky_manager_thread = start_drinky_manager()
print("Drinky Board manager started")

##########################################################
#endregion