# rock paper scissors
import numpy, sys, random

print("""
         ********************************************************
         *                                                      *
         *      Hello! and welcome! to Rock Paper Scisors!      *
         *                                                      *
         ********************************************************\n""")

while True:
    # keep score
    score = {
        "computer": 0,
        "player": 0,
        "winner": False
    }
    # possible rolls
    rolls = ["rock", "paper", "scissors"]

    # main game loop
    while not score["winner"]:
        # randomise comp roll
        # get player input
        computer = random.randint(0, len(rolls) - 1)
        print("""        
                What is your choice? 
                1). Rock
                2). Paper
                3). Scissors""")
        player = input("                Player Choice: ").lower().strip()

        # check player input to ensure vaild
        if player == "exit":
            sys.exit()

        if player in rolls:
            if player == "rock":
                if rolls[computer] == "paper":
                    score["computer"] += 1
                elif rolls[computer] == player:
                    print("tie! roll again")
                else:
                    score["player"] += 1
            elif player == "paper":
                if rolls[computer] == "scissors":
                    score["computer"] += 1
                elif computer == player:
                    print("tie! roll again")
                else:
                    score["player"] += 1
            elif player == "scissors":
                if rolls[computer] == "rock":
                    score["computer"] += 1
                elif computer == player:
                    print("tie! roll again")
                else:
                    score["player"] += 1

            # display
            print(f"Player: {score['player']}   Computer: {score['computer']}")
            print(f"Player Rolled: {player}  Computer Rolled: {rolls[computer]}")

            # check if game is won
            if score["player"] == 3:
                print("the player has won!")
                sys.exit()
            elif score["computer"] == 3:
                print("the computer has won!")
                sys.exit()

        else:
            print("That is not a vaild response. Please try again...")











    sys.exit()
