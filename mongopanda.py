from pymongo import MongoClient
import json

class client:
    def __init__(self, host='localhost', port=27017):
        self.client = MongoClient(host,port)

    def insert(self, topic, dataFrame):
        self.dataFrame_json = dataFrame.T.to_json()
        self.dataFrame_json_list = json.loads(self.dataFrame_json).values()
        db = self.client['smdbProject']
        coll = db[topic]
        coll.insert_many(self.dataFrame_json_list)
        return coll.count_documents({})