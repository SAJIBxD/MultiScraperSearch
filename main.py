import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
# from pydantic import BaseModel
# from typing import List
from scrapper import Mlwbd, MoviesMod, MoviesLeech

def get_scrappers():
    return [
        Mlwbd(),
        MoviesMod(),
        MoviesLeech()
    ]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

memory = ["info"]

@app.get("/")
async def read_index():
    return FileResponse("index.html")

@app.get("/search/{query}")
def get_info(query: str):
    results = []
    for scraper in get_scrappers():
        data = scraper
        result = {data.get_name(): data.request(query)}
        results.append(result)
    return list(results)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
