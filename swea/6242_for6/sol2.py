blood_list = ['A','A','A','O','B','B','O','AB','AB','O']
bnum_list = []
for bnum in blood_list:
    if bnum == 'A':
        bnum.count('A')
        bnum_list.append(bnum.count('A'))
    
    elif bnum == 'O':
        bnum.count('O')
        bnum_list.append(bnum.count('O'))

    elif bnum == 'B':
        bnum.count('B')
        bnum_list.append(bnum.count('B'))

    else:
        bnum.count('AB')
        bnum.count('AB')
        bnum_list.append(bnum.count('AB'))

print (bnum_list)