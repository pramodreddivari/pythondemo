a=["a","b","c","d","e"]
print(a[1])


thislist = ["apple", "banana", "cherry"]
print(thislist)

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)


thislist = ["apple", "banana", "cherry"]
print(len(thislist))

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

print(type(list1))

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
print(thislist[2:5])
print(thislist[:4])
print(thislist[::-1])  # prints the list in reverse order

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
  
thislist = ["apple", "banana", "cherry"]
thislist[1]="bambooo"
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist) 


thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)


thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist) 

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)


thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)


thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)


thislist = ["apple", "banana", "cherry"]
for i in thislist:
    print(i)
    
thislist = ["apple", "banana", "cherry"]
i=0
while i < len(thislist):
    print(thislist[i])
    i += 1
 #list comprehension   
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist] 

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

newlist = [x for x in range(10) if x < 5]

a=[x for x in range(10) if x%2==0]  
print(a)
  
thislist = [100, 50, 65, 82, 23]
thislist.sort()
thislist.sort(reverse = True)#descending
print(thislist) 


thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist) 

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.append(list2)
print(list1)


    




