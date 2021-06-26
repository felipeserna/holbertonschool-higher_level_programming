# holbertonschool-higher_level_programming

This repository has a lot of projects for learning higher level programming
mostly with Python3. Some other projects are for learning databases with
SQL, and other projects are for learning higher level programming with
JavaScript.

## Requirements for Python projects
**General**
* Allowed editors: `vi`, `vim`, `emacs`
* All your files will be interpreted/compiled on Ubuntu 14.04 LTS using `python3` (version 3.4.3)
* All your files should end with a new line
* The first line of all your files should be exactly `#!/usr/bin/python3`
* A `README.md` file, at the root of the folder of the project, is mandatory
* Your code should be documented
* Your code should use the `PEP 8` style (version 1.7.x)
* All your files must be executable

## Requirements for JavaScript projects
**General**
* Allowed editors: `vi`, `vim`, `emacs`
* All your files will be interpreted on Ubuntu 14.04 LTS using `node` (version 10.14.x)
* All your files should end with a new line
* The first line of all your files should be exactly `#!/usr/bin/node`
* A `README.md` file, at the root of the folder of the project, is mandatory
* Your code should be `semistandard` compliant. [Rules of Standard](https://standardjs.com/rules.html) + [semicolons on top](https://github.com/standard/semistandard). Also as reference: [AirBnB style](https://github.com/airbnb/javascript)
* All your files must be executable
* The length of your files will be tested using `wc`
* You are not allowed to use `var`

## Requirements for SQL projects
**General**
* Allowed editors: `vi`, `vim`, `emacs`
* All your files will be executed on Ubuntu 14.04 LTS using `MySQL 5.7` (version 5.7.8-rc)
* All your files should end with a new line
* All your SQL queries should have a comment just before (i.e. syntax above)
* All your files should start by a comment describing the task
* All SQL keywords should be in uppercase (`SELECT`, `WHERE`…)
* A `README.md` file, at the root of the folder of the project, is mandatory
* The length of your files will be tested using `wc`

## Example of Python Project Task
**Hexadecimal printing**

Write a program that prints all numbers from `0` to `98` in decimal and in hexadecimal (as in the following example)

* You can only use one `print` function with string format
* You can only use one loop in your code
* You are not allowed to store numbers or strings in a variable
* You are not allowed to import any module
```
$ ./4-print_hexa.py
0 = 0x0
1 = 0x1
2 = 0x2
3 = 0x3
4 = 0x4
5 = 0x5
6 = 0x6
7 = 0x7
8 = 0x8
9 = 0x9
10 = 0xa
11 = 0xb
12 = 0xc
13 = 0xd
14 = 0xe
15 = 0xf
16 = 0x10
17 = 0x11
18 = 0x12
...
96 = 0x60
97 = 0x61
98 = 0x62
$
```

## Example of JavaScript Project Task
**Loop to languages**

Write a script that prints 3 lines by using an array of string and a loop

* The first line: “C is fun”
* The second line: “Python is cool”
* The third line: “JavaScript is amazing”
* You must use `console.log(...)` to print all output
* You are not allowed to use `var`
* You are not allowed to use any `if/else` statement
* You can use only one `console.log`
* You must use a loop (`while`, `for`, etc.)
```
$ ./6-multi_languages_loop.js 
C is fun
Python is cool
JavaScript is amazing
$
```

## Example of SQL Project Task
**Genre ID by show**

Import the database dump from `hbtn_0d_tvshows` to your MySQL server: [download](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql)

Write a script that lists all shows contained in `hbtn_0d_tvshows` that have at least one genre linked.

* Each record should display: `tv_shows.title` - `tv_show_genres.genre_id`
* Results must be sorted in ascending order by `tv_shows.title` and `tv_show_genres.genre_id`
* You can use only one `SELECT` statement
* The database name will be passed as an argument of the `mysql` command
```
$ cat 10-genre_id_by_show.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
Enter password: 
title   genre_id
Breaking Bad    1
Breaking Bad    6
Breaking Bad    7
Breaking Bad    8
Dexter  1
Dexter  2
Dexter  6
Dexter  7
Dexter  8
Game of Thrones 1
Game of Thrones 3
Game of Thrones 4
House   1
House   2
New Girl    5
Silicon Valley  5
The Big Bang Theory 5
The Last Man on Earth   1
The Last Man on Earth   5
$
```

I think that as I already knew programming in C, I had a strong background in Low Level, and for
that reason I felt that Python was easier for me. Python was built on C, however I noticed that
pointers didn't exist in Python. Other things I noticed were the lack of semicolons (;) and curly
braces ({}). I also realized that errors in Python are easier to understand than errors in C.
The most difficult challenges encountered were about how to manipulate JSON data in JavaScript Projects.

## Author:
Felipe Serna <1509@holbertonschool.com>

Chemical Engineer with skills in the design of industrial processes for the elaboration of new products with added value, taking into account economic, environmental and safety restrictions. Knowledge in water treatment, integrated management systems HSEQ and GLP. High interest in fats and oils, particularly for the manufacture of biodiesel. In his Chemical Engineering thesis he designed and built the first microreactor in Colombia for manufacturing biodiesel.

[LinkedIn profile](https://www.linkedin.com/in/felipesernabarbosa/)

[Twitter](https://twitter.com/felipesernabar1)

[Portfolio Project repository](https://github.com/felipeserna/Portfolio_Foundations)
