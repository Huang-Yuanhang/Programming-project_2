class Place:
    def __init__(self, name="", country="", priority=0, visited=False):
        self.name = name
        self.country = country
        self.priority = priority
        self.visited = visited

    def __str__(self):
        visited_status = "Visited" if self.visited else "Unvisited"
        return f"{self.name} in {self.country} (Priority: {self.priority}) - {visited_status}"

    def mark_visited(self):
        self.visited = True

    def mark_unvisited(self):
        self.visited = False

    def is_important(self):
        return self.priority <= 2
