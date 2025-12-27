def book_seat(seat_number, total_seats, booked_seats):
    if seat_number < 1 or seat_number > total_seats:
        print("Invalid seat number")
    elif seat_number in booked_seats:
        print(f"Seat {seat_number} is already booked")
    else:
        booked_seats.append(seat_number)


def cancel_seat(seat_number, booked_seats):
    if seat_number in booked_seats:
        booked_seats.remove(seat_number)
    else:
        print(f"Seat {seat_number} is not booked, cannot cancel")


def get_available_seats(total_seats, booked_seats):
    return [seat for seat in range(1, total_seats + 1) if seat not in booked_seats]


# Input example
total_seats = 10
booked_seats = [2, 5, 7]

book_seat_number = 3
cancel_seat_number = 5

# Operations
book_seat(book_seat_number, total_seats, booked_seats)
cancel_seat(cancel_seat_number, booked_seats)

available_seats = get_available_seats(total_seats, booked_seats)

# Output
print("Available seats:", available_seats)
