import csv
import json
import random
import re
from groq import Groq
from dotenv import load_dotenv
import os

# Load API key
load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

MODEL = "llama-3.3-70b-versatile"

# --------------------------------------------------
# LOAD DATASET
# --------------------------------------------------

with open("dataset.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    data = list(reader)

print("Total dataset rows:", len(data))

# Same 50 queries for every prompt
random.seed(42)
test_data = random.sample(data, 50)

# --------------------------------------------------
# PROMPT VARIANTS
# --------------------------------------------------

prompts = {

"Prompt 1 - Basic": """
You are an AI Service Classification Assistant.

Classify the user's service request into the most appropriate
category and subcategory.

Understand Hindi, Hinglish and English.

Return ONLY valid JSON:

{
  "category": "",
  "subcategory": "",
  "confidence": 0,
  "reason": ""
}

User Query:
{query}
""",

"Prompt 2 - Detailed": """
You are an AI service classification system.

Your task is to classify the user's query into exactly ONE
category and ONE subcategory from the available taxonomy.

Important:
- Understand Hindi, Hinglish and English.
- Focus on the actual service requested.
- Ignore unnecessary words.
- Do not invent categories or subcategories.
- Return only JSON.

Available taxonomy:

Home Services:
Electrician, Plumber, Carpenter, Painter,
AC Repair & Service, Appliance Repair,
CCTV Installation, RO / Water Purifier Service

Vehicle Services:
Bike Repair, Car Repair, Tyre Puncture,
Battery Service, Towing Service, Vehicle Washing

Health & Wellness:
Doctor, Physiotherapist, Fitness Trainer

Education:
Home Tutor, Online Tutor

Business Services:
Lawyer, CA, Digital Marketing, Web Developer

Daily Needs:
House Cleaning, Laundry, Pest Control

Agriculture:
Tractor Repair, Irrigation Service, Farm Equipment Repair

Local Professionals:
Photographer, Event Planner, Interior Designer,
Graphic Designer

Return ONLY:

{
  "category": "",
  "subcategory": "",
  "confidence": 0,
  "reason": ""
}

User Query:
{query}
""",

"Prompt 3 - Intent Focused": """
You are a service-intent classification expert.

First understand what service the user actually needs.
Then map that intent to the closest available category
and subcategory.

Rules:
1. Understand Hindi, Hinglish and English.
2. Identify the main service/problem.
3. Ignore filler words such as "please", "nearby", "jaldi",
   "chahiye", "help chahiye".
4. Choose only one category and one subcategory.
5. Never create a new label.
6. If multiple services are mentioned, select the primary
   requested service.
7. Return valid JSON only.

User Query:
{query}

Return:
{
  "category": "",
  "subcategory": "",
  "confidence": 0,
  "reason": ""
}
""",

"Prompt 4 - Rule Based": """
You are a highly accurate service classification assistant.

Classify the query using these rules:

- Electrical/light/fan/wiring -> Electrician
- Water pipe/tap/leakage -> Plumber
- Furniture/wood work -> Carpenter
- Wall/room painting -> Painter
- AC cooling/AC problem -> AC Repair & Service
- Fridge/washing machine/appliance -> Appliance Repair
- CCTV camera installation -> CCTV Installation
- RO/water purifier -> RO / Water Purifier Service
- Bike engine/bike problem -> Bike Repair
- Car problem/car not starting -> Car Repair
- Tyre puncture -> Tyre Puncture
- Vehicle battery -> Battery Service
- Vehicle towing -> Towing Service
- Vehicle washing -> Vehicle Washing
- Doctor/medical consultation -> Doctor
- Physiotherapy -> Physiotherapist
- Gym/personal trainer -> Fitness Trainer
- School/subject tutor -> Home Tutor
- Online classes/tutor -> Online Tutor
- Legal help -> Lawyer
- CA/accounting -> CA
- Marketing/promotion -> Digital Marketing
- Website developer -> Web Developer
- House cleaning -> House Cleaning
- Clothes washing/laundry -> Laundry
- Cockroach/pest problem -> Pest Control
- Tractor problem -> Tractor Repair
- Irrigation -> Irrigation Service
- Farm machinery -> Farm Equipment Repair
- Photography -> Photographer
- Event/party planning -> Event Planner
- Interior design -> Interior Designer
- Graphic design -> Graphic Designer

Understand Hindi, Hinglish and English.

Return ONLY JSON:

{
  "category": "",
  "subcategory": "",
  "confidence": 0,
  "reason": ""
}

Query:
{query}
""",

"Prompt 5 - Strict": """
You are a production-grade service classification model.

TASK:
Map the user query to exactly one category and one
subcategory from the taxonomy.

REQUIREMENTS:
- Hindi/Hinglish/English supported.
- Understand natural language and spelling variations.
- Identify the user's actual intent.
- Do not classify based only on one keyword.
- Do not invent labels.
- Output JSON only.
- No markdown.
- No explanation outside JSON.
- Confidence must be between 0 and 1.

Taxonomy:

Home Services -> Electrician, Plumber, Carpenter, Painter,
AC Repair & Service, Appliance Repair, CCTV Installation,
RO / Water Purifier Service

Vehicle Services -> Bike Repair, Car Repair, Tyre Puncture,
Battery Service, Towing Service, Vehicle Washing

Health & Wellness -> Doctor, Physiotherapist, Fitness Trainer

Education -> Home Tutor, Online Tutor

Business Services -> Lawyer, CA, Digital Marketing, Web Developer

Daily Needs -> House Cleaning, Laundry, Pest Control

Agriculture -> Tractor Repair, Irrigation Service,
Farm Equipment Repair

Local Professionals -> Photographer, Event Planner,
Interior Designer, Graphic Designer

Return exactly:

{
  "category": "",
  "subcategory": "",
  "confidence": 0,
  "reason": ""
}

Query:
{query}
"""
}

# --------------------------------------------------
# CLASSIFICATION FUNCTION
# --------------------------------------------------

def classify(query, prompt_template):

    prompt = prompt_template.replace("{query}", query)

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    output = response.choices[0].message.content.strip()

    # Try JSON directly
    try:
        return json.loads(output)
    except:
        pass

    # Try extracting JSON from response
    match = re.search(r"\{.*\}", output, re.DOTALL)

    if match:
        try:
            return json.loads(match.group())
        except:
            pass

    return None


# --------------------------------------------------
# RUN EVALUATION
# --------------------------------------------------

results = {}

for prompt_name, prompt_template in prompts.items():

    print("\n" + "=" * 60)
    print(prompt_name)
    print("=" * 60)

    correct = 0

    for i, row in enumerate(test_data, 1):

        query = row["query"]
        expected_category = row["category"]
        expected_subcategory = row["subcategory"]

        result = classify(query, prompt_template)

        if result:

            actual_category = result.get("category", "").strip()
            actual_subcategory = result.get("subcategory", "").strip()

            if (
                actual_category.lower() == expected_category.lower()
                and
                actual_subcategory.lower() == expected_subcategory.lower()
            ):
                correct += 1

        if i % 10 == 0:
            print(f"Progress: {i}/50")

    accuracy = (correct / 50) * 100

    results[prompt_name] = accuracy

    print(f"Correct: {correct}/50")
    print(f"Accuracy: {accuracy:.1f}%")


# --------------------------------------------------
# FINAL COMPARISON
# --------------------------------------------------

print("\n")
print("=" * 60)
print("FINAL PROMPT COMPARISON")
print("=" * 60)

for name, accuracy in results.items():
    print(f"{name}: {accuracy:.1f}%")

best_prompt = max(results, key=results.get)

print("\nBEST PROMPT:")
print(best_prompt)
print(f"Accuracy: {results[best_prompt]:.1f}%")