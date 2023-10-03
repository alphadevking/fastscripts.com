from fastapi import FastAPI, Path
from fastapi.middleware.cors import CORSMiddleware  # Import CORS middleware
from api.endpoints import url_shortener, music_generator

app = FastAPI()

# Configure CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow requests from any origin (for testing purposes)
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

@app.get("/")
async def read_root():
    return {"Welcome"}

app.include_router(url_shortener.router, prefix="/urls", tags=["url_shortener"])
app.include_router(music_generator.router, prefix='/music', tags=['music_generator'])
