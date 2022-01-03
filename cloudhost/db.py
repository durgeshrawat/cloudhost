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

if __name__=='__main__':
    server=Authenticate('https://servertest.code.blog',
                        'stellerx','stellerx.incorrect')
    print(server)
    f='testfile'
    #print(server.createfile('testfile1','hii'))
    #server.upload(f,'how are you')
    #print(server.recieve(f))
    #print(server.clear(f))
    #print(server.showfiles())
    