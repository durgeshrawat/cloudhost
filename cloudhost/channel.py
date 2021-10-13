from cloudhost import Core
class Channel:
    def __init__(self,url,username,password):
        self.url=url
        self.username=username
        self.password=password
        self.WebQuery=Core.Console(
            self.url,
            self.username,
            self.password
        )

    def Send(self,ChannelName,data):
        self.WebQuery.Update(ChannelName,data)
        return True
    def Recieve(self,ChannelName):
        DataObtained=self.WebQuery.ShowNewData(ChannelName)
        if DataObtained!='':
            self.WebQuery.ClearFile(ChannelName)
        return DataObtained
    def NewChannel(self,ChannelName):
        try:
            self.WebQuery.CreateFile(ChannelName,'$')
            return True
        except Exception as e:
            return e


    