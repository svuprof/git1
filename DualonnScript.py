class Card:
    def __init__(self, rank, suit, name):
        self.rank = rank
        self.suit = suit
        self.name = name

cards = []

for suit in ["Diamonds", "Hearts", "Spades", "Clubs"]:
    for rank in range(1, 13):
        name = rank
        match rank:
            case 1:
                name = "Ace"
            case 10:
                name = "Jack"
            case 11:
                name = "Queen"
            case 12:
                name = "King"
        new_card = Card(rank, suit, f"{name} of {suit}")
        cards.append(new_card)

for card in cards:
    print(card.name)