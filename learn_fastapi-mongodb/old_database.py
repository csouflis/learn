import motor.motor_asyncio
from old_models import Blog


# default mongodb connections
DATABASE_URL = "mongodb://localhost:27017"
client = motor.motor_asyncio.AsyncIOMotorClient(DATABASE_URL, uuidRepresentation="standard")

# connect to db with specified names (could be whatever you want to name it)
db_name = 'FastAPI_app'
coll_name = 'blogs'

db = client[db_name]
collection = db[coll_name]


async def fetch_all_blogs():
    blogs = []
    cursor = collection.find({})
    async for document in cursor:
        blogs.append(Blog(**document))
    return blogs


async def create_blog(blog):
    document = blog
    result = await collection.insert_one(document)
    return result


async def update_blog(title, body):
    await collection.update_one({"title": title}, {"$set": {"body": body}})
    document = await collection.find_one({"title": title})
    return document


async def fetch_one_blog(title):
    document = await collection.find_one({"title": title})
    return document


async def remove_blog(title):
    await collection.delete_one({"title": title})
    return True
