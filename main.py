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
    GPIO.output(RedD, 1)  
    GPIO.output(RedC, 1)  
    GPIO.output(RedB, 1)  
    GPIO.output(GreenA, 1)  
    time.sleep(DelayGreenA)
    GPIO.output(GreenA, 0)  
    GPIO.output(YellowA, 1)  
    time.sleep(DelayYellowA)
    GPIO.output(YellowA, 0)  
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
    GPIO.output(RedD, 1)  
    GPIO.output(RedC, 1)  
    GPIO.output(RedA, 1)
    GPIO.output(GreenB, 1)  
    time.sleep(DelayGreenB)
    GPIO.output(GreenB, 0)  
    GPIO.output(YellowB, 1)  
    time.sleep(DelayYellowB)
    GPIO.output(YellowB, 0)  
    GPIO.output(RedB, 1)
    client_socket.setblocking(0)
    while True:
        try:
            client_socket.recv(4)
        except BlockingIOError:
            client_socket.setblocking(1)
            return

def side3():
    GPIO.output(GreenA, 0)
    GPIO.output(YellowA, 0)
    GPIO.output(RedB, 0)
    GPIO.output(YellowB, 0)
    GPIO.output(RedC, 0)
    GPIO.output(YellowC, 0)
    GPIO.output(GreenD, 0)
    GPIO.output(YellowD, 0)
    GPIO.output(RedD, 1)  
    GPIO.output(RedB, 1)  
    GPIO.output(RedA, 1)
    GPIO.output(GreenC, 1)  
    time.sleep(DelayGreenC)
    GPIO.output(GreenC, 0)  
    GPIO.output(YellowC, 1)  
    time.sleep(DelayYellowC)
    GPIO.output(YellowC, 0)  
    GPIO.output(RedC, 1)
    client_socket.setblocking(0)
    while True:
        try:
            client_socket.recv(4)
        except BlockingIOError:
            client_socket.setblocking(1)
            return

def side4():
    GPIO.output(GreenA, 0)
    GPIO.output(YellowA, 0)
    GPIO.output(GreenB, 0)
    GPIO.output(YellowB, 0)
    GPIO.output(GreenC, 0)
    GPIO.output(YellowC, 0)
    GPIO.output(RedD, 0)
    GPIO.output(YellowD, 0)
    GPIO.output(RedA, 1)  
    GPIO.output(RedB, 1)  
    GPIO.output(RedC, 1)
    GPIO.output(GreenD, 1)  
    time.sleep(DelayGreenD)
    GPIO.output(GreenD, 0)  
    GPIO.output(YellowD, 1)  
    time.sleep(DelayYellowD)
    GPIO.output(YellowD, 0)  
    GPIO.output(RedD, 1)
    client_socket.setblocking(0)
    while True:
        try:
            client_socket.recv(4)
        except BlockingIOError:
            client_socket.setblocking(1)
            return
        
def clear():
    client_socket.setblocking(0)
    while True:
        try:
            client_socket.recv(4)
        except BlockingIOError:
            client_socket.setblocking(1)
            return

while True:
    print(command)
    rlist, _, _ = select.select([client_socket], [], [], 0)
    if rlist:
        data = client_socket.recv(4)
        command = data.decode()
        print(command)
        if command == 'side':
            side1()
        elif command == 'rasp':
            side2()
        elif command == 'ardu':
            side3()
        elif command == 'comp':
            side4()
        elif command == 'del1':
            DelayGreenA = 10
            DelayYellowA = 6
            clear()
        elif command == 'del2':
            DelayGreenB = 10
            DelayYellowB = 6
            clear()
        elif command == 'del3':
            DelayGreenC = 10
            DelayYellowC = 6
            clear()
        elif command == 'del4':
            DelayGreenD = 10
            DelayYellowD = 6
            clear()
    GPIO.output(RedD, 1)  
    GPIO.output(RedC, 1)  
    GPIO.output(RedB, 1)  
    GPIO.output(RedA, 0)  
    GPIO.output(GreenA, 1)  
    time.sleep(DelayGreenA)
    if DelayGreenA == 10:
        DelayGreenA = 5
    rlist, _, _ = select.select([client_socket], [], [], 0)
    if rlist:
        data = client_socket.recv(4)
        command = data.decode()
        print(command)
        if command == 'side':
            side1()
        elif command == 'rasp':
            side2()
        elif command == 'ardu':
            side3()
        elif command == 'comp':
            side4()
        elif command == 'del1':
            DelayGreenA = 10
            DelayYellowA = 6
            clear()
        elif command == 'del2':
            DelayGreenB = 10
            DelayYellowB = 6
            clear()
        elif command == 'del3':
            DelayGreenC = 10
            DelayYellowC = 6
            clear()
        elif command == 'del4':
            DelayGreenD = 10
            DelayYellowD = 6
            clear()
    GPIO.output(GreenA, 0)  
    GPIO.output(YellowA, 1)  
    time.sleep(DelayYellowA)
    if DelayYellowA == 6:
        DelayYellowA = 2
    rlist, _, _ = select.select([client_socket], [], [], 0)
    if rlist:
        data = client_socket.recv(4)
        command = data.decode()
        print(command)
        if command == 'side':
            side1()
        elif command == 'rasp':
            side2()
        elif command == 'ardu':
            side3()
        elif command == 'comp':
            side4()
        elif command == 'del1':
            DelayGreenA = 10
            DelayYellowA = 6
            clear()
        elif command == 'del2':
            DelayGreenB = 10
            DelayYellowB = 6
            clear()
        elif command == 'del3':
            DelayGreenC = 10
            DelayYellowC = 6
            clear()
        elif command == 'del4':
            DelayGreenD = 10
            DelayYellowD = 6
            clear()
    GPIO.output(YellowA, 0)  
    GPIO.output(RedA, 1)  
    GPIO.output(RedB, 0)  
    GPIO.output(GreenB, 1)  
    time.sleep(DelayGreenB)
    if DelayGreenB == 10:
        DelayGreenB = 5
    rlist, _, _ = select.select([client_socket], [], [], 0)
    if rlist:
        data = client_socket.recv(4)
        command = data.decode()
        print(command)
        if command == 'side':
            side1()
        elif command == 'rasp':
            side2()
        elif command == 'ardu':
            side3()
        elif command == 'comp':
            side4()
        elif command == 'del1':
            DelayGreenA = 10
            DelayYellowA = 6
            clear()
        elif command == 'del2':
            DelayGreenB = 10
            DelayYellowB = 6
            clear()
        elif command == 'del3':
            DelayGreenC = 10
            DelayYellowC = 6
            clear()
        elif command == 'del4':
            DelayGreenD = 10
            DelayYellowD = 6
            clear()
    GPIO.output(GreenB, 0)  
    GPIO.output(YellowB, 1)  
    time.sleep(DelayYellowB)
    if DelayYellowC == 6:
        DelayYellowC = 2
    rlist, _, _ = select.select([client_socket], [], [], 0)
    if rlist:
        data = client_socket.recv(4)
        command = data.decode()
        print(command)
        if command == 'side':
            side1()
        elif command == 'rasp':
            side2()
        elif command == 'ardu':
            side3()
        elif command == 'comp':
            side4()
        elif command == 'del1':
            DelayGreenA = 10
            DelayYellowA = 6
            clear()
        elif command == 'del2':
            DelayGreenB = 10
            DelayYellowB = 6
            clear()
        elif command == 'del3':
            DelayGreenC = 10
            DelayYellowC = 6
            clear()
        elif command == 'del4':
            DelayGreenD = 10
            DelayYellowD = 6
            clear()
    GPIO.output(YellowB, 0)  
    GPIO.output(RedC, 0)  
    GPIO.output(RedB, 1)  
    GPIO.output(GreenC, 1)  
    time.sleep(DelayGreenC)
    if DelayGreenC == 10:
        DelayGreenC = 5
    rlist, _, _ = select.select([client_socket], [], [], 0)
    if rlist:
        data = client_socket.recv(4)
        command = data.decode()
        print(command)
        if command == 'side':
            side1()
        elif command == 'rasp':
            side2()
        elif command == 'ardu':
            side3()
        elif command == 'comp':
            side4()
        elif command == 'del1':
            DelayGreenA = 10
            DelayYellowA = 6
            clear()
        elif command == 'del2':
            DelayGreenB = 10
            DelayYellowB = 6
            clear()
        elif command == 'del3':
            DelayGreenC = 10
            DelayYellowC = 6
            clear()
        elif command == 'del4':
            DelayGreenD = 10
            DelayYellowD = 6
            clear()
    GPIO.output(GreenC, 0) 
    GPIO.output(YellowC, 1)  
    time.sleep(DelayYellowC)
    if DelayYellowC == 6:
        DelayYellowC = 2
    rlist, _, _ = select.select([client_socket], [], [], 0)
    if rlist:
        data = client_socket.recv(4)
        command = data.decode()
        print(command)
        if command == 'side':
            side1()
        elif command == 'rasp':
            side2()
        elif command == 'ardu':
            side3()
        elif command == 'comp':
            side4()
        elif command == 'del1':
            DelayGreenA = 10
            DelayYellowA = 6
            clear()
        elif command == 'del2':
            DelayGreenB = 10
            DelayYellowB = 6
            clear()
        elif command == 'del3':
            DelayGreenC = 10
            DelayYellowC = 6
            clear()
        elif command == 'del4':
            DelayGreenD = 10
            DelayYellowD = 6
            clear()
    GPIO.output(YellowC, 0) 
    GPIO.output(RedC, 1)  
    GPIO.output(RedD, 0)  
    GPIO.output(GreenD, 1)  
    time.sleep(DelayGreenD)
    if DelayGreenD == 10:
        DelayGreenD = 5
    rlist, _, _ = select.select([client_socket], [], [], 0)
    if rlist:
        data = client_socket.recv(4)
        command = data.decode()
        print(command)
        if command == 'side':
            side1()
        elif command == 'rasp':
            side2()
        elif command == 'ardu':
            side3()
        elif command == 'comp':
            side4()
        elif command == 'del1':
            DelayGreenA = 10
            DelayYellowA = 6
            clear()
        elif command == 'del2':
            DelayGreenB = 10
            DelayYellowB = 6
            clear()
        elif command == 'del3':
            DelayGreenC = 10
            DelayYellowC = 6
            clear()
        elif command == 'del4':
            DelayGreenD = 10
            DelayYellowD = 6
            clear()
    GPIO.output(GreenD, 0)  
    GPIO.output(YellowD, 1)  
    time.sleep(DelayYellowD)
    if DelayYellowD == 6:
        DelayYellowD = 2
    GPIO.output(YellowD, 0)  
    command = 'norm'