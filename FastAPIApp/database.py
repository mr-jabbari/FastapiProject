from motor.motor_asyncio import AsyncIOMotorClient

db = AsyncIOMotorClient("mongodb://localhost:27017").test_database
print(db)
