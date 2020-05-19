import pyUtils





import math
import argparse


args = pyUtils.getArgs()



out_rows = []
out_value = pyUtils.readCSV(args.input_file,args.verbose)

_Border = 0
_Date = 1
_FirstDate = 2
_Measure = 3

print(f'... doing analysis')
if args.verbose: print('-'*100)
average = {}
sum = {}
for key, value in out_value.items():
    if args.verbose: print(f'Before {key}:')
    sum[(key[_Border],key[_Date],key[_FirstDate])] = 0
    earliestDate = key[_FirstDate]
    for key2, value2 in out_value.items():
        if key is not key2:
            if args.verbose: print({key2})
            if key[_FirstDate] > key2[_FirstDate] and key[_Border] == key2[_Border]and key[_Measure] == key2[_Measure]:
                if args.verbose: print(f'{key2[_FirstDate]} -> {value2}')
                sum[(key[_Border],key[_Date],key[_FirstDate])] += value2
                if key2[_FirstDate] < earliestDate:
                    earliestDate = key2[_FirstDate]
    num_months = pyUtils.diff_month(key[_FirstDate],earliestDate)
    if num_months != 0:
        average[(key[_Border],key[_Date],key[_FirstDate])] = math.ceil(sum[(key[_Border],key[_Date],key[_FirstDate])]/num_months)
    else:
        average[(key[_Border],key[_Date],key[_FirstDate])] = 0
    if args.verbose:
        print(f'SUM = {sum[(key[_Border],key[_Date],key[_FirstDate])]}')
        print(f'Months = {num_months}')
        print(f'Average = {average[(key[_Border],key[_Date],key[_FirstDate])]}')
        print("Next...")
    out_rows.append( (key[_Border], key[_Date], key[_Measure] ,value,average[(key[_Border],key[_Date],key[_FirstDate])]) )

# key:  (row.Border, row.Date, row.Measure, row.Value, avg)
# Sort list
out_rows.sort(key=lambda tup: (tup[1],tup[3],tup[2],tup[0]),reverse=True)


pyUtils.writeCSV(args.output_file, out_rows,args.verbose)