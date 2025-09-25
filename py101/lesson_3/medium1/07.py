munsters = {
    "Herman": {"age": 32, "gender": "male"},
    "Lily": {"age": 30, "gender": "female"},
    "Grandpa": {"age": 402, "gender": "male"},
    "Eddie": {"age": 10, "gender": "male"},
    "Marilyn": {"age": 23, "gender": "female"},
}

def mess_with_demographics(demo_dict):
    for key, value in demo_dict.items():
        value["age"] += 42
        value["gender"] = "other"

mess_with_demographics(munsters)
# This will modify the munsters dictionary because
# keyed reassignment is actually mutating the dictionary rather than
# reassigning the reference to another (local) dictionary.
# Thus, we don't have to return the dictionary or reassign the function's
# output to munsters.

print(munsters)