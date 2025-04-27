import requests
from bs4 import BeautifulSoup

def stats_output():
    page = requests.get("https://patronite.pl/karolinakp")
    soup = BeautifulSoup(page.content, "html.parser")
    stats = soup.find(id = "stats-monthly")
    return f"{stats.string} zł"