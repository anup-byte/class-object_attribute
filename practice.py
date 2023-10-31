class Myclass:
    class_attribute = "I am a class attribute"

# creating instances of the class
obj1 = Myclass()
obj2 = Myclass()

# Accessing the class attribute
print(obj1.class_attribute)
print(obj2.class_attribute)



class Person:
    def __init__(self, name, age):
        self.name = name # Instance attribute
        self.age = age # Instance attribute

# creating instances of the class
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

print(person1.name, person1.age)
print(person2.name, person2.age)

