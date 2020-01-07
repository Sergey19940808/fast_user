from pymongo import MongoClient

from umongo import Instance

from config.api_config import ApiConfig

client = MongoClient(ApiConfig.MONGODB_URI)
db = getattr(
    client,
    ApiConfig.MONGODB_DATABASE
)

instance = Instance(db)