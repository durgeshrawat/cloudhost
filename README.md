# cloudhost
Store Data online

= = =    D O C U M E N T A T I O N    = = = 

#make a wordpress web site

from cloudhost import Core

class online:
	def __init__():
		self.url=''
		self.username=''
		self.password=''
		self.console=Core.Console(self.url,self.username,self.password)
	
	def create_file(self,filename,content):
		self.console.CreateFile(filename,content)
	
	def update(filename,content):
		self.console.Update(filename,content)
	
	def recieve(filename):
		self.console.ShowFullData(filename)
	
	def recieve_latest(filename):
		self.console.ShowNewData(filename)


command=online()
command.url='https://example.wordpress.com'
command.username='username'
command.password='password'


#[ Create a database file .. ]
fname,data='filename','data'
print(command.create_file(fname,data))

#[ Add data to file .. ]
fname,data='','' #select filename and new content
print(command.update(fname,data))

#[ Recieve all data .. ]
fname='' #set fname
result=command.recieve(fname)
print(result)

#[ Recieve latest data .. ]
fname='' #set filename
result=command.recieve_latest(fname)
print(result)
