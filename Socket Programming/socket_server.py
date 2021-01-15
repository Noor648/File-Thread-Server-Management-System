import socket
import pickle
from file import files
from definations import directories
from thread import *
import time

mydir = directories("main")
myfile = files("mainer")

# Mazimum size of a datagram
MAX_SIZE_BYTES = 65535 

#To create a socket connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 95
ThreadCount = 0

#the process that ensures the program
#is listening to the connection for the client else. 
#It throws the error message.
try:
    s.bind((host, port))
except socket.error as e:
    print(str(e))

#Some general info
print("The server's IP address is (add this to the client's input): ", socket.gethostbyname(host))
print('socket is listening..')

#To make socket ready for connections
s.listen(2)

def server(clientsocket):
    
    while True:
        #receiving data from client
        d = clientsocket.recv(65535)
        data = pickle.loads(d)
        
        #if data received is empty
        if not data:
            break

        print(data)
        print("\n")
        
        if data[0] == '1':
            a = data[1]
            b = data[2]
            d = mydir.addFile(a, b)
            if not d:
                a = ": File Created!\n" + str(data[2])
                d = a
            k = [d]
            da = pickle.dumps(k)

            #Sendind the requested data to client
            #Here address is clients ip value
            clientsocket.sendto(da, address)

        if data[0] == '2':
            b = data[1]
            c = data[2]
            d = data[3]
            mydir.writeFile(b, c, d)
            da = mydir.read(b)
            k = [da]
            m = pickle.dumps(k)
            clientsocket.sendto(m, address)

        if data[0] == '3':
            a = data[1]
            b3 = mydir.delFile(a)
            if not b3:
                a = "File not Found\nFile cannot be Deleted"
                b3 = a
            print(b3)   
            k3 = [b3]
            da = pickle.dumps(k3)
            clientsocket.sendto(da, address)
            

        if data[0] == '4':
            a = data[1]
            mydir.addChildDir(a)
            a = "Directory Added!"
            k = [a]
            m = pickle.dumps(k)
            clientsocket.sendto(m, address)
            

        if data[0] == '5':
            a = data[1]
            b = mydir.chDir(a)
            k = [b]
            m = pickle.dumps(k)
            clientsocket.sendto(m, address)

        if data[0] == '6':
            a = data[1]
            x = mydir.read(a)
            k = [x]
            m = pickle.dumps(k)
            clientsocket.sendto(m, address)

        if data[0] == '7':
            a = data[1]
            b = data[2]
            x = mydir.move(a, b)
            k = [x]
            m = pickle.dumps(k)
            clientsocket.sendto(m, address)

        if data[0] == '8':
            a = mydir.getChildren()
            k = [a]
            m = pickle.dumps(k)
            clientsocket
            clientsocket.sendto(m, address)

        if data[0] == '9':
            b = mydir.memoryMap()
            k = [b]
            m = pickle.dumps(k)
            clientsocket.sendto(m, address)

        if data[0] == '10':
            a = "Thanks for visiting us\nExiting Program..\nExited"
            k = [a]
            m = pickle.dumps(k)
            clientsocket.send(m, address)

        


while True:
    #To receive Connection request from client 
    clientsocket, address = s.accept()
    print('Connected to: ' + address[0])

    #Creating threads 
    #Server is defination
    #clientsocket is argument
    start_new_thread(server, (clientsocket, ))

    #To monitor the total number of present clients
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
s.close()
    