from pymongo import MongoClient


def insert_data(result: list):
    client = MongoClient("mongodb://localhost:27017")
    db = client["hh"]
    db.vacancy.insert_one({"test": "test"})
    for item in result:
        if not bool(*db.vacancy.find({"url": item["url"]})):
            db.vacancy.insert_one(item)
            print("insert data")
        else:
            print('existing data')
    db.vacancy.delete_many({"test": "test"})
