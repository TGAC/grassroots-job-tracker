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


job_collection = "job_collection"


# def insert_to_job_collection(uuid,status):
#     # assume data is a python dictionary
#     get_collection_ref(job_collection).insert({"job_uuid": uuid, "status": status, "timestamp": str(datetime.now())})


def get_from_job_collection(job_uuid):
    return cursor_to_list(get_collection_ref(job_collection).find({'job.job_uuid': job_uuid}))


def get_all_from_job_collection():
    return cursor_to_list(get_collection_ref(job_collection).find({}))


def update_job(server_id, job_uuid, job_dict):
    get_collection_ref(job_collection).update({'job.job_uuid': job_uuid}, {
        '$set': {'server_id': server_id, 'job': job_dict, 'timestamp': str(datetime.now())}}, True)
