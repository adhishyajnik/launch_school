def greetings(name, job):
    full_name = " ".join(name)
    full_job = f"{job['title']} {job['occupation']}"
    return f"Hello, {full_name}! Nice to have a {full_job} around."

greeting = greetings(
    ["John", "Q", "Doe"],
    {"title": "Master", "occupation": "Plumber"},
)

print(greeting)