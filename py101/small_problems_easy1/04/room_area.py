# Build a program that asks the user to enter the length and width of a room, in meters, then prints the room's area in both square meters and square feet.

def square_meters_to_ft(area):
    return area * 10.7639

def area(length, width):
    return length * width

def user_area():
    side1 = float(input('Enter the room length in meters: '))
    side2 = float(input('Enter the room width in meters: '))

    area_m = area(side1, side2)
    area_f = square_meters_to_ft(area_m)

    print(f'Area: {area_m:.2f} square meters, or {area_f:.2f} square feet.')

user_area()