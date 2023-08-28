class Employee:
    def __init__(self, employee_id, name, age, salary):
        self.employee_id = employee_id
        self.name = name
        self.age = age
        self.salary = salary

class EmployeeDatabase:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def print_employees(self):
        for employee in self.employees:
            print(f"ID: {employee.employee_id}, Name: {employee.name}, Age: {employee.age}, Salary: {employee.salary}")

    def sort_employees(self, key):
        if key == 1:
            self.employees.sort(key=lambda x: x.age)
        elif key == 2:
            self.employees.sort(key=lambda x: x.name)
        elif key == 3:
            self.employees.sort(key=lambda x: x.salary)
        else:
            print("Invalid sorting parameter")

if __name__ == "__main__":
    employee_db = EmployeeDatabase()

    employee_db.add_employee(Employee("161E90", "Raman", 41, 56000))
    employee_db.add_employee(Employee("161F91", "Himadri", 38, 67500))
    employee_db.add_employee(Employee("161F99", "Jaya", 51, 82100))
    employee_db.add_employee(Employee("171E20", "Tejas", 30, 55000))
    employee_db.add_employee(Employee("171G30", "Ajay", 45, 44000))

    print("Select sorting parameter:")
    print("1. Age\n2. Name\n3. Salary")
    sorting_param = int(input())

    employee_db.sort_employees(sorting_param)
    employee_db.print_employees()
