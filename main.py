
import json
import os

FILE_NAME = "feedback.json"

# Load saved feedback
if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r") as file:
        knowledge = json.load(file)
else:
    knowledge = {}

print("=== Feedback Learning Assistant ===")

request = input("What do you want to learn? ").strip().lower()

# Step 1 and 2: Request and response
if request in knowledge:
    response = knowledge[request]
    print("\nImproved response:", response)
else:
    response = "Start with the basics and practice every day."
    print("\nAgent response:", response)

# Step 3: Collect feedback
feedback = input(
    "\nWas this response useful? (yes/no): "
).strip().lower()

# Step 4 and 5: Save improvements
if feedback == "no":
    suggestion = input("Enter a better response: ").strip()

    if suggestion:
        knowledge[request] = suggestion

        with open(FILE_NAME, "w") as file:
            json.dump(knowledge, file, indent=4)

        print("\nThank you! Your improvement was saved.")

elif feedback == "yes":
    print("\nThank you for your feedback!")

else:
    print("\nPlease enter yes or no next time.")

print("Project completed!")
