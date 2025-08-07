print("pramod")
print("He is called 'Johnny'")
print('He is called "Johnny"')


a="Hello, World!"
print(a)

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

b="pramod"
print(b[3])

c="gnanesh"
for i in c:
    print(i)
    
    
d="veeresh"
print(len(d))

print(d.lower())
print(d.upper())
print(d.capitalize())
print(d.strip())  # removes whitespace from the beginning and end
print(d.replace("e", "a"))  # replaces "e" with "a" 
print(d.split("e"))  # splits the string into a list where "e" is the separator
print(d.find("e"))  # returns the index of the first occurrence of "e"
print(d.count("e"))  # counts how many times "e" appears in the string  
print(d.isalnum())  # checks if all characters are alphanumeric
print(d.isalpha())  # checks if all characters are alphabetic


txt="Hello, welcome to my world."
if "welcome" in txt:
    print("Yes, 'welcome' is present.")


txt="Hello, welcome to my world."
if "expensive" not in txt:
    print("no, 'welcome' is present.") 
else:
   pass


#slicing
a="pramod"
print(a[1:4])   # prints characters from index 1 to 3
print(a[0:])
print(a[:4])    # prints characters from the start to index 3
print(a[ ::-1])
print(a[-5:-2])


a = "Hello, World!"
print(a.split(","))

a="hello"
b="world"
c=a + " " + b

print(c)
name="pramod"
print(f"Hello, {name}!")  # f-string for formatting


#The escape character allows you to use double quotes when you normally would not be allowed:

txt = "We are the so-called \"Vikings\" from the north."
print(txt)
