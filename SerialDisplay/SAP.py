from time import sleep
import serial
ser=serial.Serial('/dev/ttyUSB0', 9600, timeout=1)

lines=2
rows=16
curLine=0
curRow=0

f=open("data.txt")
data=f.read().splitlines()
f.close()

def execCommand(command, ld=1):
    global curLine, curRow, lines, rows
    print(">"+command)
    if(command=="u"):
        if(curLine>0):
            curLine-=1
    elif(command=="uu"):
        if(curLine>lines):
            curLine-=lines
    elif(command=="d"):
        if(curLine<ld-1):
            curLine+=1
    elif(command=="dd"):
        if(curLine+lines<ld-1):
            curLine+=lines
    elif(command=="l"):
        if(curRow>0):
            curRow-=1
    elif(command=="ll"):
        if(curRow>rows):
           curRow-=rows
    elif(command=="r"):
        if(1):
            curRow+=1
    elif(command=="rr"):
        if(1):
            curRow+=rows
    elif(command=="s"):
        if(1):
            curRow=0
    else:
        pass
def send(it):
    global ser;
    print(it)
    ser.write((it+"\n").encode())

sleep(2)

while True:
    for line in range(lines):
        send(data[curLine+line][curRow:curRow+rows])
    while(not ser.in_waiting):
        pass
    for i in range(ser.in_waiting):
        execCommand(ser.read(2).decode(), len(data))
ser.close()
