from BluenetWebSocket._EventBusInstance import WSEventBus
from BluenetWebSocket.lib.topics.Topics import Topics


class BluenetConnector:
    def __init__(self):
        pass
        
    def connect(self, bluenetEventBus, bluenetTopics):
        for topic in vars(bluenetTopics).keys():
            if not topic.startswith("__"):
                bluenetEventBus.subscribe(topic, self.generateLambda(topic))

    
    def generateLambda(self, topic):
        """
            This is required to make sure we have a static instance of the topic variable.
            In the loop it will be overwritten continuously and only the last value is used
            :param topic:
            :return: binder function
        """
        return lambda data: self.sendOverWebsocket(topic, data)
        
    
    def sendOverWebsocket(self, bluenetTopic, payload):
        data = {
            "topic": bluenetTopic,
            "data": payload
        }
        WSEventBus.emit(Topics.wsWriteMessage, data)
        
    