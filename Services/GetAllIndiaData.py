from db.mongo import client 

class RetriveIndiaData():
    def __init__(self):
        self.db=client.Jijivisha 

    def get_data(self):
        data=self.db.india_covid_data
        data_list=data.find()
        return data_list
