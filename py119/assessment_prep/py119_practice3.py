"""
Inputs: string
Outputs: string

Explicit Rules:
- Function returns a copy of in_str where for every third word in the string,
  every second letter is converted to uppercase (i.e. every even letter)
- All other characters should remain the same

Implicit Rules:
- in_str may contain punctuation, but no numeric characters

Data Structure/s:
- string
- list

Algorithm:
- split up in_str into word_list
- out_list = []
- iterate through idx, word in enumerated word_list:
    - if idx + 1 is not divisible by 3:
        - append word to out_list
    - else:
        - out_word = ""
        - iterate through each idx, char in enumerated word:
            - if idx is 0 or even:
                - out_word += char
            - else:
                - out_word += char.upper()
        - out_list.append(out_word)
- return out_list joined to a single string with a space as the separator
"""


def to_weird_case(in_str):
    word_list = in_str.split()
    out_list = []
    for idx, word in enumerate(word_list):
        if (idx + 1) % 3 != 0:
            out_list.append(word)
        else:
            out_word = ""
            for idx, char in enumerate(word):
                if idx % 2 == 0:
                    out_word += char
                else:
                    out_word += char.upper()
            out_list.append(out_word)
    return " ".join(out_list)


original = "Lorem Ipsum is simply dummy text of the printing world"
expected = "Lorem Ipsum iS simply dummy tExT of the pRiNtInG world"
print(to_weird_case(original) == expected)

original = "It is a long established fact that a reader will be distracted"
expected = "It is a long established fAcT that a rEaDeR will be dIsTrAcTeD"
print(to_weird_case(original) == expected)

print(to_weird_case("aaA bB c") == "aaA bB c")

original = "Mary Poppins' favorite word is supercalifragilisticexpialidocious"
expected = "Mary Poppins' fAvOrItE word is sUpErCaLiFrAgIlIsTiCeXpIaLiDoCiOuS"
print(to_weird_case(original) == expected)
