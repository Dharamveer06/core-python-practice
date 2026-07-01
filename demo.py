class Car:
    
#     def __init__(self , id , name):
#         self.id = id
#         self.name = name
    
#     def display(self):
#         print(self.id)
#         print(self.name)

# a = Car("123", "fghdfhgdf")
# a.display()

        
    def dataput(self):
        self.id = int(input("Enter a id :"))
        self.name = input("Enter a name :")
        self.salary = float(input("Enter a salary:"))

    def display(self):
        print(self.id)
        print(self.name)
        print(self.salary)

obj1 = Car()
obj1.dataput()
obj1.display()

class Animal:

    def __init__(self):
        pass

    def dog(self):
        pass

