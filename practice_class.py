class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

    def fullname(self):
        print(f"{self.first} {self.last}")

emp1 = Employee("Sam", "Ayo", 2000)
print(emp1.first)
emp1.fullname()

class Animal:
    def __init__(self, name, country, number): 
        self.name = name
        self._country = country
        self.__number = number

    def sound(self):
        print("Making a sound!!")

    @staticmethod
    def grade():
        print("Grade B")

class Dog(Animal):
    def __init__(self, name, breed, color, country, number):
        super().__init__(name, country, number)
        self.breed = breed
        self.color = color
        
    def _sound(self):
        super().sound()
        print("Woof Woof")

class Cat(Animal):
    def __init__(self, name, breed, color, country, number):
        super().__init__(name, country, number)
        self.breed = breed
        self.color = color
        
    def sound(self):
        super().sound()
        print("Meow")

dog = Dog("Smart", "Local", "Cream", "Singapore", 3)
cat = Cat("Tuple", "Reed", "Black", "Rwanda", 3789)

print(dog.color)
print(cat.breed)
print(dog._country)
print(cat._Animal__number)
Animal.grade()
dog._sound()
cat.sound()
dog.grade()