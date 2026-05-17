# def calculate_sum(a, b):
#     return a + b

# print(calculate_sum(5, 7))

# def greet(name):
#     return f"Hello, {name}!"

# print(greet("Alice"))

# def count_long_words    (words):
#     count = 0
#     for word in words:
#         if len(word) > 4:
#             count += 1
#     return count

# words_list = ['tree', 'mountain', 'sky', 'river']
# print(count_long_words(words_list))


# text = "This is a sample text to keep the words in it."
# def count_long_words (text):
#      new_text = []
#      count = 0
#      for word in text.split():
#          if len(word) > 4:
#              new_text.append(word)
#              count += 1
#      return count, ' '.join(new_text)

# print(count_long_words(text))

# numbers = [4, 9, 2, 7, 5]
# def find_largest_number(numbers):
#     if not numbers:
#         return None
#     largest = numbers[0]
#     for number in numbers:
#         if number > largest:
#             largest = number
#     return largest
# print(find_largest_number(numbers))

# numbers = [3, 8, 5, 12, 7, 10]
# def extract_shadow_values(numbers):
#     shadow_values = []
#     for number in numbers:
#         if number % 2 == 0:
#             shadow_values.append(number)
#     return shadow_values

# print(extract_shadow_values(numbers))

# text = "hello dark world"
# def forge_signal_chain(text):
#     new_text = text.upper()
#     return new_text 
# print (forge_signal_chain(text))

# every word shorter than 4 letters is removed /1 solution
text = "the silent mountain of shadows"
# def calibrate_echo_matrix (text):
#     words = text.split()
#     for word in words:
#         if len(word) < 4:
#             words.remove(word)
#     return ' '.join(words)
# print(calibrate_echo_matrix(text))
# # # every word shorter than 4 letters is removed /2 solution
# def calibrate_echo_matrix (text):
#     words = text.split()
#     new_words = []
#     for word in words:
#         if len(word) >= 4:
#             new_words.append(word)
#     return ' '.join(new_words)
# print(calibrate_echo_matrix(text))

# split → loop → condition → append → join
# loop → compare → track largest
# iterate → filter → return
# build new collection safely instead of mutating during iteration

# Removeeach second character from a string 1
# text= "abcdefgh"
# def synchronize_delta_codes(text):
#     new_text = ''
#     for char in text:
#         if char in text[::2]:  # Check if the character is in the even-indexed characters':
#             new_text += char
#     return new_text       
# print(synchronize_delta_codes(text))

# text = "abcdefgh"
# def synchronize_delta_codes(text):
#     new_text = ''
#     for index, char in enumerate(text):
#         if index % 2 == 0:  # Check if the index is even
#             new_text += char
#     return new_text
# print(synchronize_delta_codes(text))
# Removeeach second character from a string 1
# text = "abcdefgh"
# def synchronize_delta_codes(text):
#     new_text = ''
#     for i in range(len(text)):
#         if i % 2 == 0:  # Check if the index is even
#             new_text += text[i]
#     return new_text
# print(synchronize_delta_codes(text))

# def transmit_fragment_patterns(text):
#     new_text = ''
#     for i in range(0, len(text), 2):  # Iterate over the string with a step of 2
#         new_text += text[i]
#     return new_text
# print(transmit_fragment_patterns(text))

# # take a list of numbers
# # return True if the list is sorted in ascending order
# # otherwise return False
# numbers = [1, 2, 3, 4]
# def stabilize_vector_flow(numbers):
#     for i in range(1, len(numbers)):
#         if numbers[i] < numbers[i-1]:
#             return False
#     return True
# print(stabilize_vector_flow(numbers))

# return a NEW list where:
# positive numbers stay the same
# negative numbers become positive
# numbers = [4, -2, 7, -9, 0]
# def transform_signal_waveform(numbers):
#     transformed = []
#     for number in numbers:
#         if number < 0:
#             transformed.append(-number)  # Convert negative to positive
#         else:
#             transformed.append(number)   # Keep positive numbers unchanged
#     return transformed
# print(transform_signal_waveform(numbers))

# def change_signal_polarity(numbers):
#     transformed = []
#     for number in numbers:
#         if number >= 0:
#             transformed.append(number)
#     # return sorted(transformed) OR
#         transformed.sort()
#     return transformed
# print(change_signal_polarity(numbers))


# a = [5, 1, 8]
# b = [2, 7, 3]
# def merge_signal_clusters(list1,  list2):
#     merged = list1 + list2
#     merged.sort()
#     return merged
# print(merge_signal_clusters(a, b))



# return a NEW string where:

# duplicate consecutive characters are removed
# text = "aaabccdddde"
# def compress_neural_trace(text):
#     if not text:
#         return ""
#     compressed = text[0]
#     for char in text[1:]:
#         if char != compressed[-1]:
#             compressed += char
#     return compressed
# print(compress_neural_trace(text))

# def validate_access_key(key):
#     if len(key) < 8:
#         return False
#     if not any(char.isdigit() for char in key):
#         return False
#     return True
# print(validate_access_key("abc123"))

# def monitor_reactor_temperature():
#     temperature = int(input("Enter the reactor temperature: "))
#     if temperature < 15:
#         return "Temperature is too low."
#     elif temperature > 30:
#         return "Temperature is too high."
#     else:
#         return "Temperature is within the safe range."
# print(monitor_reactor_temperature())

# repeatedly ask the user to enter prices
# stop when the user enters: "done"
# return the total of all the prices entered
# def calculate_supply_total():
#     total = 0
#     while True:
#         price = input("Enter a price (or 'done' to finish): ")
#         if price == "done":
#             break
#         total += float(price)
#     return total
# print(calculate_supply_total())


# text = "This is a sample text to count the number of words in it bros."
# def count_words(text):
#     return len(text.split())
# print(count_words(text))

# def count_long_words(text):
#     count = 0
#     long_words = []	
#     for word in text.split():
#         if len(word) > 4:
#             count += 1
#             long_words.append(word)
#     return {"count": count, "long_words": ', '.join(long_words)}
# print(count_long_words(text)) 

# numbers = [1, 5, 2, 5, 3, 1, 7]
# def remove_duplicates(numbers):
#     unique_numbers = []
#     for number in numbers:
#         if number not in unique_numbers:
#             unique_numbers.append(number)
#     return unique_numbers

def merge_lists(list1, list2):
    list1.extend(list2)
    return list1
print(merge_lists([1, 2, 3], [4, 5, 6]))

text = "aaabccdddde"
def remove_duplicates(text):
    compressed = ""
    for char in text:
        if char not in compressed:
            compressed += char
    return compressed
print(remove_duplicates(text))

names = ["Alice", "Bob", "Charlie"]
scores = [90, 85, 95]
def zipptehmall(names, scores):
    return list(zip(names, scores))
print(zipptehmall(names, scores))