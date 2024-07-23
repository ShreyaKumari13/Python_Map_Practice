'''
    1. Write a Python program to triple all numbers of a given list of integers. Use Python map.
'''
list1 = [1,2,3]
list2 = list(map(lambda x: x+x+x,list1))
print(list2)