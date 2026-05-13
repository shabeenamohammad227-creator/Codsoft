import random

# Function to determine the winner
def determine_winner(user, computer):
    if user == computer:
        return "It's a Tie!"
    elif (
        (user == "rock" and computer == "scissors") or
        (user == "paper" and computer == "rock") or
        (user == "scissors" and computer == "paper")
    ):
        return "You Win!"
    else:
        return "Computer Wins!"

# Initialize scores
user_score = 0
computer_score = 0

print("===== Rock Paper Scissors Game =====")

while True:
    # User input
    user_choice = input("\nEnter rock, paper, or scissors: ").lower()

    # Validate input
    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid input! Please enter rock, paper, or scissors.")
        continue

    # Computer choice
    computer_choice = random.choice(["rock", "paper", "scissors"])

    # Display choices
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    # Determine winner
    result = determine_winner(user_choice, computer_choice)
    print(result)

    # Update scores
    if result == "You Win!":
        user_score += 1
    elif result == "Computer Wins!":
        computer_score += 1

    # Display scores
    print("\nScore Board")
    print(f"You: {user_score}")
    print(f"Computer: {computer_score}")

    # Play again option
    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("\nThanks for playing Rock Paper Scissors!")
        break
