num=int(input("enter the number of elements to be given to the list "))
list1=[]
i=0
while i<num:
    element=int(input("Enter an element "))
    list1.append(element)
    i+=1
j=0
list2=[]
for j in list1:
    if j>0:
        list2.append(j)
print(list2)
        
