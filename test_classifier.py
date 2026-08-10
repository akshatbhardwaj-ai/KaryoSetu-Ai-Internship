import subprocess

test_queries = [
    "meri bike start nahi ho rahi",
    "ghar ka nal leak kar raha hai",
    "AC thanda nahi kar raha",
    "car raste me band ho gayi",
    "RO ka pani nahi aa raha",
    "room paint karwana hai",
    "CCTV camera lagwana hai",
    "fridge thanda nahi kar raha",
    "bike ka tyre puncture ho gaya",
    "ghar ki light baar baar trip ho rahi hai"
]

for query in test_queries:
    print("\nTEST QUERY:", query)
    print("-" * 50)

    result = subprocess.run(
        ["python3", "main.py"],
        input=query + "\n",
        text=True,
        capture_output=True
    )

    print(result.stdout)