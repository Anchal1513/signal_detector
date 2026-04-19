import json
from utils.fetcher import fetch_articles_from_rss
from signals.ats_modernization import detect_ats_modernization
from signals.mass_hiring import detect_mass_hiring


def save_output(signals):
    with open("output/signals.json", "w") as f:
        json.dump(signals, f, indent=4)


def run():
    try:
        articles = fetch_articles_from_rss()

        unique_signals = {}

        for article in articles:
            signal1 = detect_ats_modernization(article)
            signal2 = detect_mass_hiring(article)

            # Process ATS signal
            if signal1:
                key1 = (signal1["company"], signal1["signal_type"])
                if key1 not in unique_signals:
                    unique_signals[key1] = signal1

            # Process Mass Hiring signal
            if signal2:
                key2 = (signal2["company"], signal2["signal_type"])
                if key2 not in unique_signals:
                    unique_signals[key2] = signal2

        results = list(unique_signals.values())

        save_output(results)

        print("Detected signals:", len(results))

    except Exception as e:
        print("Error:", str(e))


if __name__ == "__main__":
    run()