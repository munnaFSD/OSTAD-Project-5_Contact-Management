import os

def add_data(all_contacts):
    #Take the name, and email from user
    name = input("\nEnter your Full name: ").strip().capitalize()
    if name.isalpha():
        email = input("Enter your valid Email address: ").strip()
    else:
        print("\nError: 'The contact's Name must be a string.'")
        return

    #valid phone and email check
    if '@gmail.com' in email:
        phone = input("Enter your Phone Number: ").strip()
        if os.path.exists("contacts.json"):
            if ((len(phone)) == 11) and (phone.isdigit()) and ((phone[:2]) == '01'):
                for each_contact in all_contacts:
                    if each_contact['phone'] == (phone):
                        print("\n'Error: Phone number already exist, please try again!'")
                        return
            else:
                print("\nError: 'The phone number must be 11 digits and valid phone number.'")
                return
    else:
        print("\nError: 'Invalid email, please type your valid email!'")
        return

    #Take the address from user
    address = input("Enter your current Address: ").strip()
    if address.isalpha():
        contacts = {
            'name' : name,
            'email' : email,
            'phone' : phone,
            'address' : address
        }
        all_contacts.append(contacts)
        print("\n'Your Contact added successfully!'")
    else:
        print("\nError: 'The Address Name must be a string.'")
        return