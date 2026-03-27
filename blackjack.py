def card_value(rank):
    if rank in {"Jack", "Queen", "King"}:
        return 10
    if rank == "Ace":
        return 11
    return int(rank)


def hand_value(hand):
    total = 0
    aces = 0

    for rank, _suit in hand:
        total += card_value(rank)
        if rank == "Ace":
            aces += 1

    while total > 21 and aces > 0:
        total -= 10
        aces -= 1

    return total
