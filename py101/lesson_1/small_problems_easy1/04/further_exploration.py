# Further Exploration: Modify the program to let the user specify the measurement type (meters or feet). Compute the area accordingly and print it and its conversion in parentheses.

def calc_area():
    side1 = float(input('Enter the room length in meters: '))
    side2 = float(input('Enter the room width in meters: '))
    units = input('Do you want the area in square meters (1) or square feet (2)? ')
    
    meas = 'meters' if units == '1' else 'feet'

    area = side1 * side2
    if units == '2':
        area *= 10.7639

    print(f'Area: {area:.2f} square {meas}')

calc_area()