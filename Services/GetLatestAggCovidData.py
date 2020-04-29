from db.mongo import client 

class RetriveLatestAggData():
    def __init__(self):
       self.db=client.Jijivisha   

    def get_latest_agg_data(self):
        data=self.db.aggregate_global_data
        data_list=data.find().sort([( '$natural', -1 )] ).limit(1)
        return data_list