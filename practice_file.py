with open("practice.txt", "r") as file:
    content = file.read()
    print(content)
with open("practicr.txt", "a") as file:
    file.write("Atom")

with open("practice.txt", "w") as file:
    file.write("Geometry")
with open("practice.txt", "a") as file:
    file.write("Atom")
with open("practice.txt", "r") as file:
    lines = file.readlines()
del lines[0]
with open("practice.txt", "w") as file:
    file.writelines(lines)
