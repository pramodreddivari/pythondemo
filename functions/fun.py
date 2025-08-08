def myfun():
    print("This is my function in fun.py")
myfun() 


def myfun(name):
    print(f"This is {name}")
myfun("pramod") 
myfun("pavan")  
myfun("veeresh")   


def myfun(name, age):
    print(f"This is {name} and age is {age}")
    
myfun("pramod", 30)    

"""Arbitrary Arguments, *args
If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.

This way the function will receive a tuple of arguments, and can access the items accordingly:"""

def myfun(*names):
    print("this name is", names[2])
myfun("pramod", "pavan", "veeresh")    

  
"""  Keyword Arguments
You can also send arguments with the key = value syntax.

This way the order of the arguments does not matter."""


def myfun(c1,c2,c3):
    print("this is", c3)
myfun(c1="pramod", c2="pavan", c3="veeresh")

"""
Arbitrary Keyword Arguments, **kwargs
If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.

This way the function will receive a dictionary of arguments, and can access the items accordingly:"""



def myfun(**kwargs):
    print("this is", kwargs["c3"])
    
myfun(c1="pramod", c2="pavan", c3="veeresh")


def myfun(country="Norway"):
    print("I am from", country)
myfun("India")
myfun("USA")

def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)    



def myfun(x):
    return 5 * x    
print(myfun(3))

#3 types of arguments
"""1: Positional Arguments
2: Keyword Arguments
3: Arbitrary Keyword Arguments, **kwargs"""
def myfun(name,age):
    print(f"my name is{name}")
    print(f"my age is{age}")
myfun("pramod", 30)


def myfun(*,c1,c2,c3):
    print("this id ", c3)
myfun(c1="pramod", c2="pavan", c3="veeresh")        


def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)


def myfun(x):
    if(x%2==0):
        print("even")
    else:
        print("odd")
myfun(3)   


#arbitary arguments
def myfun(*x):
    c=0
    for i in x:
        c=c+i
    print("length is", c)
myfun(10,20,30)

#arbitary keyword arguments
def myfun(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")
        
        
myfun(name="pramod", age=30, country="India")

#nested function
def f1():
    s="Hello, World!"
    def f2():
        print(s)
        
    f2()
f1()

