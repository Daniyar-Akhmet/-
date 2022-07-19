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
    client.close()


def find_income(number: float):
    client = MongoClient("mongodb://localhost:27017")
    db = client["hh"]
    return db.vacancy.find({"min": {"$gt": number}, "max": {"$gt": number}})


# for i in m_vacancies.find({'$and': [{'salary_min': {'$gte': x}}, {'salary_max': {'$gte': x}}]}):
#         print(i)