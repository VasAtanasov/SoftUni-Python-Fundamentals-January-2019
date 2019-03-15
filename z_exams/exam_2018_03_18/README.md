# Python Fundamentals Retake Exam - 18 March 2018

## Problem 1. Space Trip

Ivan is very tired of work on earth and wants to take a holiday abroad. Luckily, he still has about 3 days of paid leave left, so he decides to visit a random nearby star. He’s heard from all his friends that the temperatures are very tropical.

Your task is to calculate whether his fuel will be enough to reach his tropical multi-thousand-degree destination.

### Input / Constraints

The input data should be read from the console. It will consist of exactly 5 lines.

- The destination star – a string
- The destination star’s distance from Earth in gigameters (1 Gm == 1,000,000 km) – integer
- Ivan’s budget – an integer in the range [200-90000000]
- Ivan’s space shuttle fuel consumption in liters per 100 Gm – a floating-point number in the range [0.0-15.0]
- The current gas price in dollars per liter – a floating-point number in the range [0.3-12.5]

The input data will always be valid. There is no need to check it explicitly.

### Output

The output should be printed on the console.

If Ivan has enough money to afford the trip, print:

- Off to {destination} with ${leftover:.2f} for snacks

If Ivan has enough money to afford the server + storage + host combo, print:

- Maybe another time, need ${leftover:.2f} more

Note: Format all prices to the 2nd decimal point.

### Examples

<table>
<thead>
<tr>
<th>Input</th>
<th>Output</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr>
<td>41315010<br>12400000<br>15<br>2</td>
<td>Off to Alpha Centauri with $5497.00 for snacks</td>
<td>Liters per Gm: 15/100 -> $0.15<br>Price per Gm: 0.15 * 2 -> $0.3<br>Total: $12394503.00</td>
</tr>
<tr>
<td>56760000<br>1200000<br>7<br>0.3</td>
<td>Off to Proxima Centauri with $8040.00 for snacks</td>
<td>Liters per km: 7/100 -> $0.07<br>Price per Gm: $0.07 * 0.3 -> $0.021<br>Total: $1191960.0</td>
</tr>
<tr>
<td>81360000<br>8000000<br>0.8<br>12.5</td>
<td>Maybe another time, need $136000.00 more</td>
<td>Liters per km: 0.8/100 -> $0.008<br>Price per Gm: $0.008 * 12.5 -> $0.1<br>Total: $8136000.0</td>
</tr>
</tbody>
</table>

*“I am just a child who has never grown up. I still keep asking these “how” and “why” questions. Occasionally, I find an answer.”
-Stephen Hawking (08/01/1942–13/03/2018)*

<p><b>Solution: <a href="./ex_01_space_trip.py">ex_01_space_trip.py</a></b></p>

<p><b>Author's Solution: <a href="../../resources/z_exams/exam_2018_03_18/01. Space Trip_Author's Solution.py">01. Space Trip_Author's Solution.py</a></b></p>

<p><b>Document with tasks description: <a href="../../resources/z_exams/exam_2018_03_18/01. Space Trip_Problem Description.docx">01. Space Trip_Problem Description.docx</a></b></p>

## Problem 2. Command Integers

You will be given two lists of integers. One of them are the State Integers and the other ones are the Command Integers. The task is to go through each of the Command Integers and perform the following manipulations based on the parity of the command integer:

- If the integer is even, multiply all even numbers in the State Integers by the absolute value of it.
- If the integer is odd, divide all the odd numbers in the State Integers by the absolute value of it.

Then, perform the next set of operations, based on the sign of the command integer:

- If the integer is positive, add it to any positive numbers
- If the integer is negative, add it to any negative numbers

Note: use integer division, not real number division.

### Input / Constraints

On the first line of the input, you will receive the state integers, separated by spaces.

On the second line of the input, you will receive the command integers, separated by spaces.

### Output

On the only line of the output, print the final state of the list.

### Examples

<table>
<thead>
<tr>
<th>Input</th>
<th>Output</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr>
<td>1 2 -3 4 5<br>1 3 -2 -1</td>
<td>[5, 8, -4, 8, 9]</td>
<td>Command int: 1<br>Multiply all odd numbers by abs(1)<br>Add 1 to all positive numbers<br>Command int: 3<br>Divide all odd numbers by abs(3)<br>Add 3 to all positive numbers<br>Command int: -2<br>Multiply all even numbers by abs(-2)<br>Add -2 to all negative numbers<br>Command int: -1<br>Divide all odd numbers by abs(-1)<br>Add -1 to all negative numbers</td>
</tr>
<tr>
<td>5 -1 -2 42 -22<br>1 -1 3 11</td>
<td>[0, -2, -1, 12, -8]</td>
<td></td>
</tr>
<tr>
<td>0 2 1 2 0<br>2 3 2 3 2 3<br></td>
<td>[0, 17, 8, 17, 0]</td>
<td></td>
</tr>
</tbody>
</table>

<p><b>Solution: <a href="./ex_02_command_integers.py">ex_02_command_integers.py</a></b></p>

<p><b>Author's Solution: <a href="../../resources/z_exams/exam_2018_03_18/02. Command Integers_Author's Solution.py">02. Command Integers_Author's Solution.py</a></b></p>

<p><b>Document with tasks description: <a href="../../resources/z_exams/exam_2018_03_18/02. Command Integers_Problem Description.docx">02. Command Integers_Problem Description.docx</a></b></p>

## Problem 3. Chain of Responsibility

In UnidentifiedCompany LLC, we have robot workers, who all have exactly one responsibility. The cool thing is that everyone knows someone who knows someone who is responsible for something you need done. This leads to some degree of fragmentation. In order to get anything done, you need to traverse the chain of responsibility to figure out who to ask.

You will start receiving conversation snippets containing one or more robot names, which match the following rules:

- Begins with one or more digits
- After that, it has one capital Latin letter, followed by one or more non-capital Latin letters
- Ends with either a capital Latin letter or a digit, repeated two or more times.

Example valid robots: 152GoshoAAA, 1Ivan44, 43PeshoZZ

If at any point, you find a line, which has only one name in it, proceed with the following:

- If the line ends with “!!” and has a valid name in it, you have found the manager. Print “Found the manager!: {manager_name}”
- If it doesn’t, print “Did not find the manager!”
- If the first name in the line isn’t the last found name from the previous line, print “Broke the chain!”

In all above cases, print the chain of responsibility on the next line, in the format: “robot1->robot2->robot3…” and end the program.

### Input / Constraints

The input data should be read from the console.

- On the first line of the input, you will receive N -  the number of lines to follow – an integer in range [2-10]
- On the next N lines, you will receive the conversation lines, which will all be strings and each line will have at least one valid name in it.

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
<td>3<br>22IvanCC says: look for 4GoshoII<br>4GoshoII told me that 33Pesho11 manages that.<br>33Pesho11: i can help!!</td>
<td>Found the manager!: 33Pesho11<br>Chain: 22IvanCC->4GoshoII->33Pesho11</td>
</tr>
<tr>
<td>4<br>22IvanCC tells you to look for 1Stamat99<br>1Stamat99 told me 33Pesho11 is responsible.<br>33Pesho11 tells me to look for 1Gosho44<br>1Gosho44: i don't know, man</td>
<td>Did not find the manager!<br>Chain: 22IvanCC->1Stamat99->33Pesho11->1Gosho44</td>
</tr>
<tr>
<td>4<br>00PeturVVVV tells you to message 12StamatAA<br>12StamatAA told me 12Pesho11 is responsible.<br>11Pesho11 tells me to look for 1Gosho44<br>1Gosho44: i don't know, man</td>
<td>Broke the chain!<br>Chain: 00PeturVVVV->12StamatAA->12Pesho11</td>
</tr>
</tbody>
</table>

<p><b>Solution: <a href="./ex_03_chain_of_responsibility.py">ex_03_chain_of_responsibility.py</a></b></p>

<p><b>Author's Solution: <a href="../../resources/z_exams/exam_2018_03_18/03. Chain of Responsibility_Author's Solution.py">03. Chain of Responsibility_Author's Solution.py</a></b></p>

<p><b>Document with tasks description: <a href="../../resources/z_exams/exam_2018_03_18/03. Chain of Responsibility_Problem Description.docx">03. Chain of Responsibility_Problem Description.docx</a></b></p>

## Problem 4. Course Stats

It’s the end of the semester and someone’s gotta rack up some statistics for the courses that passed. That someone just so happens to be you. Start aggregatin’.

### Input / Constraints

Until you receive the line “end”, you will keep receiving lines in the format:

- {technology} – {course_name}:{participants}, {course_name}:{participants}...

The input data will always be in the format specified above. There is no need to check it explicitly.

Your task is to take all this data and aggregate it, so that you have statistics about all languages, courses and participants. If you receive a language + course combo, which already exists, add these participants to the current count of participants.

Output

- On the first line of output, print:
    - “Most popular: {technology_name} ({total_participants} participants)”
    - {total_participants} refers to the sum of all participants in courses for that technology.
- On the second line of output, print:
    - “Least popular: {technology_name} ({total_participants} participants)”
    - {total_participants} refers to the sum of all participants in courses for that technology.
- On the next lines, print all technologies, sorted descending by the sum of the participants in their courses.
    - For each technology, print its courses sorted descending by their participant count.

The printing format for each technology looks like this:

    Technology1 ({total_participants} participants):
    --{Course1} -> {participant_count}
    --{Course2} -> {participant_count}
    --{Course3} -> {participant_count}
    Technology2 ({total_participants} participants):
    --{Course1} -> {participant_count} 
    --{Course2} -> {participant_count}

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
<td>PHP - Web:2<br>C# - OOP Basics:330, Advanced:300, DB:250<br>Java - Advanced:550, DB:110<br>C# - Advanced:100<br>Java - DB:20<br>end</td>
<td>Most popular: C# (980 participants)<br>Least popular: PHP (2 participants)<br>C# (980 participants):<br>--Advanced -> 400<br>--OOP Basics -> 330<br>--DB -> 250<br>Java (680 participants):<br>--Advanced -> 550<br>--DB -> 130<br>PHP (2 participants):<br>--Web -> 2</td>
</tr>
<tr>
<td>PHP - Basics:2, Web:44<br>C# - Basics:33<br>Python - Fundamentals:20<br>Python - Basics:20<br>Java - Advanced:150, DB:50<br>Python - Basics:60<br>end</td>
<td>Most popular: Java (200 participants)<br>Least popular: C# (33 participants)<br>Java (200 participants):<br>--Advanced -> 150<br>--DB -> 50<br>Python (100 participants):<br>--Basics -> 80<br>--Fundamentals -> 20<br>PHP (46 participants):<br>--Web -> 44<br>--Basics -> 2<br>C# (33 participants):<br>--Basics -> 33</td>
</tr>
<tr>
<td>Python - Basics:10, Fundamentals:30<br>Python - Fundamentals:20<br>Python - Basics:20<br>Java - DB:60<br>Python - Basics:60<br>end</td>
<td>Most popular: Python (140 participants)<br>Least popular: Java (60 participants)<br>Python (140 participants):<br>--Basics -> 90<br>--Fundamentals -> 50<br>Java (60 participants):<br>--DB -> 60</td>
</tr>
</tbody>
</table>

<p><b>Solution: <a href="./ex_04_course_stats.py">ex_04_course_stats.py</a></b></p>
<p><b>Solution: <a href="./ex_04_course_stats_cl.py">ex_04_course_stats_cl.py</a></b></p>

<p><b>Author's Solution: <a href="../../resources/z_exams/exam_2018_03_18/04. Course Stats_Author's Solution.py">04. Course Stats_Author's Solution.py</a></b></p>

<p><b>Document with tasks description: <a href="../../resources/z_exams/exam_2018_03_18/04. Course Stats_Problem Description.docx">04. Course Stats_Problem Description.docx</a></b></p>
