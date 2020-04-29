from db.mongo import client

class RetriveAggIndiaData():
    def __init__(self):
        self.db=client.Jijivisha 

    def get_data(self):
        try:
            data=self.db.global_data
            #there are multiple covid_data entries so then using the $ positional operator only the matched entries in the array
            data_list=data.find({"covid_data":{"$elemMatch":{"country":"India"}}},{'covid_data.$':1,'published':1})

            return data_list

        except Exception as err:
            raise Exception(err)
       