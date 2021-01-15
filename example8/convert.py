#!/usr/bin/env python3
 
import csv
import datetime

# load input.csv into a variable `rows`
with open('input.csv') as f:
    rows = f.read()

# print(rows)

# parse `modeldate` in each row and sort the `rows` based on `modeldate`
from datetime import datetime

date_format = "%-d/%-m/%Y"

parsed_date = datetime.strptime(row['modeldate'], date_format)

date_str = parsed_date.strftime("%-m/%-d/%Y")
print(date_str)



# loop through the rows and output a csv, `output.csv` with the date and 6 different series:

with open('output.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['year','variableA','variableB','variableC','variableD', 'variableE', 'variableF'])

    for row in rows:
        writer.writerow([
			row['approve_estimate'],
			row['disapprove_estimate'],
			row['approve_hi'],
			row['approve_lo'],
			row['disapprove_hi'],
			row['disapprove_lo']

# don't forget the csv header. check dummy.csv

