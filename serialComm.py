// python code for arduino and RPI communication
import serial

ser = serial.Serial('/dev/ttyACM0',9600)
#s = [0,1]


def serialAvailable():
	while True:
		readSerial=ser.readline()
		#s[0] = str(int (ser.readline(),36))
		#print s[0]
		#print readSerial still in hexa format 
		readSerial = int(readSerial, 16)
		#readSerial = str(readSerial)
		#print readSerial
		
		if readSerial <1000:
			#do nothing 
			print ("TEST1")
		elif readSerial > 1800:
			#initiate python script 
			print ("TEST2")
			
		
	
serialAvailable()
print "finish"
