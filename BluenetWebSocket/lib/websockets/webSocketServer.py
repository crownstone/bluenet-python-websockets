from autobahn.twisted.websocket import WebSocketServerFactory
from twisted.internet import reactor

from BluenetWebSocket.lib.websockets.webSocketProtocol import WebSocketProtocol


class WebSocketServerCore:
    port = 9000

    def __init__(self, port = 9000):
        self.port = port

    def start(self):
        factory = WebSocketServerFactory()
        factory.protocol = WebSocketProtocol

        reactor.listenTCP(self.port, factory)
        reactor.run()

    def stop(self):
        print("\nClose Command Received: Stopping Server...")
        reactor.stop()
