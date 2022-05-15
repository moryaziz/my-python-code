import random
from random import randint
list1=['R' , 'P' , 'S']
resultsUser = 0
resultsPC = 0
while True :
    if resultsUser == 5 or resultsPC == 5:
        print('final result: user={} and pc={}'.format(resultsUser,resultsPC))
        message = 'user win the match' if resultsUser > resultsPC else 'pc win the match'
        print(message)
        break
    ChooseOfUser = input("choose between R or P or S")
    ChooseOfPc = random.choice(list1)
    if ChooseOfPc == ChooseOfUser :
        resultsUser += 0
        resultsPC += 0
        print('tie, results : user={} and pc={}'.format(resultsUser,resultsPC))
    elif ChooseOfPc == 'R' and ChooseOfUser == 'S' :
        resultsPC += 1
        print('you lost, results : user={} and pc={}'.format(resultsUser,resultsPC))
    elif ChooseOfPc == 'R' and ChooseOfUser == 'P' :
        resultsUser += 1
        print('you won, results : user={} and pc={}'.format(resultsUser,resultsPC))
    elif ChooseOfPc == 'P' and ChooseOfUser == 'S' :
        resultsUser += 1
        print('you won, results : user={} and pc={}'.format(resultsUser,resultsPC))
    elif ChooseOfPc == 'P' and ChooseOfUser == 'R' :
        resultsPC += 1
        print('you lost, results : user={} and pc={}'.format(resultsUser,resultsPC))
    elif ChooseOfPc == 'S' and ChooseOfUser == 'P' :
        resultsPC += 1
        print('you lost, results : user={} and pc={}'.format(resultsUser,resultsPC))
    elif ChooseOfPc == 'S' and ChooseOfUser == 'R' :
        resultsUser += 1
        print('you won, results : user={} and pc={}'.format(resultsUser,resultsPC))
    elif ChooseOfUser == 'q' :
        print('khaste nabashid, results : user={} and pc={}'.format(resultsUser,resultsPC))
        break
    elif ChooseOfUser != 'R' or 'S' or 'P' :
        print('input again')
        continue



