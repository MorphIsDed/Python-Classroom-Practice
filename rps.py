print("Welcome to stone paper scissors game")
import random
user_score = 0
computer_score = 0
while True:
    user_input = input("Type 's' for stone, 'p' for paper, 'c' for scissors or 'q' to quit: ").lower()
    if user_input == 'q':
        print("Thanks for playing!")
        break
    if user_input not in ['s', 'p', 'c']:
        print("Invalid input. Please try again.")
        continue

    computer_input = random.choice(['s', 'p', 'c'])
    print(f"Computer chose: {computer_input}")

    if user_input == computer_input:
        print("It's a tie!")
    elif (user_input == 's' and computer_input == 'c') or \
         (user_input == 'p' and computer_input == 's') or \
         (user_input == 'c' and computer_input == 'p'):
        print("You win this round!")
        user_score += 1
    else:
        print("Computer wins this round!")
        computer_score += 1

    print(f"Scores => You: {user_score}, Computer: {computer_score}")