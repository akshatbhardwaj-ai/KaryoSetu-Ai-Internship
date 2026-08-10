# Karyosetu AI Service Classification System

An LLM-powered service classification system developed as part of the Karyosetu AI Engineering Internship.

The system accepts natural-language service requests in **Hindi, Hinglish, and English** and classifies them into the appropriate **service category and subcategory** using an LLM-based classification pipeline.

---

## Overview

The project focuses on building a reliable service-query classification workflow using:

- LLM-based text classification
- Service taxonomy
- Prompt engineering
- Multilingual query handling
- Structured JSON outputs
- Labelled dataset generation
- Automated evaluation
- Prompt performance comparison

The system uses the **Groq API** with **Llama 3.3 70B Versatile**.

---

## Key Features

- Hindi, Hinglish, and English query support
- Service category and subcategory classification
- LLM-powered classification
- Structured JSON responses
- Confidence scoring
- Classification reasoning
- 3,500 labelled service queries
- Duplicate-query validation
- Automated evaluation
- Multiple prompt strategies
- Prompt performance benchmarking

---

## System Workflow

```text
User Query
    |
    v
Service Taxonomy
    |
    v
Prompt Template
    |
    v
Groq API
    |
    v
Llama 3.3 70B
    |
    v
Structured JSON Response
    |
    v
Category + Subcategory
    |
    v
Evaluation Pipeline
```

---

## Service Taxonomy

The current classification system covers multiple service domains.

### Home Services
- Electrician
- Plumber
- Carpenter
- Painter
- AC Repair & Service
- Appliance Repair
- CCTV Installation
- RO / Water Purifier Service

### Vehicle Services
- Bike Repair
- Car Repair
- Tyre Puncture
- Battery Service
- Towing Service
- Vehicle Washing

### Health & Wellness
- Doctor
- Physiotherapist
- Fitness Trainer

### Education
- Home Tutor
- Online Tutor
- Coaching Institute

### Business Services
- CA
- Lawyer
- Digital Marketing
- Graphic Designer
- Web Developer

### Daily Needs
- House Cleaning
- Laundry
- Pest Control

### Agriculture
- Tractor Repair
- Irrigation Service
- Farm Equipment Repair

### Local Professionals
- Photographer
- Event Planner
- Interior Designer

---

## Dataset

A labelled CSV dataset was generated for service-query classification.

| Metric | Value |
|---|---:|
| Total Queries | 3,500 |
| Unique Queries | 3,500 |
| Duplicate Queries | 0 |
| Format | CSV |
| Query Languages | Hindi / Hinglish / English |

### Example Queries

```text
meri car start nahi ho rahi
ghar ki light baar baar trip ho rahi hai
mujhe ghar ke liye tutor chahiye
nearby RO ka pani nahi aa raha
bike ka tyre puncture ho gaya
```

---

## Classification Output

The classifier returns a structured JSON response containing the query, category, subcategory, confidence, and reasoning.

### Example

```json
{
  "query": "bike ka tyre puncture ho gaya",
  "category": "Vehicle Services",
  "subcategory": "Tyre Puncture",
  "confidence": "0.9",
  "reason": "The user explicitly mentions a bike tyre puncture, which corresponds to the Tyre Puncture service."
}
```

---

## Prompt Engineering

Five prompt configurations were evaluated:

1. Basic Prompt
2. Detailed Prompt
3. Intent-Focused Prompt
4. Rule-Based Prompt
5. Strict Structured-Output Prompt

### Current 50-Query Validation

| Prompt | Accuracy |
|---|---:|
| Basic | 0% |
| Detailed | 100% |
| Intent-Focused | 2% |
| Rule-Based | 14% |
| Strict | 100% |

The **Detailed** and **Strict** prompts achieved the highest accuracy in the current validation run.

> These results represent the current validation experiment and should not be interpreted as production-level accuracy.

---

## Evaluation Pipeline

1. Load labelled queries.
2. Send queries to the classification model.
3. Parse the structured JSON response.
4. Extract predicted category and subcategory.
5. Compare predictions with expected labels.
6. Calculate classification accuracy.
7. Identify classification failures.
8. Compare different prompt configurations.

---

## Project Structure

```text
Karyosetu-AI-Internship/
|
├── main.py
├── generate_dataset.py
├── dataset.csv
├── test_classifier.py
├── evaluate_classifier.py
├── evaluate_50.py
├── evaluate_prompts.py
├── main_backup.py
├── README.md
└── .env
```

| File | Description |
|---|---|
| `main.py` | Main interactive classification application |
| `generate_dataset.py` | Generates the labelled service-query dataset |
| `dataset.csv` | Generated labelled dataset |
| `test_classifier.py` | Tests classification with sample queries |
| `evaluate_classifier.py` | Evaluates classifier performance |
| `evaluate_50.py` | Runs the 50-query evaluation |
| `evaluate_prompts.py` | Compares different prompt strategies |
| `main_backup.py` | Backup version of the main classifier |
| `README.md` | Project documentation |

---

## Technology Stack

- Python
- Groq API
- Llama 3.3 70B Versatile
- python-dotenv
- CSV
- JSON
- Prompt Engineering
- LLM-based Text Classification

---

## Setup

### 1. Clone the Repository

```bash
git clone YOUR_REPOSITORY_URL
cd Karyosetu-AI-Internship
```

### 2. Create a Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install groq python-dotenv
```

### 4. Configure the API Key

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

**Never commit the `.env` file or expose the API key publicly.**

Add to `.gitignore`:

```gitignore
.env
.venv/
__pycache__/
```

---

## Running the Classifier

```bash
python3 main.py
```

Example:

```text
Enter Service Query: meri car start nahi ho rahi
```

The system returns the predicted category, subcategory, confidence, and reasoning.

---

## Running Evaluation

### Classifier Evaluation

```bash
python3 evaluate_classifier.py
```

### 50-Query Evaluation

```bash
python3 evaluate_50.py
```

### Prompt Comparison

```bash
python3 evaluate_prompts.py
```

---

## Dataset Generation

```bash
python3 generate_dataset.py
```

The generated dataset is saved as `dataset.csv`.

---

## Quality Checks

The project includes checks for:

- Duplicate queries
- Category distribution
- Subcategory distribution
- Query diversity
- Hindi/Hinglish coverage
- English query coverage
- Structured JSON output
- Classification accuracy
- Prompt performance

The current dataset contains **3,500 unique queries with 0 duplicates**.

---

## Key Findings

The experiments demonstrate that prompt design can significantly affect LLM-based classification performance.

In the current validation experiment:

- The Basic prompt performed poorly.
- Detailed classification instructions improved performance.
- Strict output instructions produced strong results.
- Different prompt configurations can be evaluated systematically using the evaluation pipeline.

---

## Future Improvements

- Expand the evaluation dataset
- Add more rural and regional-language queries
- Add ambiguous service requests
- Improve edge-case classification
- Measure model latency
- Track token usage and API cost
- Compare multiple LLM models
- Add low-confidence fallback handling
- Add automated unit tests
- Improve dataset diversity
- Add detailed error analysis
- Add production monitoring

---

## Project Status

### Completed

- LLM-based service classification system
- Groq API integration
- Llama-based classification
- Service taxonomy implementation
- Hindi/Hinglish/English query support
- 3,500-query labelled dataset
- Duplicate validation
- Structured JSON classification output
- Automated evaluation scripts
- Multiple prompt configurations
- Prompt performance comparison
- Interactive classifier testing
- Project documentation

### Future Work

- Larger independent benchmark dataset
- Latency and cost benchmarking
- Additional edge-case testing
- Production monitoring
- Further dataset expansion

---

## Internship Context

This project was developed as part of the **Karyosetu AI Engineering Internship**.

The project involved service taxonomy understanding, labelled dataset generation, LLM-based classification, prompt engineering, automated evaluation, and performance analysis.

---

## Author

**Akshat Bhardwaj**

AI Engineering Intern

---

## Disclaimer

The accuracy values reported in this README are based on the project's current validation experiments. They should not be considered production-level performance metrics without further testing on a larger, independently held-out evaluation dataset.
