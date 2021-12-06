from fastapi_users.db import MongoDBUserDatabase
from fastapi_users.authentication import JWTAuthentication
from fastapi_users import FastAPIUsers
from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import motor.motor_asyncio
import uvicorn
from typing import Optional
import old_models
import old_database



# --- Authentication Method Setup ---------------------------------------------
# Secret Key (must be changed from "SECRET")
secret_key = 'SECRET'
# Authentication Method JWT
auth_backends = []
authentication = JWTAuthentication(secret=secret_key, lifetime_seconds=3600)
auth_backends.append(authentication)
# ------------------------------------------------------------------------------

# default mongodb connections
DATABASE_URL = "mongodb://localhost:27017"
client = motor.motor_asyncio.AsyncIOMotorClient(DATABASE_URL, uuidRepresentation="standard")

# connect to db with specified names (could be whatever you want to name it)
db_name = 'FastAPI_app'

db = client[db_name]
user_collection = db['users']

user_db = MongoDBUserDatabase(old_models.UserDB, user_collection)

fast_api_users = FastAPIUsers(
    user_db,
    auth_backends,
    old_models.User,
    old_models.UserCreate,
    old_models.UserUpdate,
    old_models.UserDB
)

# --- FastAPI Server Initialization -------------------------------------------

# Initiating FastAPI Server
myapp = FastAPI()

# Managing CORS for the hypothetical React Frontend connections
origins = [
    "http://localhost",
    "http://localhost:3000"
]

myapp.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)



# --- User Authentication Routes ----------------------------------------------

# Add route for Login     ----   -----------       POST "/auth/login"
myapp.include_router(
    fast_api_users.get_auth_router(auth_backends[0]),
    prefix="/auth",
    tags=["auth"]
)

# Add route for Registration    ------  ---      POST "/auth/register"

# Below function can be used to init any backend process like sending out a successful registration email
def on_after_register(user: old_models.UserDB, request: Request):
    print(f"User {user.id} has registered.")

myapp.include_router(
    # fast_api_users.get_register_router(),
    fast_api_users.get_register_router(on_after_register),
    prefix="/auth",
    tags=["auth"]
)


# Add route for User utilities "/auth/users/*" -----     ------------
""" 
    Get current logged in user profile          GET "/auth/users/me"
    Update current logged in user profile       PATCH "/auth/users/me"
    Get "_id" user profile                      GET "/auth/users/"
    Update "_id" user profile                   PATCH "/auth/users/{id}"
    Delete "_id" user profile                   DELETE "/auth/users/{id}" 
"""
myapp.include_router(
    fast_api_users.get_users_router(),
    prefix="/auth/users",
    tags=["auth"]
)


# Add route for Reset Password utility -----   -  -- - -  ---
"""
    Forgot Password                             POST /auth/users/forgot-password
    Reset Password                              POST /auth/users/reset-password                         
"""

myapp.include_router(
    fast_api_users.get_reset_password_router("SECRET"),
    prefix="/auth/users",
    tags=["auth"]
)
# ---------------------------------------------------------------------------------


@myapp.get('/api')
def index():
    return {'data': {'name': 'Chris'}}


@myapp.get('/api/blog')
async def get_all_blogs(limit=10, published: bool = True, sort: Optional[str] = None): #default values specified here
    # get query parameters 'limit' and 'published' from URL specifications
    # (e.g. http://localhost:8000/blog?limit=25&published=false)
    pubbed = []
    blogs = await old_database.fetch_all_blogs()
    for blog in blogs:
        if blog.published:
            pubbed.append(blog)
    return {'data': f'All published blogs from db: {pubbed}'}


@myapp.post('/api/blog', response_model=old_models.Blog)
async def post_blog(blogpost: old_models.Blog):
    response = await old_database.create_blog(blogpost.dict())
    if response:
        return {'data': f'blog is created with title {blogpost.title}, body text: {blogpost.body}'}
    raise HTTPException(400, "Something went wrong")


@myapp.get('/api/blog/{title}', response_model=old_models.Blog)
async def get_blog_by_title(title: str):
    response = await old_database.fetch_one_blog(title)
    if response:
        return {'data': response}
    raise HTTPException(400, "Something went wrong")


@myapp.put('/api/blog/{title}', response_model=old_models.Blog)
async def update_blog(title: str, new_body: str):
    response = await old_database.update_blog(title, new_body)
    if response:
        return {'data': f'updated blog: {response}'}
    raise HTTPException(404, f"There is no todo with the title {title}")


@myapp.get('/api/blog/unpublished')
def unpublished():
    unpub = []
    blogs = old_database.fetch_all_blogs()
    for blog in blogs:
        if not blog.published:
            unpub.append(blog)
    return {'data': f'all unpublished blogs: {unpub}'}




@myapp.get('/api/blog/{id}/comments')
def comments(id: int, limit=10):
    comments = []
    count = 0
    for comment in range(0, limit):
        comments.append('comment' + str(count))
        count+=1
    return {'data': f'showing blog with ID:{id}', 'comments': {'comments': comments}}


@myapp.delete('/api/blog/{id}')
def delete_blog(blogpost: old_models.Blog):
    old_database.remove_blog(blogpost.title)
    return {'task': 'deletion successful'}


if __name__ == "__main__":
    uvicorn.run(
        'main:myapp',
        host='127.0.0.1',
        reload=True,
        port=9000,
        workers=0
    )
