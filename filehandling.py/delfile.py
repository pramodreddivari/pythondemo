#f=open("neww.txt", "x")
"""import os
os.remove("neww.txt")"""

#f=open("neww.txt", "x")
f=open("neww.txt", "w")
f.write("This is a new line added to the file.\n")
f.close()

with open("neww.txt", "r") as f:
    content = f.read()
    print(content)
    f.close()
    
  #check if the file exists before deleting
import os
if os.path.exists("neww.txt"):
    os.remove("neww.txt")
    print("File deleted successfully.")  
    