class calucator:
    calucationcount=0
    def __init__(self,name):
        self.name=name
    def add(self, a, b):
        calucator.calucationcount+=1
        result=a + b   
        print(f"{self.name}, is performing addition{a}+{b}={result}")
        return result
    
    
    #class method to get the calculation count
    @classmethod
    def get_calculation_count(cls):
        return cls.calucationcount
    @classmethod
    def create_calculator(cls):
        return cls("basic calucator")
# Using instance methods    
obj=calucator("pramod")
print(obj.add(10, 20))  # Output: 30
# Using class method to get calculation count
print(calucator.get_calculation_count())

#create object using class method
obj2=calucator.create_calculator()
obj2.add(5, 15)  # Output: 20
print(calucator.get_calculation_count())  # Output: 2
# Output: basic calucator
print(obj2.name)  # Output: basic calucator
        