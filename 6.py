'''
    6. Write a Python program to convert all the characters in uppercase and lowercase
     and eliminate duplicate letters from a given sequence. Use map() function.
'''
def charuplow(s):
    return str(s).upper(),str(s).lower()
s = ["a","b","c","d","e","c","A","B","C"]
list1 = list(map(charuplow,s))
print(set(list1))

def change_cases(s):
  return str(s).upper(), str(s).lower()
chrars = {'a', 'b', 'E', 'f', 'a', 'i', 'o', 'U', 'a'}
print("Original Characters:\n",chrars)
result = map(change_cases, chrars)
print("\nAfter converting above characters in upper and lower cases\nand eliminating duplicate letters:")
print(set(result))

