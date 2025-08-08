#function call by itself is called recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
factorial_result = factorial(5)
print(factorial_result)  # Output: 120


fact=1
for i in range(1,6):
    fact=fact*i
print(fact)  # Output: 120


#lambda function
#anonymous function
c=lambda x: x + 10
print(c(5))  # Output: 15

        
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
fibonacci_result = fibonacci(5)
print(fibonacci_result)  # Output: 5

#print fionacci series
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b
    print() 
fibonacci(5)  # Output: 0 1 1 2 3

#swap
def swap(x,y):
    temp = x
    x = y
    y = temp
    return x, y
x, y = swap(5, 10)
print(x, y)  # Output: 10 5


def add(x,y):
    return x*y
add_result = add(5, 10)
print(add_result)  # Output: 50