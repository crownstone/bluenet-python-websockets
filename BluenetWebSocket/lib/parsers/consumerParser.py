
class ConsumerParserClass:
    bluenetInstance = None
    
    def __init__(self):
        pass
    
    def loadBluenet(self, bluenet):
        self.bluenetInstance = bluenet
    
    def receive(self, data):
        """
        This will handle the strings that come of the websocket and perform Bluenet commands.
        :param data:
        :return:
        """
        pass
    
ConsumerParser = ConsumerParserClass()