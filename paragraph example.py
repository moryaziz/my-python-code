# total numbers of word
# total numbers of unique word
# total number of "to be"
# number of each to be


with open('paragraph example.txt') as samplefile:
    # total numbers of word
    txt = samplefile.read()
    txt.lower()
    count = 0
    print(txt)
    print('='*50)
    txt_list = [] # در متود strip مشکل داشتم. چون لیست رو تغییر نمیشد داد.
    print(type(txt_list))
    for word in txt.split():
        txt_list.append(word.strip(',.'))
    print(txt_list)
    print(txt_list.__len__())
    # total numbers of unique word
    unique = []
    for word in txt_list:
        if word not in unique:
            unique.append(word)
    print(unique)
    print(unique.__len__())
    # total numbers of unique word mthod 2
    txt_set = set(txt_list)
    print(txt_set)
    print(txt_set.__len__())
    print('='*80)
    print('='*50)
    print('='*50)
    print('='*50)

    # total number of "to be"
    count1 = 0
    to_be_list = ['am' , 'is' , 'are' , 'was' , 'were' , 'be']
    for word1 in txt_list:
        if word1 in to_be_list:
            count1 +=1
    print(count1)
    # number of each to be
    count_to_be =[]
    for word1 in to_be_list:
        print('number of {} : {}'.format(word1,txt_list.count(word1)))


