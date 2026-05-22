#Local scope : means that a variable declared inside a function or class can only be accessed 
#within that function or class. We can call it outside of the function but can not change its parameters


def newFun():
a="Anirudh"
print(a)
newFun()


#Enclosing scope means that a function that's nested inside another function can access the '
#variables of the function it's nested within.


def newFun1():
a1='Joshi'


def childNewFun1():
print(a1)

childNewFun1()


newFun1()



#Global scope : refers to variables that are declared outside any functions or classes which can be 
#accessed from anywhere in the program. Here, my_var can be accessed anywhere, because inside a 
#function it's not defined in


my_var = 100
def checkFun():
print(my_var)


checkFun()


#built-in scope refers to all of Python's built-in functions, modules, and keywords, and are 
#available anywhere in your program:


my_var1 = "Hello world"
print(str(my_var))
print(type(my_var1))





yourAge = 18
if yourAge > 18:
print("You can give your vote!")
elif yourAge == 18:
print("You are superhuman!")
else:
print("You are minor!")




