i=1
while i <= 10:
    print(i)
    i += 1
    
print("*******************")    
   
i=1
while i <= 10:
    print(i)
    if i==3:
        break
    i += 1
print("*******************")   
i=0
while i < 10:
    i += 1    
    if i==3:
        continue
    print(i)
    
print("*******************") 
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  
  
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
  
  
for x in range(6):
  print(x)      
  
for x in range(2, 30, 3):
  print(x)


adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)     