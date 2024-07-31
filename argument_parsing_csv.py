#step1: Importing argparse
import argparse
from functions import read_csv

#step2 : creating an parser object
parser = argparse.ArgumentParser()


#step 3 : Adding arguments
parser.add_argument('-c', "--csv", required = True, help = "reading csv file")



#step4 : parsing the argument parser
args = parser.parse_args()

dataset = read_csv(args.csv)
print(dataset)