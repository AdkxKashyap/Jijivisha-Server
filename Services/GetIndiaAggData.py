from db.mongo import client
from Services.GetDataForCharts import RetriveDataForCharts
class RetriveAggIndiaData():
    def __init__(self,N):
        self.db=client.Jijivisha 
        self.N=N
    def get_data(self):
        try:
            data=self.db.global_data
            #there are multiple covid_data entries so then using the $ positional operator only the matched entries in the array
            data_list=data.find({"covid_data":{"$elemMatch":{"country":"India"}}},{'covid_data.$':1,'published':1})

            return data_list

        except Exception as err:
            raise Exception(err)
    
    def get_data_for_google_charts(self):
        try:
            data=self.get_data()
            agg_data_list=RetriveDataForCharts(data,self.N).getData()
            print("length",len(agg_data_list))
            return agg_data_list
        except Exception as identifier:
            raise Exception(identifier)