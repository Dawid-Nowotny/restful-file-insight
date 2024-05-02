from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from magic_numbers.router import router as magic_numbers_router
from file_scan.router import router as file_scan_router

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

app.include_router(magic_numbers_router, prefix="/magic-numbers", tags=["Magic numbers"])
app.include_router(file_scan_router, prefix="/scan", tags=["File scan"])