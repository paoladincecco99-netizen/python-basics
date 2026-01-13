# Storing and accessing nested dictionary data for a development team – exercise

dev_team = {
    "dev1": {
        "name": "Mark",
        "role": "Backend Developer",
        "languages": ["Python", "Go", "SQL"]
    },
    "dev2": {
        "name": "Sara",
        "role": "Frontend Developer",
        "languages": ["JavaScript", "React", "CSS"]
    },
    "dev3": {
        "name": "Luca",
        "role": "DevOps Engineer",
        "languages": ["Docker", "Kubernetes", "Bash"]
    }
}

for dev_id, info in dev_team.items():
    print(f"Developer ID: {dev_id}")
    print(f"Name: {info['name']} - Role: {info['role']}")
    print("Known Languages/Tools:")
    for lang in info["languages"]:
        print(f"- {lang}")

# Filtering data based on a condition
filter_language = "Python"
print(f"Developers who know {filter_language}")
for dev_id, info in dev_team.items():
    if filter_language in info["languages"]:
        print(f"- {info['name']} ({info['role']})")

# Adding a new skill dynamically
new_skill = "TypeScript"
target_name = "Sara"
for dev_id, info in dev_team.items():
    if info["name"] == target_name:
        info["languages"].append(new_skill)
        print(f"Added {new_skill} to {target_name}'s skills!")


