from fastapi import FastAPI
from utils.fetcher import fetch_articles_from_rss
from signals.ats_modernization import detect_ats_modernization
from signals.mass_hiring import detect_mass_hiring
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/signals")
def get_signals():
    articles = fetch_articles_from_rss()
    results = []

    for article in articles:
        signal1 = detect_ats_modernization(article)
        signal2 = detect_mass_hiring(article)

        if signal1:
            results.append(signal1)

        if signal2:
            results.append(signal2)

    return JSONResponse(content={"signals": results}, media_type="application/json")

