
from db.mongo import client
from datetime import datetime

class CheckLatestData():
    def __init__(self):
        self.delay = 30
        self.db = client.Jijivisha

    # returns true if there  is a change in covid data
    def getData(self):
      try:
        data = self.db.latest_pubdata
        db_data = data.find().next()
        # Excluding seconds
        curdate = db_data['pub_latest'];
        curdate = curdate[: curdate.rfind(":")]
        
        dt = datetime.strptime(curdate, '%Y-%m-%d %H:%M')
        return dt
      except Exception as e:
        raise Exception(e)