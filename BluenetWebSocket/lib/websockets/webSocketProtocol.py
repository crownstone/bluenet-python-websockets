import json

from autobahn.twisted.websocket import WebSocketServerProtocol

from BluenetWebSocket._EventBusInstance import WSEventBus
from BluenetWebSocket.lib.topics import Topics


class WebSocketProtocol(WebSocketServerProtocol):
    counter = 0
    writeSubscriptionId = 0
    
    
    def __init__(self):
        super().__init__()
        self.writeSubscriptionId = WSEventBus.subscribe(Topics.wsWriteMessage, self.writeMessage)


    def onConnect(self, request):
        print("Client connecting: {}".format(request.peer))


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
            WSEventBus.emit(Topics.wsReceivedMessage, payload.decode('utf8'))


    def onClose(self, wasClean, code, reason):
        print("WebSocket connection closed: {}".format(reason))
        WSEventBus.unsubscribe(self.writeSubscriptionId)


    def writeMessage(self, data):
        print("sent", self.counter, data)
        self.counter = self.counter + 1
        self.sendMessage(bytes(str(json.dumps(data)),'utf-8'), False)

