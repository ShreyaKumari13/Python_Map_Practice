'''
    7. Write a Python program to add two given lists and find the difference between lists. Use map() function.
'''
list1 = [1,2,3]
list2 = [4,5,6]
list3 = list(map(lambda x,y:x+y,list2,list1))
list4 = list(map(lambda x,y:x-y,list2,list1))
print(list3)
print(list4)

def sum_minus(x,y):
    return x+y,x-y
list1 = [1,2,3]
list2 = [4,5,6]
list3 = list(map(sum_minus,list2,list1))
print(list3)

