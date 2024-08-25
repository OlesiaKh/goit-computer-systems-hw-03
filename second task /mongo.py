from pymongo import MongoClient
from pymongo.errors import PyMongoError, ServerSelectionTimeoutError

# Establish a connection to the MongoDB server
try:
    connection = MongoClient("mongodb://localhost:27017/")
    database = connection["petDB"]
    pets_collection = database["petProfiles"]
    # Check if the connection is successful
    connection.admin.command('ping')
    print("Connected to MongoDB successfully")
except ServerSelectionTimeoutError:
    print("Unable to connect to MongoDB. Please check your connection settings.")


def add_pet_profile():
    try:
        pet_name = input("Enter the pet's name: ")
        pet_age = int(input("Enter the pet's age: "))
        traits = input("List the pet's traits, separated by commas: ")
        traits_list = [trait.strip() for trait in traits.split(",")]
        profile = {"pet_name": pet_name, "age": pet_age, "traits": traits_list}
        pets_collection.insert_one(profile)
        print("Pet profile added successfully.")
    except PyMongoError as error:
        print(f"Error encountered while interacting with MongoDB: {error}")
    except ValueError as error:
        print(f"Input error: {error}")


def display_all_pets():
    pet_profiles = list(pets_collection.find({}))
    for profile in pet_profiles:
        print(profile)


def search_pet_by_name():
    pet_name = input("Enter the pet's name to search for: ")
    pet_profile = pets_collection.find_one({"pet_name": pet_name})
    print(pet_profile)


def update_pet_age():
    try:
        pet_name = input("Enter the pet's name to update its age: ")
        new_age = int(input("Enter the new age for the pet: "))
        update_result = pets_collection.update_one({"pet_name": pet_name}, {"$set": {"age": new_age}})
        if update_result.modified_count > 0:
            print("Pet's age updated successfully.")
        else:
            print("Pet not found or age is already set.")
    except PyMongoError as error:
        print(f"Error encountered while interacting with MongoDB: {error}")
    except ValueError as error:
        print(f"Input error: {error}")


def add_trait_to_pet():
    try:
        pet_name = input("Enter the pet's name to add a trait: ")
        new_trait = input("Enter the new trait to add: ")
        update_result = pets_collection.update_one({"pet_name": pet_name}, {"$addToSet": {"traits": new_trait}})
        if update_result.modified_count > 0:
            print("Trait added to the pet successfully.")
        else:
            print("Pet not found or trait already exists.")
    except PyMongoError as error:
        print(f"Error encountered while interacting with MongoDB: {error}")


def remove_pet_profile():
    try:
        pet_name = input("Enter the pet's name to remove: ")
        delete_result = pets_collection.delete_one({"pet_name": pet_name})
        if delete_result.deleted_count > 0:
            print("Pet profile removed successfully.")
        else:
            print("Pet not found.")
    except PyMongoError as error:
        print(f"Error encountered while interacting with MongoDB: {error}")


def remove_all_profiles():
    pets_collection.delete_many({})
    print("All pet profiles removed.")


def main_menu():
    while True:
        print("\nAvailable options:")
        print("1 - Add a new pet profile")
        print("2 - Display all pet profiles")
        print("3 - Search for a pet by name")
        print("4 - Update a pet's age")
        print("5 - Add a trait to a pet")
        print("6 - Remove a pet profile")
        print("7 - Remove all pet profiles")
        print("8 - Exit")
        action = input("Choose an option: ")

        if action == "1":
            add_pet_profile()
        elif action == "2":
            display_all_pets()
        elif action == "3":
            search_pet_by_name()
        elif action == "4":
            update_pet_age()
        elif action == "5":
            add_trait_to_pet()
        elif action == "6":
            remove_pet_profile()
        elif action == "7":
            remove_all_profiles()
        elif action == "8":
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main_menu()
