#step1: Importing argparse
import argparse

#step2 : creating an parser object
parser = argparse.ArgumentParser()


#step 3 : Adding arguments
parser.add_argument('-f', "--file", required = True, help = "name of a file")


#step4 : parsing the argument parser
args = parser.parse_args()


file =  open(args.file, 'r')
data = file.read()
print(data)
file.close()
