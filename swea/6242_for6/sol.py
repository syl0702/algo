blood_list = ['A','A','A','O','B','B','O','AB','AB','O']

blood_dict ={
    'A': 0,
    'B': 0,
    'AB': 0,
    'O': 0
}


for blood in blood_list:
    blood_dict[blood] += 1

print(blood_dict)
#     if bnum == 'A':
#         bnum.count('A')
        
#         pass
#     elif bnum == 'O':
#         bnum.count('O')
#         pass
#     elif bnum == 'B':
#         bnum.count('B')
#         pass
#     else:
#         bnum.count('AB')
#         pass
# else:
#     pass

# print(result[bnum.count('A'), bnum.count('O'), bnum.count('B'), bnum.count('AB')])

location_list = ['서울', '부산', '서울', '서울', '대전', '제주', '광주', '부산', 'LA']

location_dict = {}

for location in location_list:
    # 이미 기록을 한 경우
    if location in location_dict.keys():
        location_dict[location] += 1
    # 처음 등장한 경우
    else:
        location_dict[location] = 1
        

print(location_dict)