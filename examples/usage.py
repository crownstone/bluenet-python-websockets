import signal

from BluenetLib import Bluenet

# Create new instance of Bluenet
from BluenetWebSocket import WebSocketServer

bluenet = Bluenet(catchSIGINT=False)

# Start up the USB bridge
bluenet.initializeUSB("/dev/tty.usbmodemFD131")

# start the websocket server
server = WebSocketServer(9000)

# connect the websocket server to bluenet
server.connectToBluenet(bluenet)

# make sure everything is killed and cleaned up on abort.
def stopAll(signal, frame):
    server.stop()
    bluenet.stop()

# start listener for SIGINT kill command
signal.signal(signal.SIGINT, stopAll)

# start processes
print("Starting server...")
server.start() # <---- this is blocking
