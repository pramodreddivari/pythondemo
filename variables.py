x = 5
y = "John"
print(x)
print(y)


x = float(5)
print(x)
y = "John"
print(type(x))
print(type(y))


x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
print(x,y,z)


x = y = z = "Orange"
print(x)
print(y)
print(z)



#unpack a list:

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)


x = "Python "
y = "is "
z = "awesome"
print(x + y + z)


x = 5
y = 10
print(x + y)




#global variables
#Create a variable outside of a function, and use it inside the function

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()