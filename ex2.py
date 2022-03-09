fileName=input("enter a file name:")
length=len(fileName)
count=0
for i in fileName:
    count+=1
    if(i == "."):
        lent=count
        break
extension=fileName[lent:]
if extension=="py":
    print("The extension of the file is 'python'")
elif extension=="html":
    print("The extension of the file is 'HTML'")
elif extension=="cpp":
     print("The extension of the file is 'C++'")
elif extension=="js":
    print("the extension of the file is 'Javascript'")
elif extension=="c":
    print("the extension of the file is 'c'")
elif extension=="jsp":
    print("the extension of the file is 'Java'")
elif extension=="rb":
    print("the extension of the file is 'Ruby'")
elif extension=="css":
    print("the extension of the file is 'cascading style sheet'")
else:
    print("Sorry!not in a list")
    
