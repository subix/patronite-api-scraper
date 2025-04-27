import scraper
from fastapi import FastAPI

app = FastAPI()

@app.get("/scraper")
def read_scraper():
    return scraper.stats_output()