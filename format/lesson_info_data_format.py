# 강의 정보 엑셀 최적화
import pandas as pd
import numpy as np


lesson_df = pd.read_excel('data/lesson_info.xlsx')
lesson_df.replace(np.NaN, '', inplace=True)
lesson_list = lesson_df.values.tolist()
lesson_list_col = list([col for col in pd.read_excel('data/lesson_info.xlsx')])                      # 강의 column


lesson_stack = []       # 중복되는 강의명 list
lesson_del_idx = []     # 중복되는 강의명이 포함된 lesson_list의 idx list

print(lesson_list)

# lesson_del_idx 체우는 작업
for i in range(len(lesson_list)):
    if lesson_list[i][1] in lesson_stack:
        lesson_del_idx.append(i)
        continue
    lesson_stack.append(lesson_list[i][1])

print(len(lesson_list))
print(lesson_del_idx)

# 인덱스 한칸씩 밀리니 거꾸로 돌려서 pop 시킴
for i in range(len(lesson_list) + 1, -1 , -1):
    if i in lesson_del_idx:
        lesson_list.pop(i)
print(lesson_list)
#iiiiii
# 수학과는 학년 나눔
for i in range(len(lesson_list)):
    grade_str = ""
    if '수학과' in lesson_list[i][2]:
        grade_str = lesson_list[i][2][3]
        lesson_list[i][2] = '학부'
    else:
        lesson_list[i][2] = '대학원'
    lesson_list[i][4] = grade_str
print(lesson_list)


# 엑셀 저장
# list.sort(lesson_list, key=lambda k: (k[1], k[6]))
# df = pd.DataFrame(lesson_list, columns=lesson_list_col)
# df.to_excel('data/lesson_info.xlsx', index=False)

