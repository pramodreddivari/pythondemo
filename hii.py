print("hello world")
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1) 
factorial_result = factorial(5) 
print(f"The factorial of 5 is: {factorial_result}")
#print fibonacci series
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_series = [0, 1]
        for i in range(2, n):
            fib_series.append(fib_series[-1] + fib_series[-2])
        return fib_series                   
    
fibonacci_result = fibonacci(10)
print(f"The first 10 numbers in the Fibonacci series are: {fibonacci_result}")  
                                                
           
           # ...existing code...
fibonacci_result = fibonacci(10)
print("The first 10 numbers in the Fibonacci series are:")
for num in fibonacci_result:
    print(num)
# ...existing code...                                     
                                                
                                                

        
            
                
                
                
                
                
                
                
                                                               




                            
                            
