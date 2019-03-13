# Exercise: Dictionaries, Lambdas and Functional Programming

Problems for exercises and homework for the “Python Fundamentals” course @ SoftUni.

## 01. Odd Occurrences

Write a program that extracts from a given sequence of words all elements that present in it odd number of times (case-insensitive).

- Words are given in a single line, space separated.
- Print the result elements in lowercase, in their order of appearance.

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
<td>Java C# PHP PHP JAVA C java</td>
<td>java, c#, c</td>
</tr>
<tr>
<td>3 5 5 hi pi HO Hi 5 ho 3 hi pi</td>
<td>5, hi</td>
</tr>
<tr>
<td>a a A SQL xx a xx a A a XX c</td>
<td>a, SQL, xx, c</td>
</tr>
</tbody>
</table>
	
### Hints
- Use a dictionary (string  int) to count the occurrences of each word (just like in the previous problem).
- Pass through all key-value pairs in the dictionary and append to the results list all keys that have odd value.
- Print the results list.

<p><b>Solution: <a href="./ex_01_odd_occurrences.py">ex_01_odd_occurrences.py</a></b></p>

## 02. Count Real Numbers

Read a list of real numbers and print them in ascending order along with their number of occurrences.

###Examples

<table>
<thead>
<tr>
<th>Input</th>
<th>Output</th>
</tr>
</thead>
<tbody>
<tr>
<td> 2.5 2.5 8 2.5</td>
<td>8	2.5 -> 3 times<br>8 -> 2 times</td>
</tr>
<tr>
<td>1.5 5 1.5 3</td>
<td>1.5 -> 2 times<br>3 -> 1 times<br>5 -> 1 times</td>
</tr>
<tr>
<td>-2 0.33 0.33 2</td>
<td>-2 -> 1 times<br>0.33 -> 2 times<br>2 -> 1 times</td>
</tr>
</tbody>
</table>

### Hints
- 
- Use dictionary (key=nums, value=count) named counts.
- Pass through each input number num and increase counts[num] (when num exists in the dictionary) or assign counts[num] = 1 (when num does not exist in the dictionary).
- Pass through all numbers num in the dictionary (counts.keys()) and print the number num and its count of occurrences counts[num].

<p><b>Solution: <a href="./ex_02_count_real_numbers.py">ex_02_count_real_numbers.py</a></b></p>

## 03. Letter Repetition

You will be given a single string, containing random ASCII character. Your task is to print every character, and how many times it has been used in the string.

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
<td>aaabbaaabbbccc</td>
<td>a -> 6<br>b -> 5<br>c -> 3</td>
</tr>
<tr>
<td>The quick brown fox jumps over the lazy dog</td>
<td>T -> 1<br>h -> 2<br>e -> 3<br>&nbsp; -> 8<br>q -> 1<br>u -> 2<br>i -> 1<br>c -> 1<br>k -> 1<br>b -> 1<br>r -> 2<br>o -> 4<br>w -> 1<br>n -> 1<br>f -> 1<br>x -> 1<br>j -> 1<br>m -> 1<br>p -> 1<br>s -> 1<br>v -> 1<br>t -> 1<br>l -> 1<br>a -> 1<br>z -> 1<br>y -> 1<br>d -> 1<br>g -> 1</td>
</tr>
</tbody>
</table>

<p><b>Solution: <a href="./ex_03_letter_repetition.py">ex_03_letter_repetition.py</a></b></p>

## 04. Dict-Ref

You have been tasked to create a referenced dictionary, or in other words a dictionary, which knows how to reference itself.

You will be given several input lines, in one of the following formats:

- {name} = {value}
- {name} = {secondName}

The names will always be strings, and the values will always be integers.

In case you are given a name and a value, you must store the given name and its value. If the name already EXISTS, you must CHANGE its value with the given one.

In case you are given a name and a second name, you must store the given name with the same value as the value of the second name. If the given second name DOES NOT exist, you must IGNORE that input.

When you receive the command “end”, you must print all entries with their value, by order of input, in the following format:

{entry} === {value}

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
<td>Cash = 500<br>Johny = 5<br>Cash = 200<br>Johnny = 200<br>Car = 150<br>Plane = 2000000<br>end</td>
<td>Cash === 200<br>Johny === 5<br>Johnny === 200<br>Car === 150<br>Plane === 2000000</td>
</tr>
<tr>
<td>Entry1 = 10000<br>Entry2 = 12345<br>Entry3 = 10101<br>Entry4 = Entry1<br>Entry2 = Entry3<br>Entry3 = Entry4<br>end</td>
<td>Entry1 === 10000<br>Entry2 === 10101<br>Entry3 === 10000<br>Entry4 === 10000</td>
</tr>
</tbody>
</table>

<p><b>Solution: <a href="./ex_04_dict_ref.py">ex_04_dict_ref.py</a></b></p>

## 05. Mixed Phones
You will be given several phone entries, in the form of strings in format:

{firstElement} : {secondElement}

The first element is usually the person’s name, and the second one – his phone number. The phone number consists ONLY of digits, while the person’s name can consist of any ASCII characters. 

Sometimes the phone operator gets distracted by the Minesweeper she plays all day, and gives you first the phone, and then the name. e.g. : 0888888888 : Pesho. You must store them correctly, even in those cases.

When you receive the command “Over”, you are to print all names you’ve stored with their phones. The names must be printed in alphabetical order.

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
<td>14284124 : Alex<br>Gosho : 088423123<br>Ivan : 412048192<br>123123123 : Nanyo <br>Pesho : 150925812<br>Over</td>
<td>Alex -> 14284124<br>Gosho -> 88423123<br>Ivan -> 412048192<br>Nanyo -> 123123123<br>Pesho -> 150925812</td>
</tr>
<tr>
<td>Ivan : 13213456<br>GeorgeThe2nd : 131313<br>Johnny : 5556322312<br>Donald : 3212<br>Over</td>
<td>Donald -> 3212<br>GeorgeThe2nd -> 131313<br>Ivan -> 13213456<br>Johnny -> 5556322312</td>
</tr>
</tbody>
</table>

<p><b>Solution: <a href="./ex_05_mixed_phones.py">ex_05_mixed_phones.py</a></b></p>

## 06. Exam Shopping

A supermarket has products which have quantities. Your task is to stock the shop before Exam Sunday. Until you receive the command “shopping time”, add the various products to the shop’s inventory, keeping track of their quantity (for inventory purposes). When you receive the aforementioned command, the students start pouring in before the exam and buy various products.

The format for stocking a product is: “stock {product} {quantity}”.

The format for buying a product is: “buy {product} {quantity}”.

If a student tries to buy a product, which doesn’t exist, print “{product} doesn't exist”. If it does exist, but it’s out of stock, print “{product} out of stock”. If a student tries buying more than the quantity of that product, sell them all the quantity of the product (the product is left out of stock, don’t print anything).

When you receive the command “exam time”, your task is to print the remaining inventory in the following format: “{product} -> {quantity}”. If a product is out of stock, do not print it.

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
<td>stock Boca_Cola 10<br>stock Boca_Cola 10<br>stock Kay's 3<br>stock Kay's 2<br>shopping time<br>buy Boca_Cola 5<br>buy Kay's 5<br>exam time</td>
<td>Boca_Cola -> 15</td>
</tr>
<tr>
<td>stock Lobster_Energy 20<br>stock Loreni 30 <br>stock Loreni 30<br>stock Lobster_Energy 10<br>shopping time<br>exam time</td>
<td>Lobster_Energy -> 30<br>Loreni -> 60</td>
</tr>
<tr>
<td>stock Boca_Cola 16<br>stock Kay's_Chips 33<br>stock Lobster_Energy 60<br>stock Boca_Cola 4<br>stock Loreni 15<br>stock Loreni 15<br>stock Loreni 15<br>stock Loreni 15<br>shopping time<br>buy Boca_Bola 2<br>buy Lobster_Energy 20<br>buy Boca_Cola 1<br>buy Boba_Bola 12<br>exam time</td>
<td>Boca_Bola doesn't exist<br>Boba_Bola doesn't exist<br>Boca_Cola -> 19<br>Kay's_Chips -> 33<br>Lobster_Energy -> 40<br>Loreni -> 60</td>
</tr>
</tbody>
</table>

<p><b>Solution: <a href="./ex_06_exam_shopping.py">ex_06_exam_shopping.py</a></b></p>

## 07. User Logins

Write a program that receives a list of username-password pairs in the format “{username} -> {password}”. If there’s already a user with that username, replace their password. After you receive the command “login”, login requests start coming in, using the same format. Your task is to print the status of user login, using different messages as per the conditions below:

- If the password matches with the user’s password, print “{username}: logged in successfully”.
- If the user doesn’t exist, or the password doesn’t match the user, print “{username}: login failed”. 

When you receive the command “end”, print the count of unsuccessful login attempts, using the format “unsuccessful login attempts: {count}”.

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
<td>ivan_ivanov -> java123<br>pesh0 -> qwerty<br>stamat4e -> 111111<br>princess_penka -> MyPrince<br>login<br>pesh0 -> qwertt<br>ivan_ivanov -> java123<br>stamat4e -> 111112<br>princess_penka -> MyPrince<br>end</td>
<td>pesh0: login failed<br>ivan_ivanov: logged in successfully<br>stamat4e: login failed<br>princess_penka: logged in successfully<br>unsuccessful login attempts: 2</td>
</tr>
<tr>
<td>johnny_bravo05 -> woahMama<br>login<br>johnny_bravo06 -> woahMama<br>johnny_bravo05 -> woahmama<br>johnny_bravo05 -> WoahMama<br>johnny_bravo05 -> wohMama<br>johnny_bravo05 -> woahMama<br>end</td>
<td>johnny_bravo06: login failed<br>johnny_bravo05: login failed<br>johnny_bravo05: login failed<br>johnny_bravo05: login failed<br>johnny_bravo05: logged in successfully<br>unsuccessful login attempts: 4</td>
</tr>
<tr>
<td>walter_white58 -> iamthedanger<br>krazy_8 -> ese<br>jesseABQ -> bword<br>login<br>krazy_8 -> ese<br>krazy_8 -> ese<br>jesse -> bword<br>jesseabq -> bword<br>walter_white58 -> IAmTheDanger<br>walter_white58 -> iamthedanger<br>end</td>
<td>krazy_8: logged in successfully<br>krazy_8: logged in successfully<br>jesse: login failed<br>jesseabq: login failed<br>walter_white58: login failed<br>walter_white58: logged in successfully<br>unsuccessful login attempts: 3</td>
</tr>
</tbody>
</table>

### Hints

- Parse the commands by splitting by space. The first element is the username, while the third element is the password.
- Store the user entries in dictionary with key {username} and value {password}.

<p><b>Solution: <a href="./ex_07_user_logins.py">ex_07_user_logins.py</a></b></p>

##08. Filter Base

You have been tasked to sort out a database full of information about employees. You will be given several input lines containing information in one of the following formats:

- {name} -> {age}
- {name} -> {salary}
- {name} -> {position}

As you see you have 2 parameters. There can be only 3 cases of input:

If the second parameter is an integer, you must store it as name and age.

If the second parameter is a floating-point number, you must store it as name and salary.

If the second parameter is a string, you must store it as name and position.

You must read input lines, then parse and store the information from them, until you receive the command 
“filter base”. When you receive that command, the input sequence of employee information should end.

On the last line of input you will receive a string, which can either be “Age”, “Salary” or “Position”. Depending on the case, you must print all entries which have been stored as name and age, name and salary, or name and position.
In case, the given last line is “Age”, you must print every employee, stored with its age in the following format:

Name: {name1}

Age: {age1}

====================

Name: {name2}

. . .


In case, the given last line is “Salary”, you must print every employee, stored with its salary in the following format:

Name: {name1}

Salary: {salary1}

====================

Name: {name2}

. . .

In case, the given last line is “Position”, you must print every employee, stored with its position in the following format:

Name: {name1}

Position: {position1}

====================

Name: {name2}

. . .

NOTE: Every entry is separated with the other, with a string of 20 character ‘=’.

There is NO particular order of printing – the data must be printed in order of input.

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
<td>Input	Output<br>Isacc -> 34<br>Peter -> CEO<br>Isacc -> 4500.054321<br>George -> Cleaner<br>John -> Security<br>Nina -> Secretary<br>filter base<br>Position</td>
<td>Name: Peter<br>Position: CEO<br>====================<br>Name: George<br>Position: Cleaner<br>====================<br>Name: John<br>Position: Security<br>====================<br>Name: Nina<br>Position: Secretary<br>====================</td>
</tr>
<tr>
<td>Ivan -> Chistach<br>Pesho -> Ohrana<br>Pesho -> 1323.0456<br>Ivan -> 732.404<br>Georgi -> 21<br>Georgi -> 21.02<br>filter base<br>Salary</td>
<td>Name: Pesho<br>Salary: 1323.0456<br>====================<br>Name: Ivan<br>Salary: 732.404<br>====================<br>Name: Georgi<br>Salary: 21.02<br>====================</td>
</tr>
</tbody>
</table>

### Hints:

Use int(), float() and try-except structure to find out in which case are you and where to store the data.

<p><b>Solution: <a href="./ex_08_filter_base.py">ex_08_filter_base.py</a></b></p>

## 09. Wardrobe

You just bought a new wardrobe. The weird thing about it is that it came prepackaged with a big box of clothes (just like those refrigerators, which ship with free beer inside them)! So, you’ll need to find something to wear.

###Input


On the first line of the input, you will receive n –  the number of lines of clothes, which came prepackaged for the wardrobe.

On the next n lines, you will receive the clothes for each color in the format:

- “{color} -> {item1},{item2},{item3}…”

If a color is added a second time, add all items from it and count the duplicates.

Finally, you will receive the color and item of the clothing, that you need to look for.

### Output

Go through all the colors of the clothes and print them in the following format:

    {color} clothes:
    * {item1} - {count}
    * {item2} - {count}
    * {item3} - {count}
    …
    * {itemN} - {count}

If the color lines up with the clothing item, print “(found!)” alongside the item. See the examples to better understand the output.

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
<td>4<br>Blue -> dress,jeans,hat<br>Gold -> dress,t-shirt,boxers<br>White -> briefs,tanktop<br>Blue -> gloves<br>Blue dress</td>
<td>Blue clothes:<br>* dress - 1 (found!)<br>* jeans - 1<br>* hat - 1<br>* gloves - 1<br>Gold clothes:<br>* dress - 1<br>* t-shirt - 1<br>* boxers - 1<br>White clothes:<br>* briefs - 1<br>* tanktop - 1</td>
</tr>
<tr>
<td>4<br>Red -> hat<br>Red -> dress,t-shirt,boxers<br>White -> briefs,tanktop<br>Blue -> gloves<br>White tanktop</td>
<td>Red clothes:<br>* hat - 1<br>* dress - 1<br>* t-shirt - 1<br>* boxers - 1<br>White clothes:<br>* briefs - 1<br>* tanktop - 1 (found!)<br>Blue clothes:<br>* gloves - 1</td>
</tr>
<tr>
<td>5<br>Blue -> shoes<br>Blue -> shoes,shoes,shoes<br>Blue -> shoes,shoes<br>Blue -> shoes<br>Blue -> shoes,shoes<br>Red tanktop</td>
<td>Blue clothes:<br>* shoes - 9</td>
</tr>
</tbody>
</table>

<p><b>Solution: <a href="./ex_09_wardrobe.py">ex_09_wardrobe.py</a></b></p>

### 10. Shellbound

Vladi is a crab. Crabs are scared of almost anything, which is why they usually hide in their shells. Vladi is a rich crab though. He has acquired many outer shells, in different regions, in which he can hide – each with a different size. 
However, it is really annoying to look after all your shells when they are so spread out. That is why Vladi decided to merge all shells in each region, so that he has one big shell for every region. He needs your help to do that.
You will be given several input lines containing a string and an integer, separated by a space. The string will represent the region’s name, and the integer – the shell in the given region, size. 
You must store all shells in their corresponding regions.

If the region already exists, add the new shell to it. Make sure you have NO duplicate shells (shells with same size). Vladi doesn’t like shells to have the same size.

When you receive the command “Aggregate”, you must stop reading input lines, and you must print every region, all of the shells in that region, and the size of the giant shell after you’ve merged them in the following format:

    {regionName} -> {shell 1, shell 2…, shell n…} ({giantShell})

The giant shell size is calculated when you subtract the average of the shells from the sum of the shells.

Or in other words: (sum of shells) – ((sum of shells) / (count of shells)).

###Constraints

- All numeric data will be represented with integer variables in range [0…1.000.000.000].

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
<td>Sofia 50<br>Sofia 20<br>Sofia 30<br>Varna 10<br>Varna 20<br>Aggregate</td>
<td>Sofia -> 50, 20, 30 (67)<br>Varna -> 10, 20 (15)</td>
</tr>
<tr>
<td>Sofia 2<br>Sofia 1<br>Plovdiv 100<br>Plovdiv 50<br>Aggregate</td>
<td>Sofia -> 2, 1 (2)<br>Plovdiv -> 100, 50 (75)</td>
</tr>
</tbody>
</table>

Input	Output

<p><b>Solution: <a href="./ex_10_shellbound.py">ex_10_shellbound.py</a></b></p>

<p><b>Document with tasks description: <a href="../../resources/l_04_list_and_dictionaries/dictionaries/02. Lists-and-Dictionaries-Dictionaries-Lab.docx">02. Lists-and-Dictionaries-Dictionaries-Lab.docx</a></b></p>