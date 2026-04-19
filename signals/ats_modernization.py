import datetime
from utils.scorer import calculate_score

KEYWORDS = [
    "workday",
    "successfactors",
    "ats migration",
    "hr transformation",
    "recruitment automation",
    "hiring platform",
    "upgrade"
]

TOOLS = ["workday", "successfactors", "greenhouse"]


def detect_ats_modernization(article):
    content = article["content"].lower()

    matched_keywords = [kw for kw in KEYWORDS if kw in content]
    detected_tools = [tool for tool in TOOLS if tool in content]

    if not matched_keywords:
        return None

    score = calculate_score(len(matched_keywords), detected_tools)

    return {
        "company": article["company"],
        "signal_type": "ats_modernization",
        "source_url": article["url"],
        "matched_keywords": matched_keywords,
        "detected_tools": detected_tools,
        "signal_score": score,
        "detected_at": datetime.datetime.now().isoformat(),
        "reason": f"Detected ATS modernization signal due to usage of tools like {', '.join(detected_tools)}"
    }
