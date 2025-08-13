a=10
b=0
try:
    c=a/b
except ZeroDivisionError:
    print("Error! Division by zero is not allowed.")
else:
    print("The result of the division is:", c)
finally:
    print("Execution completed.")


def divide_numbers(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Error! Division by zero is not allowed.")
    else:
        print("The result of the division is:", result)
    finally:
        print("Execution completed.")
print(divide_numbers(10, 2))

print(divide_numbers(10, 0))

def safe_file_read(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!")
    except PermissionError:
        print(f"Error: Permission denied for file '{filename}'!")
    except (IOError, OSError) as e:
        print(f"Error reading file: {e}")
    return None

# Catch all exceptions (use sparingly)
def risky_operation():
    try:
        # Some risky code
        pass
    except Exception as e:
        print(f"An error occurred: {e}")     
        
        
 """1. Exception Handling Guidelines

Be specific: Catch specific exceptions rather than generic Exception
Handle expected errors: Only catch exceptions you can meaningfully handle
Don't silence errors: Always log or handle exceptions appropriately
Use finally for cleanup: Or better yet, use context managers (with statements)

2. File Handling Best Practices

Always use with open(): Ensures files are properly closed
Specify encoding: Use encoding='utf-8' for text files
Handle common exceptions: FileNotFoundError, PermissionError, etc.
Use appropriate file modes: Don't use 'w' when you mean 'a'

3. Error Recovery Strategies
pythonimport time
import random

def retry_operation(func, max_attempts=3, delay=1):
    """Retry an operation with exponential backoff"""
    for attempt in range(max_attempts):
        try:
            return func()
        except Exception as e:
            if attempt == max_attempts - 1:
                raise  # Last attempt, re-raise the exception
            
            wait_time = delay * (2 ** attempt) + random.uniform(0, 1)
            print(f"Attempt {attempt + 1} failed: {e}. Retrying in {wait_time:.1f}s...")
            time.sleep(wait_time)

# Usage
def unreliable_operation():
    if random.random() < 0.7:  # 70% chance of failure
        raise ConnectionError("Network error")
    return "Success!"

try:
    result = retry_operation(unreliable_operation)
    print(result)
except Exception as e:
    print(f"Operation failed after all retries: {e}")
🔍 Summary
File Handling Key Points:

Use with open() for automatic resource management
Handle file-related exceptions (FileNotFoundError, PermissionError)
Specify encoding for text files
Use appropriate file modes for your needs
CSV module provides robust CSV file handling

Exception Handling Key Points:

Use try-except-else-finally structure appropriately
Create custom exceptions for domain-specific errors
Log errors for debugging and monitoring
Don't catch exceptions you can't handle meaningfully
Use specific exception types rather than generic Exception

Advanced Concepts:

Context managers ensure proper resource cleanup
Custom exceptions provide better error semantics
Logging helps with debugging and monitoring
Retry mechanisms handle transient failures
Error recovery strategies improve robustness  """           