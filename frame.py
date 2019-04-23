from packet import Packet
MODULO_CONST      =  256

class Frame:

    def __init__(self, start,  flag , packet):
         self.__flag          = flag if(isinstance(flag,int)) else 0
         self.__packet        =  packet  if(isinstance(packet, Packet)) else Packet()
         self.__checksum      = 0
         self.__start_code  =  start

    def __calculate_checksum(self):
        self.__checksum =  0
        sum      = int(self.__flag)
        sum      += self.__packet.size

        for data in self.__packet.message:
            sum   += data
        self.__checksum   = sum % MODULO_CONST
       
    @property
    def checksum(self):
        return self.__checksum

    def pack(self):
        result  =  ()
        self.__packet.build()
        self.__calculate_checksum()
        result +=  (self.__start_code, self.__flag ,
                     self.__packet.size)
        result += self.__packet.message 
        result += (self.__checksum,)

        return result