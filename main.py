from deckofcards import DeckOfCards

def main():
    deck = DeckOfCards()
    
    player_hand = []
    dealer_hand = []

    print("Shuffling deck...")
    deck.shuffle_deck()

    print("Dealing hands...")
    player_hand.append(deck.deal_card())
    player_hand.append(deck.deal_card())
    dealer_hand.append(deck.deal_card())
    dealer_hand.append(deck.deal_card())

    player_card1 = player_hand[0][0]
    player_card2 = player_hand[1][0]

    dealer_card1 = dealer_hand[0][0]
    dealer_card2 = dealer_hand[1][0]

    if player_hand[0][0] == "Jack" or player_hand[0][0] == "Queen" or player_hand[0][0] == "King":
        player_card1 = 10

    if player_hand[1][0] == "Jack" or player_hand[1][0] == "Queen" or player_hand[1][0] == "King":
        player_card2 = 10

    if player_hand[0][0] == "Ace":
        player_card1 = 11

    if player_hand[1][0] == "Ace":
        player_card2 = 11

    player_total = int(player_card1) + int(player_card2)

    if player_total > 21 and player_card1 == 11:
        player_card1 = 1
    elif player_total > 21 and player_card2 == 11:
        player_card2 = 1

    player_total = int(player_card1) + int(player_card2)

    if dealer_hand[0][0] == "Jack" or dealer_hand[0][0] == "Queen" or dealer_hand[0][0] == "King":
        dealer_card1 = 10

    if dealer_hand[1][0] == "Jack" or dealer_hand[1][0] == "Queen" or dealer_hand[1][0] == "King":
        dealer_card2 = 10

    if dealer_hand[0][0] == "Ace":
        dealer_card1 = 11

    if dealer_hand[1][0] == "Ace":
        dealer_card2 = 11

    dealer_total = int(dealer_card1) + int(dealer_card2)

    if dealer_total > 21 and dealer_card1 == 11:
        dealer_card1 = 1
    elif dealer_total > 21 and dealer_card2 == 11:
        dealer_card2 = 1

    dealer_total = int(dealer_card1) + int(dealer_card2)

    print(f"Player Hand: {player_hand}, Total: {player_total}")
    print(f"Dealer Hand: {dealer_hand}, Total: {dealer_total}")

if __name__ == "__main__":
    main()
