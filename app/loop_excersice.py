# def pin_extractor(poems):
#     secret_codes = []
#     for poem in poems:
#         secret_code = ''
#         lines = poem.split('\n')
#         for line_index, line in enumerate(lines):
#             words = line.split()
#             if len(words) > line_index:
#                 secret_code += str(len(words[line_index]))
#             else:
#                 secret_code += '0'
#         secret_codes.append(secret_code)
#     return secret_codes        

# poem = """Stars and the moon
# shine in the sky
# white and
# until the end of the night"""

# poem2 = 'The grass is green\nhere and there\nhoping for rain\nbefore it turns yellow'
# poem3 = 'There\nonce\nwas\na\ndragon'

# print(pin_extractor([poem, poem2, poem3]))


# # number pattern generator  
# def number_pattern(n):
#     if not isinstance(n, int):
#         return "Argument must be an integer value."

#     elif n < 1:
#         return "Argument must be an integer greater than 0."

#     return ' '.join(str(i) for i in range(1, n + 1))


# print(number_pattern(4))

# for i in range(1, 6):
#     print(i)

# for i in range(1, 11):
#     print(i, end=' ')

# for i in range(1, 11):
#     if i % 2 == 0:
#         print("Even")
#     else:        
#         print("Odd")

# for i in range(1, 21):
#     if i % 3 == 0:
#         print(i)

# for i in range(1, 6):
#     print('#' * i)

# for i in range(1,6):
#     print(str(i),  end=' ')
#     print()

# for i in range(6, 1, -1):
#     for j in range(i-1):
#         print("*", end='')
#     print()

# repeat something i times
# for i in range(5, 0, -1):
#      for j in range(i):      
#         print("*", end='')

#      print()

# total = 0
# for i in range(1, 6):
#     total += i
# print(total)

# text = "This is a sample text to count the number of a's in it."
# count = 0
# for letter in text:
#     if letter == 'a':
#         count += 1
# print(count)

# text = "This is a sample text to count the number of vowels in it."
# cout = 0
# for letter in text:
#     if letter in 'aeiou':
#         cout += 1
#         print(letter, end=' ')
# print()        
# print(cout)

# numbers = [4, 7, 2, 9, 1]
# largest = numbers[0]
# for number in numbers:
#     if number > largest:
#         largest = number
# print(largest)

# for i in range(1, 21):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)

# count = 0
# number = 48291
# str_number = str(number)
# for letter in str_number:
#     count +=1
# print(count)

# count = 0
# for i in range(1, 6):
#     count +=1
# print(count)

# i= 1
# while i <= 5:
#     print(i, end=' ')
#     i += 1

# password = "python"
# user_input = input("Enter the password: ")
# while user_input != password:
#     print("Incorrect password. Try again.")
#     user_input = input("Enter the password: ")
# print("Access granted!")

# for i in range(1, 11):
#     print(f"5 * {i} = {5 * i}")

#     # OR
#     i= 1
# while i <= 10:
#     print(f"5 * {i} = {5 * i}")
#     i += 1

# numbers = [1, 4, 7, 10, 12, 15]
# count = 0
# for number in numbers:   
#     if number % 2 == 0:
#         count += 1
# print(count)  
# Calculate the SUM of only the even numbers.
# numbers = [1, 4, 7, 10, 12, 15]
# total = 0
# for number in numbers:
#     if number % 2 == 0:
#         total += number
# print(total)

# numbers = [8, 3, 15, 1, 9]
# smallest = numbers[0]
# for number in numbers:
#     if number < smallest:
#         smallest = number
# print(smallest)

# reverse a list
# numbers = [1, 2, 3, 4, 5]
# reversed_numbers = []
# for i in range(len(numbers) - 1, -1, -1):
#     reversed_numbers.append(numbers[i])
# print(reversed_numbers)


# Count words in a string
# text = "This is a sample text to count the number of words in it."
# word_count = len(text.split())
# print(word_count)

# numbers = [1, 2, 2, 3, 4, 4, 5]
# unique_numbers = []
# for number in numbers:
#     if number not in unique_numbers:
#         unique_numbers.append(number)
# print(unique_numbers)
# # Find Second Largest Number
# numbers = [4, 9, 2, 7, 5]
# largest = None
# second_largest = None
# for number in numbers:
#     if largest is None or number > largest:
#         second_largest = largest
#         largest = number
#     elif second_largest is None or (number > second_largest and number < largest):
#         second_largest = number
# print(second_largest)
# numbers = [4, 9, 2, 7, 5]
# largest = numbers[0]
# second_largest = numbers[0]
# for number in numbers:
#     if number > largest:
#         second_largest = largest
#         largest = number
#     elif number > second_largest and number < largest:
#         second_largest = number
# print(second_largest)

# for i in range(1, 4):
#     for j in range(1, 4):
#         print(i*j, end=' ')
#     print()

# numbers = [1, 2, 2, 3, 2, 4]
# count_2 = 0
# for number in numbers:
#     if number == 2:
#         count_2 += 1
# print(count_2)

# Accumulator Pattern
# total = 0
# for number in numbers:
#     total += number

# Max/Min Pattern
# largest = numbers[0]
# for number in numbers:
#     if number > largest:
#         largest = number

# Build New Collection
# new_list = []
# for item in items:
#     new_list.append(item)

# Nested Loop Pattern
# for i in range(...):
#     for j in range(...):

# Count how many times EACH character appears.
# text = "banana"
# char_count = {}
# for char in text:
#     if char in char_count:
#         char_count[char] += 1
#     else:
#         char_count[char] = 1
# print(char_count)

# # 
# numbers = [-3, 5, -1, 8, 0, -7, 2]
# positive_numbers = []
# for number in numbers:
#     if number > 0:
#         positive_numbers.append(number)
# print(positive_numbers)

# for number in numbers:
#     if number > 0:
#         print(number)

# Find Index of Largest Number
# numbers = [4, 9, 2, 7, 5]
# largest = numbers[0]
# largest_index = 0
# for i in range(1, len(numbers)):
#     if numbers[i] > largest:
#         largest = numbers[i]
#         largest_index = i
# print(largest_index)

# text = "Python"
# for char in text:
#     print(char)

# text = "Python is fun"
# count = 0
# for char in text:
#     if char == ' ':
#         count += 1
# print(count)

# text = "python"
# for char in text:
#     char = char.upper()
#     print(char, end=' ')
# print()

# new_text = ""
# new_text1 = ""
# for char in text:
#     new_text = char + new_text
#     new_text1 = new_text1 + char
# print(new_text)
# print(new_text1)
# OR new_text = text[]::-1]
# text = "This is a sample text to keep the words in it."
# new_text=""
# for char in text:
#     new_text = char + new_text
# print(new_text)

# remove vowels
# text = "This is a sample text to remove the vowels."
# new_text = ""
# for char in text:
#     if char.lower() not in 'aeiou':
#         new_text += char        
# print(new_text)
# text = "This is a sample text to remove the vowels."
# new_text = ""
# for char in text:
#     if char in 'aeiouAEIOU':
#         new_text = new_text+char        
# print(new_text)

# newer_text = ""
# for i in range(len(text)):
#     if i % 2 == 0:
#         newer_text += text[i].upper()
#     else:       
#         newer_text += text[i].lower()
# print(newer_text)

# # First Non-Repeating Character
# text = "aabbcddee"
# for letter in text:
#     count = 0
#     for other_letter in text:
#         if letter == other_letter:
#             count += 1
#     if count == 1:
#         print(letter)
#         break


# word1 = "listen"
# word2 = "silent"    
# if sorted(word1) == sorted(word2):
#     print("Anagrams")
# else:    print("Not Anagrams")

# numbers = [0, 1, 0, 7, 12]
# # Move Zeroes to End
# non_zero_index = 0  
# for i in range(len(numbers)):
#     if numbers[i] != 0:
#         numbers[non_zero_index] = numbers[i]
#         non_zero_index += 1

# # Fill the rest of the list with zeros
# for i in range(non_zero_index, len(numbers)):
#     numbers[i] = 0

# print(numbers)

# numbers = [1, 2, 3, 5, 6]
# for i in range(len(numbers)):
#     if numbers[i] != i + 1:
#         numbers.insert(i, i + 1)
#         print(i + 1)
#         break

# print(numbers)

# text ="Python makes programming enjoyable"
# words = text.split()
# longest_word = ""
# for word in words:   
#     if len(word) > len(longest_word):
#         longest_word = word
# print(longest_word)
# print   (len(longest_word))