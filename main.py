from deckofcards import DeckOfCards
from blackjack import *

import time


def main():
    deck = DeckOfCards()

    player_hand = []
    dealer_hand = []

    print("Shuffling deck...")
    deck.shuffle_deck()
    time.sleep(1)

    print("Dealing hands...")
    player_hand.append(deck.deal_card())
    player_hand.append(deck.deal_card())
    dealer_hand.append(deck.deal_card())
    dealer_hand.append(deck.deal_card())
    time.sleep(1)

    player_total = hand_value(player_hand)
    dealer_total = hand_value(dealer_hand)

    game_over = False

    while not game_over:

        print(f"Player Hand: {player_hand}, Total: {player_total}")
        print(f"Dealer Hand: {dealer_hand}, Total: {dealer_total}")

        if player_total > 21:
            game_over = True
            break

        print("\n1. Hit\n2. Stand")
        choice = input()

        if choice == "1":
            player_hand.append(deck.deal_card())

        player_total = hand_value(player_hand)

if __name__ == "__main__":
    main()
