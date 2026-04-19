📡 Signal Detection System — ATS / HR Tech Modernization Detector
> Assignment Submission — Vikaas.ai Signal Detection Task

A modular Python-based system that detects recruitment technology modernization signals from public data sources using rule-based logic.

📌 Overview

This project identifies companies that are upgrading or transforming their hiring technology stack (e.g., ATS migration, HR transformation).

It processes semi-structured data (RSS feeds or sample inputs), applies keyword-based detection, and produces structured JSON outputs that can be used for business insights or outreach automation.

🎯 Objective

Detect signals such as:

ATS migration announcements
HR transformation initiatives
Recruitment automation adoption
Hiring platform upgrades

🏗️ Project Architecture
signal_detector/
│
├── fetcher/                # input data
├── parser/                 # Clean and process text
├── signals/
│   └── ats_detector.py     # ATS modernization detection logic
├── utils/                  # Scoring utilities
├── output/
│   └── signals.json        # Generated signals
│
├── data/
│   └── sample_input.json   # Example input
│
├── main.py                 # Entry point
├── requirements.txt
└── README.md

⚙️ Setup & Installation
1️⃣ Clone Repository
git clone https://github.com/Anchal1513/signal_detector.git
cd signal_detector

2️⃣ Create Virtual Environment
python -m venv venv

3️⃣ Activate Environment
venv\Scripts\activate   # Windows

4️⃣ Install Dependencies
pip install -r requirements.txt

▶️ How to Run
python main.py

🔄 What happens when you run:
Input data is loaded  (sample JSON)
Text is parsed and cleaned
ATS modernization signals are detected
Results are saved in JSON format

📥 Example Input

Sample input file:

data/sample_input.json

Example structure:

{
  "company": "Workday",
  "text": "The company is adopting Workday to improve hiring workflows.",
  "url": "https://example.com/article"
}

📤 Sample Output

Generated output:

output/signals.json
✅ Actual Output from System
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

Output will be generated in: output/signals.json

🧠 Detection Logic
🔹 Keywords Used
Workday
SuccessFactors
ATS migration
HR transformation
recruitment automation
hiring platform upgrade

🔹 Tool Detection

The system extracts HR tools mentioned in the text:

Example: Workday, SuccessFactors

🔹 Stage Detection
Migration → if "migration" detected
Upgrade → if "upgrade" detected
Unknown → default (if no clear stage found)

🔹 Scoring Logic
signal_score = number_of_matched_keywords × 20

Example:

1 keyword → score = 20
2 keywords → score = 40
📊 Design Explanation

🔹 Data Ingestion

Data is collected from public sources such as RSS feeds or sample JSON files. This ensures compliance with the constraint of using only free/public data.

🔹 Parsing

Input text is cleaned and normalized to improve keyword matching accuracy.

🔹 Signal Detection

A rule-based approach is used where predefined keywords trigger detection of ATS modernization signals.

🔹 Output Generation

Detected signals are stored in structured JSON format for easy downstream consumption.

⚠️ Assumptions
Presence of keywords indicates potential ATS modernization
Input data contains relevant HR or hiring-related content
Company name is available in input data

❗ Limitations
Keyword-based detection may produce false positives
No NLP or contextual understanding
Limited to predefined keywords and rules

💡 Future Enhancements
Add NLP-based context analysis
Real-time RSS ingestion
Support multiple signal types
Build API using FastAPI

👩‍💻 Author

Anchal Singh
GitHub: https://github.com/Anchal1513

📄 License

This project is developed for assignment and educational purposes.

⭐ Final Note

This project demonstrates:

Modular backend design
Data ingestion from public sources
Rule-based signal extraction
Structured output generation

## 🌐 API (Optional)

Run:
python api.py

Provides endpoint for signal detection.

## 📸 Screenshots

### ▶️ Running the Project
![Run](Screenshot%202026-04-17%20123114.png)

### 📤 Output File
![Output](Screenshot%202026-04-18%20131751.png)
