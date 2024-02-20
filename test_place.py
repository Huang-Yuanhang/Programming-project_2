"""(Incomplete) Tests for Place class."""
from place import Place


def run_tests():
    """Test Place class."""

    # Test empty place (defaults)
    print("Test empty place:")
    default_place = Place()
    print(default_place)
    assert default_place.name == ""
    assert default_place.country == ""
    assert default_place.priority == 0
    assert not default_place.visited  # Corrected from "is_visited" to "visited"

    # Test initial-value place
    print("Test initial-value place:")
    new_place = Place("Malagar", "Spain", 1, False)
    print(new_place)  # Check if the string representation is correct
    assert new_place.name == "Malagar"
    assert new_place.country == "Spain"
    assert new_place.priority == 1
    assert not new_place.visited

    # Test mark_visited method
    print("Test mark_visited method:")
    new_place.mark_visited()
    assert new_place.visited

    # Test mark_unvisited method
    print("Test mark_unvisited method:")
    new_place.mark_unvisited()
    assert not new_place.visited

    # Test is_important method
    print("Test is_important method:")
    assert new_place.is_important()  # Priority is 1, which is less than or equal to 2

    # Test another place with a different priority
    print("Test another place with a different priority:")
    important_place = Place("Eiffel Tower", "France", 3, True)
    assert not important_place.is_important()  # Priority is 3, which is greater than 2

    print("All tests passed!")


run_tests()
