import random
# class Dog:
#     breed = "Golden Retriever"
#     def __init__(self, name, age):
#         self.name = name       
#         self.age = age

#     def bark(self):
#         return f"{self.name} says I am {self.age} years old {self.breed}!"

# dog1 = Dog("Buddy", 7)
# print(dog1.bark()) 
# dog2 = Dog("Max", 5)
# print(dog2.bark())
# print(dog1.breed, dog2.name, dog2.age)

# class Book:
#    def __init__(self, title, pages):
#        self.title = title
#        self.pages = pages

# book1 = Book("Built Wealth Like a Boss", 420)
# book2 = Book("Be Your Own Start", 4)
# print(len(book1.title), book1.pages)
# print(book2.title, book2.pages)

# print(getattr(book1, 'title', "Description not found"))
# for attr in dir(book1):
#     if not attr.startswith('__') and not callable(getattr(book1, attr)):
#         print(attr + ": " + str(getattr(book1, attr)))
# book2_title = getattr(book2, "title", "Description not found")
# print(f"{book2_title} - this!")

# class Configuration:
#     pass

# # Data loaded at runtime (like from a config or env file)
# settings_data = {
#     'server_url': 'https://api.example.com',
#     'timeout_sec': 30,
#     'max_retries': 5
# }

# config_obj = Configuration()

# # Dynamically set attributes using dictionary keys and values
# for attr_name, attr_value in settings_data.items():
#     setattr(config_obj, attr_name, attr_value)

# print(config_obj.server_url) 
# print(config_obj.timeout_sec)
# print(config_obj.max_retries)

# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

# product_a = Product('T-Shirt', 25)

# required_attributes = ['name', 'price', 'inventory_id']

# # for attr in required_attributes:
# #     if not hasattr(product_a, attr):
# #         print(f"ERROR: Product is missing the required attribute: '{attr}'")
# #     else:
# #         # Access the attributes dynamically once their existence is confirmed
# #         print(f'{attr}: {getattr(product_a, attr)}')
# for attr in required_attributes:
#     if hasattr(product_a, attr):
#         print(f'{attr}: {getattr(product_a, attr)} exists')
#     else:
#         print(f"'{attr}' is missing")

# class UserSession:
#     def __init__(self, user_id, token):
#         self.user_id = user_id
#         self.auth_token = token # sensitive
#         self.temp_counter = 0 # temporary

# session = UserSession(101, 'a1b2c3d4e5')

# # List of attributes to remove dynamically before "saving" the session
# attributes_to_clean = ['auth_token', 'temp_counter']

# # Dynamically remove specified attributes
# for attr in attributes_to_clean:
#     if hasattr(session, attr):
#         delattr(session, attr)
#         print(f'Removed attribute: {attr}')

# print('\nFinal attributes remaining:')

# # Loop through the remaining attributes with dir()
# for attr in dir(session):
#     # Ignore dunder methods like __init__ or __str__ and regular methods
#     if not attr.startswith('__') and not callable(getattr(session, attr)):
#         print(f' - {attr}: {getattr(session, attr)}')

# print(book1.__dict__)

class Robot:
    robot_count = 0
    def __init__(self, name, battery_level=100):
        self.name = name
        self.battery_level = battery_level
        Robot.robot_count += 1
        # self.battery_level = 100
    def charge(self, amount):
        self.battery_level += amount
        if self.battery_level > 100:
            self.battery_level = 100
        return f"{self.name} charged to {self.battery_level}%" 
    def drain(self, amount):
        self.battery_level -= amount
        if self.battery_level < 0:
            self.battery_level = 0
        return f"{self.name} drained to {self.battery_level}%"
    def transfer_battery(self, other_robot, transfer_amount):
        if self.battery_level >= transfer_amount:
            self.battery_level -= transfer_amount
            other_robot.battery_level += transfer_amount
            return f"{self.name} transferred {transfer_amount}% battery to {other_robot.name}"
        else:
            return f"{self.name} does not have enough battery to transfer"
    def report_status(self):
        if self.battery_level > 70:
            return "High Battery level"
        elif self.battery_level > 30:
            return "Medium Battery level"
        else:
            return "Low Battery level"
    
# robot1 = Robot("Robo", 85)
# print(robot1.__dict__)
# print(robot1.name)
# print(robot1.battery_level)
# print(robot1.charge(10))

robot1 = Robot("Robo1", 50)
robot2 = Robot("Robo2", 80)
robot3 = Robot("Robo3", 20)
robots = [robot1, robot2, robot3]
for robot in robots:
    print(f"{robot.name} - Battery Level: {robot.battery_level}%")

robot2.transfer_battery(robot3, 30)
print("\nAfter battery transfer:")  
for robot in robots:
    print(f"{robot.name} - Battery Level: {robot.battery_level}%")
    print(f"Status: {robot.report_status()}")

print(f"\nTotal robots created: {Robot.robot_count} AND {robot1.robot_count}")


class BattleRobot(Robot):
    def __init__(self, name, weapon, battery_level=100, health=100):
        super().__init__(name, battery_level)

        self.weapon = weapon
        self.health = health
    def report_status(self):
        base_status = super().report_status()
        return f"{base_status} | Weapon: {self.weapon}"
    def attack(self, other_robot):
        damage = self.weapon.damage
        other_robot.health -= damage
        if other_robot.health < 0:
            other_robot.health = 0
        return f"{self.name} attacked {other_robot.name} for {damage} damage. {other_robot.name}'s health is now {other_robot.health}%."

battle_robot1 = BattleRobot("Warrior", "Plasma Cannon", 90, 100)
print(battle_robot1.report_status())

# print(robot1.attack(robot2))


class Weapon():
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

laser = Weapon("Laser", 20)
cannon = Weapon("Cannon", 35)
battle_robot1 = BattleRobot("Warrior", laser, 90, 100)
battle_robot2 = BattleRobot("Defender", cannon, 80, 100)
print(battle_robot1.attack(battle_robot2))
print(battle_robot2.health)

print(dir(robot1))

for attr in dir(robot1):
    if not attr.startswith('__') and not callable(getattr(robot1, attr)):
         print(attr + ": " + str(getattr(robot1, attr)))
print(getattr(robot1, 'name', "Attribute not found"))

setattr(robot1, 'color', 'red')
print(robot1.color)
if hasattr(robot1, 'color'):    print(f"{robot1.name} has a color attribute: {robot1.color}")

class Planet:
    def __init__(self, name, planet_type, star):
        self.name = name
        self.planet_type = planet_type
        self.star = star
        if not isinstance(self.name, str) or \
           not isinstance(self.planet_type, str) or \
           not isinstance(self.star, str):

            raise TypeError(
                "name, planet type, and star must be strings"
            )
        if self.name == "" or \
           self.planet_type == "" or \
           self.star == "":
            raise ValueError(
                "name, planet_type, and star must be non-empty strings"
            )
    def orbit(self):
        return f"{self.name} is orbiting around {self.star}..."

    def __str__(self):
        return f"Planet: {self.name} | Type: {self.planet_type} | Star: {self.star}"

planet_1 = Planet("Alpha", "Sun", "Beta")
planet_2 = Planet("JDJ", "rock", "Sun")
planet_3 = Planet("Alpha", "asteroid", "Sun")

print(planet_1,"\n", planet_2,"\n", planet_3 )
print(planet_1.orbit())
print(planet_2.orbit())
print(planet_3.orbit())
print(planet_1)
print(planet_2)
print(planet_3)


