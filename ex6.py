import csv
def appending(detail):
    file=open("student_detail1.csv","a",newline='')
    writer=csv.writer(file)
    if file.tell()==0:
        writer.writerow(["Name","Age","Reg no","Department","Shift"])
    writer.writerow(detail)
if __name__=="__main__":
    condition=True
    count=1
    while(condition):
        details=input("Enter Student details in the given format [Name,Age,Register number,Department,Shift]:")
        detail_list=details.split(" ")
        check=True
        a=input("Is the above mentioned input is correct(yes/no)")
        if a=="yes":
            appending(detail_list)
            print("\n\n\nSTUDENT",count," DETAIL:\n\nName:",detail_list[0],"\nAge:",detail_list[1],'\nRegister Number:',detail_list[2],'\nDepartment:',detail_list[3],'\nShift:',detail_list[4],'\n\n\n')
            continue1=input("Do you want to add another detatils (yes/no)")
            if continue1=="yes":
                condition=True
                count+=1
            else:
                condition=False
        else:
            print("Re-enter again")
    
        
