#logging = storing unlimited data
import Core
import time

class Authenticate:
    def __init__(self,serverurl,username,password):
        self.query=Core.Console(serverurl,username,password)

    def createfile(self,filename,data): #filename,content of file
        self.query.CreateFile(filename,data)
        return True
        
    def upload(self,filename,data):
        self.query.Update(filename,data) #append data into file
        return True
        
    def recieve(self,filename):
        allData=self.query.ShowFullData(filename)
        allData=allData.split('[new]')
        dictionary={}
        for i in allData:
            dictionary[allData.index(i)+1]=i
        return dictionary
        #retuen all recieved data in dictionary Format

    def showfiles(self):
        return self.query.FileKeys()
        
    def clear(self,filename):
        self.query.ClearFile(filename)
        #erase all data inside file
    
