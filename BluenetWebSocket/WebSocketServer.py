from BluenetWebSocket._EventBusInstance import WSEventBus
from BluenetWebSocket.lib.connector.BluenetConnector import BluenetConnector
from BluenetWebSocket.lib.parsers.consumerParser import ConsumerParser
from BluenetWebSocket.lib.topics.Topics import Topics
from BluenetWebSocket.lib.websockets.webSocketServer import WebSocketServerCore


class WebSocketServer(WebSocketServerCore):
    parserSubscription = None
    
    
    def __init__(self, port=9000):
        super().__init__(port)

        self.loadDefaultParser()
        
        
    def connectToBluenet(self, bluenetInstance):
        ConsumerParser.loadBluenet(bluenetInstance)
        
        connector = BluenetConnector()
        connector.connect(bluenetInstance.getEventBus(), bluenetInstance.getTopics())
    
    def loadDefaultParser(self):
        WSEventBus.unsubscribe(self.parserSubscription)
        self.parserSubscription = WSEventBus.subscribe(Topics.wsReceivedMessage, ConsumerParser.receive)

    def loadCustomParser(self, receiverFunction):
        WSEventBus.unsubscribe(self.parserSubscription)
        self.parserSubscription = WSEventBus.subscribe(Topics.wsReceivedMessage, receiverFunction)
        
    