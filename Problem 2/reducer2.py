#!/usr/bin/env python3

import sys

def main(argv):
    current_key = None
    current_count = 0
    next_key = None
    
    for line in sys.stdin:
        #line = line.strip()
        next_key, count = line.split('\t', 1)
        count = int(count)
        if next_key == current_key:
            current_count += count
        else:
            if current_key:
                print('%s:%s' % (current_key, current_count))
            current_count = count
            current_key = next_key
            
    if next_key == current_key:  #getting the last input
        print('%s:%s' % (current_key, current_count))
        
#Note there are two underscores around name and main
if __name__ == "__main__":
    main(sys.argv)