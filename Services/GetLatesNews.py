from db.mongo import client 

class RetriveLatestNews():
    def __init__(self):
        self.db=client.Jijivisha 
        
    def get_india_news(self):
        try:
            data=self.db.india_news
            data_list=data.find().sort([( '$natural', -1 )] ).limit(1)
            return data_list
        except Exception as err:
            return err
        
    def get_global_news(self):
        try:
            data=self.db.global_news
            data_list=data.find().sort([( '$natural', -1 )] ).limit(1)
            return data_list
        except Exception as err:
            return err