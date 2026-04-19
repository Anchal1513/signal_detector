# 📡 Signal Detection System — ATS / HR Tech Modernization Detector

> Assignment Submission — Vikaas.ai Signal Detection Task

A modular Python-based system that detects recruitment technology modernization signals from public data sources using rule-based logic.

---

## 📌 Overview

This project identifies companies that are upgrading or transforming their hiring technology stack (e.g., ATS migration, HR transformation).

It processes semi-structured data (RSS feeds or sample inputs), applies keyword-based detection, and produces structured JSON outputs that can be used for business insights or outreach automation.

---

## 🎯 Objective

Detect signals such as:

* ATS migration announcements
* HR transformation initiatives
* Recruitment automation adoption
* Hiring platform upgrades

---

## 🏗️ Project Architecture

```
signal_detector/
│
├── signals/
│   └── ats_detector.py
├── utils/
├── data/
│   └── sample_input.json
├── output/
│   └── signals.json
├── main.py
├── api.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup & Installation

```bash
git clone https://github.com/Anchal1513/signal_detector.git
cd signal_detector

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt
```

---

## ▶️ How to Run

```bash
python main.py
```

📌 Output will be generated in:

```
output/signals.json
```

---

## 📥 Example Input

File:

```
data/sample_input.json
```

Example:

```json
{
  "company": "Workday",
  "text": "The company is adopting Workday to improve hiring workflows.",
  "url": "https://example.com/article"
}
```

---

## 📤 Sample Output

```json
[
  {
    "company": "Workday",
    "signal_type": "ats_modernization",
    "source_url": "https://news.google.com/rss/articles/CBMinwFBVV95cUxObUtrRDZqcWJPdV9ZVWs0VXB0WE43QU5lOXd1c2xXZUl0a01JSWZDREVYUTZEaWhqb2xESjBrNGk0T2I4clVfVm5GZEJUMUlOMGROWHIzQTZLVkdzUVgtbTB5eHJSTUVTS1E4M2dGd21yak83NVNBQlJ1X2p2bG4zbldDTFN0VlBhV3pmYW95N2pBNlkxYWVFemlRcGxyZVk?oc=5",
    "matched_keywords": ["Workday"],
    "tools_detected": ["Workday"],
    "signal_score": 20,
    "detected_at": "2026-04-19T15:15:04",
    "stage": "unknown",
    "reason": "Detected ATS modernization signal based on keyword 'Workday' indicating recruitment technology usage"
  }
]
```

---

## 🧠 Detection Logic

### 🔹 Keywords Used

* Workday
* SuccessFactors
* ATS migration
* HR transformation
* recruitment automation
* hiring platform upgrade

### 🔹 Tool Detection

The system extracts HR tools mentioned in the text such as Workday and SuccessFactors.

### 🔹 Stage Detection

* migration → if "migration" keyword found
* upgrade → if "upgrade" keyword found
* unknown → default

### 🔹 Scoring Logic

```
signal_score = number_of_matched_keywords × 20
```

---

## 📊 Design Explanation

### 🔹 Data Ingestion

Data is collected from public sources such as RSS feeds or sample JSON files. No paid APIs are used.

### 🔹 Parsing

Input text is cleaned and normalized for accurate keyword matching.

### 🔹 Signal Detection

A rule-based approach is used where predefined keywords trigger ATS modernization signals.

### 🔹 Output Generation

Detected signals are stored as structured JSON for downstream usage.

---

## ⚠️ Assumptions

* Presence of keywords indicates potential ATS modernization
* Input data contains relevant HR or hiring-related content
* Company name is available in input

---

## ❗ Limitations

* Keyword-based detection may produce false positives
* No NLP or contextual understanding
* Limited to predefined keywords

---

## 🌐 API (Optional)

```bash
python api.py
```

Provides a simple endpoint for signal detection.

---

## 📸 Screenshots

### ▶️ Running the Project

![Run](Screenshot%202026-04-17%20123114.png)

### 📤 Output File

![Output](Screenshot%202026-04-18%20131751.png)

---

## 👩‍💻 Author

**Anchal Singh**
GitHub: https://github.com/Anchal1513

---

## 📄 License

This project is developed for assignment and educational purposes.

---

## ⭐ Final Note

This project demonstrates:

* Modular backend design
* Data ingestion from public sources
* Rule-based signal extraction
* Structured output generation
