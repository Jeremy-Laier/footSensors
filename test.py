import serial
ser = serial.Serial('/dev/ttyACM0', baudrate = 9600)
f = open ( "test.csv","w")
i = 0
while True:
    while ( ser.inWaiting() > 0) :
        dat = ser.readline()
        f.writelines("\n")
        f.writelines(str(dat))
