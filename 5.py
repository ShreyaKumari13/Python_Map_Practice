'''
    5. Write a Python program to square the elements of a list using map() function.
'''
list1 = [1,2,3,4]
list2 = list(map(lambda x:x**x,list1))
print(list2)

#according to question -->>

def square_num(n):
    return n*n
list1 = [1,2,3,4]
list2 = list(map(square_num,list1))
print(list2)