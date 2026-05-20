class Dog:
    breed = "Golden Retriever"
    def __init__(self, name, age):
        self.name = name       
        self.age = age

    def bark(self):
        return f"{self.name} says I am {self.age} years old {self.breed}!"

dog1 = Dog("Buddy", 7)
print(dog1.bark()) 
dog2 = Dog("Max", 5)
print(dog2.bark())
print(dog1.breed, dog2.name, dog2.age)

class Book:
   def __init__(self, title, pages):
       self.title = title
       self.pages = pages

book1 = Book("Built Wealth Like a Boss", 420)
book2 = Book("Be Your Own Start", 420)
print(len(book1.title), book1.pages)
print(book2.title, book2.pages)

print(getattr(book1, 'title', "Description not found"))
for attr in dir(book1):
    if not attr.startswith('__') and not callable(getattr(book1, attr)):
        print(attr + ": " + str(getattr(book1, attr)))

class Configuration:
    pass

# Data loaded at runtime (like from a config or env file)
settings_data = {
    'server_url': 'https://api.example.com',
    'timeout_sec': 30,
    'max_retries': 5
}

config_obj = Configuration()

# Dynamically set attributes using dictionary keys and values
for attr_name, attr_value in settings_data.items():
    setattr(config_obj, attr_name, attr_value)

print(config_obj.server_url) 
print(config_obj.timeout_sec)
print(config_obj.max_retries)

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

product_a = Product('T-Shirt', 25)

required_attributes = ['name', 'price', 'inventory_id']

# for attr in required_attributes:
#     if not hasattr(product_a, attr):
#         print(f"ERROR: Product is missing the required attribute: '{attr}'")
#     else:
#         # Access the attributes dynamically once their existence is confirmed
#         print(f'{attr}: {getattr(product_a, attr)}')
for attr in required_attributes:
    if hasattr(product_a, attr):
        print(f'{attr}: {getattr(product_a, attr)} exists')
    else:
        print(f"'{attr}' is missing")

class UserSession:
    def __init__(self, user_id, token):
        self.user_id = user_id
        self.auth_token = token # sensitive
        self.temp_counter = 0 # temporary

session = UserSession(101, 'a1b2c3d4e5')

# List of attributes to remove dynamically before "saving" the session
attributes_to_clean = ['auth_token', 'temp_counter']

# Dynamically remove specified attributes
for attr in attributes_to_clean:
    if hasattr(session, attr):
        delattr(session, attr)
        print(f'Removed attribute: {attr}')

print('\nFinal attributes remaining:')

# Loop through the remaining attributes with dir()
for attr in dir(session):
    # Ignore dunder methods like __init__ or __str__ and regular methods
    if not attr.startswith('__') and not callable(getattr(session, attr)):
        print(f' - {attr}: {getattr(session, attr)}')
