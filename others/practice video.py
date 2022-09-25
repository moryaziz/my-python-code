import shelve

names =['ali','hasan']
age = [18 , 20]

with shelve.open('shelve_practice', writeback=True) as s_file:
    s_file['names'] = names
    s_file['age'] = age

    print(s_file['names'])
    print('--------------')
    print(names)
    print('--------------')

    names.remove('hasan')
    for item in s_file:
          print(item, '\t', s_file[item])