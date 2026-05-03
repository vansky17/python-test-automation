print('My favorite colors are', 'blue', 'green', 'red')
print(type('blue'))
print(isinstance('blue', str))
print(isinstance(7, bool))
my_str_4 = '''Another another example of a
multiline and triple quoted
string'''
print(my_str_4)

print(len(my_str_4))
print("line " in my_str_4)
if "line " in my_str_4:
    print("Found it!")