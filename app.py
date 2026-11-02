
with open("sample_resume.txt", "r") as file:
    resume_text = file.read().lower()

with open("job_description.txt", "r") as file:
    job_text = file.read().lower()


all_skills = [
    "python",
    "fastapi",
    "django",
    "aws",
    "postgresql",
    "docker",
    "kubernetes"
]

required_skills = []

for skill in all_skills:
    if skill in job_text:
        required_skills.append(skill)


matched_skills = []
missing_skills = []

for skill in required_skills:
    if skill in resume_text:
        matched_skills.append(skill)
    else:
        missing_skills.append(skill)

total_skills = len(required_skills)
matched_count = len(matched_skills)
match_score = (matched_count / total_skills) * 100

print("Matched Skills:", matched_skills)
print("Missing Skills:", missing_skills)
print("Resume Match Score:", round(match_score, 2), "%")
