class Room:
    def __init__(self, name, available_hours=None):
        if available_hours is None:
            available_hours = [[9, 10, 11, 12, 13, 14, 15, 16, 17],
                               [9, 10, 11, 12, 13, 14, 15, 16, 17],
                               [9, 10, 11, 12, 13, 14, 15, 16, 17],
                               [9, 10, 11, 12, 13, 14, 15, 16, 17],
                               [9, 10, 11, 12, 13, 14, 15, 16, 17],
                               [9, 10, 11, 12, 13, 14, 15, 16, 17],
                               [9, 10, 11, 12, 13, 14, 15, 16, 17]]
        self.name = name
        self.available_hours = available_hours
