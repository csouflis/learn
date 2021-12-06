from fastapi import APIRouter, Body, Request, HTTPException, status, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from apps.user.models import User
from .models import BlogModel, UpdateBlogModel


def get_blog_router(app):

    router = APIRouter()

    @router.post(
        "/",
        response_description="Add new blog",
    )
    async def create_blog(
        request: Request,
        user: User = Depends(app.fastapi_users.get_current_active_user),
        blog: BlogModel = Body(...),
    ):
        blog = jsonable_encoder(blog)
        new_blog = await request.app.db["blogs"].insert_one(blog)
        created_blog = await request.app.db["blogs"].find_one(
            {"_id": new_blog.inserted_id}
        )

        return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_blog)

    @router.get("/", response_description="List all blogs")
    async def list_blogs(
        request: Request,
        user: User = Depends(app.fastapi_users.get_current_active_user),
    ):
        blogs = []
        for doc in await request.app.db["blogs"].find().to_list(length=100):
            blogs.append(doc)
        return blogs

    @router.get("/{id}", response_description="Get a single blog")
    async def show_blog(
        id: str,
        request: Request,
        user: User = Depends(app.fastapi_users.get_current_active_user),
    ):
        if (blog := await request.app.db["blogs"].find_one({"_id": id})) is not None:
            return blog

        raise HTTPException(status_code=404, detail=f"blog {id} not found")

    @router.put("/{id}", response_description="Update a blog")
    async def update_blog(
        id: str,
        request: Request,
        user: User = Depends(app.fastapi_users.get_current_active_user),
        blog: UpdateBlogModel = Body(...),
    ):
        blog = {k: v for k, v in blog.dict().items() if v is not None}

        if len(blog) >= 1:
            update_result = await request.app.db["blogs"].update_one(
                {"_id": id}, {"$set": blog}
            )

            if update_result.modified_count == 1:
                if (
                    updated_blog := await request.app.db["blogs"].find_one({"_id": id})
                ) is not None:
                    return updated_blog

        if (
            existing_blog := await request.app.db["blogs"].find_one({"_id": id})
        ) is not None:
            return existing_blog

        raise HTTPException(status_code=404, detail=f"blog {id} not found")

    @router.delete("/{id}", response_description="Delete blog")
    async def delete_blog(
        id: str,
        request: Request,
        user: User = Depends(app.fastapi_users.get_current_active_user),
    ):
        delete_result = await request.app.db["blogs"].delete_one({"_id": id})

        if delete_result.deleted_count == 1:
            return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)

        raise HTTPException(status_code=404, detail=f"blog {id} not found")

    return router
