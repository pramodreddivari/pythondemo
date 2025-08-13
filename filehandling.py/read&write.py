"""with open("C:/Users/Helpdesk/OneDrive/Desktop/New.txt", "r") as f:
    content = f.read()
    print(content)
    f.close()"""
    
    
"""Overwrite Existing Content
To overwrite the existing content to the file, use the w parameter:""" 

   
with open("C:/Users/Helpdesk/OneDrive/Desktop/New.txt", "w") as f:
    f.write("This is a new line added to the file.\n")
    f.write("Appending another line to the file.\n")
    f.close()

with open("C:/Users/Helpdesk/OneDrive/Desktop/New.txt") as f:
 a=f.read()
 print(a)
 
 with open("C:/Users/Helpdesk/OneDrive/Desktop/New.txt", "a") as f:
     f.write("This is a new line added to the file...........\n")


#open and read the file after the appending:
with open("C:/Users/Helpdesk/OneDrive/Desktop/New.txt") as f:
  print(f.read())   
  
  
  
   
 
 
 