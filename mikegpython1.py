import random

def first_deal(deck):
    playerhand = deck[0:3:2]
    dealerhand = deck[1:4:2]
    deck = deck[4:]

    playertot1, playerbonus1, playerspecial1 = total(playerhand)
    dealertot1, dealerbonus1, dealerspecial1 = total(dealerhand)

    print("Let's play! I will deal the first hands\n")
    print(f"Player: {showhand(playerhand)} ({playertot1}) {playerspecial1}")
    print(f"Dealer: {showhand(dealerhand)} ({dealertot1}) {dealerspecial1}\n")
    return deck, playerhand, dealerhand


def create_deck(the_list, range_len, separator=""):
    deck = []
    for data in the_list:
        for x in range(1, range_len):
            deck.append(f"{data}{separator}{x}")
    return deck


def playit(who, hand, otherhand, risklevel, deck):
    play = True
    while play:
        cardsleft = 52 - (len(hand) + len(otherhand))

        if hit_me(who, hand, cardsleft, risklevel):
            # time.sleep(1)
            a, b, c, d = evalcard(deck[0])
            hand.append(deck[0])
            tot, bonus, special = total(hand)
            print(f"{who} takes a card: {d} of {c} ({tot})  {special}")
            deck.pop(0)
            # print(f"{who}: {showhand(hand)} {tot}")
            # time.sleep(1)
            if special == ("5 Card Trick"): play = False
            if special == "Bust":
                play = False
        else:
            print(f"{who} sticks\n")
            play = False

    totalp, totalbonusp, specialp = total(hand)
    blackjack = ""
    if specialp == "BlackJack": blackjack = " --- BlackJack!!!!"
    if specialp == "Bust": blackjack = " --- Bust :("
    if specialp == "5 Card Trick": blackjack = " --- 5 Card Trick!!!"
    print(f"Final {who} hand: {showhand(hand)} {totalp} scored {blackjack}\n\n")
    return hand


def winner(who):
    if who == "D":
        return ("Result: Dealer Wins!!")
    elif who == "P":
        return ("Result: Player Wins!!")
    else:
        return ("Result: Game is a Draw")


def showhand(hand):
    texthand = ""
    for x, y in enumerate(hand):
        thenum, bonus, thesuit, thecard = evalcard(y)
        texthand += f"{thecard} of {thesuit}, "
    return texthand


def evalcard(card):
    if "H" in card: thesuit = "Hearts"
    if "D" in card: thesuit = "Diamonds"
    if "C" in card: thesuit = "Clubs"
    if "S" in card: thesuit = "Spades"
    thenum = int(card.split("-", 1)[1])
    thecard = str(thenum)
    if thenum == 11: thecard = "Jack"
    if thenum == 12: thecard = "Queen"
    if thenum == 13: thecard = "King"
    if thenum == 1: thecard = "Ace"
    bonus = 0
    if thenum - 10 > 0: bonus = thenum - 10
    if thenum > 10: thenum = 10
    return thenum, bonus, thesuit, thecard


def total(thelist):
    total = 0
    totalbonus = 0
    special = ""
    ace = False
    for x, y in enumerate(thelist):
        mynum, mybonus, mysuit, mycard = evalcard(y)
        if mynum == 1: ace = True
        total += mynum
        totalbonus += mybonus
    if len(thelist) == 2:
        if total == 11 and ace:
            total = 21
            special = "BlackJack"
    elif len(thelist) >= 5:
        special = "5 Card Trick"
    if total > 21:
        special = "Bust"

    return total, totalbonus, special


def probability_greater_than_x(diff, cards_left, hand):
    total_cards = 52
    if diff > 9:
        prob_bust = 0
    else:
        my_cards_greater_than_diff = 0
        for x, y in enumerate(hand):
            thenum, bonus, thesuit, thecard = evalcard(hand[x])
            if thenum > diff:
                my_cards_greater_than_diff += 1
        # Number of cards greater than x in each suit (assuming face cards have values 11, 12, and 13)
        cards_greater_than_x = 4 * (13 - (diff + 1)) - my_cards_greater_than_diff
        prob_bust = cards_greater_than_x / cards_left

    return prob_bust


def simple_prob_player(diff, cardsleft, mydeck):
    test_deck = []
    x = 0
    while x < 14:
        y = 0
        while y < 4:
            test_deck.append(x)
    print(test_deck)


def hit_me(who, hand, cards_left, risk_level):
    my_total, my_bonus, special = total(hand)
    diff = 21 - my_total
    prob = probability_greater_than_x(diff, cards_left, hand)
    risk = prob / risk_level
    choice = False
    if risk < 0.5:
        choice = True
    if who == "Dealer" and my_total < 17:
        choice = True
    return choice


def onegame(playerrisk, dealerrisk):
    deck = create_deck(["H", "D", "C", "S"], 14, "-")
    random.shuffle(deck)
    deck, playerhand, dealerhand = first_deal(deck)

    playerhand = playit("Player", playerhand, dealerhand, playerrisk, deck)
    totalp, bonusp, specialp = total(playerhand)
    if totalp < 22:
        dealerhand = playit("Dealer", dealerhand, playerhand, dealerrisk, deck)
    totald, bonusd, speciald = total(dealerhand)

    ending = ""

    if totalp > 21 or totald > 21:
        if totalp > 21:
            ending = winner("D")
        else:
            ending = winner("P")
    else:
        if specialp == "BlackJack" or specialp == "5 Card Trick" or speciald == "BlackJack" or speciald == "5 Card Trick":
            if specialp == "BlackJack" and speciald == "BlackJack":
                if bonusd == bonusp:
                    ending = "DD"
                elif bonusd > bonusp:
                    ending = "D"
                else:
                    ending = "P"
            elif specialp == "BlackJack" and speciald == "5 Card Trick":
                ending = "P"
            elif specialp == "5 Card Trick" and speciald == "BlackJack":
                ending = "D"
            elif specialp == "5 Card Trick" and speciald == "5 Card Trick":
                ending = "DD"
            elif specialp == "BlackJack":
                ending = "P"
            elif speciald == "BlackJack":
                ending = "D"
            elif specialp == "5 Card Trick":
                ending = "P"
            elif speciald == "5 Card Trick":
                ending = "D"
        else:
            if totald == totalp:
                ending = "DD"
            elif totald > totalp:
                ending = "D"
            else:
                ending = "P"

    returncode = ending

    ending = winner(ending)

    print(ending, "\n")
    print("---------------------------------------------------------------\n\n\n")

    return returncode


#
# Main code
#

gamesresults = []
games = 0
while games < 1:
    games += 1
    playerrisk = round(random.uniform(1, 2), 1)
    dealerrisk = round(random.uniform(1, 2), 1)
    dealerrisk = 1.0
    playerrisk = 1.0
    thisone = 0
    playwins = 0
    dealwins = 0
    draws = 0
    while thisone < 10000:
        thisone += 1
        ending = onegame(playerrisk, dealerrisk)
        if ending == "P": playwins += 1
        if ending == "D": dealwins += 1
        if ending == "DD": draws += 1
    thisgameresult = [playerrisk, playwins, dealerrisk, dealwins, draws]
    gamesresults.append(thisgameresult)

print(gamesresults)
