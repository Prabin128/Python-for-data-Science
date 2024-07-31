#step1: Importing argparse
import argparse

#step2 : creating an parser object
parser = argparse.ArgumentParser()


#step 3 : Adding arguments
parser.add_argument('-f', "--file", required = True, help = "first number")
parser.add_argument('-f1', "--file1", required = True, help = "second number")


#step4 : parsing the argument parser
args = parser.parse_args()

def add(a, b):
    result = (int(a)+ int(b)) 
    return result
output = add(args.file, args.file1)
print(output)