

#-------------------------------------------------------------------------
# Common command line option parser
#-------------------------------------------------------------------------
def getArgs():
    import argparse

    parser = argparse.ArgumentParser(description='Program to analyze the number of vehicles, equipment, passengers and pedestrians crossing into the United States by land.')

    parser.add_argument('-i', '--input', metavar='input_file', required=False, dest='input_file', action='store', default='./input/dummy.csv', help='Input csv file')
    parser.add_argument('-o', '--output', metavar='output_file', required=False, dest='output_file', action='store', default='./output/out_dummy.csv', help='Output csv file with results')
    parser.add_argument('-v', '--verbose', dest='verbose', action='store_true', help='Verbose mode')

    args = parser.parse_args()

    return args