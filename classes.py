class Human:

    def __init__(self, name):
        self.name = name
    
person1 = Human("mat")
print(person1.name)


class Family_Member(Human):

    def __init__(self, name):
        Human.__init__(self, name)
        self.surname = "Schofield"
        


person2 = Family_Member("meg")

print(person2.name, end=' ')
print(person2.surname)