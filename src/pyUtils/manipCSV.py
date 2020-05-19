import pyUtils
import csv
import re
import datetime
from collections import namedtuple

#-------------------------------------------------------------------------------------------------------------------
# Function to read CSV file and returns a map with the total number of crossings (`Value`)
# of each type of vehicle or equipment, or passengers or pedestrians, that crossed the border that month
#-------------------------------------------------------------------------------------------------------------------
def readCSV(csvfile, verbose=False):
    print(f'Start reading {csvfile}...')
    out_value = {}
    with open(csvfile) as f:
        f_csv = csv.reader(f)
        # Massage the first heading row with a regex substitution on non-valid identifier characters
        headings = [re.sub('[^a-zA-Z_]', '_', h) for h in next(f_csv)]
        # Using namedtuple instances since they are just as memory efficient as regular tuples, unlike dictionaries
        try:
            Row = namedtuple('Row',headings)
        except ValueError:
            print ("Unable to retrieve the namedtuple") # still need to handle this properly
        for r in f_csv:
            row = Row(*r)
            # Find first date of the month
            current = datetime.datetime.strptime( row.Date, '%m/%d/%Y %I:%M:%S %p')
            first = current.replace(day=1)
            if verbose: print(row.Border, row.Date, row.Measure, int(row.Value), 0)
            pyUtils.checkKey(out_value, (row.Border, row.Date, first, row.Measure), int(row.Value))
        print(f'Done reading {csvfile}...')
    return out_value


#-------------------------------------------------------------------------
# Write the output row to the CSV file
#-------------------------------------------------------------------------
def writeCSV(csvfile, out_rows, verbose=False):
    out_headers = ['Border', 'Date', 'Measure', 'Value','Average']
    with open(csvfile,'w') as f:
        f_csv = csv.writer(f)
        f_csv.writerow(out_headers)
        f_csv.writerows(out_rows)
    print(f'Done with analysis, saved to {csvfile}.')
