def penultimate(words):
    return words.split()[-2]

print(penultimate("last word") == "last")
print(penultimate("Launch School is great!") == "is")