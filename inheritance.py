class Parent():

    gender = 'female'
    def print_last_name(self):
        print("Robert")

class Child(Parent):

    gender = "male"
    def print_first_name(self):
        print("child")

    # def print_last_name(self):
    #     print("Bucky")

bucky = Child()
print(bucky.gender)
bucky.print_first_name()
bucky.print_last_name()