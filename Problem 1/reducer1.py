#!/usr/bin/env python3

# PROBLEM 1

import sys
from collections import Counter

def main(argv):
    
    current_key = None
    next_key = None
    orders = []
    
    for line in sys.stdin:
        line = line.strip()
        next_key, order = line.split('\t', 1)
        cust, value = order.split(",", 1)
        value = float(value)
        
        if next_key == current_key:
            orders.append({cust:value}) #add the current 'order' to the list
            
        else:
            if current_key:
                summation = Counter({})
                for item in orders:
                    summation += Counter(item) # adding values by cust.
                big_spender = max(summation, key=lambda key: summation[key])
                print('%s:%s' % (current_key, big_spender))
                # print the custID with the highest total value for the current_key.
                 
            # clear out/reset any variables necessary
            orders = [{cust:value}]
            current_key = next_key
    # end for loop
    
    if current_key == next_key:  # do whatever I have to to get the last output
        summation = Counter({})
        for item in orders:
            summation += Counter(item) # adding values by cust.
        big_spender = max(summation, key=lambda key: summation[key])
        print('%s:%s' % (current_key, big_spender))

if __name__ == "__main__":
    main(sys.argv)

# OUTPUT should be:
    # 2digitMonth,Country:CustomerID
  
# Reducer goal -- take each country-month key, sum up the lineValues BY CustomerID. Output
# the CustomerID with the highest spending.
# (print all tied top spending customer IDs)

