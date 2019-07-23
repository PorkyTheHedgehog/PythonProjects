import random, webbrowser, re, heapq
treasury = 0
bjscored = {
    "2" : 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "K": 10, "Q": 10, "J":10, "A*": 1
}
scores = []



def intro():
    print("---------")
    print("Blackjack")
    print("  ♠♥♣♦   ")

    print("---------")
    print("Play")
    print("Help")
    print("Highscore")
    print("---------")
    while True:
        option = input("What would you like to do? ")
        if option.lower() == "play" or option.lower() == "help" or option.lower() == "highscore":
            break
        else: print("Sorry that option is invalid.")
    return option


def bet(treasury):
    print("---------")
    print("Hi, your current balance is ${}.".format(treasury))
    while True:
        try:
            betamt = int(input("Please enter your bet amount : $"))
            if betamt > treasury:
                print("Sorry, the bet amount is more than your current balance. Please enter your bet amount again.")
            else:
                cfm = input("Please confirm that your bet amount is ${}. (Y/N): ".format(betamt))
                if cfm.upper() == "Y":
                    treasury -= betamt
                    print("You are now left with ${}".format(treasury))
                    print("---------")
                    money = [treasury, betamt]
                    return money
                else:
                    print("Confirmation failed.")
        except ValueError:
            print("Sorry. Your bet is invalid. Please try again.")


def ShuffleCards():
    Set = "A23456789JQK"
    Deck = [str(card) for card in Set * 4]
    random.shuffle(Deck)
    return Deck


def Hit():
    #print(Deck)
    card = Deck[0]
    Deck.remove(Deck[0])
    return [Deck, card]


def RoundOne():
    b = []
    p = []
    for x in range(2):
        p.append(Hit()[1])
    for x in range(2):
        b.append(Hit()[1])
    return[p,b]

def score(Hand):
    points = 0
    for card in Hand:
        try:
            points += bjscored[card]
        except KeyError:
            points += 0
    if points + 11 <= 21 and "A" in Hand:
        points += 11
    elif points + 11 > 21 and "A" in Hand:
        points += 1
    return points

def game():
    bHandShown = ["X"]
    bHandShown.extend(bHand[1:])
    mbjscore = score(mHand)
    bbjscore = score(bHand)
    if bbjscore >= 21 or len(bHand) > 4:
        print("---------")
        return [mHand, bHand, mbjscore, bbjscore]
    elif mbjscore >= 21 or len(mHand) > 4:
        print("---------")
        return [mHand, bHand, mbjscore, bbjscore]
    print("Current balance: ${}".format(money[0]))
    print("Bet Amount: ${}".format(money[1]))
    print("")
    print("Your hand: {}".format(mHand))
    print("Your points: {}".format(mbjscore))
    print("Banker hand: {}".format(bHandShown))
    #
    #
    while True:
        choice = input("Hit/ Stand: ")
        if choice.lower() == "hit":
            card = Hit()
            if card[1] == "A" and "A" in mHand:
                card[1] = "A*"
            mHand.append(card[1])
            if bbjscore < 17:
                card = Hit()
                if card[1] == "A" and "A" in bHand:
                    card[1] = "A*"
                bHand.append(card[1])
                bbjscore = score(bHand)
            return game()
        elif choice.lower() == "stand":
            while bbjscore < 17:
                card = Hit()
                if card[1] == "A" and "A" in bHand:
                    card[1] = "A*"
                bHand.append(card[1])
                bbjscore = score(bHand)
            print("---------")
            return [mHand, bHand, mbjscore, bbjscore]
        else: print("Sorry, your choice is invalid. Please indicate your choice again.")


def results():
    print("Your hand: {}".format(stats[0]))
    print("Your points: {}".format(stats[2]))
    print("Banker hand: {}".format(stats[1]))
    print("Banker points: {}".format(stats[3]))
    if stats[2] > 21:
        oc = False
    elif stats[3] > 21 and stats[2] < 21:
        oc = True
    elif stats[2] < stats[3]:
        oc = False
    elif stats[2] > stats[3]:
        oc = True
    elif stats[2] == stats[3]:
        oc = "Draw"
    if oc == False:
        print("You Lose. :<")
        print("You lost ${}".format(money[1]))
        balance = money[0]
        print("Your current balance: ${}".format(balance))
    elif oc == True:
        print("You Win. :>")
        print("You won ${}".format(money[1]))
        balance = money[0] + money[1] * 2
        print("Your current balance: ${}".format(balance))
    elif oc == "Draw":
        print("Its a Draw. :l")
        print("You won ${}".format(money[1]))
        balance = money[0] + money[1]
        print("Your current balance: ${}".format(balance))
    while True:
        reply = input("Play Again? (Y/N): ")
        if reply.upper() == "Y" or reply.upper() == "N":
            break
        else: print("Reply is invalid.")
    return [reply, balance]

def enterHighscore():
    fo = open("C:/Users/Chang Fong/PycharmProjects/untitled/BlackJack/Highscore.txt", "a+")
    fo.write("\n")
    fo.write("{} : {}".format(name, max(scores)))
    fo.close()

def getHighscore():
    try:
        fo = open("C:/Users/Chang Fong/PycharmProjects/untitled/BlackJack/Highscore.txt", "r")
        lines = fo.readlines()
        a = re.findall(r"\d+", str(lines))
        raw = heapq.nlargest(10, a)
        cooked = []
        for x in raw:
            if int(x) not in cooked:
                cooked.append(int(x))
        cooked.sort(reverse=True)
        for x in cooked:
            for line in lines[1:]:
                b = re.findall(r"\d+", str(line))
                if int(x) == int(b[0]):
                    print(line.rstrip())
    except FileNotFoundError:
        print("Sorry. No highscore exists of yet.")


option = intro()
while True:
    if option.lower() == "play":
        if treasury == 0:
            treasury = 2500
        money = bet(treasury)
        Deck = ShuffleCards()
        Hands = RoundOne()
        mHand = Hands[0]
        bHand = Hands[1]
        stats = game()
        outcome = results()
        treasury = outcome[1]
        scores.append(treasury)
        if outcome[0].lower() == "n":
            print("---------")
            print("Aww. Oh well...")
            print("Highscore: ${}".format(max(scores)))
            name = input("What is your name? ")
            enterHighscore()
            break
        elif outcome[0].lower() == "y" and treasury <= 0:
            print("---------")
            print("Sorry, you have not enough credits.")
            print("Highscore: ${}".format(max(scores)))
            name = input("What is your name? ")
            break
    elif option.lower() == "help":
        webbrowser.open('https://www.instructables.com/id/How-to-Play-Blackjack-with-Betting/')
        print("Help")
        print("---------")
        action = input("Back? (Y/N): ")
        if action.lower() == "y":
            option = intro()
        elif action.lower() == "n":
            break
        else:
            print("Sorry that option is invalid.")
    elif option.lower() == "highscore":
        print("---------")
        getHighscore()
        print("---------")
        action = input("Back? (Y/N): ")
        if action.lower() == "y":
            option = intro()
        elif action.lower() == "n":
            break
        else: print("Sorry that option is invalid.")