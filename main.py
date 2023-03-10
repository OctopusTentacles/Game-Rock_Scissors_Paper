from getpass import getpass as input

print("E P I C     ⛰️  ✂️  📜      B A T T L E ")
print()
print("Select your move R-(rock), P-(papper), S-(scissors)")
print("You need three points to win")
print()

score1 = 0
score2 = 0
round = 1
while True:
    print("\033[032m" "R O U N D ", round, "\033[037m")
    round += 1
    print()
    player1 = input("Player 1, select and Enter ")
    player2 = input("Player 2, select and Enter ")
    print()
    if player1 == "R":
        if player2 == "R":
            print("You both picked ⛰️⛰️ , draw!")
            print()
            print()
        elif player2 == "P":
            print("Player 1's Rock is smothered by Player 2's Papper.")
            print()
            print("W o N    Player 2    📜")
            score2 += 1
            print()
            print(f"Player1     {score1} : {score2}    Player2")
            print()
            print()
        elif player2 == "S":
            print("Player 1 smashed Player 2's Scissors into dust.")
            print()
            print("W o N     Player 1    ⛰️")
            score1 += 1
            print()
            print(f"Player1     {score1} : {score2}    Player2")
            print()
            print()
        else:
            print("Invalid Move Player 2!")
            print()
            print()
    elif player1 == "P":
        if player2 == "R":
            print("Player 2's Rock is smothered by Player 1's Papper.")
            print()
            print("W o N    Player 1    📜")
            score1 += 1
            print()
            print(f"Player1     {score1} : {score2}    Player2")
            print()
            print()
        elif player2 == "P":
            print("Two bits of papper flap at each other .📜📜 Draw!!!")
            print()
            print()
        elif player2 == "S":
            print("Player1's Paper is cut into tiny pieces by Player2's Scissors!")
            print()
            print("W o N    Player 2    ✂️")
            score2 += 1
            print()
            print(f"Player1     {score1} : {score2}    Player2")
            print()
            print()
        else:
            print("Invalid Move! Player 2")
            print()
            print()
    elif player1 == "S":
        if player2 == "R":
            print("Player 2's Rock makes metal-dust out of Player1's Scissors!")
            print()
            print("W o N     Player 2    ⛰️")
            score2 += 1
            print()
            print(f"Player1     {score1} : {score2}    Player2")
            print()
            print()
        elif player2 == "P":
            print("Player1's Scissors make confetti out of Player2's paper!")
            print()
            print("W o N    Player 1    ✂️")
            score1 += 1
            print()
            print(f"Player1     {score1} : {score2}    Player2")
            print()
            print()
        elif player2 == "S":
            print("Ka-Shing! Scissors bounce off each other like a dodgy sword fight! ✂️✂️ Draw.")
            print()
            print()
        else:
            print("Invalid Move! Player 2")
            print()
            print()
    else:
        print("Invalid Move! Player 1")
        print()
    if score1 == 3 or score2 == 3:
        print("Thanks for playing!")
        exit()
    else:
        continue