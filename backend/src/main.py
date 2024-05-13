from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from file.router import router as magic_numbers_router

app = FastAPI()

origins = [
    "http://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(magic_numbers_router, prefix="/file", tags=["Files"])