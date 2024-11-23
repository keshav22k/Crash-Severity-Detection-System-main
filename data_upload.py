import serial
import time
import datetime
import pymysql as pms

ardPort = serial.Serial("COM7", 9600, timeout=0.1)

connection = pms.connect("localhost", "root", "","accident_inf")
curs= connection.cursor()

severity = 'no impact'
while True:
    if(ardPort.inWaiting()):
        recvData = ardPort.readline().decode("utf-8")
        recvData = recvData.strip('/n')
        recvData = recvData.strip('/r')
        fsr_data, latitude, longitude = map(float, recvData.split(";"))

        if (fsr_data < 100 and fsr_data > 10):
            severity = 'low'
        elif (fsr_data < 250):
            severity = 'medium'
        elif (fsr_data < 400):
            severity = 'High'
        elif(fsr_data < 500):
            severity = 'Maximum'
time_now = str(datetime.datetime.now())
if (severity != 'no impact'):
    curs.execute("INSERT INTO severity_data(time,latitude,longitude,severity,google_maps) VALUES('"+str(time_now)+"',"+str(latitude)+","+
                     str(longitude)+","+ str(longitude)+",'"+str(severity)+"','"+ str("https://www.google.co.in/maps/@"+str(latitude)+ ","+ str(longitude)+",17.21z")+"');")
    severity = 'no impact'
connection.autocommit(True)
