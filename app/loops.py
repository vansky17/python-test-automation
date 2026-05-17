programming_languages = ['Rust', 'Java', 'Python', 'C++']

for bla in programming_languages:
    print(bla)

categories = ['Fruit', 'Vegetable']
foods = ['Apple', 'Carrot', 'Banana']

for category in categories:
    for food in foods:
        print(category, food)

secret_number = 3
guess = None
while guess != secret_number:
    guess = int(input('Guess the number (1-5): '))
    if guess != secret_number:
        print('Wrong! Try again.')

print('You got it!')

developer_names = ['Jess', 'Naomi', 'Tom']

for developer in developer_names:
    if developer == 'Naomi':
        break
    print(developer)

developer_names = ['Jess', 'Naomi', 'Tom']

for developer in developer_names:
    if developer == 'Naomi':
        continue
    print(developer)

words = ['sky', 'apple', 'rhythm', 'fly', 'orange']
for word in words:
    for letter in word:
        if letter.lower() in 'aeiou':
            print(f"'{word}' contains the vowel '{letter}'.")
            break
    else:
        print(f"'{word}' does not contain a vowel.")

for num in range(2, 11, 2):
    print(num)

nums = range(1, 8, 2)
for num in nums:
    print(num)


numbers = list(range(2, 11, 2))
print(numbers) 


languages = ['Spanish', 'English', 'Russian', 'Chinese']

for index, language in enumerate(languages):
    print(f'Index {index} and language {language}')


developers = ['Naomi', 'Dario', 'Jessica', 'Tom']
ids = [1, 2, 3, 4]

pairs=list(zip(developers, ids)) 
print(pairs)
for name, id in pairs:
    print(f"Developer {name} has ID {id}")

words = ['tree', 'sky', 'mountain', 'river', 'cloud', 'sun']

def is_long_word(word):
    return len(word) > 4

long_words = list(filter(is_long_word, words))
print(long_words) # ['mountain', 'river', 'cloud']

celsius = [0, 10, 20, 30, 40]

def to_fahrenheit(temp):
    return (temp * 9/5) + 32

fahrenheit = list(map(to_fahrenheit, celsius))
print(fahrenheit) # [32.0, 50.0, 68.0, 86.0, 104.0]


numbers = [5, 10, 15, 20]
total = sum(numbers)
print(total) # Result: 50