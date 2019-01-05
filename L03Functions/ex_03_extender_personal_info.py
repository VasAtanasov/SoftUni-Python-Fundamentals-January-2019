name = input()
age = int(input())
town = input()
salary = float(input())
ageRange = "teen" if age < 18 else "adult" if age < 70 else "elder"
salaryRange = "low" if salary < 500 else "medium" if salary < 2000 else "high"

print(f'Name: {name}')
print(f'Age: {age}')
print(f'Town: {town}')
print(f'Salary: ${salary:.2f}')
print(f'Age range: {ageRange}')
print(f'Salary range: {salaryRange}')
