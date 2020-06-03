#!/usr/bin/env python
import sys, re, operator, string

# Program Description:
#
# Word Index is a program that takes a plain text file as input and
# outputs all the words contained in it
# sorted alphabetically along with the page numbers on which they occur.
# The program assumes that a page is a
# sequence of 45 lines, each line has max 80 characters, and there is no
# hyphenation. Additionally, Word Index
# must ignore all words that occur more than 100 times.


# Closed-Map Style Description:
#
# - The larger problem is decomposed into 'things' that make sense for
#   the problem domain
#
# - Each 'thing' is a map from keys to values. Some values
#   are procedures/functions.

def initDataStorageManager(obj, path_to_file):
    with open(path_to_file) as f:
        # Q1: Is this a violation of the style? Should we use obj['data'] instead ?
        data = f.read()

    obj['_lines'] = data.split('\n')
    pattern = re.compile('[\W_]+')
    for idx in range(len(obj['_lines'])):
        obj['_lines'][idx] = pattern.sub(' ', obj['_lines'][idx]).lower()
    # Q2: Is this a violation of the style?
    obj['_lines'] = list(filter(lambda x: len(x) > 0, obj['_lines']))


def retrieveNextLine(obj):
    obj['_currentLine'] += 1
    return obj['_lines'][obj['_currentLine'] -1].split()


def increment_word_count(obj, word, page):
    if word in obj['_word_freqs']:
        obj['_word_freqs'][word] = (obj['_word_freqs'][word][0] + 1, obj['_word_freqs'][word][1])
        # Avoid duplicates
        if page not in obj['_word_freqs'][word][1]:
            obj['_word_freqs'][word][1].append(page)
    else:
        obj['_word_freqs'][word] = (1, [page])


def get_filtered_sorted_output(self_obj):
    self_obj['_word_freqs'] = {k: v for k, v in self_obj['_word_freqs'].items() if v[0] <= 100}
    return sorted(self_obj['_word_freqs'].items())

def main(file_path):

    dataStorageManagerObject = {
        # Fields declaration
        '_currentLine': 0,
        '_lines': [],
        # Methods declaration
        'init': lambda path_to_file: initDataStorageManager(dataStorageManagerObject, path_to_file),
        'has_next_line': lambda: dataStorageManagerObject['_currentLine'] < len(dataStorageManagerObject['_lines']),
        'next_line': lambda: retrieveNextLine(dataStorageManagerObject),
        # THIS IS NOT A VIOLATION
        'line_number': lambda: dataStorageManagerObject['_currentLine']
    }
    dataStorageManagerObject['init'](file_path)

    word_frequency_manager_object = {
        # Fields declaration
        '_word_freqs': {},
        # Methods declaration
        'increment_count': lambda word, page: increment_word_count(word_frequency_manager_object, word, page),
        'filter_and_sort': lambda: get_filtered_sorted_output(word_frequency_manager_object)
    }

    while dataStorageManagerObject['has_next_line']():
        words = dataStorageManagerObject['next_line']()
        line_number = dataStorageManagerObject['line_number']()

        for w in words:
            word_frequency_manager_object['increment_count'](w, int(line_number/ 45) + 1)

    word_freqs = word_frequency_manager_object['filter_and_sort']()
    for tf in word_freqs:
        print(tf[0], '-', str(tf[1][1])[1:-1])


if __name__ == "__main__":
    main(sys.argv[1])