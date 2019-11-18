from pymongo import MongoClient
import pandas as pd
import json

class client:
    def __init__(self, host='localhost', port=27017):
        self.client = MongoClient(host,port)
        self.db = self.client['smdbProject']

    def insert(self, topic, dataFrame):
        self.dataFrame_json = dataFrame.T.to_json()
        self.dataFrame_json_list = json.loads(self.dataFrame_json).values()
        coll = self.db[topic]
        coll.insert_many(self.dataFrame_json_list)
        return coll.count_documents({})

    def retrieve(self, topic):
        coll = self.db[topic]
        exclude_col = {'_id': False }
        data = list(coll.find({}, projection=exclude_col))
        df = pd.DataFrame(data, columns=['date','tweet', 'username','sentiment'])
        return df