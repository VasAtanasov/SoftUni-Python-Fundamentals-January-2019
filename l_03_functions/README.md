# Exercises: Functions, Debugging and Troubleshooting Code

Problems for exercises and homework for the “Python Fundamentals” course @ SoftUni. Submit your solutions in the SoftUni judge system at https://judge.softuni.bg/Contests/922/Functions-and-Debugging.

## I. Declaring and Invoking Functions

### 01. Blank Receipt

Create a function that prints a blank cash receipt. The function should invoke three other functions: one for printing the header, one for the body and one for the footer of the receipt. 

<table>
<tbody>
<tr>
<td>The header should contain the following text:</td>
<td>CASH RECEIPT<br>------------------------------</td>
</tr>
<tr>
<td>The body should contain the following text:</td>
<td>Charged to____________________<br>Received by___________________</td>
</tr>
<tr>
<td>And the text for the footer:</td>
<td>------------------------------<br>© SoftUni</td>
</tr>
</tbody>
</table>

### Examples

<table>
<thead>
<tr>
<th>Output</th>
</tr>
</thead>
<tbody>
<tr>
<td>CASH RECEIPT<br>------------------------------<br>Charged to____________________<br>Received by___________________<br>------------------------------<br>© SoftUni</td>
</tr>
</tbody>
</table>

### Hints

1.	First create a function with no parameters for printing the header. Give it a meaningful name and write the code that it will execute.
2.	Do the same for printing the receipt body and footer.
3.	Create a function that will call all three functions in the necessary order. Again, give it a meaningful and descriptive name and write the code.
4.	For printing "©" use Unicode "\u00A9"
5.	Call (invoke) the first function

<p><b>Solution: <a href="./ex_01_blank_receipt.py">ex_01_blank_receipt.py</a></b></p>

### 02. Sign of Integer Number

Create a function that prints the sign of an integer number n. 

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
<td>2</td>
<td>The number 2 is positive.</td>
</tr>
<tr>
<td>-5</td>
<td>The number -5 is negative.</td>
</tr>
<tr>
<td>0</td>
<td>The number 0 is zero.</td>
</tr>
</tbody>
</table>

### Hints

1.	Create a function with a descriptive name which should receive one paramete.
2.	Implement the body of the function by handling different cases: 
a.	If the number is greater than zero
b.	If the number is less than zero
c.	And if the number is equal to zero
3.	Call (invoke) the newly created function.

<p><b>Solution: <a href="./ex_02_sign_of_integer_number.py">ex_02_sign_of_integer_number.py</a></b></p>

### 03. Printing Triangle

Create a function for printing triangles as shown below:

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
<td>3</td>
<td>1<br>1 2<br>1 2 3<br>1 2<br>1</td>
</tr>
<tr>
<td>4</td>
<td>1<br>1 2<br>1 2 3 <br>1 2 3 4<br>1 2 3<br>1 2<br>1</td>
</tr>
</tbody>
</table>

### Hints

1.	After you read the input.
2.	Start by creating a function for printing a single line from a given start to a given end. Choose a meaningful name for it, describing its purpose.
3.	Think how you can use it to solve the problem.
4.	After you spent some time thinking, you should have come to the conclusion that you will need two loops
5.	In the first loop you can print the first half of the triangle without the middle line.
6.	Next, print the middle line.
7.	Lastly, print the rest of the triangle.

<p><b>Solution: <a href="./ex_03_print_triangle.py">ex_03_print_triangle.py</a></b></p>

### 04. Draw a Filled Square

Draw at the console a filled square of size n like in the example:

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
<td>4</td>
<td>--------<br>-\/\/\/-<br>-\/\/\/-<br>--------</td>
</tr>
</tbody>
</table>

Hints

1.	Read the input
2.	Create a function which will print the top and the bottom rows (they are the same). Don’t forget to give it a descriptive name and to give it as a parameter some length
3.	Create the function which will print the middle rows. 
4.	Use the functions that you've just created to draw a square.

<p><b>Solution: <a href="./ex_04_draw_square.py">ex_04_draw_square.py</a></b></p>

## II. Returning Values and Overloading

### 05. Calculate Triangle Area

Create a function that calculates and returns the area of a triangle by given base and height.

Use a general formatting with 12 digits after the decimal point (e.g. {area:.12g})

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
<td>3<br>3</td>
<td>6</td>
</tr>
</tbody>
</table>

### Hints
1.	After reading the input
2.	Create a function that calculates the area.
3.	Invoke the function in the main and save the return value in a new variable.

<p><b>Solution: <a href="./ex_05_triangle_area.py">ex_05_triangle_area.py</a></b></p>

### 06. Math Power

Create a function that calculates and returns the value of a number raised to a given power:

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
<td>2<br>8</td>
<td>256.0</td>
</tr>
<tr>
<td>1.5<br>3</td>
<td>3.375</td>
</tr>
</tbody>
</table>

### Hints

1.	As usual, read the input
2.	Create a function which will have two parameters - the number and the power, and will return a result
3.	Print the result with no specific formatting.

<p><b>Solution: <a href="./ex_06_math_power.py">ex_06_math_power.py</a></b></p>

### 07. Greater of Two Values

You are given two values of the same type as input. The values can be of type int, char of string. Create a function that returns the greater of the two values: 

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
<td>int<br>2<br>16</td>
<td>16</td>
</tr>
<tr>
<td>char<br>a<br>z</td>
<td>Z</td>
</tr>
<tr>
<td>string<br>Ivan<br>Todor</td>
<td>Todor</td>
</tr>
</tbody>
</table>

### Hints

1.	For this function you need to create three functions with the same name and different signatures
2.	Create a function which will compare integers.
3.	Lastly you need to create a function to compare the other types. 
4.  The last step is to read the input, use appropriate variables and call the function you’ve just written.

<p><b>Solution: <a href="./ex_07_greter_of_two.py">ex_07_greter_of_two.py</a></b></p>

### III. Debugging and Program Flow

### 08. Multiply Evens by Odds

Create a program that reads an integer number and multiplies the sum of all its even digits by the sum of all its odd digits:

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
<td>12345</td>
<td>54</td>
<td>12345 has 2 even digits - 2 and 4. Even digits has sum of 6.<br>Also it has 3 odd digits - 1, 3 and 5. Odd digits has sum of 9.<br>Multiply 6 by 9 and you get 54.</td>
</tr>
<tr>
<td>-12345</td>
<td>54</td>
<td></td>
</tr>
</tbody>
</table>

### Hints

1.	Create a function with a name describing its purpose. The function should have a single parameter and will return value. Also the function will call two other functions.
2.	Create two other functions each of which will sum either even or odd digits.
3.	Implement the logic for summing odd digits.
4.	Do the same for the function that will sum even digits.
5.	As you test your solution you may notice that it doesn't work for negative nu

<p><b>Solution: <a href="./ex_08_multiply_even_by_odds.py">ex_08_multiply_even_by_odds.py</a></b></p>
<p><b>Solution: <a href="./ex_08_multiply_even_by_odds_01.py">ex_08_multiply_even_by_odds_01.py</a></b></p>

<p><b>Document with tasks description: <a href="../resources/l_03_functions/01. Python-Fundamentals-Functions-and-Debugging-Exercises.docx">01. Python-Fundamentals-Functions-and-Debugging-Exercises.docx</a></b></p>