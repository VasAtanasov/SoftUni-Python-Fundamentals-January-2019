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

## Problem 2. SoftUni Lecture CDN

In this exam problem’s universe, SoftUni decided to store its lectures’ recordings on its own servers. Also, in this universe your job application to SoftUni was accepted and as the new intern, you have been given the simple task of implementing a Content Delivery Network for the recordings. We’ll leave storing the actual video files to the backend engineers - your job here is to simply generate lecture links based on existing data. Since you’re a sneaky little hacker, you also want to scrape some of the links for “safe keeping”.

A sample lecture link looks like this:

    https://streamcdn1.softuni.bg/course=csharp-oop-basics&lecture=polymorphism&trainer=housey
    
As you can see, every link begins with “https://streamcdn{n}.softuni.bg/”, where {n} is the stream server number. After that, it has parameters like the course, lecture and the trainer. A single server can only hold up to 10 hours of video, so keep that in mind when storing the videos.

### Input / Constraints

The input data should be read from the console.

You will receive multiple lines in the format:

	lecture:{name};trainer:{trainer};course:{course};duration:{hours}h{minutes}m
	
The tokens (lecture/trainer/course/duration) will be in random order, so you need to account for that fact when parsing them. The duration will always have hours and minutes, even if their values are 0.

When you parse the lecture info, you need to store it in the current server. As said above, each server can only hold 10 hours of video. If a video you’d store would overflow the maximum duration of 10 hours, put it on the next server (increment the server index by 1). Do not put videos in the previous server after an overflow occurs.

You will stop receiving lectures when you receive the command 

    “scrape {course/trainer} {course_name/trainer_name}”,

The input data will always be in the format specified. There is no need to check it explicitly.

### Output

Upon receiving the final line of the input, depending on what was specified (scrape course or scrape trainer), you need to look through the servers and find all lectures which have that course/trainer. Create links for them and print them on the console, separated by new lines, in order of insertion.

Finally, calculate the total duration of the lectures and print it in the following format:

    “total duration: HH:MM:SS”

Make sure each token (hour/minute/second) has leading zeroes if it needs them.
 
### Examples

#### Input

    trainer:housey;course:csharp-oop-basics;lecture:polymorphism;duration:3h05m
    lecture:matrices-extra;trainer:bojo;course:csharp-oop-basics;duration:4h35m
    duration:1h56m;trainer:housey;course:csharp-db;lecture:joins
    trainer:viktor;duration:2h33m;course:js-fundamentals;lecture:dom
    trainer:housey;course:python-fund;lecture:functional;duration:2h06m
    lecture:matrices-extra;trainer:bojo;course:csharp-oop-basics;duration:4h35m
    scrape course csharp-oop-basics

#### Output

    https://streamcdn1.softuni.bg/course=csharp-oop-basics&lecture=polymorphism&trainer=housey
    https://streamcdn1.softuni.bg/course=csharp-oop-basics&lecture=matrices-extra&trainer=bojo
    https://streamcdn2.softuni.bg/course=csharp-oop-basics&lecture=matrices-extra&trainer=bojo
    total duration: 12:15:00

#### Comments

    The first (and only) server switch happens when we attempt to insert the “dom” lecture.

#### Input

    trainer:housey;course:csharp-oop-basics;lecture:polymorphism;duration:3h05m
    lecture:matrices-extra;trainer:bojo;course:csharp-oop-basics;duration:4h35m
    duration:1h56m;trainer:housey;course:csharp-db;lecture:joins
    lecture:matrices-extra;trainer:bojo;course:csharp-oop-basics;duration:4h35m
    lecture:matrices-extra-2;trainer:bojo;course:csharp-oop-basics;duration:2h20m
    trainer:viktor;duration:2h33m;course:js-fundamentals;lecture:dom
    trainer:housey;course:python-fund;lecture:functional;duration:2h06m
    scrape trainer housey

#### Output

    https://streamcdn1.softuni.bg/course=csharp-oop-basics&lecture=polymorphism&trainer=housey
    https://streamcdn1.softuni.bg/course=csharp-db&lecture=joins&trainer=housey
    https://streamcdn3.softuni.bg/course=python-fund&lecture=functional&trainer=housey
    total duration: 07:07:00

#### Comments

    The first server switch happens when we attempt to insert the “matrices-extra” lecture. 
    The second – when we insert the “functional” lecture. 

#### Input

    lecture:softuniada;course:marathons;duration:9h30m;trainer:nakov
    lecture:softuniada2018;course:marathons;duration:10h00m;trainer:nakov
    lecture:softuniada2033;course:marathons;duration:9h45m;trainer:nakov
    scrape trainer nakov

#### Output

    https://streamcdn1.softuni.bg/course=marathons&lecture=softuniada&trainer=nakov
    https://streamcdn2.softuni.bg/course=marathons&lecture=softuniada2018&trainer=nakov
    https://streamcdn3.softuni.bg/course=marathons&lecture=softuniada2033&trainer=nakov
    total duration: 29:15:00

#### Comments

    We insert the first lecture (which is 9h30m long) into the 1st server, then we insert the second 
    lecture into the second server. Since the second server now has exactly 10 hours of video on it,
    we insert the third lecture into the third server.

<p><b>Solution: <a href="./ex_02_softuni_lecture_cdn.py">ex_02_softuni_lecture_cdn.py</a></b></p>

<p><b>Author's Solution: <a href="../../resources/z_exams/exam_2018_03_11/02. SoftUni Lecture CDN_Author's Solution.py">02. SoftUni Lecture CDN_Author's Solution.py</a></b></p>

<p><b>Document with tasks description: <a href="../../resources/z_exams/exam_2018_03_11/02. SoftUni Lecture CDN_Problem Description.docx">02. SoftUni Lecture CDN_Problem Description.docx</a></b></p>

## Problem 3. Caesar Logins

The new craze in the web dev world is to create crazy “unhackable” authentication schemes. As one of the top people in the hacker community, you want to get the credit for hacking the newest authentication scheme: the Caesar Login. It turns out that a Caesar Login is pretty simple to implement, but it’s quite difficult to read by humans (“security through obscurity” in the worst sense imaginable). As it happens, you’ve just set up a man-in-the-middle attack on one of the largest cryptocurrency trading sites, which happens to use this fictional login method and your exploit is quietly collecting Caesar Logins. Now, it’s time to crack the logins and run off with everyone’s money.

A standard Caesar Login looks like this:

- /tickticktocktockticktock/

Legend:  : username,  : password

Here’s the rules a valid Caesar Login should follow:

- It always starts and ends with the one of two separators (either / or \). It needs to be the same on both sides!
- Then, it has the username, repeated twice (a username can only contain alphanumeric characters)
- Then, it has the password, repeated twice. (a password can only contain alphanumeric characters)
- Finally, it has the username and password one after the other

In the example above, the username is “tick”, and the password is “tock”

The fun part is that each username and password can have any character that’s invalid for a username/password at their start and end.

Here’s another example:

- \^\muynu_muynu^789%;789muynu789\

This one is a little bit different, as it has non-alphanumeric before/after the usernames and passwords. This is where the “Caesar” part in a Caesar Login comes in. The upper example has 6 non-alphanumeric characters ('^', '\', '_', '^', '%', ';'). You need to count these characters and subtract that count from each character’s ASCII value in both the username and password in order to get their actual values. In the upper example, the username is “gosho” and the password is “123”

Every Caesar Login which doesn’t follow the format specified above needs to be ignored, as it is invalid.

### Input / Constraints

The input data should be read from the console.

- You will receive Caesar Login strings on the console, until you receive the command “/end/”

### Output

Print each valid Caesar Login in the following format:

- “user: {username}, pass: {password}”

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
<td>/tickticktocktockticktock/<br>/wrong-wrong->cc&passpasswrong+pass/<br>\^\muynu_muynu^789%;789muynu789\<br>\rgujq)rgujqrgpmcrgpmc+rgujqrgpmc\<br>/end/</td>
<td>user: tick, pass: tock<br>user: gosho, pass: 123<br>user: pesho, pass: penka</td>
</tr>
<tr>
<td>/gg_gg_xxxxggxx\<br>\/FkcoqpfFkcoqpfjwpvgt4jwpvgt4Fkcoqpfjwpvgt4\\<br>/c<cd>dcd/<br>/end/</td>
<td>user: Diamond, pass: hunter2<br>user: a, pass: b</td>
</tr>
<tr>
<td>\\ltxmt_ltxmt^678%678`ltxmt678\<br>/lydqlydqLYR456789-LYR456789lydq++LYR456789/<br>\lshwury\ lshwuryLS6478/LS6478lshwuryLS6478\<br>/end/</td>
<td>user: gosho, pass: 123<br>user: ivan, pass: IVO123456<br>user: ipetrov, pass: IP3145</td>
</tr>
</tbody>
</table>

<p><b>Solution: <a href="./ex_03_caesar_logins.py">ex_03_caesar_logins.py</a></b></p>

<p><b>Author's Solution: <a href="../../resources/z_exams/exam_2018_03_11/03. Caesar Logins_Author's Solution.py">03. Caesar Logins_Author's Solution.py</a></b></p>

<p><b>Document with tasks description: <a href="../../resources/z_exams/exam_2018_03_11/03. Caesar Logins_Problem Description.docx">03. Caesar Logins_Problem Description.docx</a></b></p>

## Problem 4. Train System

The Bulgarian Dreadful Zug Company (BDZ) just upgraded their ticket systems from something running on DOS 5 to a state-of-the-art system running a fancy web app. Of course, nobody bothered to migrate all the discount cards over to the new system, so all the passengers trying to buy a ticket with a discount nearly miss their train, since the cashier, grandma Penka, needs to enter it into the new system. Luckily, she heard about this great thing, called Python from her neighbor, grandma Gina, and how she can use it to automate this task.

In this problem, you assume the role of grandma Penka. You have a 15-minute lunch break, so you decide to use that time to write up a Python script to migrate all the data.

### Input / Constraints

- On the first line, you will receive the number of existing cards N – integer in range [0-5]
- On the next N lines, you will receive the existing cards in the format “firstName lastName ticketNum”.
    - Existing cards will always have a valid card number
- Then, until you receive the command “time to leave!”, keep reading lines in the format:
    - “createTicket firstName lastName destination cardNumber”

The input data will always be in the format specified. There is no need to check it explicitly.

When you receive all the existing cards, insert them into the system. Cards are tied to the person’s full name (first name + space (“ “) + last name). A person can have multiple cards.

After that, your lunch break is over and you need to start issuing tickets to people again. A standard “issue ticket” command looks like this:

- “createTicket firstName lastName destination cardNumber”

You need to check if this person already has a card with that number under that name. If they do, issue their ticket with the card number. If not, you need to check if the card number is valid. A valid card number’s digit sum is divisible by 7 (example: 297296  (2+9+7+2+9+6) % 7 == 0  valid). If the card number is invalid, print “card {cardNumber} is not valid!” and issue the ticket without a discount.

If the card number is valid, but it already belongs to another passenger, print “card {cardNumber} already exists for another passenger!” and issue the ticket without a discount.

If the card doesn’t already belong to another passenger and is not already in the existing cards, you need to issue that passenger a card. Insert it into the cards and print (“issuing card {cardNumber}”). After that, issue them a ticket with a discount.

The price of the ticket is the sum of the ASCII codes of the destination name, divided by 100 

- Example: vidin -> v+i+d+i+n -> 538 / 100 -> 5.38

Every ticket bought with a valid card that belongs to the passenger is 50% cheaper.

### Output

When you receive “time to leave!”, print all passengers in the following format:

    fullName:
    --{destination}: {ticketPrice:.2f}
    --{destination}: {ticketPrice:.2f} (using card {cardNumber})
    ...
    total: {ticketPrice:.2f}BGN

Sort the passengers by the sum of their ticket prices (descending). Sort each passenger’s tickets by the ticket’s price (descending). If a ticket was bought without a discount, don’t print “using card…” after it.

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
<td>4<br>pesho ivanov 297296<br>ivan tsekov 652530<br>gosho goshov 547989<br>ivan tsekov 468845<br>createTicket pesho ivanov vidin 297296<br>createTicket ivan petrov ruska_bela 590432<br>createTicket ivan petrov sofia 590430<br>createTicket pesho ivanov boychinovtsi 590554<br>createTicket bay ivan montana 912839<br>time to leave!</td>
<td>card 590432 is not valid!<br>issuing card 590430<br>issuing card 590554<br>card 912839 is not valid!<br>ivan petrov:<br>--ruska_bela: 10.49lv<br>--sofia: 2.65lv (using card 590430)<br>total: 13.14lv<br>pesho ivanov:<br>--boychinovtsi: 6.57lv (using card 590554)<br>--vidin: 2.69lv (using card 297296)<br>total: 9.26lv<br>bay ivan:<br>--montana: 7.50lv<br>total: 7.50lv</td>
</tr>
<tr>
<td>1<br>georgi georgiev 586790<br>createTicket pesho petrov vidin 297296<br>createTicket pesho petrov montana 630534<br>createTicket pesho petrov plovdiv 630534<br>createTicket bay ivan vidin 297296<br>createTicket bay ivan sofia 111111<br>createTicket bay ivan montana 111111<br>createTicket bay ivan mezdra 111111<br>time to leave!</td>
<td>issuing card 297296<br>issuing card 630534<br>card 297296 already exists for another passenger!<br>card 111111 is not valid!<br>card 111111 is not valid!<br>card 111111 is not valid!<br>bay ivan:<br>--montana: 7.50lv<br>--mezdra: 6.43lv<br>--vidin: 5.38lv<br>--sofia: 5.30lv<br>total: 24.61lv<br>pesho petrov:<br>--plovdiv: 3.86lv (using card 630534)<br>--montana: 3.75lv (using card 630534)<br>--vidin: 2.69lv (using card 297296)<br>total: 10.30lv</td>
</tr>
<tr>
<td>3<br>ivan ivanov 094859<br>ceko cekov 328994<br>krali marko 774154<br>createTicket ivan ivanov montana 094859<br>createTicket ivan ivanov vidin 094859<br>createTicket ivan ivanov plovdiv 094859<br>createTicket krali marko vidin 774154<br>createTicket krali marko sofia 774154<br>createTicket bay ivan mezdra 000006<br>createTicket ceko cekov montana 328994<br>time to leave!</td>
<td>card 000006 is not valid!<br>ivan ivanov:<br>--plovdiv: 3.86lv (using card 094859)<br>--montana: 3.75lv (using card 094859)<br>--vidin: 2.69lv (using card 094859)<br>total: 10.30lv<br>bay ivan:<br>--mezdra: 6.43lv<br>total: 6.43lv<br>krali marko:<br>--vidin: 2.69lv (using card 774154)<br>--sofia: 2.65lv (using card 774154)<br>total: 5.34lv<br>ceko cekov:<br>--montana: 3.75lv (using card 328994)<br>total: 3.75lv</td>
</tr>
</tbody>
</table>

<p><b>Solution: <a href="./ex_04_train_system.py">ex_04_train_system.py</a></b></p>

<p><b>Author's Solution: <a href="../../resources/z_exams/exam_2018_03_11/04. Train System_Author's Solution.py">04. Train System_Author's Solution.py</a></b></p>

<p><b>Document with tasks description: <a href="../../resources/z_exams/exam_2018_03_11/04. Train System_Problem Description.docx">04. Train System_Problem Description.docx</a></b></p>