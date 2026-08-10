# Karyosetu AI Service Classification System

## Overview

This project develops an LLM-powered service classification system for Karyosetu.

The system accepts natural-language service requests in Hindi, Hinglish and English and classifies them into the appropriate service category and subcategory.

The project focuses on building a reliable evaluation pipeline, creating a labelled query dataset, and comparing different prompt strategies for classification performance.

---

## Project Objectives

- Build an LLM-based service classification system.
- Support Hindi, Hinglish and English user queries.
- Create a large labelled service-query dataset.
- Evaluate classification performance using automated testing.
- Compare multiple prompt-engineering strategies.
- Identify an effective prompt configuration.
- Create a reproducible evaluation workflow.

---

## Technology Stack

- Python
- Groq API
- Llama 3.3 70B Versatile
- Python dotenv
- CSV-based datasets
- JSON structured outputs
- Prompt Engineering
- LLM-based Text Classification

---

## System Workflow

```text
User Query
    |
    v
Prompt + Service Taxonomy
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

===

## Service Taxonomy
The current dataset covers multiple service domains including:
Home Services
Electrician
Plumber
Carpenter
Painter
AC Repair & Service
Appliance Repair
CCTV Installation
RO / Water Purifier Service
Vehicle Services
Bike Repair
Car Repair
Tyre Puncture
Battery Service
Towing Service
Vehicle Washing
Health & Wellness
Doctor
Physiotherapist
Fitness Trainer
Education
Home Tutor
Online Tutor
Coaching Institute
Business Services
CA
Lawyer
Digital Marketing
Graphic Designer
Web Developer
Daily Needs
House Cleaning
Laundry
Pest Control
Agriculture
Tractor Repair
Irrigation Service
Farm Equipment Repair
Local Professionals
Photographer
Event Planner
Interior Designer
