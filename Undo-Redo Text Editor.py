class StackExample:
    def __init__(self):
        self.undo = []
        self.redo = []
        self.state = ""

    def make_change(self, text):
        self.undo.append(self.state)
        self.state = text
        self.redo.clear()

    def undo_action(self):
        if self.undo:
            self.redo.append(self.state)
            self.state = self.undo.pop()
            print("Undo successful!")
        else:
            print("Nothing to undo.")

    def redo_action(self):
        if self.redo:
            self.undo.append(self.state)
            self.state = self.redo.pop()
            print("Redo successful!")
        else:
            print("Nothing to redo.")

    def display(self):
        print("Current Document:", self.state)

editor = StackExample()

while True:
    print("\n<--- Text Editing Application --->")
    print("1. Make change")
    print("2. Undo")
    print("3. Redo")
    print("4. Display")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        text = input("Enter new document text: ")
        editor.make_change(text)
        print("Change applied.")
    elif choice == '2':
        editor.undo_action()
    elif choice == '3':
        editor.redo_action()
    elif choice == '4':
        editor.display()
    elif choice == '5':
        print("Exiting from System!")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")
