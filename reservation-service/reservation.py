class Reservation:
    """
        This is a class to represent a reservation.
        A reservation has name,activity,day,hours,duration and id .
        """
    def __init__(self, name,activity,day,hours,duration,id):
        """
                Initialize a new reservation instance with a given name,activity,day,hours,duration and id.

                Parameters:
                name (str): The name of the room.
                activity (str): The name of the activity.
                day (int): The day of the reservation done.
                hours (int): The hours of the reservation day.
                duration (int): Duration of the reservation.
                id (int): The identity of the reservation.

                """
        self.name = name
        self.activity = activity
        self.day = day
        self.hours = hours
        self.duration = duration
        self.id = id