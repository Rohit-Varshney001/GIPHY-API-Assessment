from fastapi import FastAPI, HTTPException
import requests
import os
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv


# Load environment variables
load_dotenv()

# Instantiate FastAPI
app = FastAPI()

# Allow cross-origin resource sharing (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=["*"]
)

# Get Giphy API key from environment variables
GIPHY_API_KEY = os.getenv("GIPHY_API_KEY")
GIPHY_URL = "https://api.giphy.com/v1/gifs/search"

@app.get("/api/gifs")
def get_gifs(search: str = "trending"):  
    params = {
        'api_key': GIPHY_API_KEY,
        'q': search,
        'limit': 10
    }
    response = requests.get(GIPHY_URL, params=params)

    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="Failed to fetch data from Giphy API")

    data = response.json()
    gifs = [{"id": item["id"], "url": item["images"]["original"]["url"]} for item in data.get("data", [])]

    return gifs



# Run the app with Uvicorn when executed directly
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
