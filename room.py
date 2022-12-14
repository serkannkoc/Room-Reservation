class Room:
    def __init__(self, name, day=-1, hour=-1, duration=-1, available_hours=None):
        if available_hours is None:
            available_hours = [9, 10, 11, 12, 13, 14, 15, 16, 17]
        self.name = name
        self.day = day
        self.hour = hour
        self.duration = duration
        self.available_hours = available_hours
