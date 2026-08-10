import subprocess
import json
import re

tests = [
    # Home Services
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

    # More Home Services
    ("kitchen ka pipe leak ho raha hai", "Home Services", "Plumber"),
    ("I need an electrician for my house", "Home Services", "Electrician"),
    ("bed repair karwana hai", "Home Services", "Carpenter"),
    ("ghar ki walls paint karwani hain", "Home Services", "Painter"),
    ("washing machine repair karwani hai", "Home Services", "Appliance Repair"),
    ("water purifier service chahiye", "Home Services", "RO / Water Purifier Service"),

    # Vehicle Services
    ("bike engine se ajeeb awaaz aa rahi hai", "Vehicle Services", "Bike Repair"),
    ("my car needs repair", "Vehicle Services", "Car Repair"),
    ("car ko tow karwana hai", "Vehicle Services", "Towing Service"),
    ("gaadi ko towing truck chahiye", "Vehicle Services", "Towing Service"),
    ("car battery dead hai", "Vehicle Services", "Battery Service"),
    ("bike tyre me puncture hai", "Vehicle Services", "Tyre Puncture"),
    ("car wash karwani hai", "Vehicle Services", "Vehicle Washing"),

    # Health & Wellness
    ("doctor se appointment chahiye", "Health & Wellness", "Doctor"),
    ("back pain ke liye physiotherapist chahiye", "Health & Wellness", "Physiotherapist"),
    ("personal fitness trainer chahiye", "Health & Wellness", "Fitness Trainer"),
    ("I need a doctor", "Health & Wellness", "Doctor"),

    # Education
    ("ghar par maths teacher chahiye", "Education", "Home Tutor"),
    ("online English tutor chahiye", "Education", "Online Tutor"),
    ("coaching institute join karna hai", "Education", "Coaching Institute"),
    ("I need an online tutor", "Education", "Online Tutor"),

    # Business Services
    ("CA chahiye tax ke liye", "Business Services", "CA"),
    ("legal advice ke liye lawyer chahiye", "Business Services", "Lawyer"),
    ("business ki digital marketing karwani hai", "Business Services", "Digital Marketing"),
    ("logo banwane ke liye graphic designer chahiye", "Business Services", "Graphic Designer"),
    ("website banwani hai", "Business Services", "Web Developer"),

    # Daily Needs
    ("ghar ki safai karwani hai", "Daily Needs", "House Cleaning"),
    ("kapde laundry ke liye dene hain", "Daily Needs", "Laundry"),
    ("ghar me cockroach bahut hain pest control chahiye", "Daily Needs", "Pest Control"),
    ("I need house cleaning service", "Daily Needs", "House Cleaning"),

    # Agriculture
    ("tractor repair karwana hai", "Agriculture", "Tractor Repair"),
    ("khet ke liye irrigation service chahiye", "Agriculture", "Irrigation Service"),
    ("farm machine repair karwani hai", "Agriculture", "Farm Equipment Repair"),
    ("tractor kharab ho gaya hai", "Agriculture", "Tractor Repair"),

    # Local Professionals
    ("wedding ke liye photographer chahiye", "Local Professionals", "Photographer"),
    ("birthday party ke liye event planner chahiye", "Local Professionals", "Event Planner"),
    ("ghar ka interior design karwana hai", "Local Professionals", "Interior Designer"),
    ("I need a photographer", "Local Professionals", "Photographer"),

    # Extra mixed-language tests
    ("meri car start nahi ho rahi mechanic chahiye", "Vehicle Services", "Car Repair"),
    ("mujhe ghar ke liye plumber chahiye", "Home Services", "Plumber")
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