
def view_data(all_contacts):
    if not all_contacts:
        print("\nError: 'No contacts available right now.'")
        return

    print("\n\t\t\t[-- All Contacts List--]")
    print("-"*75)
    print(f"{"Name"}  \t\t {"Email"} \t\t {"Phone"} \t\t {"Address"}")
    print("-"*75)
    for contact in all_contacts:
        print(f"{contact['name']}  --  {contact['email']}  --  {contact['phone']}  --  {contact['address']}")
