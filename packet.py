SOH  = 0x01
ACK  = 0x06
SIGNATURE  = 0xe4 #228

class Header:
 
    def __init__(self, **kargs):

        self.__signature         = SIGNATURE
        self.__destination_node  = None
        self.__source_node       = None
        self.__packet_id         = None
        self.__destination_port  = (None, None) #(channel, channel_address)
        self.__destination_task  = None
        self.__source_port       = (None, None) #(channel, channel_address)
        self.__source_task       = None
        self.__marker            = None
        self.__reserved          = 0

        pass

class Packet:

    def __init__(self, payload = tuple()):
        self.__message = payload  if( isinstance(payload, tuple)) else tuple()
        self.__header  =  Header()

    @property
    def size(self):
        return len(self.message)  + 1
    @property
    def message(self):
        return self.__message
    
    @message.setter
    def _message(self, value):
        if(isinstance(value , tuple)):
            self.__message = value

    def build(self):
         return self.message