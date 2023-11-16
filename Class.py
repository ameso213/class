#User class with properties
class User:
    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.location = location
# Create a new instance of the User class
user = User("Imie", 21, "Bukoto")
# Access the user's name,age and location
print(user.name)
print(user.age)
print(user.location)



class Person:
    def __init__(self, name, age):
     self.name = name
     self.age = age
p1 = Person("Imie", 21)
print(p1.name)
print(p1.age)



#The string representation of an object WITHOUT the __str__() function:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
p1 = Person("Imie", 21)
print(p1)



#The string representation of an object WITH the __str__() function:
#Example
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def __str__(self):
    return f"{self.name}({self.age})"
p1 = Person("Imie", 21)
print(p1)



#Object Methods
#Objects can also contain methods. Methods in objects are functions that belong to the object.
#Let us create a method in the Person class:
#Example
#Insert a function that prints a greeting, and execute it on the p1 object:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("Imie", 21)
p1.myfunc()
