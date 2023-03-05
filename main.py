from card import Card
from poker_hand_evaluator import Hand

def main():
    # Prompt the user to enter five cards
    card_str = input("Enter five cards (e.g. 2H 3C 4S 5D 6H): ")

    # Split the input string into pairs of characters
    card_pairs = card_str.split()
    if len(card_pairs) != 5:
        print("Error: Please enter five cards.")
        return

    # Create a Card object from each pair of characters and add them to a list of cards
    cards = []
    for card_pair in card_pairs:
        if len(card_pair) != 2:
            print("Error: Invalid card format.")
            return
        card = Card(card_pair[0], card_pair[1])
        cards.append(card)

    # Create a Hand object from the list of cards
    hand = Hand(cards)

    # Evaluate the hand and print the result
    result = hand.evaluate()
    print(result)

if __name__ == '__main__':
    main()

