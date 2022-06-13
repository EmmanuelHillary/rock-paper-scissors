import random

while True:
    user_action = input("Enter a choice (R, P, S): ")
    possible_actions = ["R", "P", "S"]
    actions = {"R": "Rock", "P": "Paper", "S": "Scissors"}
    computer_action = random.choice(possible_actions)
    print(f"\nYou chose {actions[user_action]}, computer chose {actions[computer_action]}.\n")

    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "R":
        if computer_action == "S":
            print("R smashes S! You win!")
        else:
            print("P covers R! You lose.")
    elif user_action == "P":
        if computer_action == "R":
            print("P covers R! You win!")
        else:
            print("S cuts P! You lose.")
    elif user_action == "S":
        if computer_action == "P":
            print("S cuts P! You win!")
        else:
            print("R smashes S! You lose.")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break