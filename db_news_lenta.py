from pymongo import MongoClient


def insert_data(result: list):
    client = MongoClient("mongodb://localhost:27017")
    db = client["db_lenta"]
    db.news.insert_one({"test": "test"})
    for item in result:
        if not bool(*db.news.find({"_id": item["_id"]})):
            db.news.insert_one(item)
            print("insert data")
        else:
            print('existing data')
    db.news.delete_many({"test": "test"})
    client.close()