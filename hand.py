from card import Card

# Define a Hand class to represent a poker hand
class Hand:
    def __init__(self, cards):
        self.cards = cards

    def custom_sort(self):
        def card_rank(card):
            return card.rank_to_int()

        self.cards.sort(key=card_rank, reverse=True)

        # Handle ties
        for i in range(4):
            if card_rank(self.cards[i]) == card_rank(self.cards[i + 1]):
                # Use lambda function to compare suits if ranks are tied
                self.cards[i:i+2] = sorted(self.cards[i:i+2], key=lambda x: x.suit)

    def evaluate(self):
        self.custom_sort()

        # Check for royal flush
        if self.is_royal_flush():
            return "Royal flush"

        # Check for straight flush
        if self.is_straight_flush():
            return "Straight flush"

        # Check for four of a kind
        if self.is_four_of_a_kind():
            return "Four of a kind"

        # Check for full house
        if self.is_full_house():
            return "Full house"

        # Check for flush
        if self.is_flush():
            return "Flush"

        # Check for straight
        if self.is_straight():
            return "Straight"

        # Check for three of a kind
        if self.is_three_of_a_kind():
            return f"Three of a kind, {self.get_three_of_a_kind_rank()}s"

        # Check for two pairs
        if self.is_two_pairs():
            return f"Two pairs, {self.get_two_pairs_rank()}s and {self.get_second_pair_rank()}s"

        # Check for one pair
        if self.is_one_pair():
            return f"One pair, {self.get_one_pair_rank()}s"

        # If no other hand is formed, return "High card"
        return f"High card, {self.cards[0].get_rank()}"

    def is_royal_flush(self):
        # A royal flush is a straight flush containing Ace, King, Queen, Jack, and 10
        return self.is_straight_flush() and self.cards[0].rank == "A"

    def is_straight_flush(self):
        # A straight flush is any straight all of the same suit.
        # We check if the difference between the highest and lowest card ranks is 4 and all cards have the same suit
        return self.is_straight() and self.is_flush()

    def is_four_of_a_kind(self):
        # Four of a kind is any four cards of the same rank
        ranks = [card.rank_to_int() for card in self.cards]
        return any(ranks.count(rank) == 4 for rank in ranks)

    def is_full_house(self):
        # Full house is any three cards of the same rank together with any two cards of the same rank
        ranks = [card.rank_to_int() for card in self.cards]
        return sorted(set(ranks), key=ranks.count, reverse=True) == [3, 2]

    def is_flush(self):
        # A flush is any five cards of the same suit, but not in a sequence
        suits = [card.suit for card in self.cards]
        return all(suit == suits[0] for suit in suits)

    def is_straight(self):
        # A straight is any five cards in sequence, but not of the same suit
        ranks = [card.rank_to_int() for card in self.cards]
        return max(ranks) - min(ranks) == 4 and len(set(ranks)) == 5

    def is_three_of_a_kind(self):
        # Three of a kind is any three cards of the same rank
        ranks = [card.rank_to_int() for card in self.cards]
        return any(ranks.count(rank) == 3 for rank in ranks)

    def is_two_pairs(self):
        # Two pairs is any two cards of the same rank together with another two cards of the same rank
        ranks = [card.rank_to_int() for card in self.cards]
        return sorted(set(ranks), key=ranks.count, reverse=True) == [2, 2, 1]

    def is_one_pair(self):
        # One pair is any two cards of the same rank
        ranks = [card.rank_to_int() for card in self.cards]
        return any(ranks.count(rank) == 2 for rank in ranks)
