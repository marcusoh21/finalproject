import crud
from main import fetch_and_store_weather

def main_menu():
    while True:
        print("\nWeather Database CLI")
        print("1. View all entries")
        print("2. Fetch and store latest weather")
        print("3. Modify an entry")
        print("4. Delete an entry")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            entries = crud.get_all_entries()
            if entries:
                for entry in entries:
                    print(entry)
            else:
                print("No data available.")

        elif choice == "2":
            fetch_and_store_weather()

        elif choice == "3":
            entry_id = input("Enter entry ID to modify: ")
            field = input("Which field to modify? (temperature, feels_like, humidity, wind_speed, description): ")
            new_value = input("Enter new value: ")
            crud.update_entry(entry_id, field, new_value)
            print("Entry updated successfully.")

        elif choice == "4":
            entry_id = input("Enter entry ID to delete: ")
            crud.delete_entry(entry_id)
            print("Entry deleted successfully.")

        elif choice == "5":
            print("Exiting CLI.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main_menu()
