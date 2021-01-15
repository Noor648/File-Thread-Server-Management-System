from file import files
from tree import directories
from threading import Thread
from time import sleep

mydir = directories("main")
myfile = files("mainer")


def Lab7(arg):

    for i in range(arg):

        if int(i) == 0:
            finput1 = open("C:/Users/hp/Documents/Threads/inputFiles/1input.txt")
            st = finput1.readlines()
            a = st[1]
            d = st[4]
            word = a.split()
            name = word[0]
            finput1.close()
            mydir.addFile(name, d)
            f = open("C:/Users/hp/Documents/Threads/outputFiles/1output.txt", "w")
            f.write(name)
            f.write(": Created!\n\nWritten Text: \n")
            f.write(d)
            f.close()
            print("Thread1 Completed")

        if int(i) == 1:
            fo = open("C:/Users/hp/Documents/Threads/inputFiles/2input.txt", "r")
            data = fo.readlines()
            data = [x.strip() for x in data]
            a = data[1]
            d = data[4]
            b = int(data[7])
            fo.close()
            mydir.writeFile(a, b, d)
            mydir.read(a, 1)
            print("Thread2 Completed")

        # Deleting a file
        if int(i) == 2:
            finput3 = open("C:/Users/hp/Documents/Threads/inputFiles/3input.txt")
            st = finput3.readlines()
            a = st[1]
            word = a.split()
            name = word[0]
            finput3.close()
            mydir.delFile(name)
            print("Thread3 Completed")

        # creating a directory
        if int(i) == 3:
            fo = open("C:/Users/hp/Documents/Threads/inputFiles/4input.txt", "r")
            data = fo.readlines()
            a = data[1]
            word = a.split()
            fo.close()
            mydir.addChildDir(word[0])

            f3 = open("C:/Users/hp/Documents/Threads/outputFiles/4output.txt", "w")
            f3.write("Directory has been Created successfully!")
            print("Thread4 Completed")

        # Checking if dire. is available
        if int(i) == 4:
            finput5 = open("C:/Users/hp/Documents/Threads/inputFiles/5input.txt")
            st = finput5.readlines()
            a = st[1]
            word = a.split()
            name = word[0]
            b = mydir.chDir(name)
            
            f = open("C:/Users/hp/Documents/Threads/outputFiles/5output.txt", "w")
            f.write(name)
            f.write(":  ")
            f.write(b)
            f.close()
            print("Thread5 Completed")

        # Reading a file
        if int(i) == 5:
            fo = open("C:/Users/hp/Documents/Threads/inputFiles/6input.txt", "r")
            data = fo.readlines()
            a = data[2]
            word = a.split()
            fo.close()  
            mydir.read(word[0], 0)
            f.close()
            print("Thread6 Completed")

        # Moving a File
        if int(i) == 6:
            finput7 = open("C:/Users/hp/Documents/Threads/inputFiles/7input.txt")
            st = finput7.readlines()
            source = st[1]
            desti = st[4]
            a = source.split()
            d = desti.split()
            finput7.close()
            mydir.move(a[0], d[0])

            f7 = open("C:/Users/hp/Documents/Threads/outputFiles/7output.txt", "w")
            f7.write(a[0])
            f7.write(" moved Successfully to ")
            f7.write(d[0])
            f7.close()
            print("Thread7 Completed")
    
        # Showing Directory List
        if int(i) == 7:
            mydir.getChildren()
            print("Thread8 Completed")

        # Showing Memory Map
        if int(i) == 8:
            mydir.memoryMap()
            print("Thread9 Completed")

        # Program Exit
        if int(i) == 9:
            f7 = open("C:/Users/hp/Documents/Threads/outputFiles/10output.txt", "w")
            f7.write("Program completed!\nHope to see you soon!")
            f7.close()
        # wait 0 sec in between each thread
        sleep(0)


if __name__ == '__main__':
    k = int(raw_input("Enter the number of threads:"))
    thread = Thread(target=Lab7, args=(k, ))
    thread.start()
    thread.join()
    print("thread finished...exiting")

