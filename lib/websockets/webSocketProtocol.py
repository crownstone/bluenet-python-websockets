import json

from autobahn.twisted.websocket import WebSocketServerProtocol

# or: from autobahn.asyncio.websocket import WebSocketServerProtocol
from lib.util.eventBus import eventBus, Topics


class BluenetDashboardProtocol(WebSocketServerProtocol):
    counter = 0
    writeSubscriptionId = 0
    def __init__(self):
        super().__init__()
        self.writeSubscriptionId = eventBus.on(Topics.wsWriteMessage, self.writeMessage)

    def onConnect(self, request):
        print("Client connecting: {}".format(request.peer))
        eventBus.emit(Topics.websocketConnectionInitialized)

    def onOpen(self):
        print("WebSocket connection open.")

    def onMessage(self, payload, isBinary):
        # implementation of basic ping-pong. If this is not added, the connection will fall asleep without any notification, error or event.
        if payload.decode('utf8') == 'ping':
            self.sendMessage(b"pong", isBinary)
            return

        if isBinary:
            print("Binary message received: {} bytes".format(len(payload)))
        else:
            print("Text message received: {}".format(payload.decode('utf8')))
            eventBus.emit(Topics.wsReceivedMessage, payload.decode('utf8'))

    def onClose(self, wasClean, code, reason):
        print("WebSocket connection closed: {}".format(reason))
        eventBus.off(self.writeSubscriptionId)



    def writeMessage(self, data):
        if data["type"] is not None:
            print("sent", self.counter)
            self.counter = self.counter + 1
            self.sendMessage(bytes(str(json.dumps(data)),'utf-8'), False)

