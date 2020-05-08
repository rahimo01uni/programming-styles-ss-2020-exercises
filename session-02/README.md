Programming Styles -- SoSe20
---

# Exercise 02

Implement the Word Index program using the **Cookbook Style** and the **Pipeline Style**.

Word Index is a program that takes a plain text file as input and outputs all the words contained in it sorted alphabetically along with the page numbers on which they occur. The program assumes that a page is a sequence of 45 lines, each line has max 80 characters, and there is no hyphenation. Additionally, Word Index must ignore all words that occur more than 100 times.

For both tasks there's already an empty `word_index.py` that you can fill.

## Task 1: The Cookbook Style

To complete this task you must:

1. Implement the Word Index program using the **Cookbook Style** 
2. Implement at least three new tests in Python that make use of *temporary files*. Check that after the test execution the temporary files are automatically removed.

## Task 2: The Pipeline Style

To complete this task you must:

1. Implement the Word Index program using the **Pipeline Style** 
2. Implement at least one test for each function that is used inside the pipeline. Tests must make use of *mocks* to break dependencies.
