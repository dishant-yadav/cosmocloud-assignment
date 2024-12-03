from fastapi import FastAPI
from routes import router as student_router
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

app.include_router(student_router, prefix="/api")


@app.get("/")
async def root():
    return {"message": "Hello World"}
