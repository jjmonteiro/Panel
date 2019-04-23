import wmi, serial, time

## Returns a list with all available system COM ports
## Use 'friendly' to select output type
##
def getAllCOMPorts():
  query = "SELECT * FROM Win32_PnPEntity WHERE Name LIKE '%(COM%)'"
  coms  = wmi.WMI().query(query)
  thisdict = dict()

  for com in coms:
      mystring = com.Name
      mystring = mystring.split(' (COM')[1]
      thisdict [com.Name]  = "COM" + mystring[:-1]

  return thisdict




def createCOMPortObject(portName):
  NewPortObject = serial.Serial(
    port = portName,
    baudrate = 9600,
    bytesize = serial.EIGHTBITS,
    parity = serial.PARITY_NONE,
    stopbits = serial.STOPBITS_ONE,
    timeout = None,
    xonxoff = False,
    rtscts = False,
    dsrdtr = False
  )
  return NewPortObject


############## TEST OUTPUT ################
portList = getAllCOMPorts()
COMportList = list()

print "All available COM ports detected:"
for eachItem in portList: 
  print(eachItem)


print ""
print "Trying to open all available COM ports:"
for eachItem in portList:
  try:
    #ports are automatically open when the objects are created
    newPort = createCOMPortObject(portList[eachItem])

    #check if ports are open
    if newPort.is_open == True:
      print ">" + newPort.name + " is open."   
      COMportList.append(newPort) 
  except Exception as e: print(" " + str(e))

print ""
if len(COMportList):
  print "Trying to close all opened ports:"
  for eachItem in COMportList:
    try:
      eachItem.close()
      if eachItem.is_open == False:
        print ">" + eachItem.name + " is closed."
    except Exception as e: print(" " + str(e))
else:
  print "No COM ports were opened."

print ""

try:
  #newPort = createCOMPortObject("COM3")
  #print "opening port {}: {}".format(newPort.name, str(newPort.is_open))

   numOfLines = 0

  # while True:
  #   response = newPort.read()
  #   print(response)

  #   numOfLines = numOfLines + 1
  #   #time.sleep(0.5)
  #   if (numOfLines >= 50):
  #     break

  #newPort.close()
  #print "closing port {}: {}".format(newPort.name, str(not newPort.is_open))

except Exception as e:
  print(e)
  newPort.close()
