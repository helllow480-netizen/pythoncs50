import csv
students = []
with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "house": row["house"]})
        
def get_name(student):
    return student["name"]
students.sort(key=get_name)
for student in sorted(students, key= lambda student: student["name"]):
    print(f"{student['name']} is from {student['house']} ")