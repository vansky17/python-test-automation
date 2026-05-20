products = {
    'Laptop': 990,
    'Smartphone': 600,
    'Tablet': 250,
    'Headphones': 70,
}
# print(products.values())
# for price in products.values():
#     print(price)
# for product in products.keys():
#     print(product)
# for product, price in products.items():
#     print(f'{product}: {price}')
# for i, product in enumerate(products):
#     print(f'{i}: {product}')
    
# for i, (product, price) in enumerate(products.items()):
#     print(f'{i}: {product} - {price}')

for index, product in enumerate(products.items()):
    print(f'{index}: {product[0]} - {product[1]}')
    # OR
for index, (product, price) in enumerate(products.items()):
    print(f'{index}: {product} - {price}')
for key, value in products.items():
    print(f'{key}: {value}')
person = {
    "name": "Bobo",
    "age": 40,
    "city": "Hamburg"
}
# print(person["name"], person["age"])
for key, value in person.items():
    print(key, value)

# car = {
#     "brand": "BMW",
#     "year": 2020
# }
# car["color"] = "red"
# print(car['color'])
# for key, value in person.items():
#     print(f'{key}: {value}')

# for key in person.keys():
#     if key == "age":
#         print("Age key exists in the person dictionary.")
# if "age" in person:
#     print("Age key exists in the person dictionary.")

# # Create a dictionary with values using the list
# words = ["apple", "banana", "apple", "orange", "banana", "apple"]
# fruits = {}
# for word in words:
#     if word in fruits:
#         fruits[word] += 1
#     else:
#         fruits[word] = 1
# print(fruits)


scores = {
    "Bobo": 88,
    "Anna": 95,
    "John": 79
}
# highest_score = max(scores.values())
# highest = 0
# for score in scores.values():
#     if score > highest:
#         highest = score
# print(highest)

# highest = 0
# top_student = ""

# for name, score in scores.items():
#     if score > highest:
#         highest = score
#         top_student = name
# print(f'{top_student} has the highest score: {highest}')

# prices = {
#     "apple": 2,
#     "banana": 3,
#     "orange": 4,
#     "pineapple": "fifteen"
# }
# total_cost = 0
# for price in prices.values():
#     if isinstance(price, (int, float)):
#         total_cost += price
# print(f'Total cost: {total_cost}')
# # total_cost = sum(prices.values())
# # print(f'Total cost: {total_cost}')

# text = "hello world"
# vowels_count = {}
# for char in text:
#     if char in "aeiou":
#         if char in vowels_count:
#             vowels_count[char] += 1
#         else:
#             vowels_count[char] = 1
# print(f'Vowel counts: {vowels_count}')

# a = {"x": 1, "y": 2}
# b = {"z": 3}
# # Merging dictionaries
# merged = {**a, **b}
# print(f'Merged dictionary: {merged}')
# merged = {} 
# for d in (a, b):
#     merged.update(d)
# print(f'Merged dictionary: {merged}')


# person = {}

# person.update({"age": 40}) 
# # person["age"] = 40
# print(person)

# users = {
#     "admin": {
#         "email": "admin@test.com",
#         "active": True
#     },
#     "guest": {
#         "email": "guest@test.com",
#         "active": False
#     }
# }

# users.update({"admin": {"email": "admin@newdomain.com"}})
# users["admin"]["name"] = "Admin User"
# print(users["admin"]["email"])
# print(users["admin"]["name"])

# words = ["cat", "dog", "cat", "bird", "cat", "dog"]

# occurances = {}
# highest = 0
# common_word = ""

# for word in words:
#     if word in occurances:
#         occurances[word] += 1
#     else:
#         occurances[word] = 1

#     if occurances[word] > highest:
#         highest = occurances[word]
#         common_word = word

# print(common_word)

# best_value = ?
# best_item = ?

# for item in data:
#     if current_value > best_value:
#         best_value = current_value
#         best_item = item

# data = {
#     "a": 1,
#     "b": 2,
#     "c": 3
# }
# # swapped_data = {value: key for key, value in data.items()}
# swapped_data = {}
# for key, value in data.items():
#     swapped_data[value] = key
# print(swapped_data)

# students = {
#     "Ivan": {"age": 40, "grade": "A"},
#     "Anna": {"age": 22, "grade": "B"},
#     "John": {"age": 31, "grade": "C"}
# }
# for name, info in students.items():
#     print(f'{name} is {info["age"]} years old and has grade {info["grade"]}.')

# for name in students.keys():
#     print(f'{name} is {students[name]["age"]} years old and has grade {students[name]["grade"]}.')

# # Group words by first letter
words = ["apple", "banana", "ant", "cherry", "date", "delderberry"]
# grouped_words = {}
# # create a loop through the list
# for word in words:
#     # get first letter
#     first_letter = word[0]
#     # if key exists, append word
#     if first_letter in grouped_words:
#         grouped_words[first_letter].append(word)
#     # otherwise create new list
#     else:
#         grouped_words[first_letter] = [word]
# print(grouped_words)
#  make a dictionary with first letter as key and word as value. if key exists, extend the key with next letter until key is unique
words = ["apple", "ant", "banana", "boat", "cat", "car"]

result = {}

for word in words:
    key_length = 1
    key = word[:key_length]

    while key in result:
        key_length += 1
        key = word[:key_length]

    result[key] = word

print(result)
# person = {
#     "name": "Ivan",
#     "age": 40,
#     "city": "Hamburg"
# }
# if "age" in person:
#     person.pop("age")
#     print(person)

# text = "banana"
# # Count character frequency and return a dictionary
# char_freq = {} # Initialize an empty dictionary to store character frequencies
# for char in text: # Iterate through each character in the text
#     if char in char_freq: # Check if the character is already a key in the char_freq dictionary
#         char_freq[char] += 1 # If the character is already a key, increment its count by 1
#     else:
#         char_freq[char] = 1 # If the character is not a key in the char_freq dictionary, add it with a count of 1
# print(char_freq)

# cart = {
#     "apple": {"price": 2, "quantity": 4},
#     "banana": {"price": 3, "quantity": 2},
#     "orange": {"price": 5, "quantity": 1}
# }
# total_cost = 0
# grand_total = 0
# for item, details in cart.items():
#     total_cost = details["price"] * details["quantity"]
#     grand_total += total_cost
#     print(f'{item}: {total_cost}')

# print(f'Grand total: {grand_total}')

# students = {
#     "Ivan": [5, 4, 6],
#     "Anna": [6, 6, 5],
#     "John": [3, 4, 5]
# }
# highest_average = 0
# average = 0
# top_student = ""
# for name, notes in students.items():
#     average = sum(notes) / len(notes) # Calculate the average score for the current student
#     if average > highest_average:
#         highest_average = average
#         top_student = name
# print(f"{top_student} has a score of {highest_average}")
        

