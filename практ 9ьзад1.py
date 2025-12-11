def add_note():
    global notebook
    header = input("Header: ")
    text = input("Text: ")
    notebook[header] = text
    print(f"Note '{header}' added successfully.")

def read_notes():
    global notebook
    if not notebook:
        print("Заметок нет.")
        return
    
    print(", ".join(notebook.keys()))
    note_name = input("Which note to read?\n> ")
    
    if note_name in notebook:
        print(notebook[note_name])
    else:
        print("Такой заметки нет.")

def delete_note():
    global notebook
    if not notebook:
        print("Заметок нет.")
        return
    
    print(", ".join(notebook.keys()))
    note_name = input("Which note to delete?\n> ")
    
    if note_name in notebook:
        notebook.pop(note_name)
        print(f"Note {note_name} removed")
    else:
        print("Такой заметки нет.")

def main_menu():
    while True:
        print("\n[1] - Create a new note. [2] - Read all notes. [3] - Delete entry. [4] - Exit.")
        choice = input("> ")
        
        if choice == "1":
            add_note()
        elif choice == "2":
            read_notes()
        elif choice == "3":
            delete_note()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


notebook = {}
main_menu()
