
#import os
#import time
from datetime import datetime
import math
import time
import random 
#import Adafruit_ADS1x15
#import csv


# Choose a gain of 1 for reading voltages from 0 to 4.09V.
# Or pick a different gain to change the range of voltages that are read:
#  - 2/3 = +/-6.144V
#  -   1 = +/-4.096V
#  -   2 = +/-2.048V
#  -   4 = +/-1.024V
#  -   8 = +/-0.512V
#  -  16 = +/-0.256V
# See table 3 in the ADS1015/ADS1115 datasheet for more info on gain.

#adc = Adafruit_ADS1x15.ADS1115()
#GAIN = 2/3

#The division of the two has to be a whole number 

interval = 60
speed = 0.3
sleepTime = int(interval / speed)

print('Reading ADS1x15 values, press Ctrl-C to quit...')
# Print nice channel column headers.
print('| {0:>6} |'.format(*range(1)))
print('-' * (27))

# Main loop
#f = open('/home/pi/pressure.txt', 'r+')

while 1:

    f = open('test.txt', 'r+')
    f.truncate(0)
    num = 0
    j = 0

    for i in range(0,sleepTime):
        with open('test.txt', 'a') as f:

            #value = adc.read_adc_difference(0, gain=GAIN)
            
            #Voltage is calculated from the 15 bit returned value by dividing by 32,767 for 10 bit res
            #and multiplied by 6.144 for the maximum gain voltage
            #volts = value *((3*(6.144)/32768))
            
            #Relationship between volt and pressure in a cold cathode gauge 
            #Pa = math.exp((volts-10)/1.33)
            
            #Record the time  the data was taken
            #recordTime = (time.strftime("%M:%S"))
            
            #Write the data into the .txt file
            #f.write(recordTime + ", "+ str(volts[0])+"\n")
            num = random.uniform(4,10)
            
            f.write(("{0}, {1} \n".format(j,num)))

            j += speed
            
            #Check if the device is recording values
            #print('Channel 0 minus 1: {}, {}'.format(value, volts))
            
            
            time.sleep(speed)  
    







