import csv
import random

# ---------------------------------------
# SERVICE TAXONOMY
# ---------------------------------------

taxonomy = {
    "Home Services": {
        "Electrician": [
            "electrician chahiye",
            "ghar ki light kharab hai",
            "switch kaam nahi kar raha",
            "bijli ka problem hai",
            "fan repair karwana hai"
        ],
        "Plumber": [
            "plumber chahiye",
            "nal leak kar raha hai",
            "pipe leak ho raha hai",
            "pani ki pipe repair karwani hai"
        ],
        "Carpenter": [
            "carpenter chahiye",
            "darwaza repair karwana hai",
            "bed repair karwana hai",
            "furniture repair karwana hai"
        ],
        "Painter": [
            "painter chahiye",
            "ghar paint karwana hai",
            "room paint karwana hai",
            "wall paint karwani hai"
        ],
        "AC Repair & Service": [
            "AC repair karwana hai",
            "AC thanda nahi kar raha",
            "AC service chahiye",
            "air conditioner kharab hai"
        ],
        "Appliance Repair": [
            "fridge repair karwana hai",
            "washing machine kharab hai",
            "fridge thanda nahi kar raha",
            "home appliance repair chahiye"
        ],
        "CCTV Installation": [
            "CCTV camera lagwana hai",
            "security camera install karwana hai",
            "ghar me CCTV lagana hai"
        ],
        "RO / Water Purifier Service": [
            "RO service chahiye",
            "water purifier repair karwana hai",
            "RO ka pani nahi aa raha",
            "RO kharab hai"
        ]
    },

    "Vehicle Services": {
        "Bike Repair": [
            "bike repair karwani hai",
            "bike start nahi ho rahi",
            "bike engine me problem hai"
        ],
        "Car Repair": [
            "car repair karwani hai",
            "car start nahi ho rahi",
            "car raste me band ho gayi",
            "car mechanic chahiye"
        ],
        "Tyre Puncture": [
            "bike tyre puncture hai",
            "car tyre puncture ho gaya",
            "puncture wala chahiye"
        ],
        "Battery Service": [
            "car battery dead hai",
            "bike battery kharab hai",
            "battery service chahiye"
        ],
        "Towing Service": [
            "car tow karwani hai",
            "towing truck chahiye",
            "gaadi ko tow karke le jana hai"
        ],
        "Vehicle Washing": [
            "car wash karwani hai",
            "bike wash karwani hai",
            "vehicle cleaning chahiye"
        ]
    },

    "Health & Wellness": {
        "Doctor": [
            "doctor chahiye",
            "doctor appointment chahiye",
            "doctor se consult karna hai"
        ],
        "Physiotherapist": [
            "physiotherapist chahiye",
            "physiotherapy karwani hai",
            "back pain ke liye physiotherapist chahiye"
        ],
        "Fitness Trainer": [
            "fitness trainer chahiye",
            "personal trainer chahiye",
            "gym trainer chahiye"
        ]
    },

    "Education": {
        "Home Tutor": [
            "home tutor chahiye",
            "ghar par teacher chahiye",
            "bachche ke liye tutor chahiye"
        ],
        "Online Tutor": [
            "online tutor chahiye",
            "online teacher chahiye",
            "online classes chahiye"
        ],
        "Coaching Institute": [
            "coaching institute chahiye",
            "coaching join karni hai",
            "exam coaching chahiye"
        ]
    },

    "Business Services": {
        "CA": [
            "CA chahiye",
            "chartered accountant chahiye",
            "tax filing ke liye CA chahiye"
        ],
        "Lawyer": [
            "lawyer chahiye",
            "legal help chahiye",
            "advocate chahiye"
        ],
        "Digital Marketing": [
            "digital marketing service chahiye",
            "business promotion karwana hai",
            "social media marketing chahiye"
        ],
        "Graphic Designer": [
            "graphic designer chahiye",
            "logo design karwana hai",
            "poster design karwana hai"
        ],
        "Web Developer": [
            "web developer chahiye",
            "website banwani hai",
            "business website chahiye"
        ]
    },

    "Daily Needs": {
        "House Cleaning": [
            "ghar ki safai karwani hai",
            "house cleaning chahiye",
            "home cleaning service chahiye"
        ],
        "Laundry": [
            "laundry service chahiye",
            "kapde laundry ke liye dene hain",
            "clothes washing service chahiye"
        ],
        "Pest Control": [
            "pest control chahiye",
            "ghar me cockroach bahut hain",
            "termite treatment chahiye"
        ]
    },

    "Agriculture": {
        "Tractor Repair": [
            "tractor repair karwana hai",
            "tractor kharab ho gaya",
            "tractor mechanic chahiye"
        ],
        "Irrigation Service": [
            "irrigation service chahiye",
            "khet me irrigation karwani hai",
            "pani ki irrigation system chahiye"
        ],
        "Farm Equipment Repair": [
            "farm machine repair karwani hai",
            "agriculture machine kharab hai",
            "farm equipment mechanic chahiye"
        ]
    },

    "Local Professionals": {
        "Photographer": [
            "photographer chahiye",
            "wedding photographer chahiye",
            "I need a photographer"
        ],
        "Event Planner": [
            "event planner chahiye",
            "birthday party planner chahiye",
            "function organise karwana hai"
        ],
        "Interior Designer": [
            "interior designer chahiye",
            "ghar ka interior design karwana hai",
            "room interior karwana hai"
        ]
    }
}


# ---------------------------------------
# QUERY VARIATIONS
# ---------------------------------------

prefixes = [
    "",
    "mujhe ",
    "bhai ",
    "mere ghar me ",
    "urgent ",
    "please ",
    "nearby ",
    "mere area me ",
    "jaldi ",
    "aaj "
]

suffixes = [
    "",
    " chahiye",
    " please",
    " urgently",
    " nearby",
    " mere area me",
    " aaj",
    " jaldi",
    " koi hai kya",
    " help chahiye"
]


# ---------------------------------------
# GENERATE DATASET
# ---------------------------------------

rows = []
seen = set()

while len(rows) < 3500:

    category = random.choice(list(taxonomy.keys()))

    subcategory = random.choice(
        list(taxonomy[category].keys())
    )

    base_query = random.choice(
        taxonomy[category][subcategory]
    )

    prefix = random.choice(prefixes)
    suffix = random.choice(suffixes)

    query = (prefix + base_query + suffix).strip()

    # Prevent exact duplicates
    if query not in seen:

        seen.add(query)

        rows.append([
            query,
            category,
            subcategory
        ])


# ---------------------------------------
# SHUFFLE DATA
# ---------------------------------------

random.shuffle(rows)


# ---------------------------------------
# SAVE CSV
# ---------------------------------------

with open(
    "dataset.csv",
    "w",
    newline="",
    encoding="utf-8"
) as file:

    writer = csv.writer(file)

    writer.writerow([
        "query",
        "category",
        "subcategory"
    ])

    writer.writerows(rows)


print("--------------------------------")
print("DATASET GENERATED SUCCESSFULLY")
print("Total Queries:", len(rows))
print("File: dataset.csv")
print("--------------------------------")