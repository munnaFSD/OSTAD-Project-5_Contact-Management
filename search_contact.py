
def search_data(all_contacts):

    query = input("\nSearch by (name or phone number): ").strip().lower()
    
    for each_contact in all_contacts:
        if (each_contact['name'].lower() == query) or (each_contact['phone'] == query):
            print("\nSearch result:\n--------------")
            print(f"{each_contact['name']}  --  {each_contact['email']}  --  {each_contact['phone']}  --  {each_contact['address']}")
            return
    else:
        print("\nError: 'No contacts available!, please try again.'")

    
    