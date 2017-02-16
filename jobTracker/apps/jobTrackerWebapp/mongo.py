import pymongo
from bson import ObjectId
from settings import MONGO
from datetime import datetime


def get_collection_ref(collection_name):
    return pymongo.MongoClient(MONGO['host'], MONGO['port'])[MONGO['database']][collection_name]


def cursor_to_list(cursor):
    records = []
    for r in cursor:
        records.append(r)
    return records


test_collection = "test_collection"

job_collection = "job_collection"


def insert_to_test_collection(data):
    # assume data is a python dictionary
    get_collection_ref(test_collection).insert(data)


def get_all_from_test_collection():
    return cursor_to_list(get_collection_ref(test_collection).find({}))


def insert_to_job_collection(uuid,status):
    # assume data is a python dictionary
    get_collection_ref(job_collection).insert({"job_uuid": uuid, "status": status, "timestamp": str(datetime.now())})


def get_from_job_collection(data):
    return cursor_to_list(get_collection_ref(job_collection).find(data))


def get_all_from_job_collection():
    return cursor_to_list(get_collection_ref(job_collection).find({}))


def update_job(uuid, status):
    # assume data is a python dictionary
    get_collection_ref(job_collection).update({"job_uuid": uuid}, {"$set": {"status": status, "timestamp": str(datetime.now())}})
