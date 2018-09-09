import os
import time

flag = False

while True:

    fs = open('on.txt', 'r')
    reading = fs.read()
    print(reading)
    try:
        if(reading[0] == 1 or reading[0] == '1'):
	    print('hi')
            if(not flag):
               os.system("feh /root/Desktop/sign.png &")
               flag = True
        else:
            flag = False
            os.system('pkill -9 feh')
    except:
        pass    

    fs.close()
