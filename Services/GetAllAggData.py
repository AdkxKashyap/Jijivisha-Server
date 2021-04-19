from Services.GetDataForCharts import RetriveDataForCharts
from db.mongo import client 
class RetriveAggData():
    def __init__(self,N):
        self.db=client.Jijivisha   
        self.N=N
    def get_agg_data(self):
        try:
            data=self.db.aggregate_global_data
            data_list=data.find()
            return data_list
        except Exception as identifier:
            raise Exception(identifier)
    def get_data_for_google_charts(self):
        try:
            data=self.get_agg_data()
            agg_data_list=RetriveDataForCharts(data,self.N).getData()
            print(len(agg_data_list))
            return agg_data_list
        except Exception as identifier:
            raise Exception(identifier)