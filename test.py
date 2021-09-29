'''
Test anything you want to known
'''

str = "jack 20000 25"

str = str.strip()
print(str)

array = str.split(' ')
print(type(array))
print(array)

list = [s for s in array if s]
print(list)