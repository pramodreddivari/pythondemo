a=10
b=20
c=30
if a>b &a>c:
    print("a is greater than b and c")
elif b>a & b>c:
    print("b is greater than a and c")    
else:
    print("c is greater than a and b")
    
   
a = 33
b = 200
if b > a:
  print("b is greater than a")   


a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
  
  
if a > b: print("a is greater than b")

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")


day = 4
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")

day = 4
match day:
  case 1 | 2 | 3 | 4 | 5:
    print("Today is a weekday")
  case 6 | 7:
    print("I love weekends!")
      
    
    