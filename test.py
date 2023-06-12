import pip
import serial
import Servo
from Arduino import Arduino
import time

board = Arduino('115200') #아두이노 포트 번호 115200 (다른파일코드분석필요)
board.pinMode(10, "OUTPUT") 
board.pinMode(9, "OUTPUT")

while True:
 board.digitalWrite(13,"HIGH")
 board.digitalWrite(13,"LOW")
 board.digitalWrite(9,"HIGH")
 board.digitalWrite(9,"LOW")