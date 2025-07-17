# Software Name: Office_Meeting_Room_Scheduler
# Category: Office
# Description: The Office Meeting Room Scheduler is a software designed to simplify the process of scheduling and managing meeting rooms within an office building...

import datetime

class MeetingRoom:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.bookings = {}  # {date: [list of time slots]}

    def is_available(self, date, start_time, end_time):
        """Checks if the room is available for the given date and time slot."""

        if date not in self.bookings:
            return True

        for existing_start, existing_end in self.bookings[date]:
            if start_time < existing_end and end_time > existing_start:
                return False  # Overlapping booking

        return True

    def book_room(self, date, start_time, end_time):
        """Books the room for the given date and time slot."""

        if not self.is_available(date, start_time, end_time):
            return False  # Room is not available

        if date not in self.bookings:
            self.bookings[date] = []

        self.bookings[date].append((start_time, end_time))
        self.bookings[date].sort()  # Keep bookings sorted by start time
        return True

    def cancel_booking(self, date, start_time, end_time):
        """Cancels a booking for the given date and time slot."""

        if date not in self.bookings:
            return False  # No bookings for this date

        booking_to_remove = (start_time, end_time)
        if booking_to_remove in self.bookings[date]:
            self.bookings[date].remove(booking_to_remove)
            return True
        else:
            return False # Booking not found

    def get_bookings(self, date):
        """Returns a list of bookings for the given date."""
        if date in self.bookings:
          return self.bookings[date]
        else:
          return []


class MeetingRoomScheduler:
    def __init__(self):
        self.rooms = {}  # {room_name: MeetingRoom object}

    def add_room(self, room_name, capacity):
        """Adds a new meeting room to the scheduler."""
        if room_name in self.rooms:
            return False # Room already exists
        self.rooms[room_name] = MeetingRoom(room_name, capacity)
        return True

    def remove_room(self, room_name):
        """Removes a meeting room from the scheduler."""
        if room_name in self.rooms:
            del self.rooms[room_name]
            return True
        else:
            return False # Room not found

    def get_room(self, room_name):
        """Returns the MeetingRoom object for the given room name."""
        if room_name in self.rooms:
            return self.rooms[room_name]
        else:
            return None

    def book_room(self, room_name, date_str, start_time_str, end_time_str):
        """Books a room for a specific date and time."""
        room = self.get_room(room_name)
        if not room:
            return False  # Room not found

        try:
            date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
            start_time = datetime.datetime.strptime(start_time_str, "%H:%M").time()
            end_time = datetime.datetime.strptime(end_time_str, "%H:%M").time()
        except ValueError:
            return False  # Invalid date or time format

        return room.book_room(date, start_time, end_time)

    def cancel_booking(self, room_name, date_str, start_time_str, end_time_str):
        """Cancels a booking for a specific room, date and time."""
        room = self.get_room(room_name)
        if not room:
            return False  # Room not found

        try:
            date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
            start_time = datetime.datetime.strptime(start_time_str, "%H:%M").time()
            end_time = datetime.datetime.strptime(end_time_str, "%H:%M").time()
        except ValueError:
            return False  # Invalid date or time format

        return room.cancel_booking(date, start_time, end_time)

    def get_room_availability(self, room_name, date_str):
        """Returns the availability of a room on a given date."""
        room = self.get_room(room_name)
        if not room:
            return None  # Room not found

        try:
            date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            return None #Invalid date format

        return room.get_bookings(date)


if __name__ == '__main__':
    # Example Usage
    scheduler = MeetingRoomScheduler()

    # Add some meeting rooms
    scheduler.add_room("Room 1", 10)
    scheduler.add_room("Room 2", 5)

    # Book Room 1 for a meeting
    success = scheduler.book_room("Room 1", "2024-01-20", "09:00", "10:00")
    if success:
        print("Room 1 booked successfully for 2024-01-20 09:00-10:00")
    else:
        print("Room 1 booking failed.")

    # Check Room 1 availability on 2024-01-20
    availability = scheduler.get_room_availability("Room 1", "2024-01-20")
    if availability:
        print("Room 1 bookings on 2024-01-20:", availability)
    else:
        print("Room 1 is available all day on 2024-01-20.")

    # Try to double book Room 1
    success = scheduler.book_room("Room 1", "2024-01-20", "09:30", "10:30")
    if success:
        print("Room 1 booked successfully for 2024-01-20 09:30-10:30")
    else:
        print("Room 1 booking failed (conflict).")

    # Cancel the booking
    success = scheduler.cancel_booking("Room 1", "2024-01-20", "09:00", "10:00")
    if success:
        print("Room 1 booking cancelled successfully.")
    else:
        print("Room 1 booking cancellation failed.")