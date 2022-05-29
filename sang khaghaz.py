import random
from random import randint

print('welcome to my game')
print('='* 40)
numof = input('please type in a value for winning score')
while numof.isnumeric() == False :
    print('i need an integer to carry on, please type an integer value')
    numof = input('please type in a value for winning score')
num_of_play= int(numof)
list_of_user = ['rock' , 'paper' , 'scissors','q','quit','r','s', 'p',]
list1=['r' , 'p' , 's']
resultsUser = 0
resultsPC = 0
user_short = ''
print('num_of_play:', num_of_play)
print('num_of_play:', type(num_of_play))

### nafahmidam moshkel shart while chie?
while True : #(resultsPC < num_of_play) or (resultsUser < num_of_play) :
        ChooseOfUser = input("please choose between Rock(R) or Paper(P) or Scissors(S)").lower()
        choose_of_user_input = ''
        for obj in list_of_user:
            if obj in ChooseOfUser:
                choose_of_user_input = obj
                break
        while True:
            if not choose_of_user_input in list_of_user :
                print('input is not valid.')
                ChooseOfUser = input('again choose between Rock(R) or Paper(P) or Scissors(S)')
                #choose_of_user_input = ''
                #user_short = ''
                for obj in list_of_user:
                  if obj in ChooseOfUser:
                    choose_of_user_input = obj
                    break
            else:
                break
        print('your choice is:', choose_of_user_input)

        paper = ['p' , 'paper']
        scissors = ['s' , 'scissors']
        rock = ['r' , 'rock']
        quit = ['q','quit']

        if choose_of_user_input == paper:
             user_short = 'p'
        elif choose_of_user_input == rock:
             user_short = 'r'
        elif choose_of_user_input == scissors:
            user_short = 's'
        elif choose_of_user_input == quit:
            user_short = 'q'
#
        # nafahmidam chera inha kar nakard va majboor shodam dar nahayat 'p' va 'paper' ra dakhel list bezaram.

#       if choose_of_user_input == 'p' or 'paper':
#            user_short = 'q'
#       elif choose_of_user_input == 'r' or 'rock':
#            user_short = 'r'
#      elif choose_of_user_input == 's' or 'Scissors':
#            user_short = 's'
#        elif choose_of_user_input == 'q' or 'quit':
#            user_short = 'p'
#        else:
#            continue

        ChooseOfPc = random.choice(list1)
        print('user had:{}, pc had :{}'.format(user_short,ChooseOfPc))



        if user_short == 'q':
            print('khaste nabashid, results : user={} and pc={}'.format(resultsUser, resultsPC))
            break
        elif ChooseOfPc == user_short:
            resultsUser += 0
            resultsPC += 0
            print('tie, results : user={} and pc={}'.format(resultsUser, resultsPC))
        elif ChooseOfPc == 'r' and user_short == 's':
            resultsPC += 1
            print('you lost, results : user={} and pc={}'.format(resultsUser, resultsPC))
        elif ChooseOfPc == 'r' and user_short == 'p':
            resultsUser += 1
            print('you won, results : user={} and pc={}'.format(resultsUser, resultsPC))
        elif ChooseOfPc == 'p' and user_short == 's':
            resultsUser += 1
            print('you won, results : user={} and pc={}'.format(resultsUser, resultsPC))
        elif ChooseOfPc == 'p' and user_short == 'r':
            resultsPC += 1
            print('you lost, results : user={} and pc={}'.format(resultsUser, resultsPC))
        elif ChooseOfPc == 's' and user_short == 'p':
            resultsPC += 1
            print('you lost, results : user={} and pc={}'.format(resultsUser, resultsPC))
        elif ChooseOfPc == 's' and user_short == 'r':
            resultsUser += 1
            print('you won, results : user={} and pc={}'.format(resultsUser, resultsPC))

        else :
            continue

        if resultsUser == num_of_play or resultsPC == num_of_play :
            break

print('final result: user={} and pc={}'.format(resultsUser,resultsPC))
message = 'user win the match' if resultsUser > resultsPC else 'pc win the match'
print(message)




