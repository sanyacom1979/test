class Stydent:

    def __init__(self, name, group_number, age):
        self.name = name
        self.group_number = group_number
        self.age = age

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getGroupNumber(self):
        return self.group_number

    def setName(self, name):
        self.name = name

    def setAge(self, age):
        self.age = age

    def setGroupNumber(self, group_number):
        self.group_number = group_number



st1 = Stydent("Иван", 12, 20)
print(f"Имя {st1.name}")
print(f"Группа № {st1.group_number}")
print(f"Возраст {st1.age}")
st1.setName("Петр")
print(f"Изм имя {st1.name}")

st2 = Stydent("Ольга", 9, 18)
print(f"Имя {st2.name}")
print(f"Группа № {st2.group_number}")
print(f"Возраст {st2.age}")
st2.setAge(16)
print(f"Изм Возраст {st2.age}")