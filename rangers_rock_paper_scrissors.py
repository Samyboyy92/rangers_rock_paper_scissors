import random

rps_list = ['rock', 'paper', 'scissors']
computer_choice = random.choice(rps_list)


while True:
    r = 'Rock'
    p = 'Paper'
    s = 'Scissors'    
    print("--Rock, Paper, Scissors--")
    prompt = input("Would you like to play a game of rock, paper, scissors?\n Yes('Y') No('N') or Quit('Q')")

    if prompt.lower() == 'n':
        print("\nWow, that scared to lose huh? Come back when you want to compete!")
        break
    #elif prompt.lower() != 'n' or prompt.lower() != 'y' or prompt.lower() != 'q':
        #print("invalid entry, please select from the choices given")
    elif prompt.lower() == 'q':
        print("Come back when you want to play again")
        #print(wins/losses)
        break
    elif prompt.lower() == 'y':
        print("\nLet's do it!")
        print("What's it gonna be?")
        choice = input("Rock('r') Paper('p') Scissors('s'): ")
        if choice.lower() == r or p or s:
            print(f"You Chose {choice}")



