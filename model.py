from fastapi import APIRouter

model_router = APIRouter(prefix="/model")


@model_router.get("/")
async def model():
    return {
        "message": "This is the model page"
    }


@model_router.get("/model1")
async def model1():
    return {
        "message": "This is the model page 1"
    }


@model_router.get("/model2")
async def model2():
    return {
        "message": "This is the model page 2"
    }