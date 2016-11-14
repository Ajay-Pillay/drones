//to be started by initiatePythonScript.py, and this script will invoke python2.py
import subprocess

p = subprocess.Popen(['python', 'python2.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)

while True:

	#p.stdin.write("Hello\n")
	#p.stdin.flush()
	incomingData = p.stdout.readline().strip()
	#print "Incoming data: %s" % incomingData

	if (incomingData == 'L'):
		print "L"
		return "L"
	elif (incomingData == 'R'):
		print "R"
		return "R"
	elif (incomingData == 'F'):
		print 'F'
		return 'F'
	elif (incomingData == 'B'):
		print 'B'
		return 'B'
	elif (incomingData == 'F'):
		print 'F'
		return 'F'
	elif (incomingData == 'LR'):
		print 'LR'
		return 'LR'
	elif (incomingData == 'LF'):
		print 'LF'
		return 'LF'
	elif (incomingData == 'LB'):
		print 'LB'
		return 'LB'
	elif (incomingData == 'RF'):
		print 'RF'
		return 'R'
	elif (incomingData == 'RB'):
		print 'RB'
		return 'RB'
	elif (incomingData == 'FB'):
		print 'FB'
		return 'FB'
	elif (incomingData == 'LRF'):
		print 'LRF'
		return 'LRF'
	elif (incomingData == 'LRFB'):
		print 'LRFB'
		return 'LRFB'
	else:
		incomingData = "NONE"
		print "NONE"	
		return "NONE"	
		
		
		
while True:
	incomingData = "NONE"
	incomingData = readPython()
	
	while (incomingData == "NONE"):
		print "still in the loop"
		incomingData = readPython()	
	
	print "out of the loop"

