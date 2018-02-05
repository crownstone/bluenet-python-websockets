from lib.util.eventBus import eventBus, Topics


class BluenetConnector:
    bluenetEventBus = None
    
    def __init__(self):
        pass
        
    def connect(self, bluenetEventBus, bluenetTopics):
        for topic in bluenetTopics:
            print(topic)
            bluenetEventBus.subscribe(topic, lambda data: self.sendOverWebsocket(topic, data))
        
        
    def sendOverWebsocket(self, bluenetTopic, payload):
        data = {
            "topic": bluenetTopic,
            "data": payload
        }
        
        eventBus.emit(Topics.wsWriteMessage, data)
        
    