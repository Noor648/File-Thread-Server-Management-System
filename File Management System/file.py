class files:
    filename = ""
    pages = {}
    ptr = 0
    mainPage = [False] * 1024
    pgoffset = [0] * 1024

    namer = ""

    def __init__(self, name):
        self.namer = name

    def renameFile(self, newName):
        self.filename = newName

    def getName(self):
        return self.filename

    #Calculates the offset and seeks it
    #Writes the provided data from that offset
    def writeToFile(self, txt, pgno, offset):
        fopen = open("C:/Users/hp/Desktop/FileManagementSystem/dataFile.dat", "r+")
        fopen.seek(pgno*1024+offset)
        fopen.seek(pgno*1024+offset)
        buffer = txt
        fopen.write(buffer[0:len(txt)])
        fopen.close()


    


root = files("Main")
#root.read(2,0,10)