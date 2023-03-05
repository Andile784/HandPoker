from card import Card

def parse_card_string(card_string):
    rank_string, suit_string = card_string[:-1], card_string[-1:]
    rank = int(rank_string) if rank_string.isdigit() else {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}[rank_string.upper()]
    suit = {'C': 'Clubs', 'D': 'Diamonds', 'H': 'Hearts', 'S': 'Spades'}[suit_string.upper()]
    return Card(rank, suit)

def rank_to_int(rank):
    if rank == ' A':
        return 14
    elif rank == 'K': 
        return 13
    elif rank == 'Q':
        return 12
    elif rank == 'J':
        return 11
    elif rank == 'T':
        return 10
    else: 
        return int(rank)






                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
