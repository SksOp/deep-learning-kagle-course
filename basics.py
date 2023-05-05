# print("hello")
tupple = (1, 2, 3,"i am tupple")  # immutable ie elements cannot be changed by doing tupple[0] = 5
# print(tupple)
list = [6, 2, 3, 5] # mutable ie elements can be changed by doing list[0] = 5
# print(list)

# dictionary
dict = {"name": "saurabh", "age": 21} # key value pair like json or map in c++
# print(dict)

# set
set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10} # set is a collection of unique elements , 
                                    #list can have duplicate elements, to remove duplicate elements from list we can use set as set(list)
# print(set)

# if else
length = len(list)

if length == 5:
    # print("length is 5")
    pass
else:
    # print("length is not 5")
    pass

# for loop
for i in range(0, 10):
    # print(i)
    pass

# while loop
i = 0
while i < 10:
    # print(i)
    pass
    i += 1

# function
def add(a, b):
    return a + b

# print(add(1, 2))

# built in functions
# print(len(list))
# print(max(list))
# print(min(list))
# print(sum(list))
# print(sorted(list))  # returns sorted list
# list.sort() #sorts the original list


# exception handling

# try:
#     print(1/10)
# except Exception as e:
#     print(e)
# else:
#     print("no exception")
# finally:
#     print("finally")

# object and class
class Circle(object):
    def __init__(self, radius,color):
        self.radius = radius
        self.color = color
    def add_radius(self,r):
        self.radius = self.radius + r
        return(self.radius)
    def getCircumference(self):
        return(2*3.14*self.radius)
    
RedCircle = Circle(10,"red")
# print(RedCircle.getCircumference())
# print(dir(RedCircle))

# file handling
# file = open("basics.py", "r")
# print(file.read())

# best practice for file handling is to use with statement as it automatically closes the file once we get out of the block
with open("basics.py", "r") as file:
    file_stuff = file.readline()
    print(file_stuff)
    file_stuff = file.readline()
    print(file_stuff)
    file_stuff = file.readline()
    print(file_stuff)
    