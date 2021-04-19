# import mongoengine
import math
class RetriveDataForCharts:
    def __init__(self,data,N):
        self.data=data
        self.N=N

    # this method will return N no. of documents required for google charts including the latest aggregate data.
    def getData(self):
        try:
            # We need N data incl first and last data
            if(self.N==0):
                raise Exception("Invalid Limit")
            if(not self.data):
                raise Exception("Some db issue occured")
            
            list_=[]
            documents_count=self.data.count()
            # print(documents_count)
            if(documents_count==self.N or documents_count<self.N):
                return list(self.data)
            # no of documents to skip in between
            skip=math.ceil(documents_count/(self.N)) 
            count_skip=skip

            # will throw a stopiteration exception once finished.
            # return list_
            obj=next(self.data)
            count=1
            # inserting the first element since inside loop first doc is skipped as skip might not start from 1 
            list_.append(obj)
            while obj:
                obj=next(self.data)
                if(len(list_)<(self.N-1)):
                    
                    if(count==count_skip):
                        list_.append(obj)
                        count_skip=count_skip+skip
                        
                count=count+1
                
            # return obj
        except StopIteration:
            # next() will throw a stop iteration exception once it is finished
            # print("length",len(list_))
            list_.append(obj)
            return list_
        except Exception as identifier:
            # print(type(identifier).__name__)
            raise Exception(identifier)