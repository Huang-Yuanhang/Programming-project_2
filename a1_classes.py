"""..."""
# Copy your first assignment to this file, then update it to use Place class
# Optionally, you may also use PlaceCollection class

from place import Place

import random
from place import Place
from placecollection import PlaceCollection

# Constants
UNVISITED = "n"  # Unvisited places status in the file is n.
VISITED = "v"    # visited places status in the file is v.
FILENAME = "places.csv"
LIST = ("\nMenu:\n"
        "\nL - List places"
        "\nR - Recommend random place"
        "\nA - Add new place"
        "\nM - Mark a place as visited"
        "\nQ - Quit")


# Function to display list of places and calculates the remaining number of places to visit.
def display_list_of_places(places):
    # Print the title
    print("\nList of Places:")
    # Initialise the index
    index = 1
    # Iterate over all places and print their information
    for place in places:
        print(f"{index}. {place[0]} in {place[1]} {place[2]}")
        index += 1
    # Initialise the count of unvisited places
    unvisited_count = 0
    # Iterate through all places again to count unvisited places
    for place in places:
        if place[3].strip() == UNVISITED:
            unvisited_count += 1
    # Check if there are unvisited places and provide the corresponding output
    if unvisited_count > 0:
        print(f"{index}. places. You still want to visit {unvisited_count} places.")

    else:
        print(f"{index}. No places left to visit. Why not add a new place?")


# Function to display random places for user, if the file have unvisited places.
def recommend_place(places):
    # Filter unvisited places from a list of places using list derivation
    unvisited_places = [place for place in places if place[3].strip() == UNVISITED]
    # If there are unvisited places, randomly select a place and provide a recommendation
    if unvisited_places:  # Conditional judgment, executed when the condition is equal to true.
        random_place = random.choice(unvisited_places)
        print(f"Not sure where to visit next?\nHow about... {random_place[0]} in {random_place[1]}?")

    else:
        # If there are no unvisited places, prompt for no places to visit
        print("No places left to visit!")


def mark_visited(places):
    # display list of places
    display_list_of_places(places)
    while True:
        try:
            # Get the number of a place as visited by the user
            choice = int(input("Enter the number of a place to mark as visited\n"))
            # Check if the input is valid
            if 1 <= choice <= len(places) and places[choice - 1][3].strip() == UNVISITED:
                places[choice - 1][3] = VISITED
                print(f"{places[choice - 1][0]} in {places[choice - 1][1]} visited!")
                break

            elif choice == 0:
                print("Number must be > 0")

            elif choice > len(places):
                print("Invalid place number")

            elif places[choice - 1][3].strip() == VISITED:
                print("You have already visited this place.")

        except ValueError:
            print("Invalid input; enter a valid number.")


def user_choice(places):
    while True:
        # Print menu options.
        print(LIST)
        # Get user input and convert it to lowercase
        choice = input(">>> ").lower()
        # Perform the appropriate action based on the user's choice
        if choice == "l":
            # Display the list of places
            display_list_of_places(places)
        elif choice == "r":
            # recommend places
            recommend_place(places)
        elif choice == "a":
            # Add a new place
            PlaceCollection.add_place(places)
        elif choice == "m":
            # Mark the place as visited
            mark_visited(places)
        elif choice == "q":
            # Save the place information to a file and exit the program
            PlaceCollection.save_file(places)
            print(len(places), "places saved to", FILENAME)
            print("\nHave a nice day :)")
            break
        else:
            # Handle invalid menu options
            print("Invalid menu choice")


def main():
    print("Travel Tracker 2.0 - by <Yuanhang Huang>")
    places = PlaceCollection.load_file()
    place = Place
    print(len(places), "places loaded from", FILENAME)

    user_choice(places)


if __name__ == '__main__':
    main()