class Room:
    def __init__(self, name, available_hours=None):
        # If no value is provided for available_hours, set it to a default value representing the room's
        # availability from 9am to 5pm on all days of the week
        if available_hours is None:
            available_hours = [[9, 10, 11, 12, 13, 14, 15, 16, 17],  # Monday
                               [9, 10, 11, 12, 13, 14, 15, 16, 17],  # Tuesday
                               [9, 10, 11, 12, 13, 14, 15, 16, 17],  # Wednesday
                               [9, 10, 11, 12, 13, 14, 15, 16, 17],  # Thursday
                               [9, 10, 11, 12, 13, 14, 15, 16, 17],  # Friday
                               [9, 10, 11, 12, 13, 14, 15, 16, 17],  # Saturday
                               [9, 10, 11, 12, 13, 14, 15, 16, 17]]  # Sunday

        # Set the name and available_hours attributes of the Room object to the values of the name and
        # available_hours parameters, respectively
        self.name = name
        self.available_hours = available_hours
