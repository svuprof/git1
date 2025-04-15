import random
import time

BLACKJACK = 21

# Function to create a standard deck of cards
def create_deck():
    deck = []
    # Generate cards for each suit and rank
    for suit in ['Spades', 'Hearts', 'Diamonds', 'Clubs']:
        for rank in range(2, 15):  # Ranks 2 through Ace (Ace represented as 14)
            card_rank = rank
            score = min(rank, 10)  # Score is rank unless rank exceeds 10 (for face cards)
            weight = 0  # Default weight
            if rank == 11:
                card_rank = 'Jack'
                weight = 1
            elif rank == 12:
                card_rank = 'Queen'
                weight = 2
            elif rank == 13:
                card_rank = 'King'
                weight = 3
            elif rank == 14:
                card_rank = 'Ace'
                weight = 4
            card = (card_rank, suit, score, weight)
            deck.append(card)
    return deck


# Function to read and print the cards in a hand
def read_hand(hand):
    hand_score = 0
    hand_weight = 0
    aces = 0
    # print(f"{role.capitalize()} has ", end='|')
    for card in hand:
        card_rank, suit, score, weight = card
        # print(f" {card_rank} of {suit} ", end='|')
        hand_score += score
        hand_weight += weight
        if card_rank == 'Ace':
            aces += 1

    # Adjust score if there are Aces and the total score is over 21
    while hand_score > BLACKJACK and aces > 0:
        hand_score -= 10
        aces -= 1

    # print(f" Score: {hand_score}", end='')
    # # Print special messages for Blackjack and Bust
    # if hand_score == BLACKJACK:
    #     print(" *Blackjack!*")
    # elif hand_score > BLACKJACK:
    #     print(" *Bust!*")
    # else:
    #     print("")
    return hand_score, hand_weight


# Function to determine the winner based on hand scores
def determine_winner(player_results, dealer_results):
    player_hand_score, player_hand_weight = player_results
    dealer_hand_score, dealer_hand_weight = dealer_results

    #  Break ties if possible
    if player_hand_score == dealer_hand_score:
        if player_hand_weight > dealer_hand_weight:
            return "Player wins!", 'P'
        elif player_hand_weight < dealer_hand_weight:
            return "Dealer wins!", 'D'
        else:
            return "It's a tie.", 'T'

    if player_hand_score == BLACKJACK:
        return "Player wins with Blackjack!", 'P'
    elif dealer_hand_score == BLACKJACK:
        return "Dealer wins with Blackjack!", 'D'
    elif player_hand_score > BLACKJACK:
        return "Dealer wins, Player busts!", 'D'
    elif dealer_hand_score > BLACKJACK:
        return "Player wins, Dealer busts!", 'D'
    elif player_hand_score > dealer_hand_score:
        return "Player wins!", 'P'
    else:
        return "Dealer wins!", 'D'


# Function to play the game
def play_game(deck, player_risk, dealer_risk):
    # Shuffle the deck
    random.shuffle(deck)

    # Deal initial hands
    player_hand = deck[0:2]
    dealer_hand = deck[2:4]
    deck = deck[4:]

    # Player's turn
    player_results = read_hand(player_hand)
    while player_results[0] < player_risk:
        # print("  Player hits")
        player_hand.append(deck[0])
        deck = deck[1:]
        player_results = read_hand(player_hand)

    # if player_risk <= player_results[0] < BLACKJACK:
    #     print("  Player stands")

    # Dealer's turn
    dealer_results = read_hand(dealer_hand)
    while dealer_results[0] < dealer_risk and player_results[0] <= BLACKJACK:
        # print("  Dealer hits")
        dealer_hand.append(deck[0])
        deck = deck[1:]
        dealer_results = read_hand(dealer_hand)

    # Dealer stands if their score is greater than player's and not busted
    # if player_results[0] <= BLACKJACK and dealer_results[0] < player_results[0]:
    #     print("  Dealer stands")

    # Determine the winner
    declaration, result = determine_winner(player_results, dealer_results)
    # print(declaration)
    return result


# Create the deck
start_deck = create_deck()

master_results = []

test_risk = 10
start_time = time.time()
while test_risk < 20:
    test_risk += 1
    player_wins = 0
    dealer_wins = 0
    ties = 0
    experiments = 0
    while experiments < 1000000:  # Run 1 million times!
        blackjack_deck = start_deck[:]  # Make a copy of the start_deck
        winner = play_game(blackjack_deck, test_risk, 17)
        # Increment the counters based on the game result
        if winner == 'P':
            player_wins += 1
        elif winner == 'D':
            dealer_wins += 1
        elif winner == 'T':
            ties += 1
        experiments += 1  # Increment the experiments counter

    game_results = [test_risk, player_wins, dealer_wins, ties]  # Compile results
    master_results.append(game_results)  # Add results from games to list

end_time = time.time()  # Stop the clock
elapsed_time = end_time - start_time  # Find elapsed time
minutes = int(elapsed_time // 60)  # Calculate minutes
seconds = int(elapsed_time % 60)  # Calculate seconds
print(f"\r{minutes:02}:{seconds:02}", flush=True)  # Print the time in MM:SS format

print(master_results)