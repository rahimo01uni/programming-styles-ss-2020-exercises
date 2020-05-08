#!/usr/bin/env python

# Program Description:
#
# Word Index is a program that takes a plain text file as input and
# outputs all the words contained in it
# sorted alphabetically along with the page numbers on which they occur.
# The program assumes that a page is a
# sequence of 45 lines, each line has max 80 characters, and there is no
# hyphenation. Additionally, Word Index
# must ignore all words that occur more than 100 times.


# Monolithic Style Description:
#
#  - No abstractions
#  - No use of library functions (Let's start with no USER-DEFINED)
#

import sys, string

# Global Constants:
#   Q1: Can those be considered as abstractions? Of which type?
#   Q2: Do they violate the style?
LINES_PER_PAGE = 45
# TODO Do we even use this value? What does it happen if a line ('\n') is more than 80 char long?
# Assume this never happens...
MAX_SIZE_LINE = 80
STOP_FREQUENCY_LIMIT = 100


# Q3: Defining the main method ease testing, but does this count as violation of
# the style?
def main(file_path):
    # Logically Global variables - NOTE We need to define the "global" variable here otherwise,
    # during testing they will be NOT
    # reset to their initial (empty) value - This is an example of state pollution

    # This contains the words that appear more than STOP_FREQUENCY_LIMIT times in the text.
    # TODO Maybe a set instead of list would have been a better choice?
    stop_words = []

    # The index that contains the words and the pages on which they appear.
    # The idea is to store in the list 'data' objects (i.e., tuples) with the following content:
    # data[0]:  - Word
    # data[1]:  - Frequency
    # data[2]:  - list of Page Numbers (without duplicate entries)

    word_index = []

    # We adopt an approach similar to C. Lopes:
    # - we iterate the file line by line
    # -     while doing this we keep track on which page (and line) we currently are and parse each word
    # -     when we parse a new word we store the page on which it appears and increment its frequency
    # -         if a word appears more than a number of time, it becomes automatically a stop word and must be eliminated/filtered out
    # - Before printing we sort words alphabetically (all the words are normalized lowercase)


    line_index = 0
    current_page = 0

    # In this case, it is not necessary to append the '\n' at the end of the line
    with open(file_path, 'r') as f:
        # Original code was for line in open(file_path): but that was hardly mock-able?

        for line in f:
        # Q4: The line above could have been implemented as:
        # for line_index, line in enumerate(open(file_path)).
        # Would have that violated the style? YES

            # Compute the current page using the line_index. Pages START from 1
            if line_index % LINES_PER_PAGE == 0:
                current_page += 1

            # Parse the words and update the various data structures. This code is similar to the one implementing
            # the Word Frequency program
            start_char = None
            i = 0
            for c in line:

                if start_char is None:
                    if c.isalnum():
                        # We found the start of a word
                        start_char = i
                else:
                    if not c.isalnum():
                        # We found the end of a word. Process it
                        found = False
                        word = line[start_char:i].lower()

                        # Ignore stop words:
                        # Q5: Can this ('not in') be considered a violation of the style?
                        # What would be an alternative
                        # implementation of this check?
                        if word not in stop_words:
                            # Let's see if it already exists.
                            for data in word_index[:]:  # Loop over a slice copy of the entire list.
                                # Q6: Why a copy a not the actual data?
                                # Q7: Could this ('[:]') be considered a violation of the style?
                                if word == data[0]:  # Word

                                    found = True

                                    # Increment Frequency
                                    data[1] += 1

                                    # Record Page Numbers. This must account for duplicates:
                                    # Q8: Any violations here? What about using a set instead of a list?
                                    if current_page not in data[2]:
                                        data[2].append(current_page)

                                    if data[1] > STOP_FREQUENCY_LIMIT:
                                        # Move word from word_index to stop_words
                                        stop_words.append(word)
                                        word_index.remove(data)
                                    break

                            if not found:
                                # Using set {} does not guarantee that the output string shows the pages in order !
                                data = [word, 1, [current_page]]
                                inserted = False
                                index = 0

                                # Ensure that every new word that we add is placed in the right place considering the
                                # alphabetic order
                                while index < len(word_index): # this time we iterate on the actual list and not a copy.
                                    # However, we do not iterate over the values but by index.
                                    if word < word_index[index][0]: # Check: https://thepythonguru.com/python-strings/
                                        # Q9: Does using "string-comparison" count as a violation of the style?
                                        word_index.insert(index, data)
                                        inserted = True
                                        break
                                    index += 1

                                # word is the last word
                                if not inserted:
                                    word_index.append(data)

                        # Let's reset
                        start_char = None

                # Move "line-cursor" forward
                i += 1

            # Move "page-cursor" one line below
            line_index += 1

    for tf in word_index:
        # Q10: Is this ('[1:-1]') a violation? What does it even mean ?!
        print(tf[0], '-', str(tf[2])[1:-1])


if __name__ == "__main__":
    main(sys.argv[1])