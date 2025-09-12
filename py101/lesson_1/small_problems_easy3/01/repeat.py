def repeat(string, integer):
    for i in range(integer):
        print(string)

def repeat2(string, integer):
    print(f'{(string + '\n') * integer}')

repeat('Hello', 3)

repeat2('Goodbye', 5)