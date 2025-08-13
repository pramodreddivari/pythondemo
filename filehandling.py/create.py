
"""Create a New File
To create a new file in Python, use the open() method, with one of the following parameters:

"x" - Create - will create a file, returns an error if the file exists

"a" - Append - will create a file if the specified file does not exists

"w" - Write - will create a file if the specified file does not exists"""
#Create a new file called "myfile.txt":
"""f=open("myfile.txt", "x")
f.close()"""
with open("myfile.txt", "w") as f:
    f.write("This will overwrite if file exists.")
    f.close()
with open("myfile.txt", "r") as f:
    content = f.read()
    print(content)
    f.close()