#!/usr/bin/env python3

import sys
import re

def main(argv):
    vowels = "aeiouy"
    line = sys.stdin.readline()
    pattern = re.compile("[a-zA-Z0-9]+")
    
    while line:
        for word in pattern.findall(line):
            word = list(word.lower())
            result = ""
            for char in word:
                if char in vowels:
                    result += char  # save the vowels
            # end inside for loop
            result = "".join(sorted(result))
            print(result+"\t"+"1")
        # end outter for loop
            
        line = sys.stdin.readline()
#Note there are two underscores around name and main
if __name__ == "__main__":
    main(sys.argv)
