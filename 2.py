'''
    2. Write a Python program to add three given lists using Python map and lambda.
'''
list1 = [1,2,3]
list2 = [4,5,6]
list3 = [7,8,9]
list4 = list(map(lambda x,y,z: x+y+z,list1,list2,list3))
print(list4)