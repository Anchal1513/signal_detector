📡 System Level Specification (SLS)
Signal Detection System — ATS / HR Tech Modernization Detector
📌 1. Introduction
1.1 Purpose

This document defines the System Level Specification (SLS) for the Signal Detection System. It describes the internal architecture, modules, workflow, and data processing logic used to detect recruitment technology modernization signals.

1.2 Scope

The system analyzes semi-structured data (JSON/RSS-like input) to detect signals such as ATS migration, HR transformation, and recruitment automation using rule-based keyword matching.

🏗️ 2. System Architecture

The system follows a modular Python-based architecture:

2.1 Input Layer
Reads input data from:
data/sample_input.json
RSS feeds (optional)
Input includes:
Company name
Text content
Source URL

2.2 Processing Layer
Implemented using Python
Core logic located in:
signals/ats_detector.py
utils/ (helper functions)
Responsibilities:
Text normalization
Keyword matching
Tool detection
Stage detection
Signal scoring

2.3 Output Layer
Stores results in:
output/signals.json
Output format: structured JSON containing detected signals

🧩 3. Module Design

3.1 Data Ingestion Module
Reads input from JSON file
Extracts required fields (company, text, URL)

3.2 Preprocessing Module
Cleans and normalizes text
Converts text to lowercase
Removes unnecessary characters

3.3 Signal Detection Module
Located in ats_detector.py
Uses predefined keyword list:
Workday
SuccessFactors
ATS migration
HR transformation
Recruitment automation
Matches keywords in input text

3.4 Tool Detection Module
Identifies HR tools mentioned in text
Example:
Workday
SAP SuccessFactors

3.5 Stage Detection Module
Determines stage based on keywords:
“migration” → migration stage
“upgrade” → upgrade stage
default → unknown

3.6 Scoring Module

Calculates signal strength:

Formula: signal_score = number_of_matched_keywords × 20

3.7 Output Module
Formats results into JSON
Stores detected signals in output file

🔄 4. System Workflow (Data Flow)
Input JSON is loaded from data/
Data is passed to preprocessing module
Cleaned text is sent to detection module
Keywords are matched against predefined list
Tools and stage are identified
Signal score is calculated
Result is formatted into JSON
Output is saved in output/signals.json

🗄️ 5. Data Design

Input Data Structure
{
  "company": "Company Name",
  "text": "Input text containing hiring info",
  "url": "Source URL"
}

Output Data Structure
{
  "company": "Company Name",
  "signal_type": "ats_modernization",
  "source_url": "URL",
  "matched_keywords": [],
  "tools_detected": [],
  "signal_score": 0,
  "detected_at": "timestamp",
  "stage": "migration/upgrade/unknown",
  "reason": "Explanation of detection"
}

🌐 6. Component Interaction
Example Flow:
User runs main.py
System reads input data
Detection logic processes text
Signals are generated
Output is saved as JSON

🔐 7. Security Considerations
Input validation for JSON data
Safe file handling
No external API dependency (reduces security risk)

⚙️ 8. Deployment Environment
Language: Python
Execution: Command-line (python main.py)
Platform: Windows/Linux
Dependencies: Defined in requirements.txt

⚠️ 9. Limitations
Rule-based detection (no NLP)
May generate false positives
Limited to predefined keywords
No real-time data streaming

🚀 10. Future Enhancements
NLP-based detection (using ML models)
Real-time RSS feed integration
Web dashboard for visualization
Advanced scoring algorithm
Database integration

📌 11. Conclusion

This System Level Specification provides a structured overview of the Signal Detection System, including its modular architecture, workflow, and detection logic. It ensures clarity, scalability, and maintainability of the system.
