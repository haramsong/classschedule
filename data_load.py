# DB Load
import pandas as pd

from imports import *
global today_QDate, first_semester_QDate, second_semester_QDate, year_str, semester_str

# 날짜에 관한 변수 지정
today_QDate = QDate.currentDate()   # 오늘
year_str = today_QDate.year()       # 이번 년도
semester_str = 0                    # 학기 초기 값
first_semester_QDate = QDate(year_str,2,7)      # 1학기 시작일(성적 이관 기준 : 2월 7일)
second_semester_QDate = QDate(year_str,7,7)     # 2학기 시작일(성적 이관 기준: 7월 7일)

# 1학기 혹은 2학기 둘중 하나기 때문에 당일 일자가 1학기 성적 이관과 2학기 성적 이관 사이에 있으면 1학기, 아닌 경우는 2학기
if today_QDate > first_semester_QDate and today_QDate <= second_semester_QDate:
    semester_str = 1
else:
    semester_str = 2
# 다음 해로 넘어 갈 때, 1학기 시작일 이전인 경우 아직 까지는 이번 년도 시간표이기 때문에 year를 하나 빼줌
if today_QDate <= first_semester_QDate:
    year_str -= 1

global classroom_df, lesson_assign_df,lesson_assign_under_df,lesson_assign_df_dae, lesson_df, professor_df, time_df, global_df, under_dataset_df, grad_dataset_df
global classroom_list, lesson_assign_list,lesson_assign_under_list,lesson_assign_list_dae, lesson_list, professor_list, time_list, global_list, under_dataset_list, grad_dataset_list
global classroom_list_col, lesson_assign_list_col,lesson_assign_under_list_col,lesson_assign_list_col_dae, lesson_list_col, professor_list_col, time_list_col, global_list_col

# 로컬 마스터데이터 로드 (위치 : data 폴더 안 excel 파일)
classroom_df = pd.read_excel('data/classroom_info.xlsx')
lesson_assign_df = pd.read_excel('data/lesson_assign.xlsx')
lesson_assign_under_df = pd.read_excel('data/lesson_assign_under.xlsx')
lesson_assign_df_dae = pd.read_excel('data/lesson_assign_dae.xlsx')
lesson_df = pd.read_excel('data/lesson_info.xlsx')
professor_df = pd.read_excel('data/professor_info.xlsx')
time_df = pd.read_excel('data/time_period.xlsx')
global_df = pd.read_excel('data/global_master.xlsx')

global lesson_assign_under_df_origin, lesson_assign_df_dae_origin
lesson_assign_under_df_origin = pd.read_excel('data/lesson_assign_under.xlsx')
lesson_assign_df_dae_origin = pd.read_excel('data/lesson_assign_dae.xlsx')

# nan값 제거
classroom_df.replace(np.NaN, '', inplace=True)
lesson_assign_df.replace(np.NaN, '', inplace=True)
lesson_assign_under_df.replace(np.NaN, '', inplace=True)
lesson_assign_df_dae.replace(np.NaN, '', inplace=True)
lesson_df.replace(np.NaN, '', inplace=True)
professor_df.replace(np.NaN, '', inplace=True)
time_df.replace(np.NaN, '', inplace=True)

lesson_assign_under_df_origin.replace(np.NaN, '', inplace=True)
lesson_assign_df_dae_origin.replace(np.NaN, '', inplace=True)

# decimal 제거
lesson_df['학기'] = lesson_df['학기'].astype(str).apply(lambda x: x.replace('.0',''))
lesson_df['과정(학년)'] = lesson_df['과정(학년)'].astype(str).apply(lambda x: x.replace('.0',''))
lesson_df['학점'] = lesson_df['학점'].astype(str).apply(lambda x: x.replace('.0',''))
# print(lesson_df)

classroom_list = classroom_df.values.tolist()
lesson_assign_list = lesson_assign_df.values.tolist()
lesson_assign_under_list = lesson_assign_under_df.values.tolist()
lesson_assign_list_dae = lesson_assign_df_dae.values.tolist()
lesson_list = lesson_df.values.tolist()
professor_list = professor_df.values.tolist()
time_list = time_df.values.tolist()
global_list = global_df.values.tolist()

global lesson_assign_under_list_origin, lesson_assign_list_dae_origin
lesson_assign_under_list_origin = lesson_assign_under_df_origin.values.tolist()
lesson_assign_list_dae_origin = lesson_assign_df_dae_origin.values.tolist()

# 데이터 저장할 때 필요한 column(to_excel)
classroom_list_col = list([col for col in pd.read_excel('data/classroom_info.xlsx')])                # 강의실 column
lesson_assign_list_col = list([col for col in pd.read_excel('data/lesson_assign.xlsx')])             # 강의 배정 column
lesson_assign_under_list_col = list([col for col in pd.read_excel('data/lesson_assign_under.xlsx')])             # 강의 배정 column
lesson_assign_list_col_dae = list([col for col in pd.read_excel('data/lesson_assign_dae.xlsx')])
lesson_list_col = list([col for col in pd.read_excel('data/lesson_info.xlsx')])                      # 강의 column
professor_list_col = list([col for col in pd.read_excel('data/professor_info.xlsx')])                # 교수 column
time_list_col = list([col for col in pd.read_excel('data/time_period.xlsx')])                        # 시간표 column
global_list_col = list([col for col in pd.read_excel('data/global_master.xlsx')])                    # 시간표 column


# 데이터셋 로드 (위치 : data 폴더 안 class_dataset excel 파일)
path = 'data/class_dataset/'
file_list = os.listdir(path)

dataset_df = pd.DataFrame()
new_columns = ['성명', '직급', '대상학과', '교과구분', '교과목번호', '교과목명', '분반', '강의시간', '강의실', '비고']

for file in file_list:                          # class_dataset 파일 내의 데이터를 하나씩 로드
    data = pd.read_excel(path + file)           # 경로 'data/class_dataset/' + 파일명
    data.columns = new_columns                  # 컬럼명 통일
    dataset_df = pd.concat([dataset_df, data])  # 모두 concat하여 하나의 데이터프레임으로 만들기
dataset_df = dataset_df.reset_index(drop=True)  # index 재설정

# 학부 데이터셋 추출
under_dataset_df = dataset_df[dataset_df['대상학과'].str.contains('수학과')]           # 학부수업은 대상학과 '수학과ㅇ'로 표현됨
under_dataset_classroom_df = under_dataset_df['강의실']                              # 강의실 데이터프레임을 under_dataset_classroom_df로 추출
under_dataset_df = under_dataset_df[['성명', '교과목명', '강의시간']]                   # 성명, 교과목명, 강의시간으로 under_dataset_df 추출
under_dataset_df = under_dataset_df.reset_index(drop=True)                          # index 재설정

# 요일과 시간 데이터 추출
under_dataset_df['요일'] = under_dataset_df['강의시간'].str.slice(start=0, stop=3)    # 슬라이싱으로 요일 컬럼 추가
under_dataset_df['시간'] = under_dataset_df['강의시간'].str.slice(start=3)            # 슬라이싱으로 시간 컬럼 추가
under_dataset_df = under_dataset_df.drop(['강의시간'], axis = 1)                     # 강의시간 컬럼 삭제
under_dataset_list = under_dataset_df.values.tolist()                              # 학부 데이터셋을 리스트로 저장
#print(under_dataset_list)


# 대학원 데이터셋 추출
grad_dataset_df = dataset_df[dataset_df['대상학과'].str.contains('대학원')]           # 대학원 수업은 '대학원수학전공'으로 표기됨
grad_dataset_classroom_df = grad_dataset_df['강의실']                               # 대학원 강의실을 데이터프레임으로 추출 grad_dataset_classroom_df
grad_dataset_df = grad_dataset_df[['성명', '교과목명', '강의시간']]                    # 성명, 교과목명, 강의시간을 grad_dataset_df 로 추출
grad_dataset_df = grad_dataset_df.reset_index(drop=True)                           # index 재설정

# 대학원 데이터 중 요일/시작시간/(분) 으로 된 데이터 ( 예: 수15:00(150), 월,수15:00(75) )
grad_dataset_df2 = grad_dataset_df[grad_dataset_df['강의시간'].str.contains(':')]

## 요일이 하나인 데이터 ( 예: 수15:00(150) )
grad_dataset_df3 = grad_dataset_df2[~grad_dataset_df2['강의시간'].str.contains(',')].copy()

grad_dataset_df3['요일'] = grad_dataset_df3['강의시간'].str.slice(start=0, stop=1)    # 슬라이싱으로 요일 컬럼 추가
grad_dataset_df3['시간'] = grad_dataset_df3['강의시간'].str.slice(start=1)            # 슬라이싱으로 시간 컬럼 추가
grad_dataset_df3 = grad_dataset_df3.drop(['강의시간'], axis = 1)

## 요일이 두개인 데이터 ( 예: 월,수15:00(75) )
grad_dataset_df4 = grad_dataset_df2[grad_dataset_df2['강의시간'].str.contains(',')].copy()
grad_dataset_df4['요일'] = grad_dataset_df4['강의시간'].str.slice(start=0, stop=3)    # 슬라이싱으로 요일 컬럼 추가
grad_dataset_df4['시간'] = grad_dataset_df4['강의시간'].str.slice(start=3)            # 슬라이싱으로 시간 컬럼 추가
grad_dataset_df4 = grad_dataset_df4.drop(['강의시간'], axis = 1)

grad_dataset_df2 = pd.concat([grad_dataset_df3, grad_dataset_df4])                  # 요일 하나인 데이터와 요일 두개인 데이터 concat

# 요일 시각 으로 된 데이터 ( 예: 금9,10,11 )
grad_dataset_df5 = grad_dataset_df[~grad_dataset_df['강의시간'].str.contains(':')].copy()
grad_dataset_df5['요일'] = grad_dataset_df5['강의시간'].str.slice(start= 0, stop = 1)

grad_dataset_df5['시간'] = grad_dataset_df5['강의시간'].str.slice(start= 1, stop = 3) + ':00(180)'
grad_dataset_df5 = grad_dataset_df5.drop(['강의시간'], axis = 1)                     # 강의시간 컬럼 삭제

grad_dataset_df = pd.concat([grad_dataset_df2, grad_dataset_df5])
grad_dataset_df = grad_dataset_df.reset_index(drop=True)  # index 재설정

grad_dataset_list = grad_dataset_df.values.tolist()                                 # 대학원 데이터셋을 리스트로 저장


#학부 수업 시간-> 시간id로 변경
under_dataset_df['시작시간'] = under_dataset_df['시간'].str.split('(').str[0]
under_dataset_df['수업시간'] = under_dataset_df['시간'].str.split('(').str[1]
under_dataset_df['수업시간'] = under_dataset_df['수업시간'].str.split(')').str[0]
under_dataset_df['수업시간'] = under_dataset_df['수업시간'].astype(int)


#학부 수업 시작시간의 시간ID 반환
for i in range(len(under_dataset_df)):
    for j in range(len(time_df)):
        if under_dataset_df.iloc[i, 4] == time_df.iloc[j, 1]:                           # 시작시간과 timd_df에서 시간 비교
            under_dataset_df.iloc[i, 4] = time_df.iloc[j, 0]                            # 시작시간을 시간ID로 변환

classtime = (under_dataset_df['수업시간'] // 30) + 1                                      # 학부 수업시간에 해당하는 시간ID의 개수
under_dataset_df['시간ID'] = 0

start_arr = under_dataset_df['시작시간'].values.tolist()
finish_arr = under_dataset_df['시작시간'].astype(int) + classtime

time = []
for i in range(len(start_arr)):
    time2 = []
    for j in range(start_arr[i], finish_arr[i]):
        time2.append(str(j))
    time_string = ",".join(time2)
    time.append(time_string)

under_dataset_df = under_dataset_df.drop(['시간', '시작시간', '수업시간', '시간ID'], axis = 1)           # 강의시간 컬럼 삭제
under_dataset_list = under_dataset_df.values.tolist()                                               # 학부 데이터셋을 리스트로 저장

under_classroom_arr = under_dataset_classroom_df.values.tolist()

for i in range(len(under_dataset_list)):
    under_dataset_list[i].append(time[i])
    under_dataset_list[i].append(under_classroom_arr[i])

print(under_dataset_list)

#대학원 수업 시간-> 시간id로 변경
grad_dataset_df['시작시간'] = grad_dataset_df['시간'].str.split('(').str[0]

grad_dataset_df['수업시간'] = grad_dataset_df['시간'].str.split('(').str[1]
grad_dataset_df['수업시간'] = grad_dataset_df['수업시간'].str.split(')').str[0]
grad_dataset_df['수업시간'] = grad_dataset_df['수업시간'].astype(int)                     # grad_dataset_df['수업시간'] series 타입변환 object -> int

#대학원 수업 시작시간의 시간ID 반환
for i in range(len(grad_dataset_df)):
    for j in range(len(time_df)):
        if grad_dataset_df.iloc[i, 4] == time_df.iloc[j, 1]:                           # 시작시간과 timd_df에서 시간 비교
            grad_dataset_df.iloc[i, 4] = time_df.iloc[j, 0]                            # 시작시간을 시간ID로 변환

classtime = (grad_dataset_df['수업시간'] // 30) + 1                                      # 대학원 수업시간에 해당하는 시간ID의 개수 int
grad_dataset_df['시간ID'] = 0

start_arr2 = grad_dataset_df['시작시간'].values.tolist()
finish_arr2 = grad_dataset_df['시작시간'].astype(int) + classtime

time = []
for i in range(len(start_arr2)):
    time2 = []
    for j in range(start_arr2[i], finish_arr2[i]):
        time2.append(str(j))
    time_string = ",".join(time2)
    time.append(time_string)

grad_dataset_df = grad_dataset_df.drop(['시간', '시작시간', '수업시간', '시간ID'], axis = 1)                 # 강의시간 컬럼 삭제
grad_dataset_list = grad_dataset_df.values.tolist()                                                     # 학부 데이터셋을 리스트로 저장

grad_dataset_list = grad_dataset_df.values.tolist()                                               # 학부 데이터셋을 리스트로 저장

grad_classroom_arr = grad_dataset_classroom_df.values.tolist()

for i in range(len(grad_dataset_list)):
    grad_dataset_list[i].append(time[i])
    grad_dataset_list[i].append(grad_classroom_arr[i])

# 교수 순번에 따라서 sort
under_data_sort_list = []
grad_data_sort_list = []
for i in range(len(professor_list)):
    under_professor_sort_list = []
    grad_professor_sort_list = []
    for j in range(len(under_dataset_list)):
        if under_dataset_list[j][0] == professor_list[i][1]:
            under_professor_sort_list.append(under_dataset_list[j])
    for j in range(len(grad_dataset_list)):
        if grad_dataset_list[j][0] == professor_list[i][1]:
            grad_professor_sort_list.append(grad_dataset_list[j])
    under_data_sort_list.append(under_professor_sort_list)
    grad_data_sort_list.append(grad_professor_sort_list)

print('under_data_sort_list')
for i in range(len(under_data_sort_list)):
    print(under_data_sort_list[i][0][0])
    print(under_data_sort_list[i])

print('grad_data_sort_list')
for i in range(len(grad_data_sort_list)):
    print(grad_data_sort_list[i][0][0])
    print(grad_data_sort_list[i])

# key : 과목, value : 학년인 dictionary
global lesson_dictionary, professor_dictionary
lesson_dictionary = dict()
for i in range(len(lesson_list)):
    if lesson_list[i][3] == '대학원':
        continue
    lesson_id = lesson_list[i][1]
    lesson_dictionary[lesson_id] = lesson_list[i][4]
print(lesson_dictionary)
print(lesson_dictionary['금융수리모델론'])

professor_dictionary = dict()
for i in range(len(professor_list)):
    professor_id = professor_list[i][int(3)]-1
    professor_dictionary[professor_id] = professor_list[i][1]
print(professor_dictionary)
print(professor_dictionary[0])
# directoryNm = QFileDialog.getExistingDirectory()
