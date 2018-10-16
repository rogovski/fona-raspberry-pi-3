from os import system
import serial
import subprocess
from time import sleep
from ISStreamer.Streamer import Streamer

ser=serial.Serial(
        '/dev/serial0', 
        115200, 
        bytesize=serial.EIGHTBITS, 
        parity=serial.PARITY_NONE, 
        stopbits=serial.STOPBITS_ONE, 
        timeout=1)

ser.write("AT\r")
while True:
    response = ser.readline()
    if "OK" in response:
        break
