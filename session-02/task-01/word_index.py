#!/usr/bin/env python
import sys, string

# Program Description:
#
# Word Index is a program that takes a plain text file as input and
# outputs all the words contained in it
# sorted alphabetically along with the page numbers on which they occur.
# The program assumes that a page is a
# sequence of 45 lines, each line has max 80 characters, and there is no
# hyphenation. Additionally, Word Index
# must ignore all words that occur more than 100 times.


# Cookbook Style Description:
#   - Larger problem decomposed in procedural abstractions
#   - Larger problem solved as a sequence of commands, each corresponding to a procedure


# Global Constants:
#   Q1: Do the constants violate the style?
LINES_PER_PAGE = 45
MAX_SIZE_LINE = 80
STOP_FREQUENCY_LIMIT = 100

# Global Variables. Be sure to initialize them in the main
data = None
lines = None
word_freqs = None
# stop_words = None
word_index = None


def read_file(path_to_file):
    """
    Read the entire file in memory as sequence of chars"
    """
    global data

    with open(path_to_file) as f:
        data = data + list(f.read())

# Q: Does this violate the style?
def filter_chars_and_normalize():
    """
    Replacing all the non alphanumeric chars from the data with spaces,
    but keep the '\n'
    """

    global data
    # Q: Can you find a more pythonic way to implement this?
    #   Post it to the chat !
    for i in range(len(data)):
        if not data[i].isalnum():
            if data[i] != '\n':
                data[i] = ' '
        else:
            data[i] = data[i].lower()


def scan_lines():
    """
    Create a list of lines by creating a huge string and then splitting it on new lines
    """
    # Q: Is 'global data' required for this procedure to work?
    global data
    global lines

    data_str = ''.join(data)
    lines = lines + data_str.split('\n')


def frequencies():
    """
    Scan words in each line,
    count their frequency,
    update the stop words,
    store current page if not there yet
    """
    # Q: Does this procedure violate the style?
    # Q: Can this procedure be improved? If yes, how?
    global lines
    global word_freqs

    stop_words = []

    line_index = 0
    current_page = 0
    for line in lines:
        if line_index % LINES_PER_PAGE == 0:
            current_page += 1
        for w in line.split():
            keys = [wd[0] for wd in word_freqs]
            if w in keys:
                word_freqs[keys.index(w)][1] += 1
                if word_freqs[keys.index(w)][1] >= STOP_FREQUENCY_LIMIT:
                    stop_words.append(w)
                if current_page not in word_freqs[keys.index(w)][2]:
                    word_freqs[keys.index(w)][2].append(current_page)
            else:
                word_freqs.append([w, 1, [current_page]])
        line_index += 1


def sort():
    """
    Filter the word_index if the occur too often, sort them alphabetically
    """
    global word_freqs

    # Q: Does this procedure violate the style?
    # Q: Can this procedure be improved? If yes, how?
    word_freqs = list(filter(lambda x: x[1] < STOP_FREQUENCY_LIMIT, word_freqs))
    word_freqs.sort(key=lambda x: x[0], reverse=False)


def main(file_path):
    global data
    global lines
    global word_freqs
    # global stop_words
    global word_index

    # Initialize the global variables to ensure there will be no state pollution in tests
    data = []
    lines = []
    word_freqs = []
    # stop_words = []
    word_index = []

    # The Main as sequence
    read_file(file_path)
    filter_chars_and_normalize()
    scan_lines()
    frequencies()
    sort()

    # I could have implemented this into a print_all()
    for tf in word_freqs:
        print(tf[0], '-', str(tf[2])[1:-1])

if __name__ == "__main__":
    main(sys.argv[1])