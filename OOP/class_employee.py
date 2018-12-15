class Employee:
    def __init__(self, name, position, salary, gender):
        self.name = name
        self.position = position
        self.salary = salary
        self.gender = gender

    def leave(self):
        return 'Boss I am taking leave'

    def tax(self):
        return 0.1 * self.salary




class Teacher(Employee):
    def __init__(self, name, position, salary, gender, subjects):
        self.subjects = subjects
        Employee.__init__(self, name, position, salary, gender)  # call init method of Employee

    def __str__(self):
        return 'Name : {}\nPosition : {}\nGender : {}\nSubject : {}\n'.format(self.name, self.position, self.gender,
                                                                              self.subjects)

    def com(self):
        return self.salary + 5000





class Staff(Employee):
    def __init__(self, name, position, salary, gender, department):
        self.department = department
        Employee.__init__(self, name, position, salary, gender)

    def __str__(self):
        return 'Name : {}\nPosition : {}\nGender : {}\nSubject : {}\n'.format(self.name, self.position, self.gender,
                                                                              self.department)

    def bonus(self):
        return self.salary + 5000


t = Teacher('Ram', 'Manager', 2000, 'Male', 'Maths')
print(t)
print('Tax of teacher : ', t.tax())
print('Commission of teacher : ', t.com())

s = Staff('Hari', 'Receptionist', 1000, 'Male', 'Marketing')
print('Bonus of Staff :', s.bonus())
