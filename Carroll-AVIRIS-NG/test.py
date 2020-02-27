# Test program for argument parsing
import os
import sys
import pandas as pd
import argparse
from pandas import DataFrame


def main(args):
    
    phillies = pd.DataFrame({
        'Player':['Bryce Harper', 'J.T. Realmuto', 'Rhys Hoskins', 'Scott Kingery'],
        'Position':['Right Field', 'Catcher', 'First Base', 'Second Base'],
        'BA':[.260, .275, .226, .258],
        'RBI':[114, 83, 85, 55]})

    if args.json:
        phillies.to_json(args.output)
    else:
        phillies.to_csv(args.output, index=False, header=True)
     
     
def process_args():
    
    parser = argparse.ArgumentParser(description='Test program for argument parsing')
    
    parser.add_argument(
        "-j", "--json", default=False, action="store_true",
        help='Use True to have the output in json format')     
    
    parser.add_argument(
        "-c", "--clobber", default=False, action="store_true",
        help='Use True to force overwrite of existing CSV or JSON')     
    
    parser.add_argument(
        "output", type=str, help='Name of file to save results.',
        metavar="OUTPUT_FILE")  
    
    args = parser.parse_args()

    # Validate extension.
    basename, extension = os.path.splitext(args.output)
    if args.json:
        if extension != ".json":
            print("Output file [ {} ] is not a JSON. Exiting.".format(args.output))
            sys.exit(print(1))
    else:
        if extension != ".csv":
            print("output file [ {} ] is not a CSV. Exiting.".format(args.output))
            sys.exit(print(1))

    # Validate the input file and clobber argument.
    if os.path.isfile(args.output):
        if args.clobber is False:
            raise FileExistsError(args.output)
        else:
            print("Output file [ {} ] exists. Overwriting.".format(args.output))

    return args
    
     
     
if __name__ == "__main__":     

    args = process_args()
    
    main(args)      
    
    print(0)