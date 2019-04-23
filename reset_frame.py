from packet import Packet, SOH , ACK
from frame  import Frame

RESET_FLAG  =  0x0C
def main():
    class ResetFrame(Frame):
        
        def __init__(self):
            Frame.__init__(self, SOH,RESET_FLAG,Packet((0x00, 0x06, 0x1D, 0x0E, 0x1D, 0x12, 0x00, 0xB6)))
            pass
    


    #tempCommand = ResetFrame().pack

    print_data = ""
    temp_frame = ResetFrame().pack

    for each_item in temp_frame():
        print_data += hex(each_item)
    
    print print_data.replace("0x"," ")





if __name__ == "__main__":
    main()







