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
