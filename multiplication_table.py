class Multiplication:
    def __init__(self, number, range_stop):
        self.number = number
        self.range_stop = range_stop

    def multiple(self):
        for i in range(1, self.range_stop):
           print(f"{self.number} x {i} = {self.number * i}")
        
number = int(input("Enter number to be multiplied: "))
range_stop = int(input("Enter number where the multiplication stops: ")) + 1

user_choice = Multiplication(number, range_stop)

user_choice.multiple()