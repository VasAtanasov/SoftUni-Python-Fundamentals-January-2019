def check_type(text):
    try:
        if float(text) == int(float(text)):
            return {'Age': int(float(text))}
        elif float(text) != int(float(text)):
            return {'Salary': float(text)}
    except ValueError:
        return {'Position': text}


employees_data = []

while True:
    in_line = input()
    if 'filter base' == in_line:
        break

    [name, value] = filter(None, in_line.split(" -> "))

    employees_data.append({name: check_type(value)})

criteria = input()

separator = '=' * 20
result = ''

for entry in range(len(employees_data)):
    for name, data in employees_data[entry].items():
        if criteria in data:
            result += f'Name: {name}\n{criteria}: {data[criteria]}\n{separator}\n'
print(result)
