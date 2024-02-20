"""
Name: Yuanhang Huang
Date: Sep 14, 2023
Brief Project Description: cp1404-travel-tracker-assignment-2-Huang-Yuanhang
GitHub URL: https://github.com/JCUS-CP1404/cp1404-travel-tracker-assignment-2-Huang-Yuanhang.git
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from placecollection import PlaceCollection
from place import Place


class PlaceListView(BoxLayout):
    place_list = ObjectProperty(None)
    sorter = ObjectProperty(None)
    name_input = ObjectProperty(None)
    country_input = ObjectProperty(None)
    priority_input = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(PlaceListView, self).__init__(**kwargs)
        self.places = PlaceCollection.load_file()

    def update_place_list(self):
        self.place_list.clear_widgets()
        for place in self.places:
            place_widget = PlaceWidget(place=place)
            self.place_list.add_widget(place_widget)

    def add_place(self):
        name = self.name_input.text
        country = self.country_input.text
        priority = int(self.priority_input.text)
        new_place = Place(name, country, priority)
        self.places.append(new_place)
        PlaceCollection.save_file(self.places)
        self.update_place_list()
        self.clear_input_field()

    def clear_input_field(self):
        self.name_input.text = ""
        self.country_input.text = ""
        self.priority_input.text = ""

    def on_sorter_text(self, instance, value):
        if value == "name":
            self.places.sort(key=lambda place: place.name)
        elif value == "country":
            self.places.sort(key=lambda place: place.country)
        elif value == "priority":
            self.places.sort(key=lambda place: place.priority)
        elif value == "is_visited":
            self.places.sort(key=lambda place: place.visited, reverse=True)
        self.update_place_list()


class PlaceWidget(BoxLayout):
    place = ObjectProperty(None)


class TravelTrackerApp(App):
    def build(self):
        return PlaceListView()


if __name__ == '__main__':
    TravelTrackerApp().run()
