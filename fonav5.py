from os import system
import serial
import subprocess
from time import sleep
from ISStreamer.Streamer import Streamer

# Check for a GPS fix
def checkForFix():
    print "checking for fix"
    # Start the serial connection
    ser=serial.Serial('/dev/serial0', 115200, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, timeout=1)
    # Turn on the GPS
    ser.write("AT+CGPS=1,1\r")
    while True:
        response = ser.readline()
        if " 1" in response:
            break
    # Ask for the navigation info parsed from NMEA sentences
    ser.write("AT+CGPS?\r")
    while True:
            response = ser.readline()
            # Check if a fix was found
            if "+CGPS: 1,1," in response:
                print "fix found"
                print response
                return True
            # If a fix wasn't found, wait and try again
            if "+CGPSINFO: 1,0," in response:
                sleep(5)
                ser.write("AT+CGPSINFO?\r")
                print "still looking for fix"
            else:
                ser.write("AT+CGPSINFO?\r")

checkForFix()
