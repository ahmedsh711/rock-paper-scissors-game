# Step 0: Data base:
game_choices = {1: 'Rock', 2: 'Paper', 3: 'Scissors'}
from random import randint

def play_game():
    C_winning = 0
    U_winning = 0

    print('''Winning Rules of the Rock paper scissor game as follows:
    - Rock vs paper -> paper wins
    - Rock vs scissor -> Rock wins
    - paper vs scissor -> scissor wins.
    ''')

    for round in range(3):
        # Step 2: User Input:
        print(f'Round {round + 1}')
        print('''Enter choice
        1 for Rock,
        2 for paper, and
        3 for scissor\n ''')

        try:
            user_input = int(input('User turn: '))
        except ValueError:
            print('Please enter numbers only!')
            continue

        if user_input not in [1, 2, 3]:
            print('Please enter 1, 2, or 3 only!')
            continue

        print(f'User choice is: {game_choices[user_input]}')

        # Step 3: Computer turn:
        comp_choice = randint(1, 3)
        print('Now it\'s computer\'s turn....')
        print(f'Computer choice is: {game_choices[comp_choice]}')

        # Step 4: Who wins
        print(f'{game_choices[user_input]} V/s {game_choices[comp_choice]}')

        if comp_choice == user_input:
            print("It's a Tie!!")
        elif (user_input == 1 and comp_choice == 3) or \
             (user_input == 2 and comp_choice == 1) or \
             (user_input == 3 and comp_choice == 2):
            print(f'{game_choices[user_input]} wins => <== User Wins ==>')
            U_winning += 1
        else:
            print(f'{game_choices[comp_choice]} wins => <== Computer Wins ==>')
            C_winning += 1

        print(f'Score: User {U_winning} - Computer {C_winning}\n')

    if C_winning > U_winning:
        print('Computer wins the game :(')
    elif U_winning > C_winning:
        print('Hooray! You win the game :)')
    else:
        print("It's a Tie!")

# Step 5: Game Continue:
while True:
    play_game()
    if input('Do you want to play again? (Y/N): ').lower() != 'y':
        print('Thanks for playing! See you again <3')
        break
