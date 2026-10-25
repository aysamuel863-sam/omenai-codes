class Student:
    def __init__(self, name, class_level):
        self.name = name
        self.class_level = class_level

    def introduce(self):
        print(f"Hi, I'm {self.name} and I'm in {self.class_level}")

student1 = Student("Samuel", "SS2")
student2 = Student("Desiire", "SS2")

student1.introduce()
student2.introduce()

class Note:
    def __init__(self, subject, topic, content):
        self.subject = subject
        self.topic = topic
        self.content = content
    def display(self):
        print(f"[{self.subject}] {self.topic}")
        print(f"    {self.content}\n")
    def save(self):
        with open("pocket_notes.txt", "a") as file:
            file.write(f"\n{self.subject}|{self.topic}|{self.content}\n")
        print("Note saved!")
    @staticmethod
    def load_all():
        print("---- YOUR SAVED NOTES ----")
        try:
            with open("pocket_notes.txt", "r") as file:
                for line in file:
                    subject, topic, content = line.strip().split("|")
                    print(f"[{subject}] {topic} : {content}\n")
        except FileNotFoundError:
            print("No notes yet. Create one first!")
 
print("1.   Add Note")
print("2.   View All Notes")
choice = input("Choose: ")

if choice == "1":
    subject = input("Subject: ").capitalize()
    topic = input("Topic: ").capitalize()
    content = input("Content: ").capitalize()
    new_note = Note(subject, topic, content)
    new_note.save()

elif choice == "2":
    Note.load_all()