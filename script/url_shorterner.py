import hashlib
import string
import random

class URLShortener:
    def __init__(self):
        self.url_map = {}

    def shorten_url(self, url):
        # Generate a unique short key
        short_key = self.generate_short_key()

        # Construct the shortened URL
        shortened_url = f"localhost:8000/{short_key}"

        # Store the mapping in a dictionary
        self.url_map[short_key] = url  # Store the short URL along with the original URL

        return shortened_url

    def generate_short_key(self):
        # Generate a random string of 6 characters
        characters = string.ascii_letters + string.digits
        short_key = ''.join(random.choice(characters) for _ in range(6))

        # Check if the generated key is already in use
        while short_key in self.url_map:
            short_key = ''.join(random.choice(characters) for _ in range(6))

        return short_key

    def get_original_url(self, short_key):
        # Retrieve the original URL from the mapping
        return self.url_map.get(short_key)

# Example usage
# shortener = URLShortener()
# long_url = "https://example.com/this-is-a-long-url"
# short_url = shortener.shorten_url(long_url)
# print(f"Shortened URL: {short_url}")
# original_url = shortener.get_original_url(short_url.split('/')[-1])
# print(f"Original URL: {original_url}");
