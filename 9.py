'''
    9. Write a Python program to create a new list taking specific elements from a tuple and convert a string value to integer.
'''
list1 = [("shreya",'1'),("shruti",'2'),("raja",'3')]
list2 = list(map(lambda x:x[0],list1))
list3 = list(map(lambda x:int(x[1]),list1))
print(list2)
print(list3)