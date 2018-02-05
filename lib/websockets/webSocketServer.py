from autobahn.twisted.websocket import WebSocketServerFactory
from twisted.internet import reactor

from lib.websockets.webSocketProtocol import BluenetDashboardProtocol


class WebSocketServer:
    port = 9000

    def __init__(self, port = 9000):
        self.port = port

    def start(self):
        factory = WebSocketServerFactory()
        factory.protocol = BluenetDashboardProtocol

        reactor.listenTCP(self.port, factory)
        reactor.run()

    def stop(self):
        reactor.stop()
