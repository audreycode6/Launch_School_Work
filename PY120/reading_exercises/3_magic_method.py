''' Create the classes needed to make the following code work as shown:
Don't worry about ties or whether votes should be singular.'''


class Candidate:
    def __init__(self, name):
        self.name = name
        self.votes = 0

    def __iadd__(self, other):
        # ensure we are adding an int
        if not isinstance(other, int):
            return NotImplemented
        self.votes += other
        return self

class Election:
    def __init__(self, candidates):
        self.candidates = candidates 
    
    def results(self):
        max_votes = 0
        total_votes = 0
        winner = None

        # loop throguh candidates and calculate votes and find the winner
        for candidate in self.candidates:
            total_votes += candidate.votes
            if candidate.votes > max_votes:
                max_votes = candidate.votes
                winner = candidate.name

        # print each candidate total votes
        for candidate in self.candidates:
            print(f"{candidate.name}: {candidate.votes} votes")
            
        # calculate and print th winners percentage of votes
        percent = 100 * (max_votes / total_votes)
        print()
        print(f"{winner} won: {percent}% of votes")

# Test cases
mike_jones = Candidate('Mike Jones')
susan_dore = Candidate('Susan Dore')
kim_waters = Candidate('Kim Waters')

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

'''OUTPUT:
Mike Jones: 3 votes
Susan Dore: 4 votes
Kim Waters: 1 votes

Susan Dore won: 50.0% of votes'''