# Python Fundamentals Exam - 11 March 2018

## Problem 1. Cloud Storage

Pesho wants to run his site in the cloud, but since he doesn't have an unlimited amount of money, he needs to calculate the amount of money the cloud solution will cost him. He needs several servers, storage units and hosts.

One server can support up to 50 concurrent users. One storage unit can store up to 500MB of data.

One server costs $2/hour. One storage unit costs $0.5/hour. One host costs $10/month

Your task is to calculate whether Pesho can afford to run the website for an entire month given his own requirements.

Assume every month has 30 days.

### Input / Constraints

The input data should be read from the console. It will consist of exactly 5 lines.

- Pesho’s monthly budget – floating-point number in the range [0-25000]
- The number of concurrent clients he needs to support – integer number in the range [0-800]
- The gigabytes of data he needs to store– integer number in the range [0-30]
- The number of hosts he needs for his site– integer number in the range [0-10]
- The expected uptime in percent– floating-point number in the range [0-100]

The input data will always be valid. There is no need to check it explicitly.

### Output

The output should be printed on the console.

If Pesho has enough money to afford the server + storage + host combo, print:

- Clouds Ahoy! Monthly cost: $x.xx ($x.xx leftover)

If Pesho has enough money to afford the server + storage + host combo, print:

- Stay Grounded! Monthly cost: $x.xx (Need $x.xx more)

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
<td>9000<br>190<br>4<br>2<br>100</td>
<td>Clouds Ahoy! Monthly cost: $8660.00 ($340.00 leftover)</td>
<td>Servers needed: 190 / 50 = 3.8 -> 4<br>Storage needed: 4 / 0.5 -> 8<br>Hourly cost: $2*4 + $0.5*8 -> $12/hour -> $288/day<br>Hosts cost: 2 * $10 -> $20/month<br>Monthly cost: $288 * 30 -> $8640/month<br>Total: ($8640 + $20) * 100% uptime -> $8660</td>
</tr>
<tr>
<td>3615.5<br>100<br>1<br>1<br>100</td>
<td>Clouds Ahoy! Monthly cost: $3610.00 ($5.50 leftover)</td>
<td>Servers needed: 100 / 50 = 2 -> 2<br>Storage needed: 1 / 0.5 -> 2<br>Hourly cost: $2*2 + $0.5*2 -> $5/hour -> $120/day<br>Hosts cost: 1 * $10 -> $10/month<br>Monthly cost: $120 * 30 -> $3600/month<br>Total: ($3600 + $10) * 100% uptime -> $3610</td>
</tr>
<tr>
<td>24000<br>753<br>10<br>4<br>8</td>
<td>Stay Grounded! Monthly cost: $24224.00 (Need $224.00 more)</td>
<td>Servers needed: 753 / 50 = 15.06 -> 16<br>Storage needed: 10 / 0.5 -> 20<br>Hourly cost: $2*16 + $0.5*20 -> $42/hour -> $1008/day<br>Hosts cost: 4 * $10 -> $40/month<br>Monthly cost: $1008 * 30 -> $30240/month<br>Total: ($30240 + $40) * 80% uptime -> $24224</td>
</tr>
</tbody>
</table>

<p><b>Solution: <a href="./ex_01_cloud_storage.py">ex_01_cloud_storage.py</a></b></p>

<p><b>Author's Solution: <a href="../../resources/z_exams/exam_2018_03_11/01. Cloud Storage_Author's Solution.py">01. Cloud Storage_Author's Solution.py</a></b></p>

<p><b>Document with tasks description: <a href="../../resources/z_exams/exam_2018_03_11/01. Cloud Storage_Problem Description.docx">01. Cloud Storage_Problem Description.docx</a></b></p>



