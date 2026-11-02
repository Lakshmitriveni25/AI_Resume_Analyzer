# AI Resume Analyzer

A beginner-friendly Python project that compares a resume with a job description, identifies matching and missing skills, and calculates a resume match score.

## Features

- Reads resume and job description from text files.
- Identifies required skills from the job description.
- Finds matching skills in the resume.
- Identifies missing skills.
- Calculates a resume match percentage.

## Technologies Used

- Python 3
- File Handling
- Lists and Loops
- Conditional Statements
- String Operations

## Project Structure

```text
AI_Resume_Analyzer/
├── app.py
├── sample_resume.txt
├── job_description.txt
├── .gitignore
└── README.md
```

## How to Run

1. Clone this repository:

   ```bash
   git clone https://github.com/Lakshmitriveni25/AI_Resume_Analyzer.git
   ```

2. Open the project folder:

   ```bash
   cd AI_Resume_Analyzer
   ```

3. Run the application:

   ```bash
   python app.py
   ```

## Sample Output

```text
Matched Skills: ['python', 'fastapi', 'aws', 'postgresql', 'docker']
Missing Skills: ['django', 'kubernetes']
Resume Match Score: 71.43 %
```

## Future Improvements

- Support more technical skills.
- Improve skill matching accuracy.
- Add PDF and DOCX resume support.
- Build a web interface using FastAPI.
- Integrate AI-based resume analysis.

## Author

Lakshmitriveni25