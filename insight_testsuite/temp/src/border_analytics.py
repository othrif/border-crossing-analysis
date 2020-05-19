import pyUtils

def main():

    args = pyUtils.getArgs()
    log = pyUtils.getLog('border_analytics')

    log.info('Starting the program...')
    print(type(args.nmax), args.nmax)
    out_value = pyUtils.readCSV(args.input_file,args.verbose,int(args.nmax))
    log.info('Starting the analysis...')
    out_rows = pyUtils.doAnalysis(out_value)
    log.info('Saving the output...')
    pyUtils.writeCSV(args.output_file, out_rows,args.verbose)
    log.info('Done with the program.')

#-----------------------------------------------------------------------------------------
# Main function for command line execution
#-----------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()