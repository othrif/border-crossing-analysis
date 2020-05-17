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


class Crossing(namedtuple('Crossing', ['Border', 'Date', 'Measure', 'Value'])):

    def __lt__(self, other):
        return self.time < other.time

    def addVal(self, val):
        if key not in self.dict:
            self.dict[self.key] = val
        else:
            self.dict[self.key] += val


def read_crossings(csvfile, _strptime=datetime.datetime.strptime):
    with open(csvfile) as f:
        f_csv = csv.reader(f)
        # Massage the first heading row with a regex substitution on non-valid identifier characters
        headings = [re.sub('[^a-zA-Z_]', '_', h) for h in next(f_csv)]
        # Using namedtuple instances since they are just as memory efficient as regular tuples, unlike dictionaries
        try:
            Row = namedtuple('Row',headings)
        except ValueError:
            print ("Error") # still need to handle this properly
        for r in f_csv:
            row = Row(*r)
            yield Crossing(row.Border, row.Date, row.Measure,int(row.Value))



crossings = tuple(read_crossings(args.input_file))

print(crossings)
