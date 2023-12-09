from fastapi import APIRouter, Path, FastAPI, HTTPException, Body
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from script.url_shorterner import URLShortener

router = APIRouter()

shortener = URLShortener()

@router.post("/shorten-url/")
async def shorten_url(long_url: str = Body(...)):
    result = shortener.shorten_url(long_url)
    return {"Short Url is ": result}

@router.get("/get-original-url/{short_url:path}")
async def get_original_url(short_url: str = Path(...)):
    # Extract the short_key from the URL
    short_key = short_url.split('/')[-1]

    original_url = shortener.get_original_url(short_key)

    if original_url:
        return RedirectResponse(original_url)
    else:
        raise HTTPException(status_code=404, detail="Short URL not found");

# Assuming you want to integrate this router into a main FastAPI app:
app = FastAPI()

# CORS middleware settings
origins = [
    "http://localhost:8000",  # Assuming your Vite React app runs on this port
    # Add any other origins you want to whitelist
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router);
