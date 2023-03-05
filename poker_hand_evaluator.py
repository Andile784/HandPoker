from card import Card
from hand import Hand

# Define the poker hands in descending order of rank
POKER_HANDS = [
    ("Royal Flush", lambda ranks, cards: ranks == [10, 11, 12, 13, 14] and len(set([c.suit for c in cards])) == 1),
    ("Straight Flush", lambda ranks, cards: ranks[4] - ranks[0] == 4 and len(set([c.suit for c in cards])) == 1),
    ("Four of a Kind", lambda ranks, cards: len(set(ranks)) == 2 and ranks.count(ranks[0]) in [1, 4]),
    ("Full House", lambda ranks, cards: len(set(ranks)) == 2 and ranks.count(ranks[0]) in [2, 3]),
    ("Flush", lambda ranks, cards: len(set([c.suit for c in cards])) == 1),
    ("Straight", lambda ranks, cards: ranks[4] - ranks[0] == 4 and len(set(ranks)) == 5),
    ("Three of a Kind", lambda ranks, cards: len(set(ranks)) == 3 and ranks.count(ranks[2]) == 3),
    ("Two Pairs", lambda ranks, cards: len(set(ranks)) == 3 and ranks.count(ranks[1]) == 2),
    ("Pair", lambda ranks, cards: len(set(ranks)) == 4),
    ("High Card", lambda ranks, cards: len(set(ranks)) == 5)
]

def evaluate_hand(cards):
    # Create a Hand object and sort the cards by rank
    hand = Hand(cards)
    hand.custom_sort()
    ranks = [card.rank for card in hand.cards]
    
    # Check each hand in descending order of rank
    for hand_name, hand_func in POKER_HANDS:
        if hand_func(ranks, hand.cards):
            return hand_name
    
    # If no hand was found, return "High Card"
    return "High Card"

def test_evaluate_straight_flush():
    hand = Hand([
        Card(10, 'H'),
        Card(9, 'H'),
        Card(8, 'H'),
        Card(7, 'H'),
        Card(6, 'H'),
    ])
    
    assert hand.evaluate() == 'Straight Flush'
