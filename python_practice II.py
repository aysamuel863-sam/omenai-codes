def uppercase(func):
    def wrapper():
        orig_message = func()
        modified_message = orig_message.upper()
        return modified_message
    return wrapper
def lowercase(func):
    def wrapper():
        orig_message = func()
        modified_message = orig_message.lower()
        return modified_message
    return wrapper     
#@lowercase
@uppercase
def greett():
    return "Welcomee"
real = greett()
print(real)
def greet(name):
    return "Hi " + name
def welcome(name, func):
    print(func(name))
    return func
welcome(input("Enter a name: "), greet)
list = [2, 4, "Sam"]
tuple = (2, 4, "Sam")
set = {2, 2, 4, "Sam"}
dict = {2: 2, "Sam": 14}
print(list, tuple, set, dict)