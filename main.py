from groq import Groq
from dotenv import load_dotenv
import os

# Load API key
load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# Take user input
query = input("Enter Service Query: ")

prompt = f"""
You are an AI Service Classification Assistant.

Your job is to classify the user's service request into the correct category and subcategory.

Available Categories:

1. Home Services
- Electrician
- Plumber
- Carpenter
- Painter
- AC Repair & Service
- Appliance Repair
- CCTV Installation
- RO / Water Purifier Service

2. Vehicle Services
- Bike Repair
- Car Repair
- Tyre Puncture
- Battery Service
- Towing Service
- Vehicle Washing

3. Health & Wellness
- Doctor
- Physiotherapist
- Fitness Trainer

4. Education
- Home Tutor
- Online Tutor
- Coaching Institute

5. Business Services
- CA
- Lawyer
- Digital Marketing
- Graphic Designer
- Web Developer

6. Daily Needs
- House Cleaning
- Laundry
- Pest Control

7. Agriculture
- Tractor Repair
- Irrigation Service
- Farm Equipment Repair

8. Local Professionals
- Photographer
- Event Planner
- Interior Designer

Rules:
1. Understand Hindi, Hinglish and English.
2. Return ONLY JSON.
3. Choose the most appropriate category and subcategory.
4. Confidence must be between 0 and 1.
5. If a car has stopped/broken down and the user wants it repaired, classify as "Car Repair".
6. Use "Towing Service" only when the user explicitly asks to tow, transport, or move the broken vehicle.

Output Format:

{{
  "query": "",
  "category": "",
  "subcategory": "",
  "confidence": "",
  "reason": ""
}}

User Query:
{query}
"""

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ],
    temperature=0
)

print("\n========== CLASSIFICATION RESULT ==========\n")
print(response.choices[0].message.content)