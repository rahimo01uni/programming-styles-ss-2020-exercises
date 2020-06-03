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

#
# The Plugins Style Description:
#
# - The problem is decomposed using some form of abstraction
#   (procedures, functions, objects, etc.)
# 
# - All or some of those abstractions are physically encapsulated into
#   their own, usually pre-compiled, packages. Main program and each of
#   the packages are compiled independently. These packages are loaded
#   dynamically by the main program, usually in the beginning (but not
#   necessarily).
# 
# - Main program uses functions/objects from the dynamically-loaded
#   packages, without knowing which exact implementations will be
#   used. New implementations can be used without having to adapt or
#   recompile the main program.
# 
# - External specification of which packages to load. This can be done
#   by a configuration file, path conventions, user input or other
#   mechanisms for external specification of code to be linked at run
#   time.
#
def main():
    # Load the plugins from the ./plugins folder !
    pass

if __name__ == "__main__":
    main(sys.argv)