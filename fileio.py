with open("file.txt","w") as f:
    f.write("Hello, World!\n")
    f.write("What's up?\n")
    
f.close()


#To read the file
f = open("file.txt","r")

print(f.read())   
print(f.readlines())   

f.close()
