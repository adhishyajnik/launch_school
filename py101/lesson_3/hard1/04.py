def is_an_ip_number(num_string):
    try:
        num = int(num_string)
    except (TypeError, ValueError):
        return False
    if 0 <= num <= 255:
        return True
    return False

def is_dot_separated_ip_address(input_string):
    dot_separated_words = input_string.split(".")
    if len(dot_separated_words) != 4:
        return False
    while len(dot_separated_words) > 0:
        word = dot_separated_words.pop()
        if not is_an_ip_number(word):
            return False

    return True

print(is_dot_separated_ip_address('192.168.0.1'))
print(is_dot_separated_ip_address('192.168.0'))
print(is_dot_separated_ip_address('192.168.0.5.7'))
print(is_dot_separated_ip_address('192.168.a.1'))