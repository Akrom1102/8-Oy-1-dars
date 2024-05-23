from fastapi import FastAPI
from auth import auth_router
from model import model_router

# Download and Install FASTAPI
"""pip install fastapi uvicorn """

# run fastapi
"""uvicorn main:app --reload"""

app = FastAPI()
app.include_router(auth_router)
app.include_router(model_router)


@app.get("/")
async def intro():
    return {
        "message": "This is landing page! Created by © Akram ®"
    }


@app.get("/test")
async def test1():
    return {
        "message": "Hello! Akram"
    }


@app.get("/test2")
async def test2():
    return {
        "message": "Group -> N37. Hello"
    }
