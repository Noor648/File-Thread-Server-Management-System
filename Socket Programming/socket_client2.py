import socket
import pickle

# Mazimum size of a datagram
MAX_SIZE_BYTES = 65535 


def clients(usr, ip):
    #To create a socket connection
    c = socket.socket()
    host = ip
    port = 95

    #the process that ensures the program
    #is listening to the connection for the client else. 
    #It throws the error message.
    try:
        c.connect((host, port))
    except socket.error as e:
        print(str(e))

    while True:
        print("-----------------------------------------------")
        print("Which operation would you like to perform?")
        print("1. Create File")
        print("2. Write to File")
        print("3. Delete File")
        print("4. Create Directory")
        print("5. Check Directory")
        print("6. Read File")
        print("7. Move")
        print("8. Directory Names")
        print("9. Memory Map")     
        print("10. Exit")
        print("-----------------------------------------------")
        y = raw_input("Enter your choice: ")

        # creating a file
        if int(y) == 1:
            a = raw_input("Enter File name: ")
            d = raw_input("Enter text to be written to file: ")
            bound = [y, a, d, usr]

            #To convert list(in this case) into character stream
            #inorder to reconstruct this object in another python file(Server)
            data = pickle.dumps(bound)
            c.send(data)

            #Receiving data
            addr = c.recv(MAX_SIZE_BYTES)
            
            #To retrieve pickled data 
            #comming from server
            datar = pickle.loads(addr)
            print(a + datar[0])
            
            

        #writing  to file
        if int(y) == 2:
            a = raw_input("Enter File Name: ")
            d = raw_input("Enter text to be written: ")
            b = int(input("Enter offset: "))
            e = [y, a, b, d, usr]
            data = pickle.dumps(e)
            c.send(data)
            addr = c.recv(MAX_SIZE_BYTES)
            datar = pickle.loads(addr)
            print("Text written:")
            print(datar[0])

        #Deleting a file
        if int(y) == 3:
            a = raw_input("Enter file name: ")
            b = [y, a, usr]
            data = pickle.dumps(b)
            c.send(data)

            #Receiving data
            addr3 = c.recv(MAX_SIZE_BYTES)
            datar3 = pickle.loads(addr3)
            print(a + datar3[0])

        #creating a directory
        if int(y) == 4:
            a = raw_input("Enter directory name: ")
            b = [y, a, usr]
            data = pickle.dumps(b)
            c.send(data)
            
            addr = c.recv(MAX_SIZE_BYTES)
            datar = pickle.loads(addr)
            print(datar[0])

        #Checking if dire. is available
        if int(y) == 5:
            a = raw_input("Enter directory name: ")
            b = [y, a, usr]
            data = pickle.dumps(b)
            c.send(data)

            #Receiving data
            addr = c.recv(MAX_SIZE_BYTES)
            datar = pickle.loads(addr)
            print(a)
            print(datar[0])
            
        #Reading a file
        if int(y) == 6:
            a = raw_input("Enter file name: ")
            b = [y, a, usr]
            data = pickle.dumps(b)
            c.send(data) 

            addr = c.recv(MAX_SIZE_BYTES)
            datar = pickle.loads(addr)
            print("File content:")
            print(datar[0])


        # Moving a File
        if int(y) == 7:
            a = raw_input("Enter Source File Name: ")
            d = raw_input("Enter Destination Directory: ")
            b = [y, a, d, usr]
            data = pickle.dumps(b)
            c.send(data)

            #Receing Data
            addr = c.recv(MAX_SIZE_BYTES)
            datar = pickle.loads(addr)
            print(a + " " + datar[0] + d)
        
        
        # Showing Directory List
        if int(y) == 8:
            a = "Directory Names: "
            print(a)
            b = [y, a, usr]
            data = pickle.dumps(b)
            c.send(data)

            addr = c.recv(MAX_SIZE_BYTES)
            datar = pickle.loads(addr)
            print(datar[0])


        # Showing Memory Map
        if int(y) == 9:
            print("Memory Map: ")
            a = "Memory Map"
            b = [y, a, usr]
            data = pickle.dumps(b)
            c. send(data)

            #Receiving data
            addr = c.recv(MAX_SIZE_BYTES)
            datar = pickle.loads(addr)
            print(datar[0])

        # Program Exit
        if int(y) == 10:
            a = "Exit"
            b = [y, a, usr]
            data = pickle.dumps(b)
            c.send(data)

            addr = c.recv(MAX_SIZE_BYTES)
            datar = pickle.loads(addr)
            print(datar[0])
            break


if __name__ == '__main__':
    
    x = raw_input("Enter the IP Address of the machine: ")
    y = raw_input("Enter the username: ")
    #function call
    clients(y, x)
    
    


    
