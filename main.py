##import functions
##addition =  functions.add(5,4)
##print(addition)



##next method 

from newfolder.functions import add, mul,square, freq_table, movie_datasets,student_datasets
addition =  add(5,4)
print("REsult of addition is : {}".format(addition))
multiplication =  mul(5,4)
print("REsult of multiplication is : {}".format(multiplication))
s =  square(5)
print(s)

movie_genre_count = freq_table(datasets = movie_datasets, index_num = 1)
print(movie_genre_count)




student_gender_count = freq_table(datasets = student_datasets, index_num = 1)
print(student_gender_count)



