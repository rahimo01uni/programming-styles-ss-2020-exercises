#!/usr/bin/env python
import sys, string

def main(file_path):
    # the global variables
    stop_words = []
    # The index that contains the words and their pages. Are pages handled using sets?
    # Keep the frequency and use it as filter to decide on stop words?
    word_index = []

    # 45 lines make a page
    page_limit = 45
    stop_words_threshold = 100

    # iterate through the file one line at a time
    line_index = 0
    current_page = 0

    with open(file_path) as f:
        for line in f:
            # Compute the current page using the line_index
            if line_index % page_limit == 0:
                current_page += 1

            # Parse the words and update the data structures
            start_char = None
            i = 0
            for c in line:
                if start_char == None:
                    if c.isalnum(): # We found the start of a word
                        start_char = i
                else:
                    if not c.isalnum(): # We found the end of a word. Process it
                        found = False
                        word = line[start_char:i].lower()
                        # Ignore stop words
                        if word not in stop_words:
                            # Let's see if it already exists.
                            for data in word_index[:]:  # Loop over a slice copy of the entire list.
                                if word == data[0]:  # Word
                                    # Frequency
                                    data[1] += 1
                                    # Page Numbers. This must account for duplicates:
                                    if current_page not in data[2]:
                                        data[2].append(current_page)
                                    found = True
                                    if data[1] > stop_words_threshold:
                                        stop_words.append(word)
                                        word_index.remove(data)
                                    break

                            if not found:
                                # Using set {} does not guarantee that the output string shows the pages in order !
                                data = [word, 1, [current_page]]
                                inserted = False
                                index = 0
                                while index < len(word_index): # this time we iterate on the actual list and not a copy but by index
                                    if word < word_index[index][0]:
                                        word_index.insert(index, data)
                                        inserted = True
                                        break
                                    index += 1
                                if not inserted:
                                    word_index.append( data )
                        # Let's reset
                        start_char = None
                i += 1
            line_index += 1

    result = []
    for tf in word_index:
        result.append( " ".join([tf[0], '-', str(tf[2])[1:-1]]))
    # Make sure that also the last line is terminated with '\n'
    result.append("")

    return "\n".join(result)