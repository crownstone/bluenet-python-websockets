import signal
import sys

sys.path.append('./bluenet/')

from BluenetLib import Bluenet
from lib.connector.BluenetConnector import BluenetConnector
from lib.websockets.webSocketServer import WebSocketServer

# Create new instance of Bluenet
bluenet = Bluenet()

# Start up the USB bridge
bluenet.initializeUsbBridge("/dev/tty.usbmodemFA1331")

# initiate the Websocket server
server = WebSocketServer(port=9000)

# connect the Bluenet lib eventBus to the webSockets
connector = BluenetConnector()
connector.connect(bluenet.getEventBus(), bluenet.getTopics())

# make sure everything is killed and cleaned up on abort.
def stopAll(signal, frame):
    server.stop()

# start listener for SIGINT kill command
signal.signal(signal.SIGINT, stopAll)

# start processes
server.start() # <---- this is blocking
