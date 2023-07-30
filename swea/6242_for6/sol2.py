blood_list = ['A','A','A','O','B','B','O','AB','AB','O']
bnum_dict = {}
for blood in ['A', 'B', 'O', 'AB']:
    bnum_dict[blood] = blood_list.count(blood)

print (bnum_dict)