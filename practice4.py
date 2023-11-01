class MyClass:
    
    class_attribute = "I am a class attribute"

    
obj1 = MyClass()
obj2 = MyClass()

print(obj1.class_attribute)  
print(obj2.class_attribute)



class Person:
    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute

# Creating instances of the class
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

# Accessing instance attributes
print(person1.name, person1.age)  
print(person2.name, person2.age)



class Dog:
    # Class attribute shared by all instances
    species = "Canis familiaris"

    def __init__(self, name, age):
        # Instance attributes unique to each instance
        self.name = name
        self.age = age

    def description(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"

# Creating instances of the Dog class
dog1 = Dog("Buddy", 3)
dog2 = Dog("Sadie", 5)

# Accessing class attribute (shared among all instances)
print(f"{dog1.name} belongs to the species {dog1.species}")
print(f"{dog2.name} belongs to the species {dog2.species}")

# Accessing instance attributes
print(dog1.description())  # Output: Buddy is 3 years old
print(dog2.description())  # Output: Sadie is 5 years old

# Using instance methods
print(dog1.speak("Woof!"))  # Output: Buddy says Woof!
print(dog2.speak("Bark!"))  # Output: Sadie says Bark!


# Static methods

class Student:
    passingPercentage = 40
    
    def studentDetails(self):
        self.name = "Anup"
        print("Name : ", self.name)
        self.percentage = 75
        print("Percentage : ", self.percentage)
        pass
    
    def isPassed(self):
        if self.percentage > Student.passingPercentage:
            print("Student is passed")
            
        else:
            print("Student is not passed")
            
            
    @staticmethod
    def welcomeToSchool():
        print("Welcome to AI KI PATHSHALA")



s1 = Student()
print()
s1.studentDetails()
print()
Student.studentDetails(s1)
print()
s1.isPassed()
print()
s1.welcomeToSchool()
print()
Student.welcomeToSchool()
print()




class MathUtils:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def subtract(x, y):
        return x - y

    @staticmethod
    def multiply(x, y):
        return x * y

    @staticmethod
    def divide(x, y):
        if y != 0:
            return x / y
        else:
            return "Division by zero is not allowed."

# Using static methods
result_add = MathUtils.add(5, 3)
result_subtract = MathUtils.subtract(8, 2)
result_multiply = MathUtils.multiply(4, 6)
result_divide = MathUtils.divide(10, 2)

print("Addition:", result_add)
print()
print("Subtraction:", result_subtract)
print()
print("Multiplication:", result_multiply)
print()
print("Division:", result_divide)
print()



class MyClass1:
    class_variable = "I am a class variable"

    def __init__(self, value):
        self.instance_variable = value

    def instance_method(self):
        print(f"Instance Method: {self.instance_variable}")
        print(f"Accessing Class Variable from Instance Method: {self.class_variable}")

    @classmethod
    def class_method(cls):
        print(f"Class Method: {cls.class_variable}")

# Creating an instance of the class
obj = MyClass1("Hello")

# Accessing instance method
obj.instance_method()

# Accessing class method
MyClass1.class_method()












