import random



def player1():
    rps_list = ['Rock', 'Paper', 'Scissors']
    Player1_Wins = 0
    CPU_Wins = 0
    r = 'Rock'
    p = 'Paper'
    s = 'Scissors'
    computer_choice = random.choice(rps_list)


    print("--Rock, Paper, Scissors--")
    prompt = input("Would you like to play a game of rock, paper, scissors?\n Yes('Y') No('N')")
    if prompt.lower() == 'n':
        print("\nWow, that scared to lose huh? Come back when you want to compete!")
    elif prompt.lower() == 'y':
        while True:
            print("\nLet's do it!")
            print("What's it gonna be?")
            choice = input("Rock('r') Paper('p') Scissors('s'): ")
            if choice == 'r':
                computer_choice = random.choice(rps_list)
                print(f"You Chose {r}")
                print(f"I Chose {computer_choice}")
                if computer_choice == 'Rock':
                    print('\nIt\'s a draw!')
                elif computer_choice == 'Paper':
                    print('\nPaper beats rock, I win!!')
                    CPU_Wins += 1
                    print('Player 1 Score: ', Player1_Wins, 'CPU Score: ', CPU_Wins)
                elif computer_choice == 'Scissors':
                    print('\nWow, defeated...')
                    Player1_Wins += 1
                    print('Player 1 Score: ', Player1_Wins, 'CPU Score: ', CPU_Wins)
            if choice == 'p':
                computer_choice = random.choice(rps_list)
                print(f"You Chose {p}")
                print(f"I Chose {computer_choice}")
                if computer_choice == 'Rock':
                    print('\nWow, defeated...')
                    Player1_Wins += 1
                    print('Player 1 Score: ', Player1_Wins, 'CPU Score: ', CPU_Wins)
                elif computer_choice == 'Paper':
                    print('\nIt\'s a draw!')
                elif computer_choice == 'Scissors':
                    print('\nScissors beats paper, I win!!')
                    CPU_Wins += 1
                    print('Player 1 Score: ', Player1_Wins, 'CPU Score: ', CPU_Wins)
            if choice == 's':
                computer_choice = random.choice(rps_list)
                print(f"You Chose {s}")
                print(f"I Chose {computer_choice}")
                if computer_choice == 'Rock':
                    print('\nRock beats scissors, I win!!')
                    CPU_Wins += 1
                    print('Player 1 Score: ', Player1_Wins, 'CPU Score: ', CPU_Wins)
                elif computer_choice == 'Paper':
                    print('\nWow, defeated...')
                    Player1_Wins += 1
                    print('Player 1 Score: ', Player1_Wins, 'CPU Score: ', CPU_Wins)
                elif computer_choice == 'Scissors':
                    print('\nIt\'s a draw!')
            repeat = input('\nWant to play again? Yes("y") No("n"): ')
            if repeat.lower() != 'y':
                print('\nThank you for playing!')
                print('Here are the finishing scores:')
                print('Player 1: ', Player1_Wins, 'CPU: ', CPU_Wins)
                break
    else:
        print('\nInvalid entry, restart and select from the options given.')

player1()
