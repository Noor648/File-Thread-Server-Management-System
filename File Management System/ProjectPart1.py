from file import files
from definations import directories
mydir = directories("main")
myfile = files("mainer")

#def Lab5():


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
        mydir.addFile(a, d)
        print("File Created!!")

    #writing  to file
    if int(y) == 2:
        a = raw_input("Enter File Name: ")
        d = raw_input("Enter text to be written: ")
        b = int(input("Enter offset: "))
        mydir.writeFile(a, b, d)
        mydir.read(a)

    #Deleting a file
    if int(y) == 3:
        a = raw_input("Enter file name: ")
        mydir.delFile(a)

    #creating a directory
    if int(y) == 4:
        a = raw_input("Enter directory name: ")
        mydir.addChildDir(a)
        print("Now all available directories are: ")
        print(mydir.getChildren())

    #Checking if dire. is available
    if int(y) == 5:
        a = raw_input("Enter directory name: ")
        b = mydir.chDir(a)
        print(b)
        
    #Reading a file
    if int(y) == 6:
        a = raw_input("Enter file name: ")
        mydir.read(a)


    # Moving a File
    if int(y) == 7:
            a = raw_input("Enter Source File Name: ")
            d = raw_input("Enter Destination Directory: ")
            print("File Moving is in process... ")
            mydir.move(a, d)
            print("File Moved Successfully. ")
    # Showing Directory List
    if int(y) == 8:
         a = "Directory Names: "
         print(a)
         print(mydir.getChildren())

    # Showing Memory Map
    if int(y) == 9:
        print("Memory Map: ")
        mydir.memoryMap()

    # Program Exit
    if int(y) == 10:
        print("Exiting program....")
        print("Thank you for visiting us. Hope to see you soon!")
        break


#if __name__ == '__main__':
#    Lab5()
