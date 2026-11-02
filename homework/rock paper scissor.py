import random

print("===================================")
print("   ROCK PAPER SCISSORS WITH AI")
print("===================================")

# Possible choices
choices = ["rock", "paper", "scissors"]

# Score variables
player_score = 0
ai_score = 0
draws = 0

# Function to determine the winner
def find_winner(player, ai):

    if player == ai:
        return "draw"

    elif (player == "rock" and ai == "scissors") or \
         (player == "paper" and ai == "rock") or \
         (player == "scissors" and ai == "paper"):
        return "player"

    else:
        return "ai"


# AI strategy
def ai_move():
    return random.choice(choices)


# Main game
while True:

    print("\nChoose your move:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    player_choice = input("\nEnter your choice: ").lower()

    # Validate user input
    if player_choice not in choices:
        print("Invalid choice! Please enter rock, paper or scissors.")
        continue

    # AI selects its move
    computer_choice = ai_move()

    print("\nYou chose:", player_choice)
    print("AI chose:", computer_choice)

    # Determine winner
    result = find_winner(player_choice, computer_choice)

    if result == "player":
        print("\nCongratulations! You won!")
        player_score += 1

    elif result == "ai":
        print("\nAI wins! Better luck next time.")
        ai_score += 1

    else:
        print("\nIt's a draw!")
        draws += 1

    # Display scores
    print("\n========== SCOREBOARD ==========")
    print("Player Score:", player_score)
    print("AI Score:", ai_score)
    print("Draws:", draws)
    print("================================")

    # Ask whether to play again
    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        break

# Final result
print("\n========== FINAL RESULT ==========")

if player_score > ai_score:
    print("You are the overall winner!")

elif ai_score > player_score:
    print("AI is the overall winner!")

else:
    print("The game ended in a tie!")

print("\nThank you for playing!")
