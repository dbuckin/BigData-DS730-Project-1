# PROBLEM 1

#!/usr/bin/env python3

import sys

def main(argv):
    row = sys.stdin.readline()
    while row:
        row = row.strip()
        splitted = row.split(",")
        if "invoice" in splitted[0].lower(): # If this is the first row, pass. (Perhaps this does nothing?)
            pass # skip and go to the next row.
        if "c" in splitted[0].lower() or splitted[6] == "":
            pass # skip and go to the next row.
        else:
            datesplit = splitted[4].split("/")
            month = datesplit[0] # extracting month
            country = splitted[7] # extracting country
            country.strip()
            lineValue = float(splitted[3])*float(splitted[5]) # calculating the line value
            cust = round(float(splitted[6])) # formatting custID properly.
            print(month+","+country+"\t"+str(cust)+","+str(lineValue))
            
        row = sys.stdin.readline() # read in the next line  
        
if __name__ == "__main__":
    main(sys.argv)

# Mapper goal -- each country-month key "\t" and all the CustomerIDs and (quantity * price)
    # for that country-month.


    

    
