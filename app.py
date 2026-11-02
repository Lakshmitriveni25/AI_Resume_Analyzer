def read_resume():
    with open("sample_resume.txt", "r") as file:
        resume_text = file.read().lower()

    return resume_text


resume_text = read_resume()    

def read_job_description():
    with open("job_description.txt", "r") as file:
        job_text = file.read().lower()

    return job_text


job_text = read_job_description()


all_skills = [
    "python",
    "fastapi",
    "django",
    "aws",
    "postgresql",
    "docker",
    "kubernetes"
]

def extract_required_skills(job_text):
    required_skills = []

    for skill in all_skills:
        if skill in job_text:
            required_skills.append(skill)

    return required_skills


required_skills = extract_required_skills(job_text)
resume_words = resume_text.replace(",", " ").split()


def match_skills(resume_words, required_skills):
    matched_skills = []
    missing_skills = []

    for skill in required_skills:
        if skill in resume_words:
            matched_skills.append(skill)
        else:
            missing_skills.append(skill)

    return matched_skills, missing_skills


matched_skills, missing_skills = match_skills(resume_words, required_skills)      

def calculate_match_score(matched_skills, required_skills):
    total_skills = len(required_skills)
    matched_count = len(matched_skills)

    if total_skills > 0:
        match_score = (matched_count / total_skills) * 100
    else:
        match_score = 0

    return round(match_score, 2)


match_score = calculate_match_score(matched_skills, required_skills)    

print("Matched Skills:", matched_skills)
print("Missing Skills:", missing_skills)
print("Resume Match Score:", match_score, "%")
