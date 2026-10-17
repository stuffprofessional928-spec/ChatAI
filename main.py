
from fastapi import FastAPI
from routers import userservice



app = FastAPI()



app.include_router(userservice.router)










