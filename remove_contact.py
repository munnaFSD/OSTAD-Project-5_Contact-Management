from save_and_load import load_data,save_data

all_contacts = load_data()

def remove_data(all_contacts):
    phone  = input("\nEnter your phone number for removal: ").strip().lower()

    if ((len(phone)) == 11) and (phone.isdigit()):
        for each_contact in all_contacts:
            if (each_contact['phone']) == (phone):
                all_contacts.remove(each_contact)
                save_data(all_contacts)
                print("\n'The contact has been removed successfully.'")
                return
    else:
        print("\nError: 'The phone number must be 11 digits.'")
        return


    
