with open("notes.txt", "w") as file:
    file.write("Python is awesome!\n")
    file.write("I am learning file handling.")

with open("notes.txt", "a") as file:
    file.write("\nI am learning Python!")
