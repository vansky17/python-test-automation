cities = ['Los Angeles', 'London', 'Tokyo']
print(cities[-1])

developer = ['Jane Doe', 23, 'Python Developer']
del developer[1]
print(developer)

programming_languages = ['Python', 'Java', 'C++', 'Rust']
if "Rust" in programming_languages:
    print("I want to learn Rust!")

developer = ['Alice', 25, ['Python', 'Rust', 'C++']]
print(developer[2][2])

developer = ['Alice', 34, 'Rust Developer']
name, age, job = developer

print(name) # 'Alice'
print(age) # 34
print(job) # 'Rust Developer'

developer = ['Alice', 34, 'Rust Developer']
name, *rest = developer

print(name) # 'Alice'
print(rest) # [34, 'Rust Developer']



numbers = [1, 2, 3, 4, 5]
numbers.append(7)
print(numbers)
numbers.pop(2)
print(numbers)
numbers.insert(2, 3.4)
print(numbers)
numbers.remove(3.4)
print(numbers)
numbers.clear()
print(numbers)
numbers = [19, 2, 35, 1, 67, 41]
numbers.sort()
print(numbers)
if 19 in numbers and 2 in numbers:
    print("Found the numbers!")

developer = ('Alice', 34, 'Rust Developer')
name, age, job = developer
print(name, age, job) # 'Alice'