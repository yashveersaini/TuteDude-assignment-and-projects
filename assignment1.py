data = {
    101: {'name': 'Satya',
          'age': 27,
          'department': 'HR',
          'salary': 50000
          }
}


class Employees:

    def addEmployee(self, emp_id, name, age, department, salary):

        employee_Data = {
            'name': name,
            'age': age,
            'department': department,
            'salary': salary
        }

        data[emp_id] = employee_Data

    def viewAllEmployee(self):
        print("Details of all Employees ======================>>>>")
        for employeeId in data.keys():
            print("Employee id: ", employeeId)
            print("Information: ")
            print(data[employeeId])
            print("---------------------------------------------------------------------")

    def searchEmployee(self, emp_id):

        searching = False
        for employeeId in data:

            if employeeId == emp_id:
                searching = True
                print("---------------------------------------------------------------------")
                print("Search result: ")
                print(data[employeeId])
                print("---------------------------------------------------------------------")

        if searching == False:
            print("No data Found !!")


if __name__ == "__main__":

    emp = Employees()

    while True:

        print()
        print("Enter your choice: ")
        print("1. Add Employee \n2. View all employees \n3. Search for employees\n4. Exit\n")
        choice = int(input())

        if choice == 1:

            print("Enter the employee data: ")
            emp_id = int(input("Employee id: "))

            if emp_id not in data:
                name = input('name: ')
                age = int(input('age: '))
                department = input('department: ')
                salary = float(input('salary: '))
                emp.addEmployee(emp_id, name, age, department, salary)
            else:
                print("This id is already Exist! Try another Employee ID.")

        elif choice == 2:
            emp.viewAllEmployee()

        elif choice == 3:
            emp_id = int(input("Enter the employee Id (which do you want to search): "))
            emp.searchEmployee(emp_id)

        else:
            break
