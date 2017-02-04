# -*- coding: utf-8 -*-
"""
Created on Thu Dec 01 08:43:34 2016

@author: Hao Ren
"""

#Library to force stop the code
import sys

#Libraries for Drone
from dronekit import connect, Command, VehicleMode
import time

#Libraries for Ultrasonic
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

import argparse  
parser = argparse.ArgumentParser ()
parser.add_argument('--connect', default='127.0.0.1:14550')
args = parser.parse_args()

#Pins for LED
LedPin = 18
GPIO.setup(LedPin, GPIO.OUT)

def centering():
    while True:
        manualOverride()
                
        tunnelRadius = 2.0
        factor = 70
        middleRoll = 1519
        error = 0
        sonarLimit = 6.0
        
        SevenString = vehicle.channels['7']
        SevenInt = int(SevenString)
        
        vehicle.channels.overrides['1'] = {}
        vehicle.channels.overrides['2'] = {}
        Roll = vehicle.channels['1']
        Pitch = vehicle.channels['2']
        print("Current Roll = %s"	)%Roll   
        print("Current Pitch = %s") %Pitch 
        
        distanceRight = round(vehicle.rangefinder.distance,2)
        print("Distance Right = %s")%distanceRight
        
        GPIO.output(LedPin,GPIO.LOW)
        
        while(SevenInt > 1500):
            print("----------------------Centering")
            manualOverride()
            
            SevenString = vehicle.channels['7']
            SevenInt = int(SevenString)
         
            distanceRight = round(vehicle.rangefinder.distance,2)
            print("Distance Right = %s")%distanceRight
            
            if(distanceRight < sonarLimit):
				print("In range")
				print("Led on")
				GPIO.output(LedPin,GPIO.HIGH)
				
				error = distanceRight - tunnelRadius
				print("Error = %s") %error
            
				Roll = middleRoll - (error*factor)
				print("Roll  = %s" ) %Roll
				
				#limit the Roll values 
				if(Roll < 1400):
					Roll = 1400
				elif(Roll > 1850):
					Roll = 1850
				
				vehicle.channels.overrides['1'] = Roll
				
				#vehicle.channels.overrides['2'] = {}
				Pitch = 1470
				vehicle.channels.overrides['2'] = Pitch
				print("Pitch = %s") %Pitch
				
				time.sleep(.1)
				
            elif(distanceRight > sonarLimit):
				print("Out of range")
				print("Led Off")
				GPIO.output(LedPin,GPIO.LOW)
				
				#not receiving real time roll
				vehicle.channels.overrides['1'] = {}
				Roll = vehicle.channels['1']
				print("Roll = %s") %Roll
				vehicle.channels.overrides['1'] = Roll
				time.sleep(.05)
            
            
        time.sleep(.1)
        print("Waiting for activation")
    
#Function to change flight mode
def modeChange(mode): 
	print "Changing the vehicle mode to %s" % mode
	vehicle.mode    = VehicleMode(mode)
	
	#Keep trying to change flight mode
	while (vehicle.mode != mode):
		print "Changing mode ..."
		vehicle.mode    = VehicleMode(mode)
		time.sleep(1)
	
	#Indicate it has successfully changed flight mode
	print "Mode has been changed to %s " %mode 

#Fail safe function
def manualOverride():
	#Channel 6 is the activation switch
	SixString = vehicle.channels['6']
	SixInt = int(SixString)
	
	if(SixInt > 1500):
			print("Manual Override")
			print("Force Land now")
			modeChange("LAND")
			time.sleep(5)
			vehicle.channels.overrides['3'] = 1100
			time.sleep(1)
			vehicle.channels.overrides= {}
			time.sleep(5)
			sys.exit()


# /\/\/\/\/\End of functions/\/\/\/\/\
# /\/\/\/\/\Beginning of code/\/\/\/\/\

# Connect to the Vehicle
print 'Connecting to vehicle on: %s' % args.connect
vehicle = connect(args.connect, baud=57600, wait_ready=True)

#Clears any previous override values
print ('Reset all channels')
vehicle.channels.overrides= {}
time.sleep(1)

#1 to enable, 0 to disable all arming check parameters
vehicle.parameters['ARMING_CHECK']=0
print "Arming check status:  %s" % vehicle.parameters['ARMING_CHECK']

time.sleep(3)

while True:
    centering()

#Close vehicle object before exiting script
print "Close vehicle object"
vehicle.close()

# /\/\/\/\/\/\End of codes/\/\/\/\/\/\/\   




