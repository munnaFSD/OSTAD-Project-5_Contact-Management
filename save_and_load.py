import json

file_Name = "contacts.json"

def load_data():
    try:
        with open(file_Name, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("\nError: 'No previous contacts found'")
        return 
    except json.JSONDecodeError:
        print("\nError: 'Error reading contacts file.'")
        return 

def save_data(contacts):
    with open(file_Name, 'w') as file:
        json.dump(contacts, file, indent=4)
