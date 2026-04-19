import datetime

KEYWORDS = [
    "hiring aggressively",
    "mass hiring",
    "scale hiring",
    "expanding team rapidly",
    "100 engineers",
    "hiring 100",
    "large hiring",
    "bulk hiring"
]


def detect_mass_hiring(article):
    content = article["content"].lower()

    matched_keywords = [kw for kw in KEYWORDS if kw in content]

    if not matched_keywords:
        return None

    score = min(50 + len(matched_keywords) * 15, 100)

    return {
        "company": article["company"],
        "signal_type": "mass_hiring",
        "source_url": article["url"],
        "matched_keywords": matched_keywords,
        "signal_score": score,
        "detected_at": datetime.datetime.now().isoformat(),
        "reason": "Mass hiring signal detected"
    }