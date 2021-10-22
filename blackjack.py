import time
import random
import sys


# Author: Enoc Mena
# Date: 1/31/2021
# Description: This is a fully functioning BlackJack game that lets the user bet chips, hit, and stand
# Program Version: 1.0.0

###############################################################
#                                                             #
#                         BLACKJACK                           #
#                                                             #
###############################################################

# HANDLES PLAYERS CHIPS, BET, CARDS, etc
class Player:

    def __init__(self, MAX_BET, MIN_BET, START_CHIPS):
        self.MAX_BET = MAX_BET
        self.MIN_BET = MIN_BET
        self.START_CHIPS = START_CHIPS

    # CREATES PLAYER MENU
    def PLAYER_MENU(self):

        print("                     ")
        print(" Welcome to BlackJack")
        print("                     ")
        print("      1. Play        ")
        print("      2. Quit        ")

    # GETS PLAYERS BET AND SHOWS NEW START_CHIPS TOTAL
    def PLAYER_BETAMNT(self):

        print("Chips:", self.START_CHIPS)
        print("")

        global USER_BET  # Gets players bet
        global TOTAL_BET  # Gives player their total bet

        print("Enter (2) to QUIT")

        USER_BET = int(input("Enter your bet | minimum(50) - maximum(100): "))

        if USER_BET == 2:
            print("")

            time.sleep(3)

            sys.exit("Good Bye!!")

        # WHILE LOOP KEEPS ASKING USER TO INPUT A BET BETWEEN 50 - 100 CHIPS IF (USER_BET > 100 or USER_BET < 50)
        while USER_BET > 100 or USER_BET < 50:

            print("")
            print("Bet must be between minimum of 50 or a maximum of 100 chips")
            print("")

            USER_BET = int(input("Enter your bet | minimum(50) - maximum(100): "))

        else:

            self.START_CHIPS -= USER_BET
            TOTAL_BET = USER_BET + 0

            print("")
            print("**************************************************")
            print("Chips:", self.START_CHIPS)
            print("Total Bet:", TOTAL_BET)
            print("**************************************************")
            print("")

    # DEALS THE PLAYER CARDS USING THE RANDOM MODULE
    def PLAYER_CARDS(self):

        global CARDS
        global PLAYER_CARDS

        CARDS = []
        while (len(CARDS) < 2):

            PLAYER_CARDS = random.randint(1, 11)
            CARDS.append(PLAYER_CARDS)

            time.sleep(2)

            print("Cards:", CARDS)

            time.sleep(2)

            print("Hand total:", sum(CARDS))
            print("")

            if (sum(CARDS) == 21):
                print("")
                print("BLACKJACK!!")

                # EXAMPLE: PLAYER BET IS 100 CHIPS, RETURNS 100 + 150 (3:2 PAYOUT)
                self.START_CHIPS = self.START_CHIPS + int(TOTAL_BET * 1.5)

                break

            if (sum(CARDS) > 21):
                print("")
                print("BUST!!")
                print("")

                break

    # LETS PLAYER HIT FOR MORE CARDS
    def PLAYER_HIT(self):

        global HIT
        global NEW_CARD
        global TRUE
        global CARDS

        TRUE = True

        while TRUE:

            HIT = int(input("Enter 1 to (HIT) OR 2 to (STAND): "))

            if HIT == 1:

                NEW_CARD = random.randint(1, 11)
                CARDS.append(NEW_CARD)

                print("")

                time.sleep(2)

                print("Cards:", CARDS)

                time.sleep(2)

                print("Hand total:", sum(CARDS))
                print("")

                print("Dealer cards:", DEALER_CARDS_ARR)
                print("")

                if sum(CARDS) > 21:
                    print("BUST!")
                    PLAYER_BUST(self)
                    break

            if HIT == 2:
                DEALER_HAND_TOTAL(self)
                WIN_OR_LOSE(self)

                break

    # LETS PLAYER KNOW IF THEY WON
    global PLAYER_WON

    def PLAYER_WON(self):

        self.START_CHIPS = self.START_CHIPS + (TOTAL_BET * 2)

    # LETS PLAYER KNOW IF THEY BUST
    global PLAYER_BUST

    def PLAYER_BUST(self):

        self.START_CHIPS = self.START_CHIPS - TOTAL_BET


# DEALS THE DEALERS CARDS
class Dealer(Player):

    # DEALS THE FIRST CARD OF THE DEALER
    def DEALER_HAND(self):
        global DEALER_CARDS_ARR
        global DEALER_CARDS
        global DEALER_CARDS_TWO

        DEALER_CARDS_ARR = []

        while len(DEALER_CARDS_ARR) < 1:
            DEALER_CARDS = random.randint(1, 11)
            DEALER_CARDS_ARR.append(DEALER_CARDS)

            time.sleep(2)

        print("Dealer cards:", DEALER_CARDS_ARR)
        print("")

    # SHOWS THE DEALER HAND TOTAL
    global DEALER_HAND_TOTAL

    def DEALER_HAND_TOTAL(self):
        while sum(DEALER_CARDS_ARR) <= 17:
            DEALER_CARDS = random.randint(1, 11)
            DEALER_CARDS_ARR.append(DEALER_CARDS)

            time.sleep(2)

        print("Dealer cards:", DEALER_CARDS_ARR)
        print()


# DEALS WITH WHETHER THE DEALER OR PLAYER WINS
class Win_or_lose(Dealer):
    global WIN_OR_LOSE

    def WIN_OR_LOSE(self):
        if sum(DEALER_CARDS_ARR) == 21 or sum(DEALER_CARDS_ARR) <= 21 and sum(CARDS) > 21 or sum(CARDS) < sum(
                DEALER_CARDS_ARR) < 21:
            PLAYER_BUST(self)
            print("BUST!")

        elif sum(CARDS) > 21:
            PLAYER_BUST(self)
            print("BUST!")

        elif (sum(CARDS) <= 21):
            PLAYER_WON(self)
            print("")
            print("YOU WIN!!")

        elif 21 >= sum(CARDS) > sum(DEALER_CARDS_ARR):
            PLAYER_WON(self)
            print("")
            print("YOU WIN!!")


###########################################################################################
player = Player(100, 50, 1000)  # Player Creation (Max bet, Minimum bet, Starting chips)
dealer = Dealer(100, 50, 1000)
winLose = Win_or_lose(100, 50, 1000)
###########################################################################################

# GAME RUNS HERE
player.PLAYER_MENU()  # Game Menu (1st)

print("")

USER_OPT = int(input("Please enter an option (1 - 2): "))  # Gets players option

while True:

    if USER_OPT == 1:

        time.sleep(1)

        print("")
        print("Starting game....")

        time.sleep(1)

        print("")

        player.PLAYER_BETAMNT()  # Gets players bet (2nd)
        player.PLAYER_CARDS()  # Deals player their cards (3rd)
        dealer.DEALER_HAND()
        player.PLAYER_HIT()

    else:

        time.sleep(1)

        print("")
        print("Quitting game....")

        time.sleep(2)

        break
# GAME RUNS HERE
