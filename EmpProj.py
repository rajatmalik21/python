#Basic Project to store employee information
print("System to store employee information")

l=[]

def view_list():
    for i in l:
        print("\nName: ",i[0],"\nDOB: ",i[1],"\nE-mail ID:",i[2])

def add_data():
    while True:
        x=input("\nPlease enter Name, DOB, E-mail:").split(",")
        l.append(x)
        ans=input("Do you want to enter more information? (Yes / No)")
        if ans in ['yes','y']:
            pass
        else:
            break

def search_info():
    name=input("\nEnter the name to be searched:")
    for i in l:
        if name==i[0]:
            print("Employee name found in the list!")
            print("\nName {i[0]} \nDOB: {i[1]} \nE-mail ID: {i[2]}")
            break
    else:
        print("Name of this employee not found")

def end():
    print("\n Print any key to exit: ")
    exit()

while True:
    print("************************")
    print("\nPlease choose an option:")
    print("\n1. Add new data ")
    print("\n2. View Data ")
    print("\n3. Search Data ")
    print("\n4. Exit")
    x=input("\nEnter your option: ")
    if x=='1':
        add_data()
    elif x=='2':
        view_list()
    elif x=='3':
        search_info()
    elif x=='4':
        end()
    else:
        print("\nX X X X X X X INCORRECT OPTION ENTERED X X X X X X X ")
