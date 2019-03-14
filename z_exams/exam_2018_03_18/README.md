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

<p><b>Document with tasks description: <a href="../../resources/z_exams/exam_2018_03_18/01. Space Trip_Problem Description.docx>01. Space Trip_Problem Description.docx</a></b></p>
