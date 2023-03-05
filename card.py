#Define a Card class to represent a playing card
class Card:
    def __init__(self, rank, suit):
        self.rank = int(rank)
        self.suit = suit


    def __repr__(self):
        return f"{self.rank}{self.suit}"

    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit

    def __lt__(self, other):
        return self.rank < other.rank

    def __hash__(self):
        return hash(str(self))

    def get_rank(self):
        return self.rank

    def get_suit(self):
        return self.suit

    def is_same_rank(self, other):
        return self.rank == other.rank

    def is_one_rank_higher_than(self, other):
        return self.rank - other.rank == 1

    def is_one_rank_lower_than(self, other):
        return other.rank - self.rank == 1

    def is_ace(self):
        return self.rank == 'A'

    def is_king(self):
        return self.rank == 'K'

    def is_queen(self):
        return self.rank == 'Q'

    def is_jack(self):
        return self.rank == 'J'

    def is_ten(self):
        return self.rank == 'T'
    
    # Convert rank to integer. Ace is 14, King is 13, Queen is 12, Jack is 11, and 10 is 10.
    def rank_to_int(self):
        if self.rank == 'A':
            return 14
        elif self.rank == 'K':
            return 13
        elif self.rank == 'Q':
            return 12
        elif self.rank == 'J':
            return 11
        elif self.rank == 'T':
            return 10
        else:
            return int(self.rank)
