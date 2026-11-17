"""
Challenge: Create the classes needed to make the following code work as shown.
Don't worry about ties or whether votes should be singular.
"""


class Candidate:
    def __init__(self, name):
        self.name = name
        self.votes = 0

    def __iadd__(self, number):
        if not isinstance(number, int):
            return NotImplemented
        self.votes += 1
        return self


class Election:
    def __init__(self, candidate_set):
        self.candidates = candidate_set

    def results(self):
        total_votes = 0
        most_votes = 0
        winner = None

        for candidate in self.candidates:
            print(f"{candidate.name}: {candidate.votes} votes")

            total_votes += candidate.votes

            if candidate.votes > most_votes:
                most_votes = candidate.votes
                winner = candidate.name

        winner_pct = (most_votes / total_votes) * 100
        print(f"\n{winner} won: {winner_pct}% of votes")


mike_jones = Candidate("Mike Jones")
susan_dore = Candidate("Susan Dore")
kim_waters = Candidate("Kim Waters")

candidates = {
    mike_jones,
    susan_dore,
    kim_waters,
}

votes = [
    mike_jones,
    susan_dore,
    mike_jones,
    susan_dore,
    susan_dore,
    kim_waters,
    susan_dore,
    mike_jones,
]

for candidate in votes:
    candidate += 1

election = Election(candidates)
election.results()
# Mike Jones: 3 votes
# Susan Dore: 4 votes
# Kim Waters: 1 votes

# Susan Dore won: 50.0% of votes
