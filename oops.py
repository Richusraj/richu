# class Student:
#     """method()"""
#     def exam():
#         print("exam starts on 08/04/2004")

# richu = Student()
# print(id(richu))
# print(type(richu))

# ronaldo=Student()
# print(id(ronaldo))
# print(type(ronaldo))


# class Student:
#     """method()"""
#     def exam(self):
#         print("exam starts on 08/04/2004")



# richu = Student()
# ronaldo=Student()

# richu.exam()
# ronaldo.exam()


# class Players:
#     """players function or methords here"""
#     def name(self):
#         print("welcome to football")

#     def plyr(slef):
#         pass
#     def joo(self):
#         print("jooo")
        

# ronaldo=Players()
# messi=Players()
# neymar=Players()

# ronaldo.name()
# messi.plyr()
# neymar.joo()


# class employee:
#     company_name="real madrid fc"
#     branch_place="madrid"

#     def __init__(self,id,name,email,salary):
#         self.e_id=id
#         self._name=name
#         self.email=email
#         self.salary=salary
    
#     def greet(self):
#         print(f"employee id : {self.e_id}\n employee name : {self._name}")
#         print(f"employee email : {self.email}\n employee salary : {self.salary}")

#     def update_salary(self):
#         if self.salary >100000:
#             update=self.salary * 0.25
#             self.salary+=update
#             print(self.salary)

# ronaldo=employee(id=7,name="ronaldo",email="cr7.com",salary=100007)
# ronaldo.greet()
# benzema=employee(id=9,name='benzema',email="karim.com",salary=9000)
# benzema.greet()
# ronaldo.update_salary()
# ronaldo.greet()









class Bank:
    bank_name="sbi"

    def __init__(self,acc_number,name,ifsc,balance):
        self.acc_no=acc_number
        self.name=name
        self.ifsc=ifsc
        self.balance=balance

    def getdetials(self):
        print(f"account number : {self.acc_no} \nname : {self.name} \nifsc : {self.ifsc} ")

    def getbalance(self):
        print(self.balance)

    def deposite(self,amount):
        self.balance+=amount
        print(f"deposit successful,your current balance is {amount}")
        

richu=Bank(acc_number=2222,name='richu',ifsc="sbin0307",balance=77)
richu.getdetials()
richu.getbalance()
richu.deposite()


