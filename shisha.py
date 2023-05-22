import RPi.GPIO as GPIO  #include GPIO library
import time
import socket
import select
######################################

RedA = 7
YellowA = 11
GreenA = 13

RedB = 15
YellowB = 29
GreenB = 31

RedC = 33
YellowC = 35
GreenC = 37

RedD = 40
YellowD= 38
GreenD = 36

DelayGreenA = 5
DelayYellowA = 2
DelayGreenB = 5
DelayYellowB = 2
DelayGreenC = 5
DelayYellowC = 2
DelayGreenD = 5
DelayYellowD = 2

GPIO.setmode(GPIO.BOARD)  #Raspi mode set as board mode
GPIO.setup(RedA, GPIO.OUT)  #making pin number 7 as output pin for RED of 'A' way
GPIO.setup(YellowA, GPIO.OUT)  #making pin number 11 as output pin for YELLOW of 'A'
GPIO.setup(GreenA, GPIO.OUT)  #making pin number 13 as output pin for GREEN of 'A'
GPIO.setup(RedB, GPIO.OUT)  #making pin number 15 as output pin for RED of 'B'
GPIO.setup(YellowB, GPIO.OUT)  #making pin number 29 as output pin for YELLOW of 'B'
GPIO.setup(GreenB, GPIO.OUT)  #making pin number 31 as output pin for GREEN of 'B'
GPIO.setup(RedC,GPIO.OUT)  #making pin number 33 as output pin for RED of 'C' way
GPIO.setup(YellowC, GPIO.OUT)  #making pin number 35 as output pin for YELLOW of 'C'
GPIO.setup(GreenC, GPIO.OUT)  #making pin number 37 as output pin for GREEN of 'C'
GPIO.setup(RedD, GPIO.OUT)  #making pin number 40 as output pin for RED of 'D'
GPIO.setup(YellowD, GPIO.OUT)  #making pin number 38 as output pin for YELLOW of 'D'
GPIO.setup(GreenD, GPIO.OUT)  #making pin number 36 as output pin for GREEN of 'D'


ip_address = "192.168.0.108"
port = 12345
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((ip_address, port))
server_socket.listen()
print("Waiting for connection...")
client_socket, address = server_socket.accept()
print("Conncted to:", address)
command = client_socket.recv(4).decode()
def side1():
    GPIO.output(RedA, 0)
    GPIO.output(YellowA, 0)
    GPIO.output(GreenB, 0)
    GPIO.output(YellowB, 0)
    GPIO.output(GreenC, 0)
    GPIO.output(YellowC, 0)
    GPIO.output(GreenD, 0)
    GPIO.output(YellowD, 0)
    GPIO.output(RedD, 1)  #making pin number 7 low
    GPIO.output(RedC, 1)  #making pin number 7 low
    GPIO.output(RedB, 1)  #making pin number 7 low
    GPIO.output(GreenA, 1)  #making pin number 13 high
    time.sleep(DelayGreenA)
    GPIO.output(GreenA, 0)  #making pin number 13 low
    GPIO.output(YellowA, 1)  #making pin number 11 high
    time.sleep(DelayYellowA)
    GPIO.output(YellowA, 0)  #making pin number 11 high
    GPIO.output(RedA, 1)
    client_socket.setblocking(0)
    while True:
        try:
            client_socket.recv(4)
        except BlockingIOError:
            client_socket.setblocking(1)
            return
        
def side2():
    GPIO.output(GreenA, 0)
    GPIO.output(YellowA, 0)
    GPIO.output(RedB, 0)
    GPIO.output(YellowB, 0)
    GPIO.output(GreenC, 0)
    GPIO.output(YellowC, 0)
    GPIO.output(GreenD, 0)
    GPIO.output(YellowD, 0)
    GPIO.output(RedD, 1)  #making pin number 7 low
    GPIO.output(RedC, 1)  #making pin number 7 low
    GPIO.output(RedA, 1)
    GPIO.output(GreenB, 1)  #making pin number 13 high
    time.sleep(DelayGreenB)
    GPIO.output(GreenB, 0)  #making pin number 13 low
    GPIO.output(YellowB, 1)  #making pin number 11 high
    time.sleep(DelayYellowB)
    GPIO.output(YellowB, 0)  #making pin number 11 high
    GPIO.output(RedB, 1)
    client_socket.setblocking(0)
    while True:
        try:
            client_socket.recv(4)
        except BlockingIOError:
            client_socket.setblocking(1)
            return

def jassim():
    client_socket.setblocking(0)
    while True:
        try:
            client_socket.recv(4)
        except BlockingIOError:
            client_socket.setblocking(1)
            return
def clean():
    GPIO.output(RedA, 0)
    GPIO.output(GreenA, 0)
    GPIO.output(YellowA, 0)
    GPIO.output(RedB, 0)
    GPIO.output(GreenB, 0)
    GPIO.output(YellowB, 0)
    GPIO.output(RedC, 0)
    GPIO.output(GreenC, 0)
    GPIO.output(YellowC, 0)
    GPIO.output(RedD, 0)
    GPIO.output(GreenD, 0)
    GPIO.output(YellowD, 0)
    

while True:
    print(command)
    print(DelayGreenA)
    print(DelayYellowA)
    clean()
    rlist, _, _ = select.select([client_socket], [], [], 0)
    if rlist:
        data = client_socket.recv(4)
        command = data.decode()
        print(command)
        #print('\n')
        if command == 'side':
            side1()
        elif command == 'rasp':
            side2()
        elif command == 'del1':
            DelayGreenA = 10
            DelayYellowA = 6
            jassim()
        elif command == 'del2':
            DelayGreenB = 10
            DelayYellowB = 6
            jassim()
    GPIO.output(RedD, 1)  #making pin number 7 low
    GPIO.output(RedC, 1)  #making pin number 7 low
    GPIO.output(RedB, 1)  #making pin number 7 low
    GPIO.output(RedA, 0)  #making pin number 7 low
    GPIO.output(GreenA, 1)  #making pin number 13 high
    time.sleep(DelayGreenA)
    if DelayGreenA == 10:
        DelayGreenA = 5
    rlist, _, _ = select.select([client_socket], [], [], 0)
    if rlist:
        data = client_socket.recv(4)
        command = data.decode()
        print(command)
        #print('\n')
        if command == 'side':
            side1()
        elif command == 'rasp':
            side2()
        elif command == 'del1':
            DelayGreenA = 10
            DelayYellowA = 6
            jassim()
        elif command == 'del2':
            DelayGreenB = 10
            DelayYellowB = 6
            jassim()
    GPIO.output(RedA, 0)
    GPIO.output(GreenA, 0)  #making pin number 13 low
    GPIO.output(YellowA, 1)  #making pin number 11 high
    time.sleep(DelayYellowA)
    if DelayYellowA == 6:
        DelayYellowA = 2
    rlist, _, _ = select.select([client_socket], [], [], 0)
    if rlist:
        data = client_socket.recv(4)
        command = data.decode()
        print(command)
        #print('\n')
        if command == 'side':
            side1()
        elif command == 'rasp':
            side2()
        elif command == 'del1':
            DelayGreenA = 10
            DelayYellowA = 6
            jassim()
        elif command == 'del2':
            DelayGreenB = 10
            DelayYellowB = 6
            jassim()
    GPIO.output(YellowA, 0)  #making pin number 11 low
    GPIO.output(RedA, 1)  #making pin number 7 high
    GPIO.output(RedB, 0)  #making pin number 7 low
    GPIO.output(GreenB, 1)  #making pin number 7 low
    time.sleep(DelayGreenB)
    if DelayGreenB == 10:
        DelayGreenB = 5
    rlist, _, _ = select.select([client_socket], [], [], 0)
    if rlist:
        data = client_socket.recv(4)
        command = data.decode()
        print(command)
        #print('\n')
        if command == 'side':
            side1()
        elif command == 'rasp':
            side2()
        elif command == 'del1':
            DelayGreenA = 10
            DelayYellowA = 6
            jassim()
        elif command == 'del2':
            DelayGreenB = 10
            DelayYellowB = 6
            jassim()
    GPIO.output(RedB, 0)
    GPIO.output(GreenB, 0)  #making pin number 7 low
    GPIO.output(YellowB, 1)  #making pin number 7 low
    time.sleep(DelayYellowB)
    if DelayYellowB == 6:
        DelayYellowB = 2
    rlist, _, _ = select.select([client_socket], [], [], 0)
    if rlist:
        data = client_socket.recv(4)
        command = data.decode()
        print(command)
        #print('\n')
        if command == 'side':
            side1()
        elif command == 'rasp':
            side2()
        elif command == 'del1':
            DelayGreenA = 10
            DelayYellowA = 6
            jassim()
        elif command == 'del2':
            DelayGreenB = 10
            DelayYellowB = 6
            jassim()
    GPIO.output(YellowB, 0)  #making pin number 7 low
    GPIO.output(RedC, 0)  #making pin number 7 high
    GPIO.output(RedB, 1)  #making pin number 7 low
    GPIO.output(GreenC, 1)  #making pin number 7 high
    time.sleep(DelayGreenC)
    rlist, _, _ = select.select([client_socket], [], [], 0)
    if rlist:
        data = client_socket.recv(4)
        command = data.decode()
        print(command)
        #print('\n')
        if command == 'side':
            side1()
        elif command == 'rasp':
            side2()
        elif command == 'del1':
            DelayGreenA = 10
            DelayYellowA = 6
            jassim()
        elif command == 'del2':
            DelayGreenB = 10
            DelayYellowB = 6
            jassim()
    GPIO.output(RedC, 0)
    GPIO.output(GreenC, 0)  #making pin number 7 high
    GPIO.output(YellowC, 1)  #making pin number 7 high
    time.sleep(DelayYellowC)
    rlist, _, _ = select.select([client_socket], [], [], 0)
    if rlist:
        data = client_socket.recv(4)
        command = data.decode()
        print(command)
        #print('\n')
        if command == 'side':
            side1()
        elif command == 'rasp':
            side2()
        elif command == 'del1':
            DelayGreenA = 10
            DelayYellowA = 6
            jassim()
        elif command == 'del2':
            DelayGreenB = 10
            DelayYellowB = 6
            jassim()
    GPIO.output(YellowC, 0)  #making pin number 7 high
    GPIO.output(RedC, 1)  #making pin number 7 low
    GPIO.output(RedD, 0)  #making pin number 7 low
    GPIO.output(GreenD, 1)  #making pin number 7 low
    time.sleep(DelayGreenD)
    rlist, _, _ = select.select([client_socket], [], [], 0)
    if rlist:
        data = client_socket.recv(4)
        command = data.decode()
        print(command)
        #print('\n')
        if command == 'side':
            side1()
        elif command == 'rasp':
            side2()
        elif command == 'del1':
            DelayGreenA = 10
            DelayYellowA = 6
            jassim()
        elif command == 'del2':
            DelayGreenB = 10
            DelayYellowB = 6
            jassim()
    GPIO.output(RedD, 0)
    GPIO.output(GreenD, 0)  #making pin number 7 low
    GPIO.output(YellowD, 1)  #making pin number 7 low
    time.sleep(DelayYellowD)
    GPIO.output(YellowD, 0)  #making pin number 7 low
    #command = 'norm'