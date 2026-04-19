import feedparser


def fetch_articles_from_rss():
    url = "https://news.google.com/rss/search?q=HR+technology+ATS"

    feed = feedparser.parse(url)

    articles = []

    for entry in feed.entries:
        company_name = entry.title.split(" ")[0].replace("'s", "")

        articles.append({
            "company": company_name,
            "url": entry.link,
            "content": entry.title + " " + entry.get("summary", ""),
        })
    return articles