# AI Interview Coach

print("================================")
print("       AI INTERVIEW COACH")
print("================================")

skills = {
    "python": "Python",
    "machine learning": "Machine Learning",
    "artificial intelligence": "Artificial Intelligence",
    "data science": "Data Science",
    "data analysis": "Data Analysis",
    "sql": "SQL",
    "tensorflow": "TensorFlow",
    "communication": "Communication",
    "leadership": "Leadership",
    "problem solving": "Problem Solving",
    "creativity": "Creativity",
    "teamwork": "Teamwork"
}

answer = input("\nTell me about yourself: ").lower()

found = []

for keyword, skill in skills.items():
    if keyword in answer:
        found.append(skill)

print("\n================================")
print("        INTERVIEW FEEDBACK")
print("================================")

if found:
    print("\nSkills detected:")
    
    for skill in found:
        print("✓", skill)

    print("\nGood! Your answer mentions useful skills.")

else:
    print("\nNo specific skills detected.")
    print("Try mentioning skills such as:")
    print("Python, Machine Learning, AI, SQL, Communication")

print("\n================================")
print("        INTERVIEW TIP")
print("================================")

if "communication" in answer:
    print("Good communication skill mentioned!")

if "python" in answer:
    print("Mention a Python project you have worked on.")

if "machine learning" in answer or "artificial intelligence" in answer:
    print("Be ready to explain one AI/ML project.")

print("\nKeep your answers clear, confident and specific!")
print("================================")
