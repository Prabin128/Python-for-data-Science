
def add(a,b):
    result = a+b
    return result


def mul(a,b):
    result = a*b
    return result

def square(num):
    return num *num



from datasets import *  

#import datasets
def freq_table(datasets,index_num):
    freq_dict = {}
    for item in datasets[1:]:
        if item[index_num] not in freq_dict:
            freq_dict[item[index_num]] = 1
        else:
            freq_dict[item[index_num]] += 1
    return freq_dict



from csv import reader

def read_csv(file):
    f = open(file)
    data = reader(f)
    dataset = list(data)
    return dataset
