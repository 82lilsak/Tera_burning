# 테라버닝 레벨
# 200, 197, 194,....

# my_lev = int(input())

mung = 0
maxl = 0

tera = 0
tera2 = 0
list_idiot = []
list_end200 = []
# need1lev = my_lev + 1

for i in range(1, 201, 3):
    tera = 200-i    # 반복 중에 199~ 3씩 뺀 값
    list_idiot.append(tera)

    to_tera = tera % 3  # 그 값에서 3으로 나눈 나머지


#     if to_tera == 1 and tera == my_lev: # 나머지 가 1 이고 내 래밸과 같은 경우
#         if my_lev == 199:
#             mung = 1
#             print('199 레벨이라 멍청이 퀘스트만 클리어 하면 200레벨 입니다.')
#         else:
#             mung = 1
#             print('해당 레벨에 테라버닝 사용시 199 레벨에 종료됩니다.')
# #
#     if mung != 1 and tera == need1lev:
#         print('1업만 더하면 199레벨에 테라버닝이 끝납니다. 이후에 멍청이 퀘스트를 클리어하십시오.')


for ii in range(0, 200, 3):
    tera2 = 200 - ii  # 반복 중에 200~ 3씩 뺀 값
    list_end200.append(tera2)

#     if tera2 == my_lev:  # 나머지 가 1 이고 내 래밸과 같은 경우
#         if my_lev == 200:
#             maxl = 1
#             print('이미 200레벨 이어서 테라버닝 사용이 불가능 합니다.')
#         else:
#             maxl = 1
#             print('해당 레벨에 테라버닝 사용시 200 레벨에 마무리 됩니다.')
#     if maxl != 1 and tera2 == need1lev:
#         print('1업만 더하면 200마무리')
#
# if my_lev == 198:
#     print('198레벨이라 테라버닝 사용을 추천드리지 않고 199까지 레벨업 하고 멍청이 퀘스트 클리어시 200이 됩니다.')


