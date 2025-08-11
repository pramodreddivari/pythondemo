class abc:
    total_students = 0  # Class variable to keep track of total students
    schoolname="ABC School"  # Class variable for school name
    def __init__(self,name,age):
        self.name = name
        self.age = age 
        abc.total_students += 1  
    def myfun(self):
        print(f"my name is { self.name} and my age is {self.age}")
obj= abc("pramod", 20)
obj2=abc("suresh", 22)
obj.myfun() 
print(obj.name)
print(obj.age) 
print(abc.total_students)  # This will raise an error since totalstudents is not defined
print(abc.schoolname)
abc.schoolname="XYZ School"  # Changing the school name
print(abc.schoolname)  # Accessing the class variable for school name