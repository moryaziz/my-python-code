import random
# Description:
#
#         Write a Python program that simulates the "Rock, Paper, Scissors" game.
#
#         The game should ask the user to enter an option (either "Rock", "Paper", or "Scissors").
#
#         The player should play against the computer, which will select a random option.
#
#         The computer's selection will be compared against the player's selection to determine who wins.
#
#         A descriptive message should be displayed indicating if the player won, lost, or if the game ended in a tie.



# ====== Welcome to the game ======
# Please enter Rock, Paper, or Scissors below:
def game():
    while True:
        player = input('Please enter Rock, Paper, or Scissors below:').lower()
        pc = random.randint(0,2)
        pc_dict = ['Rock','Paper','Scissors']
        pc_choose = pc_dict[pc]
        print('pc_choose:',pc_choose)
        print('player:',player)
        result = ''
        if player == 'rock':
            if pc_choose == 'Paper':
                result = 'lose'
            elif pc_choose == 'Scissors':
                result = 'win'
            else :
                result = 'tie'
            # print(result)

        elif player == 'paper':
            if pc_choose == 'Paper':
                result = 'tie'
            elif pc_choose == 'Scissors':
                result = 'lose'
            else :
                result = 'win'
            # print(result)

        elif player == 'scissors':
            if pc_choose == 'Paper':
                result = 'win'
            elif pc_choose == 'Scissors':
                result = 'tie'
            else :
                result = 'lose'
            # print(result)
        else:
            print('you quit')
            break
        # print(result)
        if result == 'lose':
            print ('You lose! Your opponent chose {}'.format(pc_choose))
        elif result == 'win':
            print ('You win! Your opponent chose {}'.format(pc_choose))
        elif result == 'tie':
            print ('It\'s a tie! Try again.')

game()







