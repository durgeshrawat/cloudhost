# web
from wordpress_xmlrpc import Client
from wordpress_xmlrpc.methods import posts
from wordpress_xmlrpc import WordPressPost



class Console:
	def __init__(self,url,username,password):
		self.url=url+'/xmlrpc.php'
		self.username=username
		self.password=password
        
	def CreateFile(self,Title,Description):
	    your_blog = Client(self.url,self.username,self.password)
	    post = WordPressPost()
	    post.title = Title
	    post.slug='0'
	    post.content = Description
	    #post.post_status = 'publish'
	    post.id = your_blog.call(posts.NewPost(post))
	    return post.id
	
	def FileKeys(self):
	    client = Client(self.url, self.username, self.password)
	    wp_posts = client.call(posts.GetPosts())
	    indexes={}
	    for i in wp_posts:
	    	indexes[i.title]=wp_posts.index(i)
	    return indexes
	    
	def FileID(self,FileName):
		_data=self.FileKeys()
		return _data[FileName]
		
	
	def ShowFullData(self,FileName):
	    client = Client(self.url, self.username, self.password)
	    wp_posts = client.call(posts.GetPosts())
	    return wp_posts[self.FileID(FileName)].content

	def ShowNewData(self,FileName):
		_data=self.ShowFullData(FileName)
		_data=_data.split('[new]')
		return _data[len(_data)-1]
		
	def Update(self,FileName,Data):
		client = Client(self.url, self.username, self.password)
		wp_posts = client.call(posts.GetPosts())
		index=self.FileID(FileName)
		chat=wp_posts[index].content
		chatTitle=wp_posts[index].title
		newChat=chat+'[new]'+Data
		post = WordPressPost()
		post.slug='0'
		post.title=chatTitle
		post.content=newChat
		client.call(posts.EditPost(wp_posts[index].id, post))
		return True
	
	
	def ClearFile(self,FileName): #de.encrypt(username.server)
		client = Client(self.url, self.username, self.password)
		wp_posts = client.call(posts.GetPosts())
		index=self.FileID(FileName)
		chatTitle=wp_posts[index].title
		newChat='$'
		post = WordPressPost()
		post.slug='0'
		post.title=chatTitle
		post.content=newChat
		client.call(posts.EditPost(wp_posts[index].id, post))
		return True
