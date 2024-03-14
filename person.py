class  teacher:
    def __init__(self,name,phone_number,):
        self.name = name
        self.phone_number = phone_number

class staff(teacher):
    def __init__(self,name,phone_number,occupation):
        super().__init__(name,phone_number)
        self.occupation = occupation

t1 = teacher("Jack Mghalu",'0745923788')
print(f'{t1.name} {t1.phone_number}')
s1 = staff("John Nderitu",'0743454998','cook')
print(f'{s1.name} {s1.phone_number} {s1.occupation}')








class person:

    def __init__(self,name,country,birth_year):
        self.name = name
        self.country = country
        self.birth_year = birth_year

    def display(self):
        print(self.name,self.country,self.birth_year)
    def calculate_age(self):
        self.birth_year=int(2024)-int(self.birth_year)
        print(self.birth_year)

p1 = person('John Kigotho','Kenya',1997)
p1.display()
p1.calculate_age()

class person:
    def __init__(self,name,id):
        self.name = name
        self.id = id

    def display1(self):
        print(self.name,self.id)

    # class employee:
    #     def __init__(self,name,id,occupation):
    #         self.name = name
    #         self.id = id
    #         self.occupation = occupation
    #
    #
    # class student:
    #     def __init__(self,name,form):
    #         self.name = name
    #         self.form = form
    #
    #
    # class person_info(employee,student):
    #     def __init__(self,name,id,form,occupation):
    #         super().__init__(name,id,form,occupation)
    #
    #
    #
    #
    # pi1 = person_info('Leah Mwihia',"n/a","4e","n/a")
    # pi1.person_info()


