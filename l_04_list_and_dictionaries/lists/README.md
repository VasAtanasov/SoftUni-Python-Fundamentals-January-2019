# Exercise: Lists

Problems for exercises and homework for the “Python Fundamentals” course @ SoftUni.

### 01. Sum List Items

Write a program, which reads a list of integers, calculates its sum and prints it. 
The input consists of a number n (the number of items) + n integers, each as a separate line.

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
<td>4<br>1<br>2<br>3<br>4</td>
<td>10</td>
</tr>
<tr>
<td>5<br>1<br>1<br>1<br>1<br>1</td>
<td>5</td>
</tr>
<tr>
<td>4<br>2<br>-1<br>-2<br>8</td>
<td>7</td>
</tr>
</tbody>
</table>

### Hints

- First, read the number n.
- Read the integers in a for-loop.

<p><b>Solution: <a href="./ex_01_sum_list_items.py">ex_01_sum_list_items.py</a></b></p>
<p><b>Solution: <a href="./ex_01_sum_list_items_01.py">ex_01_sum_list_items_01.py</a></b></p>

### 02. Multiply a List of Integers

Write a program to read a list of integers, an integer p, multiply each item by p and print the resulting list.

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
<td>1 3 12 4<br>4</td>
<td>4 12 48 16</td>
</tr>
<tr>
<td>6 8 1 -9<br>3</td>
<td>18 24 3 -27</td>
</tr>
</tbody>
</table>

### Hints

- Read the list
- Loop through the list, multiplying each item by p
- Finally, print the resulting list, using a for loop

<p><b>Solution: <a href="./ex_02_multiply_list_of_ints.py">ex_02_multiply_list_of_ints.py</a></b></p>

### 03. Smallest Item in List

Write a program to read a list of integers, find the smallest item and print it.

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
<td>1 2 3 4</td>
<td>1</td>
</tr>
<tr>
<td>3 2 9 -9 6 1</td>
<td>-9</td>
</tr>
<tr>
<td>-6 0 -17 -1</td>
<td>-17</td>
</tr>
</tbody>
</table>

### Hints

- Loop through the integer list until you find the smallest item

<p><b>Solution: <a href="./ex_03_smallest_item_in_list.py">ex_03_smallest_item_in_list.py</a></b></p>

### 04. Rotate List of Strings

Write a program to read a list of strings, rotate it to the right and print its rotated items.

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
<td>a b c d e</td>
<td>e a b c d</td>
</tr>
<tr>
<td>soft uni hi</td>
<td>hi soft uni</td>
</tr>
<tr>
<td>i r a b</td>
<td>b i r a</td>
</tr>
</tbody>
</table>

### Hints

- You can store the rotated list in a second list alongside the first one

<p><b>Solution: <a href="./ex_04_rotate_list_of_strings.py">ex_04_rotate_list_of_strings.py</a></b></p>

### 05. Count of Odd Numbers in List

Write a program to read a list of integers and find how many odd items it holds.

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
<td>1 -2 3 4</td>
<td>2</td>
</tr>
<tr>
<td>3 9 -9 -6 1 -2</td>
<td>4</td>
</tr>
<tr>
<td>66 0 2 1</td>
<td>1</td>
</tr>
</tbody>
</table>

###Hints:

- You can check if a number is odd if you divide it by 2 and check whether you get a remainder of 1.
- Odd numbers, which are negative, have a remainder of -1.

<p><b>Solution: <a href="./ex_05_count_odd_numbers_in_list.py">ex_05_count_odd_numbers_in_list.py</a></b></p>

### 06. Odd Numbers at Odd Positions

Write a program to read a list of integers and find how many odd numbers at odd positions the list holds. If there are no numbers, which match this criterion, do not print anything

### Examples

<table>
<thead>
<tr>
<th>Input</th>
<th>Output</th>
<th>Explanation</th>
</tr>
</thead>
<tbody>
<tr>
<td>2 3 5 2 7 9 -1 -7</td>
<td>Index 1 -> 3<br>Index 5 -> 9<br>Index 7 -> -7</td>
<td>Indexes: 0 1 2 3 4 5  6  7<br>Numbers: 2 3 5 2 7 9 -1 -7<br>Odd positions with odd numbers: 1, 5 and 7</td>
</tr>
<tr>
<td>2 3 55 2 4 1</td>
<td>Index 1 -> 3<br>Index 5 -> 1</td>
<td>Indexes: 0 1 2 3 4 5<br>Numbers: 2 3 55 2 4 1<br>Odd positions with odd numbers: 1 and 5</td>
</tr>
<tr>
<td>5 0 1 2</td>
<td>(no output)</td>
<td>Indexes: 0 1 2 3<br>Numbers: 5 0 1 2<br>Odd positions with odd numbers: none</td>
</tr>
</tbody>
</table>

### Hints

- Positions are counted from 0 from left to right, so if for example the second item (index 1) is odd, then we should count it, and so on…
- Do NOT count odd numbers, which are at even positions (0, 2, 4, etc…)

<p><b>Solution: <a href="./ex_06_odd_numbers_at_odd_pos.py">ex_06_odd_numbers_at_odd_pos.py</a></b></p>

### 07. Remove Negatives and Reverse

Read a list of integers, remove all negative numbers from it and print the remaining items in reversed order. In case of no items left in the list, print “empty”.

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
<td>10 -5 7 9 -33 50</td>
<td>50 9 7 10</td>
</tr>
<tr>
<td>7 -2 -10 1</td>
<td>1 7</td>
</tr>
<tr>
<td>-1 -2 -3</td>
<td>empty</td>
</tr>
</tbody>
</table>
	
### Hints

- Read the list
- Create a new empty list for the results.
- Scan the input list from the end to the beginning. Check each item and append all non-negative items to the result list.
- Finally, print the results list (at a single line holding space-separated numbers).

<p><b>Solution: <a href="./ex_07_remove_negatives_and_reverse.py">ex_07_remove_negatives_and_reverse.py</a></b></p>

### 08. Append Lists

Write a program to append several lists of numbers.

- Lists are separated by ‘|’.
- Values are separated by spaces (‘ ’, one or several)
- Order the lists from the last to the first, and their values from left to right.

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
<td>1 2 3 |4 5 6 |  7  8</td>
<td>7 8 4 5 6 1 2 3</td>
</tr>
<tr>
<td>7 | 4  5|1 0| 2 5 |3</td>
<td>3 2 5 1 0 4 5 7</td>
</tr>
<tr>
<td>1| 4 5 6 7  |  8 9</td>
<td>8 9 4 5 6 7 1</td>
</tr>
</tbody>
</table>
	
Hints

- Create a new empty list for the results.
- Split the input by ‘|’ into list of tokens.
- Pass through each of the obtained tokens from tight to left.
    - For each token, split it by space and append all non-empty tokens to the results.
- Print the results.

<p><b>Solution: <a href="./ex_08_append_list.py">ex_08_append_list.py</a></b></p>

### 09. Sort Numbers

Read a list of integers and sort them in ascending order. Print the output as shown in the examples below.

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
<td>8 2 7 3</td>
<td>2 <= 3 <= 7 <= 8</td>
</tr>
<tr>
<td>2 4 -9</td>
<td>-9 <= 2 <= 4</td>
</tr>
</tbody>
</table>

### Hints

- Use the built-in method list.sort().

<p><b>Solution: <a href="./ex_09_sort_numbers.py">ex_09_sort_numbers.py</a></b></p>

### 10. Square Numbers

Read a list of integers and extract all square numbers from it and print them in descending order. A square number is an integer which is the square of any integer. For example, 1, 4, 9, 16 are square numbers.

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
<td>3 16 4 5 6 8 9</td>
<td>16 9 4</td>
</tr>
<tr>
<td>12 1 9 4 16 8 25 49 16</td>
<td>49 25 16 16 9 4 1</td>
</tr>
</tbody>
</table>
	
### Hints

- To find out whether an integer is “square number”, check whether its square root is integer number (has no fractional part):
    - if (√num == (int)√num) …
- To order the results list in descending order use so

<p><b>Solution: <a href="./ex_10_square_numbers.py">ex_10_square_numbers.py</a></b></p>
<p><b>Solution: <a href="./ex_10_square_numbers_01.py">ex_10_square_numbers_01.py</a></b></p>
<p><b>Solution: <a href="./ex_10_square_numbers_02.py">ex_10_square_numbers_02.py</a></b></p>

<p><b>Document with tasks description: <a href="../../resources/lists/l_04_list_and_dictionaries/lists/02. Lists-and-Dictionaries-Lists-Lab.docx">02. Lists-and-Dictionaries-Lists-Lab.docx</a></b></p>