#!/usr/bin/env python3
 
import csv
from datetime import datetime

# load input.csv into a variable `rows`

date_format_input = "%m/%d/%Y"
date_format_output = "%Y-%m-%d"

with open('input.csv') as f:
	reader = csv.DictReader(f)
	rows = list(reader)
# print(rows)
# parse `modeldate` in each row and sort the `rows` based on `modeldate`
	for row in rows:
		row['modeldate'] = datetime.strptime(row['modeldate'], date_format_input)

# sort the `rows` based on `modeldate`
rows = sorted(rows, key=lambda x: x['modeldate'])

# loop through the rows and output a csv, `output.csv` with the date and 6 different series:

with open('output.csv', 'w') as f:
	writer = csv.writer(f)
	writer.writerow(['year','variableA','variableB','variableC','variableD', 'variableE', 'variableF'])

	for row in rows:
		writer.writerow([
			row['modeldate'].strftime(date_format_output),
			row['approve_estimate'],
			row['disapprove_estimate'],
			row['approve_hi'],
			row['approve_lo'],
			row['disapprove_hi'],
			row['disapprove_lo']
		])

# don't forget the csv header. check dummy.csv
