import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return 'tie'
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        return 'user'
    else:
        return 'computer'

def main():
    print("Welcome to Rock-Paper-Scissors Game!")
    user_score = 0
    computer_score = 0

    while True:
        print("\nChoose: rock, paper, or scissors (or type 'exit' to quit)")
        user_choice = input("Your choice: ").lower()

        if user_choice == 'exit':
            print("Thanks for playing!")
            print(f"Final Scores -> You: {user_score} | Computer: {computer_score}")
            break

        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid input. Please choose rock, paper, or scissors.")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        winner = determine_winner(user_choice, computer_choice)

        if winner == 'tie':
            print("It's a tie!")
        elif winner == 'user':
            print("You win!")
            user_score += 1
        else:
            print("You lose!")
            computer_score += 1

        print(f"Score -> You: {user_score} | Computer: {computer_score}")

if __name__ == "__main__":
    main()
