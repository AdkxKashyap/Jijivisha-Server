from db.mongo import client 

class RetriveAggData():
    def __init__(self):
       self.db=client.Jijivisha   

    def get_agg_data(self):
        data=self.db.aggregate_global_data
        data_list=data.find()
        return data_list