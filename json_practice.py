import json
with open("contacts.json", "a") as file:
    f = file.write("I am a boy")
    json.dump(f, file)
