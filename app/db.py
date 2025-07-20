from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorCollection
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI=os.getenv("MONGO_URI")
client=AsyncIOMotorClient(MONGO_URI)
db=client["ecommerce"]
products_collection:AsyncIOMotorCollection=db["products"]
orders_collection:AsyncIOMotorCollection=db["orders"]