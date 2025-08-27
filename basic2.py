listofthings = {"table": 1, "fork": 2, "spoon": 3, "plate": 4}
for items, values in listofthings.items():
    print(f"{items} : {values}")

#DESTRUCTURING VARIABLES
person = ("bob", 42, "mechanic")
name, _, profession = person
print(f"{name} : {profession}")

head, *tail = [1,2,3,4,5] # *variable for the rest of the values in array
print(tail)

#FUNCTIONS IN PYTHON
def hello():
    print("function hello");

hello()

#FUNTION ARGUMENTS AND PARAMETERS
def add(x,y):
    pass #do nothing

def say_hello(name, surname):
    print(f"Hello, {name} {surname}")

say_hello(surname="Bob", name="Smith")

#DEFAULT PARAMETER VALUES
def add(x, y=8):
    print(x + y)

add(5);

#FUNCTIONS RETURNING VALUES
def return_42():    
    return 42 

# Create a function below, called my_function, that takes two arguments and returns the result of its two arguments multiplied together.
def my_function(multiplicand, multiplier):
    return multiplicand * multiplier


#LAMBDA FUNCTIONS
add = lambda x, y: x + y
print(add(5,7))

#or
print((lambda x, y: x + y)(5,7))

#same as def add(x,y) 
    #       return x + y

def double(x):
    return x * 2

sequence2 = [1,3,5,9]
doubled = [double(x) for x in sequence2]
doubled = map(double, sequence2) #same
doubled = [(lambda x:x*2)(x) for x in sequence2] #same
doubles = list(map(lambda x: x*2, sequence2)) #same

#DICTIONARY COMPREHENSION

userlist = [
    (0, "Bob", "password"),
    (1, "Ro", "bob123"),
    (2, "Jos", "longpassword"),
    (3, "username", "1234")
]
username_mapping = {user[1]: user for user in userlist}
print(username_mapping)

#username_input = input("Username: ")
#password_input = input("Password: ")
#get username and password from list
#_,username,password = username_mapping[username_input] 

# if(password_input == password):
#     print("Your details are correct")
# else:
#     print("Your detailes are incorrect")

student_ ={'name': 'Jose', 'school' : 'Computing', 'grades' : (66,77,88) } 

def average_grade(data):
    grades = data["grades"]
    return sum(grades) / len(grades)


def average_grade_all_students(student_list):
    total = 0
    count = 0
    for student in student_list:
            total += sum(student["grades"])
            count += len(student["grades"])
    return total / count

#UNPACKING ARGUMENTS
def multiply(*args):
    print(args)
    total = 1
    for arg in args:
        total = total * arg
    return total
print(multiply(1,2,3))


def anotheradd(x,y):
    return x + y

nums = {"x" : 15, "y" : 25}
print(add(x=nums["x"], y=nums["y"]))
print(add(**nums)) #same thing

def apply(*args, operator):
    if operator == "*":
        return multiply(*args)
    elif operator == "+":
        return sum(args)
    else:
        return "No valid operator provided." 
print(apply(1,2,4,5, operator="*"))

#UNPACKING KEYWORD ARGUMENTS
def named(**kwargs):
    print(kwargs)

named(name="bob", age=35)

details = {"name":"bob", "age" : 25}
named(**details)

#another example
def both(*args, **kwargs):
    print (args)
    print(kwargs)

both(1,2,3, name="bob", age=25)

#OOP IN PYTHON

class StudentNew:
    def __init__(self, name, grade):
        self.name = name
        self.grades = grade

    def average_grade(self):
        return sum(self.grades) / len(self.grades)

student = StudentNew("bobx", {90,93,94,78,90})
print(student.name)
print(student.average_grade())

#MAGIC METHODS __str__ and __repr__

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    #def __str__(self):
    #    return f"Person {self.name}, {self.age} years old."
    
    def __repr__(self): #its like an alt when str is not , for unambigous string
        return f"<Person({self.name}, {self.age})>"
    

bob = Person("Bob", 44)
print(bob)

#EXERCISE FOR CLASSES AND OBJECTS
class Store:
    def __init__(self, name):
        self.name = name
        self.items = []
        # You'll need 'name' as an argument to this method.
        # Then, initialise 'self.name' to be the argument, and 'self.items' to be an empty list.
    
    def add_item(self, name, price):
        # Create a dictionary with keys name and price, and append that to self.items.
        self.items.append({"name" : name, "price": price})
        

    def stock_price(self):
        # Add together all item prices in self.items and return the
        #total = 0;
        #for item in self.items:
        #    total += item['price']
            
        #return total        
        return sum([item['price'] for item in self.items])
    

#CLASSMETHOD AND STATICMETHOD
class ClassTest:
    def instance_method(self):
        print(f"called instance_method of {self}")

    @classmethod
    def class_method(cls):
        print(f"called class_method of {cls}")

    @staticmethod
    def static_method(): #no passed parameter
        print("Called static method")

test = ClassTest()
test.static_method()

#another example

class Book:
    TYPES  = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight
        
    def __repr__(self):
        return f"<book {self.name}, {self.book_type}, weighing {self.weight}g>"
        
    @classmethod
    def hardcover(cls, name, page_weight): #cls == Book class
        return cls(name, cls.TYPES[0], page_weight + 100)
    
    @classmethod
    def paperback(cls, name, page_weight):
        return cls(name, cls.TYPES[1], page_weight + 100)


book = Book.hardcover("Harry Potter", 1500)
book2 = Book.paperback("Harry", 1200)

print(book2)

#2nd Example

class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        self.items.append({
            'name': name,
            'price': price
        })

    def stock_price(self):
        total = 0
        for item in self.items:
            total += item['price']
        return total
    
    def __repr__(self):
         return f"<store {self.name}, {self.items}>"
        

    @classmethod
    def franchise(cls, store):
        # Return another store, with the same name as the argument's name, plus " - franchise"
        newstr = Store(store.name + " - franchise")
        print(newstr)

    @staticmethod
    def store_details(store):
        # Return a string representing the argument
        # It should be in the format 'NAME, total stock price: TOTAL'
        #return f"{store.name}, total stock price: {store.stock_price()}" or
        print('{}, total stock price: {}'.format(store.name, int(store.stock_price())))


store2 = Store("Amazon");
store2.add_item("Keyboard", 160);

Store.franchise(store2)
Store.store_details(store2)
print(store2)

#CLASS INHERITANCE

class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True
    
    def __str__(self):
        return f"Device {self.name!r} ({self.connected_by})"
    
    def disconnect(self):
        self.connected = False
        print("Disconnected")
    
    def connect(self):
        self.connected = True
        print("Connected")

class Printer(Device): #inherit
    def __init__(self, name, connected_by, capacity):
        super().__init__(name, connected_by)
        self.capacity = capacity
        self.remaining_pages = capacity
    
    def __str__(self):
        return f"{super().__str__()} ({self.remaining_pages} pages remaining)"

    def print(self, pages):
        if not self.connected:
            print(f"Your printer is not connected")
            return
        print ("Printing {pages} pages")
        self.remaining_pages -= pages

printerMain = Printer("Printer", "USB", 500)
printerMain.disconnect()
printerMain.print(20)

print(printerMain)

printerMain.connect()
printerMain.print(50)

print(printerMain)

#CLASS COMPOSITION, the inverse of inheritance, 
#not all bookshelf has books, but books can be in bookshelf
#no neet to inherit some properties, but is related

class BookShelf:
    def __init__(self, *books):
        self.books = books
    
    def __str__(self):
        return f"Bookshelf with {len(self.books)} books."
    
class Book:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f"Book {self.name}"

book = Book("Harry Pots")
book2 = Book("Python")
shelf = BookShelf(book, book2)
print(shelf)

#TYPE HINTING IN PYTHON 3.5+, new feature
from typing import List

def list_avg(sequence: List) -> float: #will error if data passed is not a list, returns float (or any type set)
    return sum(sequence) / len(sequence)

#list_avg(123) #error since List is required

#IMPORTS IN PYTHON
#RELATIVE IMPORTS IN PYTHON
#Discusses references coming from another py file.
#to use relative imports use from, example
#from .mymodule import 


#ERRORS IN PYTHON, CUSTOM ERROR CLASSES
def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0") #built in python error handler
        #raise RuntimeError
        #raise TypeError
        #raise ValueError

grades = []
print("Welcome to the average grade program")
try:
    average = divide(sum(grades), len(grades))    
except ZeroDivisionError as e:
    print(e)
    print("There are no grades yet in your list.")
else:
    print(f"The average grade is {average}")
finally:
    print("Thank you")

#custom error
class TooManyPagesReadError(ValueError): #copied error, customized
    pass

class AnotherBook:
    def __init__(self, name: str, page_count: int):
        self.name = name
        self.page_count = page_count
        self.pages_read = 0
    
    def __repr__(self):
        return (
            f"<Book {self.name}, read {self.pages_read} pages out of {self.page_count}"
        )

    def read(self, pages: int):
        if self.pages_read + pages > self.page_count:
            raise TooManyPagesReadError(
                f"You tried to read {self.pages_read + pages} pages, but this book only has {self.page_count} pages"
            )
        self.pages_read += pages
        print(f"You have now read {self.pages_read} pages out of {self.page_count}.")

python101 = AnotherBook("PY 101", 50)
python101.read(35)
#python101.read(50)

#or
try:
    python101.read(35)
    python101.read(50)
except TooManyPagesReadError as e:
    print(e); 

#FIRST CLASS FUNCTIONS
def anotherDivide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be zero")
    
    return dividend/divisor

def calculate(*values, operator):
    return operator(*values)

result = calculate(20,4, operator=anotherDivide)

#another example
def search(sequence, expected, finder):
    for elem in sequence:
        if(finder(elem) == expected):
            return elem
    raise RuntimeError(f"Could not find an element with {expected}")

friends = [
    {"name" : "Rol", "age": 24},
    {"name" : "Ad", "age":30},
    {"name" : "An", "age": 27}
]

def get_friend_name(friend):
    return friend["name"]

#print(search(friends, "Rol", get_friend_name))
print (search(friends, "Rol", lambda friend: friend["name"]))


#SIMPLE DECORATORS IN PYTHON / THE "AT" SYNTAX
#DECORATING FUNCTIONS WITH PARAMETERS

import functools
user = {"username": "jose", "access_level" : "guest"}
#user = {"username": "jose", "access_level" : "admin"}

def make_secure(access_level): #an example of factory
    def decorator(func):
        @functools.wraps(func)
        #def secure_function(panel):
        def secure_function(*args, **kwargs):           
            if user["access_level"] == access_level:
                #return func(panel)
                return func(*args, **kwargs)
            else:
                return f"No {access_level} permissions for {user['username']}."
            
        return secure_function
    return decorator


@make_secure #decorator
def get_password(panel):
    if panel == "admin":
        return "1234"
    elif panel == "billing":
        return "super_secure_password"

#get_admin_password = make_secure(get_password)
#print(get_admin_password())

@make_secure("admin") 
def get_admin_password():
    return "admin:1234"

@make_secure("guest")
def get_dashboard_password():
    return "user: user_password"

print(get_admin_password())
print(get_dashboard_password())

#MUTABILITY IN PYTHON
#MUTABLE DEFAULT PARAMETERS

from typing import List, Optional

class Student:
    #def __init__(self, name: str, grades: List[int] = []): # this is bad
    #   self.name = name
    #   self.grades = grades
    
    #solution
    def __init__(self, name: str, grades: Optional[List[int]] = None): # this is the fix
        self.name = name
        self.grades =  grades or []

    def take_exam(self, result: int):
        self.grades.append(result)

bob22 = Student("Bob")
rolf22 = Student("Rolf")
bob22.take_exam(90)

#Results to same grade due to wrong mutability
print(bob22.grades)
print(rolf22.grades)






















