# total numbers of word
# total numbers of unique word
# total number of "to be"
# number of each to be
list1=[]
with open('paragraph example.txt') as samplefile:
    line = samplefile.readline()
    line.lower()
    count = 0
    while line:
        print(line)
        line_list = line.split()
        for char in line_list:
            list1.append(char)
            print(char)
            count += 1
        line = samplefile.readline()
    print(list1)

print(count)
print('='*50)
print('='*50)
print('='*50)
print('='*50)

with open('paragraph example.txt') as samplefile:
    txt = samplefile.read()
    txt.lower()
    count = 0
    print(line)
    txt_str = txt.split()
    for word in txt_str:
        word.strip(', .')
        txt_str.append(word)
    print(txt_str)
 #       for char in line_list:
 #           print(char)
 #           count += 1
 #       line = samplefile.readline()

print(count)
print('='*50)
print('='*50)
print('='*50)
print('='*50)
set1= set()

with open('paragraph example.txt') as samplefile:

    line = samplefile.readline()
    line.lower()
    count = 0
    while line:
        print(line)
        line_list = line.split()
        line_set= set(line_list)
        for char in line_set:
            set1.add(char)
            print(char)
            count += 1
        line = samplefile.readline()

print(count)
print(set1)
