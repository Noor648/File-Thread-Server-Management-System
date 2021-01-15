import pickle

class directories:
    from file import files
    myfile = files("mainer")
    child = []
    namer = ""

    def __init__(self, name):
        self.namer = name

    def getName(self):
        return self.namer

    #Firstly checks if there's any file of same name
    #If there is no such file then it proceeds further and creates new file else the defination terminates
    #Moves to segment 3 to update file number
    #Writes files name in segment 1 (Dedicated for storing file names only)
    #Dedicate a segment for file and generates content in it
    #Add its dirctory in segment3 (Dedicated for memory map only)
    #Writes file name with respect to the directory name in memory map
    def addFile(self, name, txt):
        file = open("C:/Users/hp/Desktop/FileManagementSystem/dataFile.dat", "r+")
        u = len(name)
        c = 0
        for i in range(64):
            file.seek(i * 16)
            a = file.read(u)
            if a == name:
                b = ": File Already exists\nA file of same name cannot be created again"
                c=0
                return b
            else :
                c = 1
        if c != 0:
            a = self.offsetcalcFile()
            b = int(a)
            c = self.pageallocF()
            d = int(c)
            e = b + 1
            f = str(e)
            h = int(self.offsetMM())
            i = h * 32
            j = i + 16
            self.myfile.writeToFile(f, 4, 0)
            self.dictToText(name, d, b)
            self.myfile.writeToFile(txt, d, 0)
            self.myfile.writeToFile("main          ~ ", 2, i)
            self.myfile.writeToFile(name, 2, j)

    #Assigns file a unique file number(File number is used to assign segment for file content)
    #Adds file to segment 1 (Linked with addFile() )
    def dictToText(self, fname, pg, off):
        a = fname + ":" + str(pg)
        b = off * 16
        self.myfile.writeToFile(a, 0, b)


    #Reads the value of ongoing filenumber from segemtent3
    def offsetcalcFile(self):
        file = open("C:/Users/hp/Desktop/FileManagementSystem/dataFile.dat", "r+")
        page_size = 16
        page_num = 256
        file.seek(page_num * page_size)
        a = file.read(page_size)
        return a

    #Checks for the file name in segment1
    #If present overrides it with spaces
    #Deletes filename from memorymap too 
    def delFile(self, filename):
        file = open("C:/Users/hp/Desktop/FileManagementSystem/dataFile.dat", "r+")
        u = len(filename)
        pgnum = 0
        for i in range(64):
            file.seek(i * 16)
            a = file.read(u)
            if a == filename:
                a = "File Found\nFile Deleted"
                done = a
                self.myfile.writeToFile("                ", pgnum, i * 16)
                self.delFfromMM(filename)
                return done

    #To add new directories in directory list
    def addChildDir(self, dirname):
        # returns count for total number of directories
        a = self.numberofDirs()
        b = int(a)
        c = b * 16
        # New dir name is written at offset c (from where last dir name was present)
        self.myfile.writeToFile(dirname, 1, c)


    # returns count for total number of directories
    def numberofDirs(self):
        file = open("C:/Users/hp/Desktop/FileManagementSystem/dataFile.dat", "r+")
        page_size = 16
        counter = 0
        page_num = 64
        # starting with page num 64 from 2nd segment upto page 128 (ending of 2nd segment)
        while page_num in range(128):
            # sets the current position at the starting of the segment containing directory
            # names (2nd segment) by defining values for page num and page size
            file.seek(page_num * page_size)
            a = file.read(page_size)
            if a == "                ":
                break
            else:
                counter += 1
                page_num += 1
        return counter

    
    #Checks fr the dirctory name in second segment
    #if directory name exists it notifies with "Directory Available"
    #else "Directory not available"
    def chDir(self, dirname):
        file = open("C:/Users/hp/Desktop/FileManagementSystem/dataFile.dat", "r+")
        page_size = 16
        count = len(dirname)
        page_num = 64
        c = ""
        while page_num in range(128):
            file.seek(page_num * page_size)
            a = file.read(page_size)
            b = a[0:count]
            if a == "                ":
                break
            else:
                if b == dirname:
                    c += "Directory Available. "
                page_num += 1
        if not c:
            c += "Directory not Available. "
        return c

            
    #counts the total number of files present in first segment
    #By going intn pages page and see  if there is any file present or not
    def numberofFiles(self):
        file = open("C:/Users/hp/Desktop/FileManagementSystem/dataFile.dat", "r+")
        page_size = 16
        counter = 0
        for page_num in range(64):
            file.seek(page_num * page_size)
            a = file.read(page_size)
            if a == "                ":
                counter = counter
            else:
                counter += 1
        return counter

    #gets the number of files for, numberofFiles()
    #add 5 to it as content area for the files stars form segment5
    #This way it reaches to the first very next empty segment
    #This segment is given to new created file 
    def pageallocF(self):
        a = self.numberofFiles()
        b = int(a)
        c = b + 5
        return c

    #To show directory list
    def getChildren(self):
        file = open("C:/Users/hp/Desktop/FileManagementSystem/dataFile.dat", "r+")
        page_size = 16
        page_num = 64
        dirlist = ""
        # starting with page num 64 from 2nd segment upto page 128 (ending of 2nd segment)
        while page_num in range(128):
            # sets the current position at the starting of the segment containing directory
            # names (2nd segment) by defining values for page num and page size
            file.seek(page_num * page_size)
            a = file.read(page_size)
            if a == "                ":
                break
            else:
                dirlist += a
                page_num += 1
        return dirlist

    #Reads the entire filled segment dedicated for memory map
    #Displays each file name along its diectory with a line break
    def memoryMap(self):
        file = open("C:/Users/hp/Desktop/FileManagementSystem/dataFile.dat", "r+")
        page_size = 32
        counter = 0
        page_num = 64
        mmap = ""
        while page_num in range(256):
            file.seek(page_num * page_size)
            a = file.read(page_size)
            if a == "                                ":
                break
            else:
                mmap += a + str("\n")
                counter += 1
                page_num += 1
        return mmap

    # returns the count of pages filled in the memory map i.e. 3rd segment
    def offsetMM(self):
        file = open("C:/Users/hp/Desktop/FileManagementSystem/dataFile.dat", "r+")
        page_size = 32
        counter = 0
        page_num = 64
        while page_num in range(256):
            # points to the starting of 3rd segment
            file.seek(page_num * page_size)
            a = file.read(page_size)
            if a == "                                ":
                break
            else:
                counter += 1
                page_num += 1
        return counter


    # deletes filename from memory map segment 
    def delFfromMM(self, filename):
        file = open("C:/Users/hp/Desktop/FileManagementSystem/dataFile.dat", "r+")
        page_size = 32
        counter = 0
        page_num = 64
        u = len(filename)
        while page_num in range(256):
            # points to the starting of 3rd segment
            file.seek(page_num * page_size)
            a = file.read(page_size)
            # finding length of filename found in dat file starting from 16 bytes(first 16 are for dirname)
            b = a[16:16+u]
            if b == filename:
                # replaces matched filename in 3rd segment with " " to delete it at the calculated offset
                self.myfile.writeToFile("                ", 2, counter+16)
            page_num += 1
            counter += 32

    #Replaces old directory name with the current new one
    #This happens in the segment dedicated for memory map
    #Firstly searches for the file name is memorymap 
    #Overrides the it with emty spaces
    #Adds current directory name to the very next empty subsegment(page)
    #Writes filename on the right f the directory name in the same page
    def move(self, srcFilename, destDirectory):
        file = open("C:/Users/hp/Desktop/FileManagementSystem/dataFile.dat", "r+")
        page_size = 32
        counter = 0
        count = 0
        page_num = 64
        u = len(srcFilename)
        k = self.offsetMM()
        m = int(k)
        j = m * 16
        while page_num in range(256):
            file.seek(page_num * page_size)
            a = file.read(page_size)
            b = a[16:16 + u]
            c = len(destDirectory)
            d = a[0:c]
            x = 0
            y = 0
            f = len(destDirectory)
            e = 14 - f
            g = len(srcFilename)
            h = 16 - g
            i = 16 + g
            if b == srcFilename:
                self.myfile.writeToFile("              ", 2, counter)
                self.myfile.writeToFile(destDirectory, 2, counter)
                while e > x:
                    f += 1
                    self.myfile.writeToFile(" ", 2, f)
                    x += 1
                self.myfile.writeToFile("~ ", 2, 14)
                self.myfile.writeToFile(srcFilename, 2, counter + 16)
                while h > y:
                    i += 1
                    self.myfile.writeToFile(" ", 2, i)

                    y += 1

            page_num += 1
            counter += 32
            b = "moved successfully to "
            print(b)
            return b

    #First checks for the filename in first most segment
    #Takes whole data from that specific page where filename lies
    #Read the file number presrnt after : in that page
    def checkFileForPage(self, filename):
        file = open("C:/Users/hp/Desktop/FileManagementSystem/dataFile.dat", "r+")
        offset = 16
        u = len(filename)
        k = ""
        m = ""
        j = 0
        for page_num in range(64):
            file.seek(page_num * offset)
            a = file.read(offset)
            b = a[0:u]
            if b == filename:
                for i in a:
                    if i == ":":
                        k = a[j: ]
                    j += 1
            m = k[1: ]
        return m

    #Reads content of a specific file
    def read(self, filename):
        file = open("C:/Users/hp/Desktop/FileManagementSystem/dataFile.dat", "r+")
        u = len(filename)
        for i in range(64):
            file.seek(i * 16)
            a = file.read(u)
            # finding if the entered file exists
            if a == filename:
                # returns page number of entered file
                a = self.checkFileForPage(filename)
                b = int(a)
                offset = 16
                page = b * 64
                limit = page + 64
                c = ""
                # defining range which takes us to the segment for the content of the entered file
                while page in range(limit):
                    # sets the current position of dat file where the required segment (entered file) containing content is started
                    file.seek(page * offset)
                    a = file.read(offset)
                    # reads page in that segment and the pages are incremented to read the entire contents of that segment
                    c += a
                    page += 1
                return c


    # writes the content in the entered file with offset specified
    def writeFile(self, filename, position, text):
        file = open("C:/Users/hp/Desktop/FileManagementSystem/dataFile.dat", "r+")
        # gives page num of the entered file
        a = self.checkFileForPage(filename)
        b = int(a)
        offset = 0
        # gives the segment where content is to be written for the entered filename
        page = b * 64
        # points to where the position/offset of the content to be written is specified by user
        limit = page + position
        while page in range(limit):
            file.seek(1)
            page += 1
            offset += 1
        file.seek(limit)
        # replaces the exisiting content of file or add a new one at the specified offset/position
        self.myfile.writeToFile(text, b, position)

    
        
root = directories("hsk")