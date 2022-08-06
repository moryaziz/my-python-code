# A Class is an object constructor or a "blueprint" for creating objects.
# Objects are nothing but an encapsulation of variables(att) and functions(def) into a single entity.
# Objects get their variables and functions from classes.
# To create a class we use the keyword "class".
# The first string inside the class is called docstring which gives the brief description about the class.
# All classes have a function called which is always executed when the class is being initiated.
# We can use function to assign values to object properties or other operations ,
# that are necessary to perform when the object is being created.
# The "self" parameter is a reference to the current instance of the class and is used to access class variables.
# "self" must be the first parameter of any function in the class.
# The super() builtin function returns a temporary object of the superclass,
# that allows us to access methods and variables of the base class.
# super() allows us to avoid using the base class name explicitly and to enable multiple inheritance.



# Create an employee class
class Employeeeeee(object):
    def __init__(self,name,id):
        # __init__() function is used to assign values to the variable that define in body of __init__.
        # we have two variables(instance attribute): name and empid.
        # get name and id from user and assign to name and empid,respectively.
        self.name = name
        self.empid = id
        self.name_id = list()

    def nlist(self):
        self.name_id.append(f'{str(self.name)}= {str(self.empid)}')
        print(str(self.name_id))

emp1 = Employeeeeee("Asif", 34163)      # Create an employee object
emp1.nlist()

emp1.name = 'Basit' # Modify Object Properties
print(emp1.name)

emp1.country = 'India'      #instance variable can be created manually
print(emp1.__dict__)

print('='*50)

# *** Inheritance ****
# Inheritance is a powerful feature in object oriented programming.
# Inheritance provides code reusability in the program because we can use an :
# existing class (Super Class/ Parent Class / Base Class) to
# create a new class (Sub Class / Child Class /Derived Class) instead of creating it from scratch.
# The child class inherits data definitions and methods from the parent class which facilitates the reuse of features already available.
# The child class can add few more definitions or redefine a base class method.
# Inheritance comes into picture when a new class possesses the 'IS A' relationship with an existing class.
# E.g Student is a person. Hence person is the base class (parent) and student is derived class(child).

class person(object): # Parent Class

    def __init__(self, name , age , gender):
        self.name = name
        self.age = age
        self.gender = gender

    def PersonInfo(self):
        print('Name :- {}'.format(self.name))
        print('Age :- {}'.format(self.age))
        print('Gender :- {}'.format(self.gender))

    def greet(self):
        print('person say hello')

class student(person):

    def __init__(self, name, age, gender, studentid, fees):
        self.studentid = studentid
        self.fees = fees
        super().__init__(name, age, gender)  # super() builtin function allows us to access methods of the base class.
        # we have 2 att for student more than person.
        # we get 5 att in def __init__ but pass 3 common att , to super class.

    def StudentInfo(self):
        super().PersonInfo()        # call method of super class for print 3 common att.
        print('Student ID :- {}'.format(self.studentid))
        print('Fees :- {}'.format(self.fees))

    def greet(self):
        print('student say hello')

class teacher(person): # Child Class
    def __init__(self,name,age,gender,empid,salary):
        self.empid = empid
        self.salary = salary
        super().__init__(name, age, gender)

    def TeacherInfo(self):
        super().PersonInfo()
        print('Employee ID :{}'.format(self.empid))
        print('Salary :{}'.format(self.salary))


stud1 = student('Asif' , 24 , 'Male' , 123 , 1200)
print('Student Details')
print('---------------')
# PersonInfo() method presnt in Parent Class will be access
stud1.StudentInfo()
print()
teacher1 = teacher('Basit' , 36 , 'Male' , 456 , 80000)
print('Employee Details')
print('---------------')
# PersonInfo() method presnt in Parent Class will be acc
teacher1.TeacherInfo()





# Multi-level Inheritance
# In this type of inheritance, a class can inherit from a child class or derived class.
# Multilevel Inheritance can be of any depth in python


class employee(person): # Child Class

    def __init__(self,name,age,gender,empid,salary):
        super().__init__(name,age,gender) # get 5 instance and pass 3 common to person.
        self.empid = empid
        self.salary = salary

    def employeeInfo(self):
        super().PersonInfo()
        print('Employee ID :- {}'.format(self.empid))
        print('Salary :- {}'.format(self.salary))

class fulltime(employee): # Grand Child Class

    def __init__(self,name,age,gender,empid,salary,WorkExperience):
        # get 6 instance and pass 5 common to employee.
        super().__init__(name,age,gender,empid,salary)
        self.WorkExperience = WorkExperience

    def FulltimeInfo(self):
        super().employeeInfo()
        print('Work Experience :- {}'.format(self.WorkExperience))


class contractual(employee): # Grand Child Class

    def __init__(self,name,age,gender,empid,salary,ContractExpiry):
        super().__init__(name,age,gender,empid,salary)
        self.ContractExpiry = ContractExpiry

    def ContractInfo(self):
        super().employeeInfo()
        print('Contract Expiry :- {}'.format(self.ContractExpiry))


print('\n \n')

print('Contractual Employee Details')
print('****************************')
contract1 = contractual('Basit' , 36 , 'Male' , 456 , 80000,'21-12-2021')
contract1.ContractInfo()
print('\n \n')

print('Fulltime Employee Details')
print('****************************')
fulltim1= fulltime('Asif' , 22 , 'Male' , 567 , 70000, 12)
fulltim1.FulltimeInfo()


print('****************************')

# Multiple Inheritance
# Multiple inheritance is a feature in which a class (derived class) can inherit attributes and
# methods from more than one parent class.
# The derived class inherits all the features of the base case.

# Super Class
class Father(object):
    def __init__(self,fathername):
        self.fathername = fathername

# Super Class
class Mother(object):
    def __init__(self,mothername):
        self.mothername = mothername

# Sub Class
class Son(Father, Mother):

    def __init__(self,fathername,mothername,sonname):
        Father.__init__(self,fathername)
        Mother.__init__(self,mothername)
        self.name = sonname
    def show(self):
        print('My Name :- ',self.name)
        print("Father :", self.fathername)
        print("Mother :", self.mothername)
s1 = Son("John","Kristen",'bill')
s1.show()


# Method Overriding (change method of super class in sub class)
# Overriding is a very important part of object oreinted programming because it makes inheritance exploit its full power.
# Overriding is the ability of a class (Sub Class / Child Class / Derived Class) to change the
# implementation of a method provided by one of its parent classes.
# When a method in a subclass has the same name, same parameter and same return type as
# a method in its super-class, then the method in the subclass is said to override the method in the super-class.
# The version of a method that is executed will be determined by the object that is used to invoke it.
# If an object of a parent class is used to invoke the method, then the version in the parent class will be executed,
# but if an object of the subclass is used to invoke the method, then the version in the child class will be executed.

print('='*40)
p = person('ali',18,'male')
s1 = student('mory',25,'male',14,25000)
p.greet()
s1.greet()










