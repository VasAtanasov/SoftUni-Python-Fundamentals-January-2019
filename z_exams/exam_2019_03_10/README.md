# Python Fundamentals Exam - 10 March 2019

## Problem 1. Listmon’s delivery problem

Listmon is a delivery guy. He should deliver a barrels with a mystic liquid. He has got a truck but he is not good at math so he asks you to help him.

You have a task to estimate how many barrels can be transported with the single truck. The shape is rectangular parallelepiped and the barrel's shape always will be circular cylinder.

If at some point the truck get full, you should stop receiving  barrels data and print 

    „Truck is full.{count_of_barrels} on board!“.

Where the count_of_barrels are the barrels you have succesfuly loaded up.

If you have succesfully loaded up all barrels without breaking up the program you should print – 

    „All barrels on board.Capacity left - {volume_of_truck}.“

where the volume_of_truck is the free volume space has left.Where the volume is formatetd up to 2 digit after decimal point.

### Input

You will recieve on the first 3 lines:

- a – width of the truck [floating  number]
- b – depth of the truck [floating number]
- c – height of the truck [floating number]

On the next line you will recieve 

- n - number of barrels [integer number]

For each barrel tou will receive:

- r - radius of the barrel [floating  number]
- h -  height of the barrel [floating  number]

### Output

If you have loaded up all barrels you should print

- "All barrels on board. Capacity left - {volume_of_truck}."

Formatted two digits after decimal point.

If you have no space left in the truck you should print

- "Truck is full. {count_of_barrels} on board!"

### Example input/output


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
<td>300<br>150<br>200<br>6<br>100<br>100<br>100<br>100<br>100<br>100<br>100<br>100<br>100<br>100<br>100<br>100</td>
<td>Truck is full. 2 on board!</td>
<td>We should estimate the volume of the truck –    300*150*200  = 9 000 000.
We know we will receive 6 barrels. For each barrel we estimate its volume -   pi*r*r*h  = V ->  3.141592653589793 * 100*100*100 = 3141592.653589793. Now we have the volume of the first barrel. We should check if there is enough space for it = 9 000 000 - 3141592.653589793 = 5858407.346410207. We have enough space. So we now have one barrel. We continue doing that and we see that the second barrel fits two. So now we have two on board. We received the data for the third one. We check if there is enough space – so far we left with 2716814.692820414truck space -> 
2716814.692820414 - 3141592.653589793 =
 -424777.960769379. Here we see that the truck has no capacity for the third one so we left just with two barrels, print the result and stop reading barrel’s data.</td>
</tr>
<tr>
<td>100<br>100<br>50<br>2<br>20<br>40<br>30<br>60</td>
<td>All barrels on board. Capacity left - 280088.51.</td>
<td></td>
</tr>
</tbody>
</table>

<p><b>Solution: <a href="./ex_01_listmons_delivery_problem.py">ex_01_listmons_delivery_problem.py</a></b></p>

<p><b>Author's Solution: <a href="../../resources/z_exams/exam_2019_03_10/01.Listmon's delivery problem (solution).py">01.Listmon's delivery problem (solution).py</a></b></p>

<p><b>Document with tasks description: <a href="../../resources/z_exams/exam_2019_03_10/01. Listmons delivery problem_Условиe.docx">01. Listmons delivery problem_Условиe.docx</a></b></p>

## Problem 2. Listmon says

### Input / Constraints

We are at the Listmon's playground. The collection defines its own rules and if we want to beat It in its own game, we must play by the rules .A game is pretty similar to 'Simon says'. So, It will tell us what to do and we should read very carefully what It wants from us.

At the beginning of the game Listmon will give us an input with different elements separated by space (one or several). The elements will be numbers.

After that It will start giving us commands in format:

- set
- filter {command} (where command will be either odd or even)
- multiply {number}
- divide {number}
- slice {indexN} {indexM}
- sort
- reverse

*If you receive command 'set' you should check if the list is not already with unique elements, if this is so -

print:

- "It is a set"

If it isn't, make it one and print it as a list. Keep the order of the elements exactly the same as Listmon gave it to you, just remove the non-unique elements. 

*If you receive ‘filter’ you should print only either odds elements, or even, depending on the command next to filter.

If there are no elements in the list after filter command do not print the list.

*If you receive 'multiply', multiply every element of the list by the given number. 

*If you receive ‘divide’ you must divide every element by the given number and print the list. If the number is 0, print:

- 'ZeroDivisionError caught'  And do not print the list.

*If you receive ‘slice’ {indexN} {indexM} you should print the elements from n to m including without actually changing the list! Keep in mind that Listmon is tricky and can give you indexes which are not part of the list. In this case you should print:

- 'IndexError caught '. 

And do not print the list.

Index N always will be smaller number than M if the two indexes are valid

*If you receive sort - print the elements in ascending order.

*If you receive reverse – print all elements in reversed order.

ALWAYS keep in mind that the Listmon’s list never should be changed, otherwise we are going to lose the game.

NOTE:

- After each command you should print the result ONLY if there are elements in the list. If the list is empty do not print it!
 
### Output

When you recieve a commant which says 'exhausted', you should print the count of roundes played in format:

- "I beat It for {count} rounds!"

where count is the number of commands you have recieved during the game.

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
<td>1 3 2 4 5<br>set<br>slice 1 5<br>sort<br>reverse<br>exhausted</td>
<td>It is a set<br>IndexError caught<br>[1, 2, 3, 4, 5]<br>[5, 4, 2, 3, 1]<br>I beat It for 4 rounds!</td>
<td>On the first line we receive Listmon’s list.
On the seccond we see set. We check if all elements are unique – they are so we just prin ‘It is a set’.After that we receive ‘slice 1 5’ the first index is valid but the second one is not because we have only 4 indexes (5 elements), so we print  ‘IndexError caught’. After that we receive ‘sort’ and we sort all elememnts by ascending order and print them.After that we receive ‘reverse’ and we should reverse Listmon’s list, so we get [5, 4, 2, 3, 1]
not [5, 4, 3, 2, 1], because we never ever change the Listmon’s list. After command ‘exausted’ we print ‘I beat It for 4 rounds!’ because in this case we receive 4 commands from It.</td>
</tr>
<tr>
<td>1 15 3 279 12<br>filter odd<br>multiply 7<br>divide 0<br>reverse<br>exhausted</td>
<td>[1, 15, 3, 279]<br>[7, 105, 21, 1953, 84]<br>ZeroDivisionError caught<br>[12, 279, 3, 15, 1]<br>I beat It for 4 rounds!</td>
<td></td>
</tr>
</tbody>
</table>

<p><b>Solution: <a href="./ex_02_listmon_says.py">ex_02_listmon_says.py</a></b></p>

<p><b>Author's Solution: <a href="../../resources/z_exams/exam_2019_03_10/02.Listmon says (solution).py">02.Listmon says (solution).py</a></b></p>

<p><b>Document with tasks description: <a href="../../resources/z_exams/exam_2019_03_10/02. Listmon says_Условие.docx">02. Listmon says_Условие.docx</a></b></p>
	
## Problem 3. Listmon’s DB

### Input / Constraints

Listmon is as like a Google. It tracks every of its players in the game. You beat It in its own game, so It asks you now to help It with the database and make several reports for It, because it is a mess there. 

You will start receiving players data in format:

    {playerName} -> {resultOfTheGame}, {resultOfTheGame}, {resultOfTheGame}, {resultOfTheGame} ...

Keep in mind that it is possible to have two players with the same playerName. You should store the data separately, not replacing it.

Every line is different data and different player.

You must store it until you receive command 'report'. After that you will receive reporting tickets in format:

- score descending
- score ascending
- numberOfGames descending
- numberOfGames ascending

### Output

* If you receive 'score descending' you must print all players by the order of the score descending, after that by name ascending in format

     {name}: {score}
     
* If you receive 'score ascending' you must print all players by the order of the score ascending, after that by name ascending in format

     {name}: {score}
     
* If you receive 'number of games descending' you must print all players by the number of games played descending, after that by name ascending in format

     {name}: {count of the games}
     
* If you receive 'number of games ascending’  you must print all players by the number of games played ascending after that by name ascending in format

     {name}: {count of the games}

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
<td>Sims -> 15, 25, 65, 85<br>Misho -> 5, 5, 5<br>Azzi -> 0, 0, 2, 5<br>Sims -> 5, 5, 5, 5, 5, 5, 5<br>report<br>score ascending<br>end</td>
<td>Azzi: 7<br>Misho: 15<br>Sims: 35<br>Sims: 190</td>
<td>Here we have two players with the same name. We store data for each separatly and becoming a ‘score ascending’ command, we put players from smallest amount of score points to the highest.</td>
</tr>
<tr>
<td>theBest -> 952, 26, 83, 15, 25<br>ultimatePlayer -> 1998, 0, 25<br>nick_name -> 25, 0, 9852648<br>report<br>numberOfGames descending<br>numberOfGames ascending<br>end</td>
<td>theBest: 5<br>nick_name: 3<br>ultimatePlayer: 3<br>nick_name: 3<br>ultimatePlayer: 3<br>theBest: 5</td>
<td></td>
</tr>
</tbody>
</table>

<p><b>Solution: <a href="./ex_03_listmons_db.py">ex_03_listmons_db.py</a></b></p>

<p><b>Author's Solution: <a href="../../resources/z_exams/exam_2019_03_10/03.Listmon's DB (solution).py">03.Listmon's DB (solution).py</a></b></p>

<p><b>Document with tasks description: <a href="../../resources/z_exams/exam_2019_03_10/03. Listmons DB_Условие.docx">03. Listmons DB_Условие.docx</a></b></p>

## Problem 4. Listmon’s Monsters

### Input / Constraints

An evil genius never works alone.  Listmon has own army. He wants to start tracking data for his army. You have been asked to create a data base for Listmon's monsters.

A basic monster will always  have:

- name -  string of any asci character without space and comma 
- id  – integer number
- strength - integer point number
- ugliness - integer number

In his army he accepts only two types of monsters: Hydralisks and Zerglings. Both types has the same parameters as a basic monsters but also:

- Hydralisk has another property – range - string of any asci character without space and comma
- Zergling has another property – speed – integer number

Listmon does not get in his army basic monsters. They must be one of the two types mentioned above.

You will start receiving input data in format:

- Hydralisk({name}, {id}, {strength}, {ugliness}, {range})
    - if there is no fifth parameter you should print '\_\_init__() missing 1 required positional argument: 'range''
    - if the fifth parameter is not a string you should print 'Range must be string'
    - In both cases you do not add the monster in DB

- Zergling({name}, {id}, {strength}, {ugliness}, {speed})
    - if there is no fifth parameter you should print '\_\_init__() missing 1 required positional argument: 'speed''
    - if the fifth parameter is not a string you should print 'Speed must be string'
    - In both cases you do not add the monster in DB

Is it possible a basic monster to try to apply in the army. If you receive a command:

 - *BasicMonster({name}, {id}, { strength }, {ugliness})
    - You must print ‘Can't instantiate abstract class BaseMonster with abstract methods \_\_init__’  and you must  not add it in the DB.

### Output

When you receive a command ‘stopAddingArmy’ you must print the information about the army in the following format:

    Overall speed of army: {speed}
    Overall strength: {strength}
    Hydralisk: {count}; Zergling: {count}

Where {speed} is the sum of all Zerglings monsters speed in DB;
{strength} is the sum of strength of all monsters;
{count} is the number of all Hydralisks/Zerglings in the DB

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
<td>Zergling('Pesho', 10, 10, 10, 10)<br>Zergling('Pesho', 10, 10, 10, 20)<br>Hydralisk('a', 100, 100, 100, 'min')<br>Zergling('Pesho', 10, 10, 10, 30)<br>stopAddingArmy</td>
<td>Overall speed of army: 60<br>Overall stength: 130<br>Hydralisk: 1; Zergling: 3</td>
<td>On the first row we receive a Zergling. We check that there are five parameters, and the last one is integer number, so we add it in DB.
Same for the second row.
Third is Hydralisk. We check if there are five parameters and the last one is string so we add it. Fourth is the same as the first two. After a command ‘stopAddingArmy’ we print the result. Overall speed of the army is all Zerglings speed and we sum the results – 10 +20+30 = 60. Overall strength is the sum of all strength of every soldier in the army: 10+10+100+10 = 130. After that we should count the amount of Hydralisks which in this case is 1, and the amount of Zaerglings which is 3.</td>
</tr>
<tr>
<td>BaseMonster('A12', 150, 200, 300)<br>Zergling('Pesho', 10, 10, 10, 'min')<br>Hydralisk('a', 100, 100, 100, 10)<br>Zergling('Pesho', 10, 10, 10)<br>Hydralisk('a', 100, 100, 100)<br>stopAddingArmy</td>
<td>Can't instantiate abstract class BaseMonster with abstract methods __init__<br>Speed must be integer <br>Range must be string<br>__init__() missing 1 required positional argument: 'speed'<br>__init__() missing 1 required positional argument: 'range'<br>Overall speed of army: 0<br>Overall stength: 0<br>Hydralisk: 0; Zergling: 0</td>
<td></td>
</tr>
</tbody>
</table>

<p><b>Solution: <a href="./ex_04_listmons_monsters.py"></a></b></p>

<p><b>Author's Solution: <a href="../../resources/z_exams/exam_2019_03_10/04.Listmon's Monsters (solution_classes_advanced).py">04.Listmon's Monsters (solution_classes_advanced).py</a></b></p>

<p><b>Author's Solution: <a href="../../resources/z_exams/exam_2019_03_10/04.Listmon's Monsters (solution_dicts).py">04.Listmon's Monsters (solution_dicts).py</a></b></p>

<p><b>Document with tasks description: <a href="../../resources/z_exams/exam_2019_03_10/04. Listmons Monsters_Условие.docx">04. Listmons Monsters_Условие.docx</a></b></p>