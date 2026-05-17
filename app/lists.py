# cities = ['Los Angeles', 'London', 'Tokyo']
# print(cities[-1])

# developer = ['Jane Doe', 23, 'Python Developer']
# del developer[1]
# print(developer)

# programming_languages = ['Python', 'Java', 'C++', 'Rust']
# if "Rust" in programming_languages:
#     print("I want to learn Rust!")

# developer = ['Alice', 25, ['Python', 'Rust', 'C++']]
# print(developer[2][2])

# developer = ['Alice', 34, 'Rust Developer']
# name, age, job = developer

# print(name) # 'Alice'
# print(age) # 34
# print(job) # 'Rust Developer'

# developer = ['Alice', 34, 'Rust Developer']
# name, *rest = developer

# print(name) # 'Alice'
# print(rest) # [34, 'Rust Developer']



# numbers = [1, 2, 3, 4, 5]
# numbers.append(7)
# print(numbers)
# numbers.pop(2)
# print(numbers)
# numbers.insert(2, 3.4)
# print(numbers)
# numbers.remove(3.4)
# print(numbers)
# numbers.clear()
# print(numbers)
# numbers = [19, 2, 35, 1, 67, 41]
# numbers.sort()
# print(numbers)
# if 19 in numbers and 2 in numbers:
#     print("Found the numbers!")

# developer = ('Alice', 34, 'Rust Developer')
# name, age, job = developer
# print(name, age, job) # 'Alice'

# numbers = [1, 2, 4, 5]
# numbers.insert(2, 3)
# print(numbers) # [1, 2, 3, 4, 5]

# numbers = [1, 0, 2, 0, 3, 0, 4]
# while 0 in numbers:
#     numbers.remove(0)
# print(numbers)

# letters = ['a', 'b', 'c', 'd', 'e']
# middle= letters.pop(len(letters) // 2   )  # Remove and return the middle element
# print(middle) # 'c'

# numbers.sort(reverse=True)
# print(numbers)
# sorted_numbers = sorted(numbers)
# print(sorted_numbers)

# text = "This is a sample text to keep the words in it."
# print(text.count('s'))  
# for num in range(2, 11, 2):
#     print(num)

# fruits = ['apple', 'banana', 'orange']
# for index, fruit in enumerate(fruits):
#     print(f"Index {index} and fruit {fruit}")

# names = ['Alice', 'Bob', 'Charlie']
# scores = [85, 92, 78]
# pairs = list(zip(names, scores))
# print(pairs)  # [('Alice', 85), ('Bob', 92), ('Charlie', 78)]
# for name, score in pairs:
#     print(f"{name} scored {score}")

# # filter() applies the is_long_word function to each element in the words list and returns an iterator containing only the elements for which the function returns True. We then convert that iterator to a list using list() to get the final result.
# words = ['tree', 'sky', 'mountain', 'river', 'cloud', 'sun']

# def is_long_word(word):
#     return len(word) > 4

# long_words = list(filter(is_long_word, words))
# print(long_words) # ['mountain', 'river', 'cloud']

# celsius = [0, 10, 20, 30, 40]
# # map() applies the to_fahrenheit function to each element in the celsius list and returns an iterator. We then convert that iterator to a list using list() to get the final result.
# def to_fahrenheit(temp):
#     return (temp * 9/5) + 32

# fahrenheit = list(map(to_fahrenheit, celsius))
# print(fahrenheit) # [32.0, 50.0, 68.0, 86.0, 104.0]

cities = ['Los Angeles', 'London', 'Tokyo']
print(cities[0])
print(len(cities))

def calculator():
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    if operator == "+":
        print("Result:", num1 + num2)

    elif operator == "-":
        print("Result:", num1 - num2)

    elif operator == "*":
        print("Result:", num1 * num2)

    elif operator == "/":
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Cannot divide by zero")

    else:
        print("Invalid operator")


calculator()