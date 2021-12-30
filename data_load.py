# DB Load
from imports import *
global today_QDate

today_QDate = QDate.currentDate()

global classroom_list, lesson_assign_list, lesson_list, professor_list, time_list
global classroom_list_col, lesson_assign_list_col, lesson_list_col, professor_list_col, time_list_col

# 로컬 마스터데이터 로드(위치 : data 폴더 안 excel 파일)
classroom_list = pd.read_excel('data/classroom_info.xlsx').values.tolist()      # 강의실 데이터
lesson_assign_list = pd.read_excel('data/lesson_assign.xlsx').values.tolist()   # 강의 배정 데이터
lesson_list = pd.read_excel('data/lesson_info.xlsx').values.tolist()            # 강의 데이터
professor_list = pd.read_excel('data/professor_info.xlsx').values.tolist()      # 교수 데이터
time_list = pd.read_excel('data/time_period.xlsx').values.tolist()              # 시간표 데이터

# 데이터 저장할 때 필요한 column(to_excel)
classroom_list_col = list([col for col in pd.read_excel('data/classroom_info.xlsx')])                # 강의실 column
lesson_assign_list_col = list([col for col in pd.read_excel('data/lesson_assign.xlsx')])             # 강의 배정 column
lesson_list_col = list([col for col in pd.read_excel('data/lesson_info.xlsx')])                      # 강의 column
professor_list_col = list([col for col in pd.read_excel('data/professor_info.xlsx')])                # 교수 column
time_list_col = list([col for col in pd.read_excel('data/time_period.xlsx')])                        # 시간표 column


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