import random


VALID_OPTIONS = ["rock", "paper", "scissors"]


def determine_winner(u, c):
    if u == "rock" and c == "rock":
        return "TIE GAME"
    elif u == "rock" and c == "paper":
        return "COMPUTER WINS"
    elif u == "rock" and c == "scissors":
        return "USER WINS"
    elif u == "paper" and c == "rock":
        return "USER WINS"
    elif u == "paper" and c == "paper":
        return "TIE GAME"
    elif u == "paper" and c == "scissors":
        return "COMPUTER WINS"
    elif u == "scissors" and c == "rock":
        return "COMPUTER WINS"
    elif u == "scissors" and c == "paper":
        return "USER WINS"
    elif u == "scissors" and c == "scissors":
        return "TIE GAME"


if __name__ == "__main__":
    user_choice = input("Please choose one of 'rock', 'paper', or 'scissors': ")
    print("USER:", user_choice)

    if user_choice not in VALID_OPTIONS:
        print("OOPS INVALID INPUT, PLEASE TRY AGAIN")
        quit()

    computer_choice = random.choice(VALID_OPTIONS)
    print("COMP:", computer_choice)

    result = determine_winner(user_choice, computer_choice)
    print(result)
