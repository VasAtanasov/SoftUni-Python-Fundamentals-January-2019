# Exercises: Python Intro
Problems for exercises and homework for the “Python Fundamentals” course @ SoftUni. Submit your solutions in the SoftUni judge system at https://judge.softuni.bg/Contests/917.

### 1. Hello World

Write a Python program that prints out a simple “Hello World!” to get acquainted with writing Python code.

### Examples

<table>
<thead>
<tr>
<th>Input</th>
<th>Output</th>
</tr>
</thead>
<tbody>
<tr>
<td>(no input)</td>
<td>Hello World!</td>
</tr>
</tbody>
</table>

<p><b>Solution: <a href="./ex_01_hello_world.py">ex_01_hello_world.py</a></b></p>

### 2. Person Info

Write a Python program, which reads a person’s name, age, town and salary, and prints it back to the console with the following format:

“{name} is {age} years old, is from {town} and makes ${salary}”

Note: Leave floating point numbers unformatted.

### Examples

<table>
<thead>
<tr>
<th>Input</th>
<th>Output</th>
</tr>
</thead>
<tbody>
<tr>
<td>Gosho<br>20<br>Sofia<br>530</td>
<td>Gosho is 20 years old, is from Sofia and makes $530.0</td>
</tr>
<tr>
<td>Pesho<br>22<br>Plovdiv<br>450</td>
<td>Pesho is 22 years old, is from Plovdiv and makes $450.0</td>
</tr>
</tbody>
</table>

<p><b>Solution: <a href="./ex_02_personal_info.py">ex_02_personal_info.py</a></b></p>

### Hints
- To format a string, you can either use the .format() function, or a template string (f'format')

### 3. Extended Person Info

Write a Python program, which reads information about a person in the same format as the previous problem, and prints it back to the console with the following format:

    Name: {name}
    Age: {age}
    Town: {town}
    Salary: ${salary}
    Age range: {ageRange}
    Salary range: {salaryRange}
    
Format the salary to the 2nd decimal point.

The age range is as follows:

- If the person is less than 18 years old, they are a “teen”
- If the person is less than 70 years old, they are an “adult”
- Otherwise, the person is an “elder”

The salary range is as follows:

- If the salary is less than $500, it is “low”
- If the salary is less than $2000, it is “medium”
- Otherwise, the salary is “high”
 
### Examples

<table>
<thead>
<tr>
<th>Input</th>
<th>Output</th>
</tr>
</thead>
<tbody>
<tr>
<td>Gosho<br>20<br>Sofia<br>530</td>
<td>Name: Gosho<br>Age: 20<br>Town: Sofia<br>Salary: $530.00<br>Age range: adult<br>Salary range: medium</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th>Input</th>
<th>Output</th>
</tr>
</thead>
<tbody>
<tr>
<td>Pesho<br>17<br>Plovdiv<br>4500</td>
<td>Name: Pesho<br>Age: 17<br>Town: Plovdiv<br>Salary: $4500.00<br>Age range: teen<br>Salary range: high</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th>Input</th>
<th>Output</th>
</tr>
</thead>
<tbody>
<tr>
<td>Ivan<br>77<br>Montana<br>250</td>
<td>Name: Ivan<br>Age: 77<br>Town: Montana<br>Salary: $250.00<br>Age range: elder<br>Salary range: low</td>
</tr>
</tbody>
</table>

<p><b>Solution: <a href="./ex_03_extender_personal_info.py">ex_03_extender_personal_info.py</a></b></p>

### 4. Numbers from 1 to 10

Write a simple for loop, with which to print all the numbers from 1 to 10 on separate lines.

Use the range() function.

### Examples

<table>
<thead>
<tr>
<th>Input</th>
<th>Output</th>
</tr>
</thead>
<tbody>
<tr>
<td>(no input)</td>
<td>1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10</td>
</tr>
</tbody>
</table>

### Hints

- The range() function generates an exclusive range, so using 10 as an end value probably won’t work.

<p><b>Solution: <a href="./ex_04_numbers_from_1_to_10.py">ex_04_numbers_from_1_to_10.py</a></b></p>

### 5. Numbers with Step

Write a python program, which receives a start number, an end number and a step. Write a simple for loop, which prints all the numbers from the start number to the end number, using the specified step. Print the numbers on separate lines.

Use the range() function.

### Examples

Input	Output		Input	Output

<table>
<thead>
<tr>
<th>Input</th>
<th>Output</th>
<th>Input</th>
<th>Output</th>
</tr>
</thead>
<tbody>
<tr>
<td>1<br>10<br>1</td>
<td>1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9</td>
<td>-20<br>20<br>2</td>
<td>-20<br>-18<br>-16<br>-14<br>-12<br>-10<br>-8<br>-6<br>-4<br>-2<br>0<br>2<br>4<br>6<br>8<br>10<br>12<br>14<br>16<br>18</td>
</tr>
</tbody>
</table>

<p><b>Solution: <a href="./ex_05_numbers_with_step.py">ex_05_numbers_with_step.py</a></b></p>

<p><b>Document with tasks description: <a href="../resources/l_02_intro/01. Python-Fundamentals-Python-Intro-Exercises.docx">01. Python-Fundamentals-Python-Intro-Exercises.docx</a></b></p>


