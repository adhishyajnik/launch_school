# Launch School - Introduction to Programming With Python
# Introduction to Programming, Chapter 7: Intro To Collections

country_dict = {
    'Alice' : 'USA',
    'Francois' : 'Canada',
    'Inti' : 'Peru',
    'Monika' : 'Germany',
    'Sanyu' : 'Uganda',
    'Yoshitaka' : 'Japan',
}

def get_country(key):
    return country_dict[key]

repeat = 'y'
while repeat.lower() == 'y':
    input_name = input('Enter a name from the following:\n'
                    'Alice\n'
                    'Francois\n'
                    'Inti\n'
                    'Monika\n'
                    'Sanyu\n'
                    'Yoshitaka\n\n'
                    )

    print(f'{input_name} is from {get_country(input_name)}\n')
    repeat = input('Do you want to enter another name (Y/N)? ')