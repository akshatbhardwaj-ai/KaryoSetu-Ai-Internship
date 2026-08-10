import subprocess
import json
import re

tests = [
    ("meri bike start nahi ho rahi", "Vehicle Services", "Bike Repair"),
    ("ghar ka naal leak kar raha hai", "Home Services", "Plumber"),
    ("AC thanda nahi kar raha", "Home Services", "AC Repair & Service"),
    ("car raste me band ho gayi", "Vehicle Services", "Car Repair"),
    ("RO ka pani nahi aa raha", "Home Services", "RO / Water Purifier Service"),
    ("room paint karwana hai", "Home Services", "Painter"),
    ("CCTV camera lagwana hai", "Home Services", "CCTV Installation"),
    ("fridge thanda nahi kar raha", "Home Services", "Appliance Repair"),
    ("bike ka tyre puncture ho gaya", "Vehicle Services", "Tyre Puncture"),
    ("ghar ki light baar baar trip ho rahi hai", "Home Services", "Electrician"),
]

correct = 0

for query, expected_category, expected_subcategory in tests:
    result = subprocess.run(
        ["python3", "main.py"],
        input=query + "\n",
        text=True,
        capture_output=True
    )

    output = result.stdout

    try:
        match = re.search(r'\{.*\}', output, re.DOTALL)

        if not match:
            raise ValueError("JSON not found")

        data = json.loads(match.group())

        actual_category = data.get("category", "")
        actual_subcategory = data.get("subcategory", "")

        passed = (
            actual_category == expected_category
            and actual_subcategory == expected_subcategory
        )

        if passed:
            correct += 1
            status = "PASS"
        else:
            status = "FAIL"

        print("\n" + "=" * 60)
        print("QUERY:", query)
        print("EXPECTED:", expected_category, "->", expected_subcategory)
        print("ACTUAL:", actual_category, "->", actual_subcategory)
        print("RESULT:", status)

    except Exception as e:
        print("\nERROR:", query)
        print("Details:", e)

accuracy = (correct / len(tests)) * 100

print("\n" + "=" * 60)
print("FINAL EVALUATION")
print("Correct:", correct, "/", len(tests))
print("Accuracy:", round(accuracy, 2), "%")
print("=" * 60)