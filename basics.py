# n = int(input('Number: '))

# if n > 0:
#     print('n is positive')
# elif n < 0:
#     print("n is negative")
# else:
#     print("n is zero")

# names = ['Harry', 'Ron']
# print(names[0])

# coordinateX = 10.0
# coordinateY = 20.0

# coordinate = (10.0, 20.0)
# print(coordinate)

# Define a list of names

# names = ['Harry', 'Ron', 'Hermione', 'Ginny']
# names.append("Draco")
# names.sort()
# print(names)

#Sets
# s= set()
# s.add(1)
# s.add(2)
# s.add(3)
# s.add(4)
# # s.remove(2)
# print(f'The set has {len(s)} elements')

#loops
# names = ['Harry', 'Ron', 'Hermione', 'Ginny']
# for i in names:
#     print(i)

#dictionaries

# houses = {
#     'Harry': "Gryffindor",
#     'Draco': "Slytherin"
# }
# houses['Hermione'] = 'Gryffindor'

# print(houses)

#functions
# def square(x):
#     return  x * x

# for i in range(10):
#     print(f' The square of {i} is {square(i)}' )

# squares

# classes

# class Point():
#     def __init__(self, input1, input2):
#         self.x = input1
#         self.y = input2
    
# p = Point(2,8)
# print(p.x)
# print(p.y)


# class Flight():
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.passengers = []
    
#     def add_passenger(self, name):
#         if not self.open_seats():
#             return False
#         self.passengers.append(name)
#         return True
            
#     def open_seats(self):
#         return self.capacity - len(self.passengers)
            

# flight = Flight(3)

# people = ["Harry", "Ron", "Hermione", "Ginny"]

# for person in people:
#     # success = flight.add_passenger(person)

#     if flight.add_passenger(person):
#         print(f'Added {person} to flight successfully')
#     else:
#         print(f'No available seats for {person}')




# decorators !!!!!!!

# def announce(f):
#     def wrapper():
#         print("About to run the function..")
#         f()
#         print('Done with the function.')
#     return wrapper

# @announce
# def hello():
#     print("Hello, world!")

# hello()


# lambda

# people  = [
#     {'name': 'Harry', 'house': 'Gryffindor'},
#     {'name': 'Cho', 'house': 'Ravenclaw'},
#     {'name': "Draco", 'house': "Slytherin"} 
# ]

# # def f(person):
# #     return person['name']

# people.sort(key = lambda person: person['name'])
# print(people)
import sys

try:
    x = int(input('x: '))
    y = int(input('y: '))
except ValueError:
    print("Please enter digits ONLY")
    sys.exit(1)

try:
    result = x / y
except ZeroDivisionError:
    print('Error: Cannot devide by 0.')
    sys.exit(1)

print(f'{x} / {y} = {result}')



