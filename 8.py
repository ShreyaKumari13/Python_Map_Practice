'''
    8. Write a Python program to convert a given list of integers and a tuple of integers in a list of strings.
'''
list1 = [1,2,3]
list2 = (4,5,6)
list3 = list(map(str,list1))
list4 = tuple(map(str,list2))
print(list3)
print(list4)

