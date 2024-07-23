'''
    4. Write a Python program to create a list containing the power of said number
     in bases raised to the corresponding number in the index using Python map.
'''
list1 = [10,20,30,40,50]
base_index = [0,1,2,3,4]
list2 = list(map(pow,list1,base_index))
print(list2)