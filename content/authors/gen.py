import os

# List of students with their graduation years and nationalities
students = [
    {"name": "Zuyan Chen", "graduation_year": 2018, "nationality": "China"},
    {"name": "Jinsong Li", "graduation_year": 2018, "nationality": "China"},
    {"name": "Ronghua Peng", "graduation_year": 2018, "nationality": "China"},
    {"name": "Ling Chenrong", "graduation_year": 2018, "nationality": "China"},
    {"name": "K.M.S. Reza", "graduation_year": 2022, "nationality": "Bangladesh"},
    {"name": "S. Khaya Sambo", "graduation_year": 2022, "nationality": "South Africa"},
    {"name": "Sazedul Haque", "graduation_year": 2022, "nationality": "Bangladesh"},
    {"name": "Md Nafiz", "graduation_year": 2023, "nationality": "Bangladesh"},
]

# Template for the index.md file
template = """---
title: {first_name} {last_name}
role: Alumni
bio: {bio}
interests:
{interests}
social:
  - icon: envelope
    icon_pack: fas
    link: ""
organizations:
  - name: Jiangxi University of Science and Technology
    url: ""
education:
  courses:
    - course: Undergraduate in Computer Science and Technology
      institution: Jiangxi University of Science and Technology
      year: {year}
superuser: false
user_groups:
  - Alumni
last_name: {last_name}
highlight_name: false
first_name: {first_name}
email: ""
---
{first_name} {last_name} was a student at Jiangxi University of Science and Technology (JXUST). They completed their Undergraduate in Computer Science and Technology in the year {year}.
"""

# Bios and interests based on nationality
bios_interests = {
    "China": {
        "bio": "An alumnus from China with a strong foundation in computer science and technology.",
        "interests": [
            "Artificial Intelligence",
            "Machine Learning",
            "Software Development"
        ]
    },
    "Bangladesh": {
        "bio": "An alumnus from Bangladesh with a passion for technology and innovation.",
        "interests": [
            "Data Analysis",
            "Cybersecurity",
            "Web Development"
        ]
    },
    "South Africa": {
        "bio": "An alumnus from South Africa dedicated to advancing technological solutions.",
        "interests": [
            "Network Engineering",
            "System Administration",
            "Cloud Computing"
        ]
    }
}

# Create folders and files
base_path = "students"
os.makedirs(base_path, exist_ok=True)

for student in students:
    full_name = student["name"].split()
    first_name = full_name[0]
    last_name = " ".join(full_name[1:])
    folder_name = student["name"].replace(" ", "_")
    student_path = os.path.join(base_path, folder_name)
    os.makedirs(student_path, exist_ok=True)

    # Get bio and interests based on nationality
    bio_info = bios_interests.get(student["nationality"], {})
    bio = bio_info.get("bio", "An alumnus with a background in computer science.")
    interests_list = bio_info.get("interests", ["Technology", "Innovation"])
    interests = "\n".join([f"  - {interest}" for interest in interests_list])

    # Write the tailored index.md file
    content = template.format(
        first_name=first_name,
        last_name=last_name,
        year=student["graduation_year"],
        bio=bio,
        interests=interests
    )
    with open(os.path.join(student_path, "index.md"), "w") as file:
        file.write(content)

print(f"Folders and index.md files have been created in the '{base_path}' directory.")
