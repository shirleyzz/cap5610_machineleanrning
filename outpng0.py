import cv2
import os
import numpy as np
from sys import argv
import shutil
import math

#read path from input by input
cap = cv2.VideoCapture(argv[1],0)
a,b = str(argv[1]).split('.')
path = a
fe = 600
counter = 0
i = 0
cap.open(a + "." + b)


#check if path empty
if os.path.exists(a):
	shutil.rmtree(path)
os.mkdir(path)


#pictures per second
fps = cap.get(cv2.CAP_PROP_FPS)
total_frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)

print "fps= " + str(fps) + "\n"
print "total frames= " + str(total_frames)


#create a txt file

with open("./" + path + "/" + "Readme.txt","w") as file:
	file.write("total frames = " + str(total_frames))
	file.close()
while(True):	
	ret, frame = cap.read()
	print "total: "+ str(round(i/total_frames,3)) + "||" + "output image " + str(counter) + " " + str(round(total_frames/fe,0))
	if (i < fe):
		i += 1
		continue
	else:
		i = 0
		counter += 1
		cv2.imwrite("./" + path + "/" + path +"_" +str(counter) + ".png",frame)
	if (counter == int(total_frames/fe)):
		break	
	if cv2.waitKey(1) & 0xFF == ord("q"):
		break	
cap.release()
cv2.destroyAllWindows()

