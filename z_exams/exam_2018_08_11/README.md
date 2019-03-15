# Python Fundamentals Exam - 11 August 2018

Problem 1 – Gladiator Expenses
As a gladiator, Pesho has to repair his broken equipment when he loses a fight. His equipment consists of helmet, sword, shield and armor. You will receive the Pesho`s lost fights count.

Every second lost game, his helmet is broken.

Every third lost game, his sword is broken.

When both his sword and helmet are broken in the same lost fight, his shield also brakes.

Every second time, when his shield brakes, his armor also needs to be repaired. 

You will receive the price of each item in his equipment. Calculate his expenses for the year for renewing his equipment. 

### Input / Constraints

You will receive 5 lines:

- First parameter – lost fights count – integer in the range \[0, 1000].
- Second parameter – helmet price - floating point number in range \[0, 1000]. 
- Third parameter – sword price - floating point number in range \[0, 1000]. 
- Fourth parameter – shield price - floating point number in range \[0, 1000]. 
- Fifth parameter – armor price - floating point number in range \[0, 1000]. 

### Output

- As output you must print Pesho`s total expenses for new equipment: "Gladiator expenses: {expenses} aureus"
- Allowed working time / memory: 100ms / 16MB.

### Examples

<table>
<thead>
<tr>
<th>Input</th>
<th>Output</th>
<th>Comment</th>
</tr>
</thead>
<tbody>
<tr>
<td>7<br>2<br>3<br>4<br>5</td>
<td>Gladiator expenses: 16.00 aureus</td>
<td>Trashed helmet -> 3 times<br>Trashed sword -> 2 times<br>Trashed shield -> 1 time<br>Total: 6 + 6 + 4 = 16.00 aureus;</td>
</tr>
<tr>
<td>23<br>12.50<br>21.50<br>40<br>200</td>
<td>Gladiator expenses: 608.00 aureus</td>
<td></td>
</tr>
</tbody>
</table>

<p><b>Solution: <a href="./ex_01_gladiator_expenses.py">ex_01_gladiator_expenses.py</a></b></p>

<p><b>Document with tasks description: <a href="../../resources/z_exams/exam_2018_08_11/01. Gladiator Expenses_Условие.docx">01. Gladiator Expenses_Условие.docx</a></b></p>

## Problem 2 – Gladiator Inventory

As a gladiator, Pesho has cool Inventory. He loves to buy new equipment. You are given Pesho`s inventory with all of his equipment -> strings, separated by whitespace. Until you receive "Fight!" you will be receiving commands which Pesho does with his inventory.

You may receive the following commands:

- Buy {equipment}
- Trash {equipment}
- Repair {equipment}
- Upgrade {equipment}-{upgrade}

If you receive Buy command, you should add the equipment at last position in the inventory, but only if it isn\`t bought already.

If you receive Trash command, delete the equipment if it exists.

If you receive Repair command, you should Repair the equipment if it exists and place it on last position.

If you receive Upgrade command, you should check if the equipment exists and insert after it the upgrade in the following format: "{equipment}:{upgrade}";

### Input / Consrtaints

You will receive input in several lines. Each line is a command:

- One the first line, you will receive Pesho\`s inventory – sequence of equipment names, separated by space.
- Each following line, until you receive "Fight!" will be a command. 

### Output

- As output you must print Pesho`s inventory. 

### Constraints

- The command will always be valid.
- The equipment and Upgrade will be strings and will contain any character, except '-'.
- Allowed working time / memory: 100ms / 16MB.

### Examples

<table>
<thead>
<tr>
<th>Input</th>
<th>Output</th>
<th>Comment</th>
</tr>
</thead>
<tbody>
<tr>
<td>SWORD Shield Spear<br>Buy Bag<br>Trash Shield<br>Repair Spear<br>Upgrade SWORD-Steel<br>Fight!</td>
<td>SWORD SWORD:Steel Bag Spear</td>
<td>We receive the inventory => SWORD, Shield, Spear<br>We Buy Bag => SWORD, Shield, Spear, Bag<br>Trash Shield => SWORD, Spear, Bag<br>Repair Spear => SWORD, Bag, Spear<br>We add Upgrade => SWORD, SWORD:Steel, Bag,Spear<br>We print the inventory.</td>
</tr>
<tr>
<td>SWORD Shield Spear<br>Trash Bow<br>Repair Shield<br>Upgrade Helmet-V<br>Fight!</td>
<td>SWORD Spear Shield</td>
<td></td>
</tr>
</tbody>
</table>

<p><b>Solution: <a href="./ex_02_gladiator_inventory.py">ex_02_gladiator_inventory.py</a></b></p>

<p><b>Document with tasks description: <a href="../../resources/z_exams/exam_2018_08_11/02. Gladiator Inventory_Условие.docx">02. Gladiator Inventory_Условие.docx</a></b></p>

### Problem 3 – Ancient VS Memory

As a gladiator, Pesho is thrilled with ancient scrolls and is excited to have deeper understanding of the encoded knowledge, so he started digging. But because he can\`t read the ancient computer codes, you should write a programm which transforms it in readable form. 

You will receive lines from the ancient memory view in 2-byte integer unsigned display. Each line consists of exactly 22 integers, separated by whitespace. You should find every string in the whole input and print them on the console.

Every string starts with -> "32656 19759 32763"

After the pointer there is one zero and the size of the string -> "0 5"

After the size of string there is one more zero and on the next n columns are the integers for 

each character -> " 0 80 101 115 104 111" 

The above example is the string "Pesho".

You must find all strings and display them on the console, using the ASCII code for each character.

### Input

- The input will consist of a series of lines, containing 22 integers each, separated by whitespaces.
- On the last line, you will receise the string "DEBUG"

### Output

- You should print on a new line every string you`ve found in the input in their order of appearance.

### Constraints

- The lines of the input may contain any 32-bit integer. 
- Allowed working time / memory: 100ms / 16MB.

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
<td>32656 19759 32763 0 5 0 80 101 115 104 111 0 0 0 0 0 0 0 0 0 0 0<br>0 32656 19759 32763 0 7 0 83 111 102 116 117 110 105 0 0 0 0 0 0 0 0<br>DEBUG</td>
<td>Pesho<br>Softuni</td>
</tr>
<tr>
<td>0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 32656 19759 32763 0<br>5 0 71 111 115 104 111 0 0 0 0 0 0 0 0 0 32656 19759 32763 0 4 0<br>75 105 114 111 0 0 0 0 0 0 0 0 0 0 32656 19759 32763 0 8 0 86 101<br>114 111 110 105 107 97 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>DEBUG</td>
<td>Gosho<br>Kiro<br>Veronika</td>
</tr>
</tbody>
</table>

<p><b>Solution: <a href="./ex_03_ancient_vs_memory.py">ex_03_ancient_vs_memory.py</a></b></p>

<p><b>Document with tasks description: <a href="../../resources/z_exams/exam_2018_08_11/03. Ancient VS Memory_Условие.docx">03. Ancient VS Memory_Условие.docx</a></b></p>

## Problem 4 – Arena Tier

Pesho is a pro gladiator, he is struggling to become master of the Arena. // TODO some more story

You will receive several input lines in one of the following formats:

    "{gladiator} -> {technique} -> {skill}"
    "{gladiator} vs {gladiator}"

The gladiator and technique are strings, the given skill will be an integer number. You need to keep track of every gladiator. 

When you receive a gladiator and his technique and skill, add him to the gladiator pool, if he isn\`t present, else add his technique or update his skill, only if the current technique skill is lower than the new value.

If you receive "{gladiator} vs {gladiator}" and both gladiators exist in the tier, they duel with the following rules:

Compare their techniques, if they got at least one in common, the gladiator with better total skill points wins and the other is demoted from the tier -> remove him.

If they don\`t have techniques in common, the duel isn`t happening and both continue in the Season.

You should end your program when you receive the command "Ave Cesar". At that point you should print the gladiators, ordered by total skill in desecending order, then ordered by name in ascending order. Foreach gladiator print their technique and skill, ordered desecending, then ordered by technique name in ascending order

### Input / Constraints

You will receive input on several lines.

- The input comes in the form of commands in one of the formats specified above.
- Gladiator and technique will always be one word string, containing no whitespaces.
- Skill will be an integer in the range \[0, 1000].
- There will be no invalid input lines.
- The programm ends when you receive the command "Ave Cesar".

### Output

- The output format for each gladiator is:

    "{gladiator}: {totalSkill} skill"
    "- {technique} <!> {skill}"

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
<td>Pesho -> BattleCry -> 400<br>Gosho -> PowerPunch -> 300<br>Stamat -> Duck -> 200<br>Stamat -> Tiger -> 250<br>Ave Cesar</td>
<td>Stamat: 450 skill<br>- Tiger &lt;!&gt; 250<br>- Duck &lt;!&gt; 200<br>Pesho: 400 skill<br>- BattleCry &lt;!&gt; 400<br>Gosho: 300 skill<br>- PowerPunch &lt;!&gt; 300</td>
<td>We order the gladiators by total skill points descending,<br>then by name.We print every technique along its skill<br>ordered descending by skill, then by technique name.</td>
</tr>
<tr>
<td>Pesho -> Duck -> 400<br>Julius -> Shield -> 150<br>Gladius -> Heal -> 200<br>Gladius -> Support -> 250<br>Gladius -> Shield -> 250<br>Pesho vs Gladius<br>Gladius vs Julius<br>Gladius vs Gosho<br>Ave Cesar</td>
<td>Gladius: 700 skill<br>- Support &lt;!&gt; 250<br>- Shield &lt;!&gt; 250<br>- Heal &lt;!&gt; 200<br>Pesho: 400 skill<br>- Duck &lt;!&gt; 400</td>
<td>Gladius and Pesho don`t have common technique, so the duel isn`t valid.<br>Gladius wins vs Julius /common technique: "Shield". Julius is demoted.<br>Gosho doesn`t exist so the duel isn`t valid.<br>We print every gladiator left in the tier.</td>
</tr>
</tbody>
</table>

<p><b>Solution: <a href="./ex_04_arena_tier.py">ex_04_arena_tier.py</a></b></p>

<p><b>Document with tasks description: <a href="../../resources/z_exams/exam_2018_08_11/04. Arena Tier_Условие.docx">04. Arena Tier_Условие.docx</a></b></p>