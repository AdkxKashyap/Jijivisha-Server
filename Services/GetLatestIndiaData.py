from db.mongo import client 
from Services.GetDataForCharts import RetriveDataForCharts
class RetriveIndiaData():
    def __init__(self):
        self.db=client.Jijivisha 

    def get_all_data_state(self,state):
        # returns all data of a state
        try:
            data=self.db.india_covid_data
            data_list=data.find({"covid_data":{"$elemMatch":{"state":state}}},{"covid_data.$":1,"published":1})
            if(data_list.count()==0):
                raise Exception("No documents found")
            return data_list
        except Exception as identifier:
            raise Exception(identifier)
    def get_latest_data(self):
        data=self.db.india_covid_data
        data_list=data.find().sort([( '$natural', -1)] ).limit(1)
        if(data_list.count()==0):
                raise Exception("No documents found")
        return data_list

    # get district data of a state
    def get_districts_data(self,state):
        try:
            data=self.db.indian_district_data
            data_list=data.find({"covid_data":{"$elemMatch":{"state":state}}},{'covid_data.$':1,'published':1}).sort([('$natural', -1 )]).limit(1)
            if(data_list.count()==0):
                raise Exception("No documents found")

            
            # print(data_list.count)
            return data_list
        except Exception as identifier:
            raise Exception(identifier)

    def get_data_state(self,N,state):
        # N is the no. of documents to be sent.According to N the documents will be divided
        # Clent side is using this data to draw charts.N data is used for the charts.
        try:
            print(state)
            state_data=self.get_all_data_state(state)
            data_list=RetriveDataForCharts(state_data,12).getData()
            return data_list
        except Exception as identifier:
            raise Exception(identifier)
        

        

