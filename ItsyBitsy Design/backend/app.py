from flask import Flask
from flask_cors import CORS
import threading
import signal
import atexit
import time
from logic.itsybitsy_device import ItsyBitsyDevice

app = Flask(__name__)
CORS(app, origins=['http://localhost:3000'])

#region Drinky Board manager
##########################################################
# Global variable for the ItsyBitsy device
itsy_device = None
# Global state for modifier keys in Direct Input mode
active_modifiers = set()

stop_event = threading.Event()

def drinky_manager():
    '''Background thread for device discovery and health monitoring'''
    global itsy_device
    
    def find_and_connect_device():
        '''Find and connect to an ItsyBitsy device'''
        global itsy_device
        devices = ItsyBitsyDevice.find_devices()
        if devices:
            # Close any existing device
            if itsy_device:
                itsy_device.close()
            
            # Connect to the first available device
            itsy_device = devices[0]
            print(f'Connected to device on port {itsy_device.port}')
            
            # Close any additional devices found
            for unused in devices[1:]:
                unused.close()
            return True
        return False

    # Initial device discovery
    if not find_and_connect_device():
        print('No devices found on startup')
    
    # Health monitoring loop
    last_device_check = time.time()
    device_check_interval = 1.0  # Check device health every 1 second
    last_device_scan = time.time()
    device_scan_interval = 2.0  # Scan for new devices every 2 seconds

    while not stop_event.is_set():
        try:
            time.sleep(1)  # Check every second
            
            current_time = time.time()
            
            # Check device health
            if current_time - last_device_check > device_check_interval:
                if itsy_device and not itsy_device.is_connected():
                    print('Device is unresponsive, will attempt reconnection...')
                    itsy_device.close()
                    itsy_device = None
                last_device_check = current_time
            
            # Scan for new devices if we don't have one
            if current_time - last_device_scan > device_scan_interval:
                if not itsy_device:
                    print('Scanning for devices...')
                    find_and_connect_device()
                last_device_scan = current_time
                
        except Exception as e:
            print(f'Error in drinky_manager: {e}')
            time.sleep(0.5)  # Wait before retrying

    # Cleanup on shutdown
    if itsy_device:
        print('Closing device connection...')
        itsy_device.close()

def start_drinky_manager():
    '''Start the background device management thread'''
    thread = threading.Thread(target=drinky_manager, daemon=True)
    thread.start()
    return thread

def stop_drinky_manager():
    '''Stop the background device management thread'''
    stop_event.set()
    print('Stopping Drinky Board manager...')

def drinky_shutdown_handler(signum, frame):
    '''Handle shutdown signals gracefully'''
    print(f'\nReceived signal {signum}, shutting down...')
    stop_drinky_manager()
    # Force exit after a short delay to allow cleanup
    import os
    def force_exit():
        time.sleep(1)
        print('Force exiting...')
        os._exit(0)
    threading.Thread(target=force_exit, daemon=True).start()

# Register cleanup handlers
atexit.register(stop_drinky_manager)
signal.signal(signal.SIGINT, drinky_shutdown_handler)
signal.signal(signal.SIGTERM, drinky_shutdown_handler)

# Start the device manager
drinky_manager_thread = start_drinky_manager()
print('Drinky Board manager started')
##########################################################
#endregion

# Import routes after global variables are defined to avoid circular imports
from routes import connection_status, direct_input, output_tests

# Register blueprints
app.register_blueprint(connection_status.bp)
app.register_blueprint(direct_input.bp)
app.register_blueprint(output_tests.bp)