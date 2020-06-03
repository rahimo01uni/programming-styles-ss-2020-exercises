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

#
# The Dataspaces Style Description:
#
# - Existence of one or more units that execute concurrently
# 
# - Existence of one or more data spaces where concurrent units store and
#   retrieve data
# 
# - No direct data exchanges between the concurrent units, other than via the data spaces
# 
#
def main():
    pass

if __name__ == "__main__":
    main(sys.argv[1])