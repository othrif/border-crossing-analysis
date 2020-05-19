

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


#---------------------------------------------------------------------
# Make logger object
#
def getLog(name, level = 'INFO', debug=False):

    import logging
    import sys

    f = logging.Formatter("%(name)s: %(levelname)s - %(message)s")
    h = logging.StreamHandler(sys.stdout)
    h.setFormatter(f)

    log = logging.getLogger(name)
    log.addHandler(h)

    if debug:
        log.setLevel(logging.DEBUG)
    else:
        if level == 'DEBUG':   log.setLevel(logging.DEBUG)
        if level == 'INFO':    log.setLevel(logging.INFO)
        if level == 'WARNING': log.setLevel(logging.WARNING)
        if level == 'ERROR':   log.setLevel(logging.ERROR)

    return log
