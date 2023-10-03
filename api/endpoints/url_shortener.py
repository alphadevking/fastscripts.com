from fastapi import APIRouter, Path
from fastapi.responses import RedirectResponse
from script.url_shorterner import URLShortener

router = APIRouter()

shortener = URLShortener()

@router.post("/shorten-url/{long_url}")
async def shorten_url(long_url: str):
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
        return {"error": "Short URL not found"}
    