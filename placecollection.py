class PlaceCollection:
    UNVISITED = "n"
    VISITED = "v"
    FILENAME = "places.csv"

    @staticmethod
    def load_file():
        with open(PlaceCollection.FILENAME, "r") as file:
            places = [line.strip().split(",") for line in file]
        return places

    @staticmethod
    def save_file(places):
        with open(PlaceCollection.FILENAME, "w") as file:
            for place in places:
                file.write(",".join(place) + "\n")

    @staticmethod
    def add_place(places):
        name = PlaceCollection.empty_input_exception("Name: ")
        country = PlaceCollection.empty_input_exception("Country: ")
        priority = PlaceCollection.negative_priority_exception("Priority: ")
        places.append([name, country, str(priority), PlaceCollection.UNVISITED])
        print(f"{name} in {country} ({priority}) added to Travel Tracker")

    @staticmethod
    def empty_input_exception(prompt):
        while True:
            try:
                user_input = input(prompt)
                if user_input.strip() != "":
                    return user_input
                else:
                    raise ValueError
            except ValueError:
                print("Input cannot be blank")

    @staticmethod
    def negative_priority_exception(prompt):
        while True:
            try:
                user_input = int(input(prompt))
                if user_input <= 0:
                    raise ValueError
                else:
                    return user_input
            except ValueError:
                print("Invalid input. Please enter a positive integer for priority.")
