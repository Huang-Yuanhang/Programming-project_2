# Import the necessary classes
from placecollection import PlaceCollection
from place import Place


def run_tests():
    """Test PlaceCollection class."""

    # Test empty PlaceCollection (defaults)
    print("Test empty PlaceCollection:")
    place_collection = PlaceCollection()
    print(place_collection)
    assert not place_collection.load_file()  # an empty list is considered False

    # Test loading places
    print("Test loading places:")
    place_collection.load_file()
    print(place_collection)
    assert place_collection.load_file()  # assuming CSV file is non-empty, non-empty list is considered True

    # Test adding a new Place with values
    print("Test adding new place:")
    place_collection.add_place(Place("Smithfield", "Australia", 5, PlaceCollection.UNVISITED))
    print(place_collection)

    # Test sorting places by priority
    print("Test sorting - priority:")
    print(place_collection)

    # Test sorting places by name
    print("Test sorting - name:")
    print(place_collection)

    # Test saving places
    print("Test saving places:")
    place_collection.save_file(place_collection.load_file())  # Save places back to the file (check CSV file manually)

    # Test clearing places
    print("Test clearing places:")
    print(place_collection)
    assert not place_collection.load_file()  # After clearing, the list should be empty

    # TODO: Add more tests, as appropriate, for each method


run_tests()
