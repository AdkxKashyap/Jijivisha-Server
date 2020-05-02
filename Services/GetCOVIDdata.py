
from db.mongo import client 




class RetriveCOVIdDATA: 
    def __init__(self):
       self.db=client.Jijivisha                         
    
    #gets data of all the countries and also continents
    def get_data_allcountries(self):
        data=self.db.global_data
        
        data_list=data.find().sort([( '$natural', -1 )] ).limit(1)
        return data_list 

            
        