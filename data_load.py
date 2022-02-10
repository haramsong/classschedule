# DB Load
from imports import *
global today_QDate

today_QDate = QDate.currentDate()

global classroom_df, lesson_assign_df, lesson_df, professor_df, time_df, global_df, under_dataset_df, grad_dataset_df
global classroom_list, lesson_assign_list, lesson_list, professor_list, time_list, global_list, under_dataset_list, grad_dataset_list
global classroom_list_col, lesson_assign_list_col, lesson_list_col, professor_list_col, time_list_col, global_list_col

# 로컬 마스터데이터 로드 (위치 : data 폴더 안 excel 파일)
classroom_df = pd.read_excel('data/classroom_info.xlsx')
lesson_assign_df = pd.read_excel('data/lesson_assign.xlsx')
lesson_df = pd.read_excel('data/lesson_info.xlsx')
professor_df = pd.read_excel('data/professor_info.xlsx')
time_df = pd.read_excel('data/time_period.xlsx')
global_df = pd.read_excel('data/global_master.xlsx')


# nan값 제거
classroom_df.replace(np.NaN, '', inplace=True)
lesson_assign_df.replace(np.NaN, '', inplace=True)
lesson_df.replace(np.NaN, '', inplace=True)
professor_df.replace(np.NaN, '', inplace=True)
time_df.replace(np.NaN, '', inplace=True)

classroom_list = classroom_df.values.tolist()
lesson_assign_list = lesson_assign_df.values.tolist()
lesson_list = lesson_df.values.tolist()
professor_list = professor_df.values.tolist()
time_list = time_df.values.tolist()
global_list = global_df.values.tolist()

# 데이터 저장할 때 필요한 column(to_excel)
classroom_list_col = list([col for col in pd.read_excel('data/classroom_info.xlsx')])                # 강의실 column
lesson_assign_list_col = list([col for col in pd.read_excel('data/lesson_assign.xlsx')])             # 강의 배정 column
lesson_list_col = list([col for col in pd.read_excel('data/lesson_info.xlsx')])                      # 강의 column
professor_list_col = list([col for col in pd.read_excel('data/professor_info.xlsx')])                # 교수 column
time_list_col = list([col for col in pd.read_excel('data/time_period.xlsx')])                        # 시간표 column
global_list_col = list([col for col in pd.read_excel('data/global_master.xlsx')])                        # 시간표 column


##### 해야하는 일 교수님 강의명 요일 시간id 로 array 저장
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
under_dataset_df = dataset_df[dataset_df['대상학과'].str.contains('수학과')]
under_dataset_df = under_dataset_df[['성명', '교과목명', '강의시간']]
under_dataset_df = under_dataset_df.reset_index(drop=True)                          # index 재설정

# 요일과 시간 데이터 추출
under_dataset_df['요일'] = under_dataset_df['강의시간'].str.slice(start=0, stop=3)    # 슬라이싱으로 요일 컬럼 추가
under_dataset_df['시간'] = under_dataset_df['강의시간'].str.slice(start=3)            # 슬라이싱으로 시간 컬럼 추가
under_dataset_df = under_dataset_df.drop(['강의시간'], axis = 1)                     # 강의시간 컬럼 삭제

under_dataset_list = under_dataset_df.values.tolist()                              # 학부 데이터셋을 리스트로 저장

# 대학원 데이터셋 추출
grad_dataset_df = dataset_df[dataset_df['대상학과'].str.contains('대학원')]
grad_dataset_df = grad_dataset_df[['성명', '교과목명', '강의시간']]
grad_dataset_df = grad_dataset_df.reset_index(drop=True)  # index 재설정

# 요일과 시간 데이터 추출 전에 "시간 통일 필요"
# grad_dataset_df['요일'] = grad_dataset_df['강의시간'].str.slice(start=0, stop=3)    # 슬라이싱으로 요일 컬럼 추가
# grad_dataset_df['시간'] = grad_dataset_df['강의시간'].str.slice(start=3)            # 슬라이싱으로 시간 컬럼 추가
# grad_dataset_df = grad_dataset_df.drop(['강의시간'], axis = 1)
print(grad_dataset_df)

# grad_dataset_df = grad_dataset_df.values.tolist()                                 # 대학원 데이터셋을 리스트로 저장


# github test
# 아직 안쓰이는 함수
#
# global season_active_idx, Selected_season_ID, Selected_season_SDate, Selected_season_EDate, season_tabarray
# comboBox_season_arr = []
# season_tabarray = []
# for i in range(len(AA_master_list)):
#     active_flag = ""
#     if AA_master_list[i][11] != "":        # 활성 상태인 경우
#         active_flag = "(활성)"
#         season_active_idx = i
#     comboBox_season_arr.append("AA" + str(AA_master_list[i][1]) + " : " + AA_master_list[i][2] + " (" + \
#                                AA_master_list[i][4] + " ~ " + AA_master_list[i][5] + ") " + active_flag)
# Selected_season_ID = comboBox_season_arr[season_active_idx].split(" :")[0]
# Selected_season_SDate = QDate.fromString(AA_master_list[season_active_idx][4], 'yyyy-MM-dd')
# Selected_season_EDate = QDate.fromString(AA_master_list[season_active_idx][5], 'yyyy-MM-dd')
# season_tabarray = []
# for i in range(len(df_time_period_list)):
#     if df_time_period_list[i][0] == Selected_season_ID:
#         season_tabarray.append(df_time_period_list[i])
# global tab_id, combobox_idx
# tab_id = 0
# combobox_idx = 0



# global comboBox_select_arr
# comboBox_select_arr = []
# comboBox_select_arr.append(CC_master_list)
# comboBox_select_arr.append(BB_master_list)
# comboBox_select_arr.append(CC_master_list)
# comboBox_select_arr.append(DD_master_list)
# comboBox_select_arr.append(EE_master_list)
#
# global bg_color_arr
# bg_color_arr = ["greenyellow", "lightpink", "yellow", "aquamarine", "peachpuff"]
#
# global teacher_dictionary
# teacher_dictionary = dict()
# for i in range(len(df_lesson_schedule_list)):
#     for j in range(len(df_teacher_lesson_list)):
#         if df_lesson_schedule_list[i][1] == df_teacher_lesson_list[j][2]:
#             teacher_dictionary[df_lesson_schedule_list[i][1]] = df_teacher_lesson_list[j][1]
# print("season_tabarray")
# print(season_tabarray)
