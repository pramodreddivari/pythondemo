class MathUtils:
    @staticmethod
    def add(x, y):
        """Add two numbers"""
        return x + y
    
    @staticmethod
    def multiply(x, y):
        """Multiply two numbers"""
        return x * y
    
    @staticmethod
    def is_prime(n):
        """Check if a number is prime"""
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    @staticmethod
    def factorial(n):
        """Calculate factorial"""
        if n == 0 or n == 1:
            return 1
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

class DateUtils:
    @staticmethod
    def is_leap_year(year):
        """Check if a year is a leap year"""
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    
    @staticmethod
    def days_in_month(month, year):
        """Get number of days in a month"""
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if month == 2 and DateUtils.is_leap_year(year):
            return 29
        return days[month - 1]

# Use static methods - can call without creating instances
print(MathUtils.add(5, 3))          # 8
print(MathUtils.multiply(4, 6))     # 24
print(MathUtils.is_prime(17))       # True
print(MathUtils.factorial(5))       # 120

print(DateUtils.is_leap_year(2024)) # True
print(DateUtils.days_in_month(2, 2024)) # 29

# Can also call from instances (but not recommended)
math_obj = MathUtils()
print(math_obj.add(10, 20))         # 30