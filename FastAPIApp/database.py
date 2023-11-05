from motor.motor_asyncio import AsyncIOMotorClient
import pymongo

database = AsyncIOMotorClient("mongodb://localhost:27017/") # conect running localy
#database = pymongo.MongoClient("mongodb://mongodb:27017/") # connect running on docker
db = database['fastAPI_project']
print(db)