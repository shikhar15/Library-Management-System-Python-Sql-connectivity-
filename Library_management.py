from LMS import Menu
from LMS import Book
from LMS import issue
while True:
    Book.clrscreen()
    print("\t\t\t Library Management\n")
    print("==============================================================")
    print("1. Book Management ")
    print("2. Members Management s ")
    print("3. Issue/Return Book ")
    print("5. Exit ")
    print("===============================================================")
    choice=int(input("Enter Choice between 1 to 4-------> : "))
    if choice==1:
        Menu.MenuBook()
    elif choice==2:
        Menu.MenuMember()
    elif choice==3:
        Menu.MenuIssueReturn()
    elif choice==4:
        break
    else:
        print("Wrong Choice......Enter Your Choice again")
        x=input("Enter any key to continue")