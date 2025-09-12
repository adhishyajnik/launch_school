def clean_up(alphanum):
    cleaned = ""
    for idx in range(len(alphanum)):
        if alphanum[idx].isalpha():
            cleaned += alphanum[idx]
        elif idx == 0 or cleaned[-1] != " ":
            cleaned += " "
    return cleaned

print(clean_up("---what's my +*& line?"))