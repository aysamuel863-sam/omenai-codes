with open("test.txt", "w") as file:
    file.write("Samuel is learning Python.\n")
    file.write("I am building Pocket Tutor")
with open("test.txt", "a") as file:
    file.write("\nPython is fun!")
with open("test.txt", "r") as file:
    content = file.read()
print(content)