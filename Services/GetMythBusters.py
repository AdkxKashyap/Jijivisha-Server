from db.mongo import client 

class  RetriveMythBusters():
    def __init__(self):
        self.db=client.Jijivisha   

    def get_mythbusters(self):
        try:
            data=self.db.myth_busters
            data_list=data.find()
            return data_list
        except Exception as err:
            return err
        