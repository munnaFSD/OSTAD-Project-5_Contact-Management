from save_and_load import load_data,save_data
from add_contact import add_data
from view_contact import view_data
from remove_contact import remove_data
from search_contact import search_data



def menu_options():
    print(
        "\n\n---------------------------------------------"
        "\nWelcome to the Contact Book Management System",
        "\n---------------------------------------------"
    )
    options = [
        "Add New Contact",
        "View All Contacts",
        "Remove Contact",
        "Search Contact",
        "Exit the Program"
    ]
    for index, each_option in enumerate(options, start=1):
        print(f"{index}. {each_option}")
    return True
    
def main():
    #all data stored by contacts variable
    all_contacts = load_data()
    
    while True:
        #user option showing
        menu_options()

        choice = input("\nEnter your choice Number(1/5): ")

        if choice == '1':
            add_data(all_contacts)
            save_data(all_contacts)
        elif choice == '2':
            view_data(all_contacts)
        elif choice == '3':
            remove_data(all_contacts)
        elif choice == '4':
            search_data(all_contacts)
        elif choice == '5':
            print("\n'Thank you for choosing our contact management system!'")
            break
        else:
            print("\n'Invalid option! Try again.'\n")

if __name__ == "__main__":
    main()