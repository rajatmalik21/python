class Employee():

    def __init__(self, name, empid, department, job):
        self.name = name
        self.empid = empid
        self.department = department
        self.job = job
    def set_name(self, name):
        self.name = name
    def set_empid(self, empid):
        self.empid = empid
    def set_department (self, department):
        self.department = department
    def set_job (self, job):
        self.job = job
    def get_name(self):
        return self.name
    def get_empid(self):
        return self.empid
    def get_department(self):
        return self.department
    def get_job(self):
        return self.job
    def __str__(self):
        return "Name: " +self.name+ "\nEmployee ID "+self.empid+"\nDepartment "+self.department+"\nJob "+self.job

import pickle
def main():
    emp_file = load_emp()
    menu()
    choice = input('Enter your choice: ')
    if choice in ['1', '2', '3', '4','5']:
        if choice == 1:
            lookup(emp_file)
        elif choice == 2:
            add_data(emp_file)
        elif choice == 3:
            change(emp_file)
        elif choice ==4:
            dele_(emp_file)
        elif choice == 5:
            print("The program would quit now...")
        menu()
        choice = input("Enter your choice: ")
    else:
        print("Wrong Choice")
    save_emp(emp_file)


def load_emp():
    try:
        load_file = open('employee.dat', 'rb')
        emp_details = pickle.load(load_file)
        load_file.close()
    except IOError:
        emp_details = {}
    return emp_details

def save_emp(emp_file):
    save_file = open('employee.dat','wb')
    pickle.dump(emp_file , save_file)
    save_file.close()

def lookup(emp_file):
    search = raw_input("Enter your search query")
    search_result = emp_file.get(search, "Entry not found")
    print(search_result)

def add_data(emp_file):
    again = "y"
    while again == "y":
        empname = raw_input("Enter employee name")
        empid = raw_input("Enter the ID number")
        depart = raw_input("Enter Department")
        job = raw_input("Enter Job title")
        if empname not in emp_file:
            entry = Employee(empname ,empid, depart, job)
            emp_file[empname]  = entry
            print(empname, "has been successfully added")
        else:
            print(empname, "already exists!")
        again = raw_input("Enter 'y' to continue or any other alphabet to quit")

def change(emp_file):
    search = raw_input("Enter the name you want to change the details")
    if search in emp_file:
        empname = raw_input("Enter new employee name")
        empid = raw_input("Enter new the ID number")
        depart = raw_input("Enter new Department")
        job = raw_input("Enter new Job title")
        entry = Employee(empname,empid, depart, job)
        emp_file[empname]  = entry
        print(empname, "has been successfully updated")
    else:
        print("Entry not found")

def delete_ (emp_file):
    search = raw_input("Enter the name you want to change the details")
    if search in emp_file:
        del emp_file[search]
        print(search, " has been deleted successfully")
    else:
        print("Entry not found")
def menu():
    print("Choose your Option below")
    print("Look-up Employee Details = 1")
    print("Add new Employee Details = 2")
    print("Change an existing Employee Details = 3")
    print("Delete an Employee Details = 4")
    print("Quit the program = 5 ")


main()