from fastapi import FastAPI, Path
from fastapi.middleware.cors import CORSMiddleware  # Import CORS middleware
from fastapi.responses import RedirectResponse
from script.url_shorterner import URLShortener

app = FastAPI()

# Configure CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow requests from any origin (for testing purposes)
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

shortener = URLShortener()

@app.get("/")
async def read_root():
    return {"Welcome"}

@app.post("/shorten-url/{long_url}")
async def shorten_url(long_url: str):
    result = shortener.shorten_url(long_url)
    return {"Short Url is ": result}

@app.get("/get-original-url/{short_url:path}")
async def get_original_url(short_url: str = Path(...)):
    # Extract the short_key from the URL
    short_key = short_url.split('/')[-1]

    original_url = shortener.get_original_url(short_key)

    if original_url:
        return RedirectResponse(original_url)
    else:
        return {"error": "Short URL not found"}
