from collections import namedtuple
import csv
import re
import datetime
import math
import argparse

parser = argparse.ArgumentParser(description='Program to analyze the number of vehicles, equipment, passengers and pedestrians crossing into the United States by land.')
parser.add_argument('-i', '--input', metavar='input_file', required=False, dest='input_file', action='store', default='./input/dummy.csv', help='Input csv file')
parser.add_argument('-o', '--output', metavar='output_file', required=False, dest='output_file', action='store', default='./output/out_dummy.csv', help='Output csv file with results')
parser.add_argument('-v', '--verbose', dest='verbose', action='store_true', help='Verbose mode')
args = parser.parse_args()


def checkKey(dict, key, val):
    if key not in dict:
        dict[key] = val
    else:
        dict[key] += val

def diff_month(d1, d2):
    return (d1.year - d2.year) * 12 + d1.month - d2.month


print(f'Start reading {args.input_file}...')
out_rows = []
out_value = {}
with open(args.input_file) as f:
    f_csv = csv.reader(f)
    # Massage the first row, heading row, with a regex substitution on non-valid identifier characters
    headings = [re.sub('[^a-zA-Z_]', '_', h) for h in next(f_csv)]

# Using namedtuple instances since they are just as memory efficient as regular tuples, unlike dictionaries
    try:
        Row = namedtuple('Row',headings)
    except ValueError:
        print ("Error") # still need to handle this properly
    for r in f_csv:
        row = Row(*r)
        # Find first date of the month
        current = datetime.datetime.strptime( row.Date, '%m/%d/%Y %I:%M:%S %p')
        first = current.replace(day=1)
        if args.verbose: print(row.Border, row.Date, row.Measure, int(row.Value), 0)
        checkKey(out_value, (row.Border, row.Date, first, row.Measure), int(row.Value))

print(f'... doing analysis')
if args.verbose: print('-'*100)
average = {}
sum = {}
for key, value in out_value.items():
    if args.verbose: print(f'Before {key}:')
    sum[(key[0],key[1],key[2])] = 0
    earliestDate = key[2]
    for key2, value2 in out_value.items():
        if key is not key2:
            if args.verbose: print({key2})
            if key[2] > key2[2] and key[0] == key2[0]and key[3] == key2[3]:
                if args.verbose: print(f'{key2[2]} -> {value2}')
                sum[(key[0],key[1],key[2])] += value2
                if key2[2] < earliestDate:
                    earliestDate = key2[2]
    num_months = diff_month(key[2],earliestDate)
    if num_months != 0:
        average[(key[0],key[1],key[2])] = math.ceil(sum[(key[0],key[1],key[2])]/num_months)
    else:
        average[(key[0],key[1],key[2])] = 0
    if args.verbose:
        print(f'SUM = {sum[(key[0],key[1],key[2])]}')
        print(f'Months = {num_months}')
        print(f'Average = {average[(key[0],key[1],key[2])]}')
        print("Next...")
    out_rows.append( (key[0], key[1], key[3] ,value,average[(key[0],key[1],key[2])]) )

# key:  (row.Border, row.Date, row.Measure, row.Value, avg)
# Sort list
out_rows.sort(key=lambda tup: (tup[1],tup[3],tup[2],tup[0]),reverse=True)

# Output file:
out_headers = ['Border', 'Date', 'Measure', 'Value','Average']
with open(args.output_file,'w') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(out_headers)
    f_csv.writerows(out_rows)
print(f'Done with analysis, saved to {args.output_file}.')
