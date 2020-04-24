Programming Styles -- SoSe20
---

# Exercise 01

## Task 1: Setup
During this class, we will use Python (v3.7), Java (JDK11) and JavaScript (NodeJS v10.20) for the exercise sessions and the assignments. 

To complete this task you must:

1. Install the required versions of Python, Java and JavaScript.
2. Implement the "Hello world" program with all the languages.
3. Execute all the programs and checking that they work correctly

Please follow the installation instructions listed in the [`instructions file`](./instructions.md).

> NOTE: The installation instructions describe only some of the possible ways to install the required software, hence they are incomplete. If you find better, simpler, or simply different ways to install the required software feel free to contribute to them to the repository.

## Task 2: The Monolithic Style
Implement the Word Index program using the **Monolithic Style**.

Word Index is a program that takes a plain text file as input and outputs all the words contained in it sorted alphabetically along with the page numbers on which they occur. The program assumes that a page is a sequence of 45 lines, each line has max 80 characters, and there is no hyphenation. Additionally, Word Index must ignore all words that occur more than 100 times.

To complete this task you must:

1. Implement Word Index in Python. An empty `word_index.py` file is already given to you.
2. Implement at least three tests in Python using [`unittest`](https://docs.python.org/3/library/unittest.html). An example of unittest, `sample_unittest.py` is already given to you.