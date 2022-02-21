from imports import *
from dialog import *
from data_load import *
from show_under_timetable import *
from show_grad_timetable import *
import json
import os
import random

# 사용자 지정 창 만들기
class Ui_Lesson_Assign(QDialog):
    def __init__(self):
        super().__init__()
        self.get_init_data()
        self.setupUi()

    # 데이터 불러오기
    def get_init_data(self):
        global tool_button_arr, tool_button_arr2, configData, refresh_button_arr, reset_button_arr
        # 버튼 관련 설정
        tool_button_arr = [
            ["입력", "img/plus.png",40, 40, self.writeInfo],
            ["수정", "img/shuffle.png", 40, 40, self.changeInfo],
            ["삭제", "img/delete.png", 40, 40, self.deleteInfo],
            ["배정", "img/play.png", 40, 40, self.randomAssign],
            ["저장", "img/floppy-disk", 40, 40, self.saveInfo]
        ]

        tool_button_arr2 = ["시간표 미리보기", 770, 700, 40, 50, "img/lesson_schedule.png", 50, 50, self.showTimetable]

        refresh_button_arr = ["새로고침",50,40,40,40, "img/refresh.png", 40, 40, self.refreshInfo]
        reset_button_arr = ["초기화",750,40,40,40, "img/reset.png", 40, 40, self.resetInfo]

        global under_timetable_list, grad_timetable_list
        under_timetable_list = lesson_assign_under_list

        global count
        count = 10
        # 시작, 종료시간 combobox 정보
        global time_start_arr, time_end_arr
        time_start_arr = [""]
        time_end_arr = [""]
        for i in range(len(time_list)):
            time_start_arr.append(time_list[i][1])
            time_end_arr.append(time_list[i][2])

        with open("info_type.json", "r") as info:
             configData = json.load(info)

        # 테이블 위젯 이름 깔끔하게 넣기 위해 설정
        global header_arr
        header_arr = ['교수명', '강좌명', '분반', '분류', '요일', '시작시간', '종료시간', '강의실명']

    def jsonLoad(self):
        global configData
        with open("info_type.json", "r") as info:
            configData = json.load(info)

    # 화면 출력
    def setupUi(self):
        self.setObjectName("Dialog")
        self.setFixedSize(818, 750)

        # 그룹박스 만들기
        self.groupBox = QGroupBox(self)
        self.groupBox.setGeometry(QRect(50, 40, 721, 61))

        # 그룹박스 내 layout -> 라디오 버튼 넣으려고
        self.horizontalLayoutWidget = QWidget(self.groupBox)
        self.horizontalLayoutWidget.setGeometry(QRect(110, 20, 491, 22))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")


        # 라디오 버튼 2개 만들기
        self.radioButton_2 = QRadioButton(self.horizontalLayoutWidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout.addWidget(self.radioButton_2, 0, Qt.AlignHCenter)
        self.radioButton = QRadioButton(self.horizontalLayoutWidget)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout.addWidget(self.radioButton, 0, Qt.AlignHCenter)


        # 두번째 그룹박스 만들기
        self.groupBox_2 = QGroupBox(self)
        self.groupBox_2.setGeometry(QRect(50, 110, 721, 551))


        # 입력창(교수,강의,시작시간,종료시간 등등 ) 만드려고 그룹박스 내 그리드위젯 만들기
        self.gridLayoutWidget = QWidget(self.groupBox_2)
        self.gridLayoutWidget.setGeometry(QRect(20, 20, 691, 100))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")

        # 교수 글씨
        self.label_8 = QLabel(self.gridLayoutWidget)
        self.label_8.setAlignment(Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 0, 1, 1, 1)
        # 강의 글씨
        self.label_9 = QLabel(self.gridLayoutWidget)
        self.label_9.setAlignment(Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 0, 2, 1, 1)
        # 분반 글씨
        self.label_6 = QLabel(self.gridLayoutWidget)
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 0, 3, 1, 1)
        # 분류 글씨
        self.label_16 = QLabel(self.gridLayoutWidget)
        self.label_16.setAlignment(Qt.AlignCenter)
        self.label_16.setObjectName("label_6")
        self.label_16.setText("분류")
        self.gridLayout_2.addWidget(self.label_16, 0, 4, 1, 1)
        # 요일 글씨
        self.label_10 = QLabel(self.gridLayoutWidget)
        self.label_10.setAlignment(Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 2, 1, 1, 1)
        # 시작시간 글씨
        self.label_7 = QLabel(self.gridLayoutWidget)
        self.label_7.setAlignment(Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 2, 2, 1, 1)
        # 종료시간 글씨
        self.label_12 = QLabel(self.gridLayoutWidget)
        self.label_12.setAlignment(Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 2, 3, 1, 1)
        # 강의실 글씨
        self.label_13 = QLabel(self.gridLayoutWidget)
        self.label_13.setAlignment(Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_13, 2, 4, 1, 1)
        # 필수입력  글씨
        self.label_14 = QLabel(self.gridLayoutWidget)
        self.label_14.setAlignment(Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.gridLayout_2.addWidget(self.label_14, 1, 0, 1, 1)
        # 선택입력  글씨
        self.label_15 = QLabel(self.gridLayoutWidget)
        self.label_15.setAlignment(Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.gridLayout_2.addWidget(self.label_15, 3, 0, 1, 1)



        # 교수 콤보박스
        self.comboBox = QComboBox(self.gridLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout_2.addWidget(self.comboBox, 1, 1, 1, 1)
        self.comboBox.addItems(professor_df['성명'])
        # 강의 콤보박스
        self.comboBox_2 = QComboBox(self.gridLayoutWidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.gridLayout_2.addWidget(self.comboBox_2, 1, 2, 1, 1)
        # 분반
        self.lineEdit_8 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout_2.addWidget(self.lineEdit_8, 1, 3, 1, 1)
        # 분류 콤보박스
        self.comboBox_5 = QComboBox(self.gridLayoutWidget)
        self.comboBox_5.setObjectName("comboBox_3")
        self.gridLayout_2.addWidget(self.comboBox_5, 1, 4, 1, 1)
        self.comboBox_5.addItems(["전공기초", "전공선택", "전공필수", "전공", "교양선택"])
        # 요일
        self.lineEdit_9 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.gridLayout_2.addWidget(self.lineEdit_9, 3, 1, 1, 1)
        # 시작 콤보박스
        self.comboBox_3 = QComboBox(self.gridLayoutWidget)
        self.comboBox_3.setObjectName("comboBox_3")
        self.gridLayout_2.addWidget(self.comboBox_3, 3, 2, 1, 1)
        self.comboBox_3.addItems(time_start_arr)
        # 종료 콤보박스
        self.comboBox_4 = QComboBox(self.gridLayoutWidget)
        self.comboBox_4.setObjectName("comboBox_4")
        self.gridLayout_2.addWidget(self.comboBox_4, 3, 3, 1, 1)
        self.comboBox_4.addItems(time_end_arr)
        # 강의실
        self.lineEdit_11 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.gridLayout_2.addWidget(self.lineEdit_11, 3, 4, 1, 1)

        # refresh 버튼
        self.toolButton = QToolButton(self)
        global_funtion.tool_button_setting(self, self.toolButton, refresh_button_arr)

        self.toolButton = QToolButton(self)
        global_funtion.tool_button_setting(self, self.toolButton, reset_button_arr)

        # 시간표 보여주기 showShedule 버튼
        self.toolButton = QToolButton(self)
        global_funtion.tool_button_setting(self, self.toolButton, tool_button_arr2)

        # 테이블 위젯 만들기( 목록 띄우기 위함 )
        self.tableWidget =QTableWidget(self.groupBox_2)
        self.tableWidget.setGeometry(QRect(30, 150, 571, 380))
        self.tableWidget.setObjectName("tableWidget")
        # 행과 열 만들기
        self.tableWidget.setColumnCount(8)

        # 테이블위젯 이름 넣으려고 만듬 (맨 윗줄)
        for i in range(0,8):
            item = QTableWidgetItem()  # 교수
            item.setText(header_arr[i])
            self.tableWidget.setHorizontalHeaderItem(i, item)
            self.tableWidget.horizontalHeader().setSectionResizeMode(i, QHeaderView.Stretch)
        self.tableWidget.verticalHeader().hide()


        # 사용자 지정 배정 라벨
        self.label_11 = QLabel()
        self.label_11.setGeometry(QRect(5, 20, 151, 16))
        self.label_11.setObjectName("label_11")


        # 아이콘 배열
        self.verticalLayoutWidget = QWidget(self.groupBox_2)
        self.verticalLayoutWidget.setGeometry(QRect(640, 120, 111, 451))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        for i in range(len(tool_button_arr)):
            self.toolButton = QToolButton(self.verticalLayoutWidget)
            global_funtion.tool_button_setting_widget(self, self.toolButton, self.verticalLayout, tool_button_arr[i])



        # 텍스트 출력
        self.retranslateUi()

        # 라디오 버튼 연결시키기
        self.radioButton.toggled.connect(self.onClicked)
        self.radioButton_2.toggled.connect(self.onClicked2)
        self.radioButton_2.click()

        # TableWidget 클릭 메소드 연결
        self.tableWidget.itemClicked.connect(self.tableClick)

    def refreshInfo(self):
        self.close()
        self.__init__()
        self.exec_()

    def resetInfo(self):
        global lesson_assign_under_list, lesson_assign_list_dae, lesson_assign_arr, lesson_assign_under_list_origin, lesson_assign_list_dae_origin
        global professor_sorted_assign_list
        global_funtion().message_box_2(QMessageBox.Question, "경고", "저장을 안하고 초기화 시 등록했던 데이터가 삭제됩니다. 초기화하시겠습니까?", "예", "아니오")

        global count
        count = 10

        self.jsonLoad()
        if configData['message'] == 'Y':
            if configData['random'] == 'Y':
                lesson_assign_arr = []
                configData['random'] = 'N'
                json.dumps(configData, indent="\t")
                with open('info_type.json', 'w', encoding='utf-8') as make_file:
                    json.dump(configData, make_file, indent="\t")

            global_funtion().message_box_1(QMessageBox.Information, "확인", "초기화되었습니다.", "확인")
            if self.radioButton_2.isChecked():
                # print('lesson_assign_under_list_origin')
                professor_sorted_assign_list = []
                # print(lesson_assign_under_list_origin)
                lesson_assign_under_list = lesson_assign_under_list_origin
                lesson_assign_under_df_origin = pd.read_excel('data/lesson_assign_under.xlsx')
                lesson_assign_under_df_origin.replace(np.NaN, '', inplace=True)
                lesson_assign_under_list_origin = lesson_assign_under_df_origin.values.tolist()
                lesson_assign_under_df_origin.to_excel('data/lesson_assign_under_tableview.xlsx',
                                  index=False)  # dataframe excel 저장
                self.df_load()
            else:
                lesson_assign_list_dae = lesson_assign_list_dae_origin
                lesson_assign_df_dae_origin = pd.read_excel('data/lesson_assign_dae.xlsx')
                lesson_assign_df_dae_origin.replace(np.NaN, '', inplace=True)
                lesson_assign_list_dae_origin = lesson_assign_df_dae_origin.values.tolist()
                lesson_assign_df_dae_origin.to_excel('data/lesson_assign_grad_tableview.xlsx',
                                  index=False)  # dataframe excel 저장
                self.df_dae_load
            self.tableData()
        else:
            global_funtion().message_box_1(QMessageBox.Information, "확인", "저장을 해주시길 바랍니다.", "확인")

    def df_dae_load(self):
        global df
        df = pd.DataFrame(lesson_assign_list_dae, columns = lesson_assign_list_col_dae)
        df = df.reset_index()[['교수명', '강좌명', '분반', '분류', '요일', '시간ID', '강의실명']]
        df['분반'] = df['분반'].astype(str).apply(lambda x: x.replace('.0', ''))
        df['시간ID'] = df['시간ID'].astype(str)
        # 시간 id 중 가장 작은 숫자에 해당하는 time 시작시간으로 불러오기
        start = time_df.iloc[df['시간ID'].str.split(',').str[0]]['시작시간']
        start = start.reset_index()['시작시간']
        df = pd.concat([df, start], axis=1)
        # 시간 id 중 가장 큰 숫자에 해당하는 time 종료시간으로 불러오기
        finish = time_df.iloc[df['시간ID'].str.split(',').str[-1]]['종료시간']
        finish = finish.reset_index()['종료시간']
        df = pd.concat([df, finish], axis=1)
        df = df[header_arr]

    def df_load(self):
        global df2
        df2= pd.DataFrame(lesson_assign_under_list, columns = lesson_assign_under_list_col)
        df2 = df2.reset_index()[['교수명', '강좌명', '분반', '분류', '요일', '시간ID', '강의실명']]
        df2['분반'] = df2['분반'].astype(str).apply(lambda x: x.replace('.0', ''))
        df2['시간ID'] = df2['시간ID'].astype(str)
        # 시간 id 중 가장 작은 숫자에 해당하는 time 시작시간으로 불러오기
        start2 = time_df.iloc[df2['시간ID'].str.split(',').str[0]]['시작시간']
        start2 = start2.reset_index()['시작시간']
        df2 = pd.concat([df2, start2], axis=1)
        # 종료 id 중 가장 큰 숫자에 해당하는 time 종료시간으로 불러오기
        finish2 = time_df.iloc[df2['시간ID'].str.split(',').str[-1]]['종료시간']
        finish2 = finish2.reset_index()['종료시간']
        df2 = pd.concat([df2, finish2], axis=1)
        df2 = df2[header_arr]

    # 대학원 라디오 버튼 연결 ( 대학원 데이터 불러오기 )
    def onClicked(self):
        global df, radioBtn
        self.comboBox_2.clear()
        radioBtn = self.sender()
        if radioBtn.isChecked():
            self.lineEdit_8.setText("")
            self.lineEdit_9.setText("")
            self.lineEdit_11.setText("")
            grad_lesson_arr = []
            for i in range(len(lesson_list)):
                if str(lesson_list[i][2]) != str(semester_str):
                    continue
                if str(lesson_list[i][3]) != '대학원':
                    continue
                grad_lesson_arr.append(lesson_list[i][1])
            self.comboBox_2.addItems(grad_lesson_arr)
            self.tableWidget.setRowCount(0)
            # 대학원 파일을 불러온다
            self.df_dae_load()
            self.tableWidget.setRowCount(len(df))
            # 테이블 위젯에 데이터 집어넣기
            for i in range(len(df)):
                # row = self.tableWidget.rowCount()
                # self.tableWidget.insertRow(row)
                for j in range(len(df.columns)):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(df.iloc[i, j])))

    # 학부 라디오 버튼 연결 ( 학부 데이터 불러오기 )
    def onClicked2(self):
        global df2, radioBtn2
        self.comboBox_2.clear()
        radioBtn2 = self.sender()
        if radioBtn2.isChecked():
            self.lineEdit_8.setText("")
            self.lineEdit_9.setText("")
            self.lineEdit_11.setText("")
            under_lesson_arr = []
            for i in range(len(lesson_list)):
                if str(lesson_list[i][2]) != str(semester_str):
                    continue
                if str(lesson_list[i][3]) != '학부':
                    continue
                under_lesson_arr.append(lesson_list[i][1])
            self.comboBox_2.addItems(under_lesson_arr)
            self.tableWidget.setRowCount(0)
            # 학부 파일을 불러온다
            self.df_load()
            self.tableWidget.setRowCount(len(df2))
            # 테이블 위젯에 데이터 집어넣기
            for i in range(len(df2)):
                # row = self.tableWidget.rowCount()
                # self.tableWidget.insertRow(row)
                for j in range(len(df2.columns)):
                        self.tableWidget.setItem(i, j, QTableWidgetItem(str(df2.iloc[i, j])))

    # tableClick Event ( 테이블 위젯 클릭시 창에 정보 띄우기 )
    def tableClick(self):
        global curr_row, curr_col, df2_list, df_list
        curr_row = self.tableWidget.currentRow()  # 테이블 위젯에서 선택한 행 인덱스
        curr_col = self.tableWidget.currentColumn()  # 테이블 위젯에서 선택한 열 인덱스
        if radioBtn2.isChecked():  #학부 라디오 버튼 체크시 , df2 = 학부 파일
            self.df_load()
            df2_list = df2.values.tolist()
            item = df2_list[curr_row]

        else:  # 대학원 라디오 버튼 체크시 , df = 대학원 파일
            self.df_dae_load()
            df_list = df.values.tolist()
            item = df_list[curr_row]

        # 교수명
        self.comboBox.setCurrentText(item[0])
        # 강좌명
        self.comboBox_2.setCurrentText(item[1])
        # 분반 ( str으로 변환 필요 )
        self.lineEdit_8.setText(str(item[2]))
        # 분류
        self.comboBox_5.setCurrentText(item[3])
        # 요일
        self.lineEdit_9.setText(item[4])
        # 시작시간
        self.comboBox_3.setCurrentText(item[5])
        # 종료시간
        self.comboBox_4.setCurrentText(item[6])
        # 강의실명
        self.lineEdit_11.setText(item[7])

   # 텍스트 출력
    def retranslateUi(self):
        _translate = QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "사용자 지정 배정"))
        self.radioButton.setText(_translate("Dialog", "대학원"))
        self.radioButton_2.setText(_translate("Dialog", "학부"))
        self.label_6.setText(_translate("Dialog", "분반"))
        self.label_7.setText(_translate("Dialog", "시작시간"))
        self.label_8.setText(_translate("Dialog", "교수"))
        self.label_9.setText(_translate("Dialog", "강의"))
        self.label_10.setText(_translate("Dialog", "요일"))
        self.label_11.setText(_translate("Dialog", "사용자지정 배정"))
        self.label_12.setText(_translate("Dialog", "종료시간"))
        self.label_13.setText(_translate("Dialog", "강의실"))
        self.label_14.setText(_translate("Dialog", "필수입력"))
        self.label_15.setText(_translate("Dialog", "선택입력"))

    # 입력하기
    def writeInfo(self):
        global write_data , lesson_assign_under_list, lesson_assign_list_dae
        # 데이터순서: 교수 강의 분반 분류 요일 시작시간 종료시간 강의실
        write_data=[]
        write_data.append(self.comboBox.currentText())      # 교수
        write_data.append(self.comboBox_2.currentText())    # 강의명
        write_data.append(self.lineEdit_8.text())           # 분반
        write_data.append(self.comboBox_5.currentText())    # 교과분류
        write_data.append(self.lineEdit_9.text())           # 요일

        # 시작시간 종료시간 담는 코드
        time = []
        start = self.comboBox_3.currentIndex()      # 시작시간의 시간ID
        end = self.comboBox_4.currentIndex()        # 종료시간의 시간ID
        if start == 0 & end == 0:                   # 시작시간 종료시간 선택 안함
            time.append(26)
            write_data.append(str(time)[1:-1])      # 시간ID
        else:                                       # 시작시간 종료시간 선택함
            for i in range(start - 1, end):
                time.append(i)
            time_arr = []
            for ele in time:
                ele.replace(' ', '')
                time_arr.append(ele)
            write_data.append(str(time_arr)[1:-1])      # 시간ID
        write_data.append(self.lineEdit_11.text())  # 강의실

        if radioBtn2.isChecked():                   # 학부 라디오버튼 체크시
            for i in range(len(lesson_assign_under_list)):
                if lesson_assign_under_list[i][0] == write_data[0] and lesson_assign_under_list[i][1] == write_data[1] and \
                    str(lesson_assign_under_list[i][2]) == write_data[2] and lesson_assign_under_list[i][3] == write_data[3]:
                    global_funtion().message_box_1(QMessageBox.Information, "경고", "중복된 데이터를 입력할 수 없습니다.", "확인")
                    return
            lesson_assign_under_list.append(write_data)
            # list.sort(lesson_assign_under_list, key=lambda k: (k[0]))  # data array의 0번째 index를 기준으로 sort
            df_write = pd.DataFrame(lesson_assign_under_list,
                                    columns=lesson_assign_under_list_col)  # data array, column은 label_col로 하는 dataframe 생성
            df_write.to_excel('data/lesson_assign_under_tableview.xlsx',
                              index=False)  # dataframe excel 저장
            # print("1",lesson_assign_under_list)
        else:                                       # 대학원 라디오버튼 체크시
            for i in range(len(lesson_assign_list_dae)):
                if lesson_assign_list_dae[i][0] == write_data[0] and lesson_assign_list_dae[i][1] == write_data[1] and \
                    str(lesson_assign_list_dae[i][2]) == write_data[2] and lesson_assign_list_dae[i][3] == write_data[3]:
                    global_funtion().message_box_1(QMessageBox.Information, "경고", "중복된 데이터를 입력할 수 없습니다.", "확인")
                    return
            lesson_assign_list_dae.append(write_data)
            # list.sort(lesson_assign_list_dae, key=lambda k: (k[0]))  # data array의 0번째 index를 기준으로 sort
            df_write = pd.DataFrame(lesson_assign_list_dae,
                                    columns=lesson_assign_list_col_dae)  # data array, column은 label_col로 하는 dataframe 생성
            df_write.to_excel('data/lesson_assign_grad_tableview.xlsx',
                              index=False)  # dataframe excel 저장
            # print("1",lesson_assign_list_dae)
        global_funtion().message_box_1(QMessageBox.Information, "정보", "입력되었습니다", "확인")


        self.tableData()

    # 수정하기
    def changeInfo(self):
        global lesson_assign_under_list, lesson_assign_list_dae, curr_row, changed_data
        global_funtion().message_box_2(QMessageBox.Question, "확인", "작성내용을 수정하시겠습니까?", "예", "아니오")
        self.jsonLoad()
        if configData['message'] == 'Y':
            if radioBtn2.isChecked(): # 학부 버튼 클릭 시
                for i in range(len(lesson_assign_under_list)):  # data 개수만큼 for문
                    if i == curr_row:                           # 위젯list에서 선택한 row와 i번째 data가 일치하면
                        changed_data = []
                        changed_data.append(self.comboBox.currentText())        # 교수
                        changed_data.append(self.comboBox_2.currentText())      # 강의명
                        changed_data.append(self.lineEdit_8.text())             # 분반
                        changed_data.append(self.comboBox_5.currentText())      # 교과분류
                        changed_data.append(self.lineEdit_9.text())             # 요일
                        # 시작시간 종료시간 담는 코드
                        time = []
                        start = self.comboBox_3.currentIndex()          # 시작시간의 시간ID
                        end = self.comboBox_4.currentIndex()            # 종료시간의 시간ID
                        if start == 0 & end == 0:                       # 시작시간 종료시간 선택 안함
                            time.append(26)
                            changed_data.append(str(time)[1:-1])        # 시간ID
                        else:                                           # 시작시간 종료시간 선택함
                            for j in range(start - 1, end):
                                time.append(j)
                            # time_arr = []
                            # for ele in time:
                            #     ele.replace(' ','')
                            #     time_arr.append(ele)
                            # changed_data.append(str(time_arr)[1:-1])        # 시간ID
                            changed_data.append(str(time)[1:-1])
                        changed_data.append(self.lineEdit_11.text())    # 강의실
                        # print(changed_data)
                        lesson_assign_under_list[i] = changed_data
                        df_write = pd.DataFrame(lesson_assign_under_list,
                                                columns=lesson_assign_under_list_col)  # data array, column은 label_col로 하는 dataframe 생성
                        df_write.to_excel('data/lesson_assign_under_tableview.xlsx',
                                          index=False)  # dataframe excel 저장

            else: #대학원 라디오버튼 클릭시
                for i in range(len(lesson_assign_list_dae)):    # data 개수만큼 for문
                    if i == curr_row:                           # 위젯list에서 선택한 row와 i번째 data가 일치하면
                        changed_data = []
                        changed_data.append(self.comboBox.currentText())    # 교수
                        changed_data.append(self.comboBox_2.currentText())  # 강의명
                        changed_data.append(self.lineEdit_8.text())         # 분반
                        changed_data.append(self.comboBox_5.currentText())  # 교과분류
                        changed_data.append(self.lineEdit_9.text())         # 요일
                        # 시작시간 종료시간 담는 코드
                        time = []
                        start = self.comboBox_3.currentIndex()          # 시작시간의 시간ID
                        end = self.comboBox_4.currentIndex()            # 종료시간의 시간ID
                        if start == 0 & end == 0:                       # 시작시간 종료시간 선택 안함
                            time.append(26)
                            changed_data.append(str(time)[1:-1])        # 시간ID
                        else:                                           # 시작시간 종료시간 선택함
                            for j in range(start - 1, end):
                                time.append(j)
                            # time_arr = []
                            # for ele in time:
                            #     ele.replace(' ', '')
                            #     time_arr.append(ele)
                            # changed_data.append(str(time_arr)[1:-1])        # 시간ID
                            changed_data.append(str(time)[1:-1])
                        changed_data.append(self.lineEdit_11.text())    # 강의실
                        lesson_assign_list_dae[i][1:8] = changed_data
                        df_write = pd.DataFrame(lesson_assign_list_dae,
                                                columns=lesson_assign_list_col_dae)  # data array, column은 label_col로 하는 dataframe 생성
                        df_write.to_excel('data/lesson_assign_grad_tableview.xlsx',
                                          index=False)  # dataframe excel 저장
            global_funtion().message_box_1(QMessageBox.Information, "정보", "수정되었습니다", "확인")

        elif configData['message'] == 'N':
            # print("no")
            return

        self.tableData()

    # 삭제 메소드
    def deleteInfo(self):
        global lesson_assign_under_list, lesson_assign_list_dae, curr_row
        global_funtion().message_box_2(QMessageBox.Question, "확인", "작성내용을 삭제하시겠습니까?", "예", "아니오")
        self.jsonLoad()
        if configData['message'] == 'Y':
            if radioBtn2.isChecked():                   # 학부 라디오 버튼이 체크 되어있을 때
                del lesson_assign_under_list[curr_row]  # lesson_assign_list 에서 선택한 행 삭제
                df_write = pd.DataFrame(lesson_assign_under_list,
                                        columns=lesson_assign_under_list_col)  # data array, column은 label_col로 하는 dataframe 생성
                df_write.to_excel('data/lesson_assign_under_tableview.xlsx',
                                  index=False)  # dataframe excel 저장
            else:                                       # 대학원 라디오 버튼 체크시
                del lesson_assign_list_dae[curr_row]    # lesson_assign_grad_list 에서 선택한 행 삭제
                df_write = pd.DataFrame(lesson_assign_list_dae,
                                        columns=lesson_assign_list_col_dae)  # data array, column은 label_col로 하는 dataframe 생성
                df_write.to_excel('data/lesson_assign_grad_tableview.xlsx',
                                  index=False)  # dataframe excel 저장
            global_funtion().message_box_1(QMessageBox.Information, "정보", "삭제되었습니다", "확인")

        elif configData['message'] == 'N':
            # print("삭제 안함")
            return

        self.tableData()

    # 랜덤 배정
    def randomAssign(self):
        global lesson_assign_under_list, lesson_assign_list_dae, lesson_assign_arr, professor_sorted_assign_list, count
        random_code = 0
        random_denied_list = []
        if count == 0:
            if self.radioButton_2.isChecked():
                df_write = pd.DataFrame(lesson_assign_under_list,
                                        columns=lesson_assign_under_list_col)  # data array, column은 label_col로 하는 dataframe 생성
                df_write.to_excel('data/lesson_assign_under_tableview.xlsx',
                                  index=False)  # dataframe excel 저장
            else:
                df_write = pd.DataFrame(lesson_assign_under_list,
                                        columns=lesson_assign_under_list_col)  # data array, column은 label_col로 하는 dataframe 생성
                df_write.to_excel('data/lesson_assign_under_tableview.xlsx',
                                  index=False)  # dataframe excel 저장
            global_funtion().message_box_1(QMessageBox.Information, "정보", "성공적으로 배정되었습니다.", "확인")
            return
        # 모든 강의가 요일, 시간이 다 차있을 때 랜덤 배정 x
        if self.radioButton_2.isChecked():
            for i in range(len(lesson_assign_under_list)):
                if lesson_assign_under_list[i][4] != '':
                    continue
                random_code += 1
            if random_code == 0:
                global_funtion().message_box_1(QMessageBox.Information, "정보", "랜덤 배정할 강의가 없습니다", "확인")
                return
        else:
            for i in range(len(lesson_assign_list_dae)):
                if lesson_assign_list_dae[i][4] != '':
                    continue
                random_code += 1
            if random_code == 0:
                global_funtion().message_box_1(QMessageBox.Information, "정보", "랜덤 배정할 강의가 없습니다", "확인")
                return

        # 요일, 시간 체크 arr 생성
        self.jsonLoad()
        if configData['random'] == 'N':
            lesson_assign_arr = []
            for i in range(len(time_list) - 1):
                lesson_assign_arr.append([])
                for j in range(0,5):
                    lesson_assign_arr[i].append([])
            configData['random'] = 'Y'
            json.dumps(configData, indent="\t")

            with open('info_type.json', 'w', encoding='utf-8') as make_file:
                json.dump(configData, make_file, indent="\t")

            # print(lesson_assign_arr)

        # 학부 랜덤 배정
        if self.radioButton_2.isChecked():
            # 교수님 순번별로 다시 sort
            global professor_sorted_assign_list
            professor_sorted_assign_list = []
            for i in range(len(professor_list)):
                for j in range(len(lesson_assign_under_list)):
                    if professor_dictionary[i] == lesson_assign_under_list[j][0]:
                        professor_sorted_assign_list.append(lesson_assign_under_list[j])
            # print(professor_sorted_assign_list)

            # print(lesson_assign_under_list)
            for i in range(len(professor_sorted_assign_list)):
                check_arr = []
                if professor_sorted_assign_list[i][4] == '':
                    continue
                for j in professor_sorted_assign_list[i][5].split(","):  # 12,13,14,15,16
                    check_arr = [professor_sorted_assign_list[i][0], professor_sorted_assign_list[i][6], lesson_dictionary[professor_sorted_assign_list[i][1]]]
                    # print(check_arr)
                    if "월" in professor_sorted_assign_list[i][4]:
                        lesson_assign_arr[int(j)][0].append(check_arr)
                    if "화" in professor_sorted_assign_list[i][4]:
                        lesson_assign_arr[int(j)][1].append(check_arr)
                    if "수" in professor_sorted_assign_list[i][4]:
                        lesson_assign_arr[int(j)][2].append(check_arr)
                    if "목" in professor_sorted_assign_list[i][4]:
                        lesson_assign_arr[int(j)][3].append(check_arr)
                    if "금" in professor_sorted_assign_list[i][4]:
                        lesson_assign_arr[int(j)][4].append(check_arr)
                # print(lesson_assign_arr)

            # print('professor_sorted_assign_list')
            # print(professor_sorted_assign_list)

            # 랜덤 배정 start
            for i in range(len(professor_sorted_assign_list)):
                idx = 0
                overlap_stack = 0
                # 요일 비지 않았으면 랜덤 배정 x
                if professor_sorted_assign_list[i][4] != '':
                    continue

                # 랜덤
                for j in range(len(under_data_sort_list)):
                    # 새로오신 교수님은 데이터셋에 없음... 그래서 아쉽지만 continue....
                    if len(under_data_sort_list[j]) == 0:
                        continue
                    if professor_sorted_assign_list[i][0] != under_data_sort_list[j][0][0]:
                        continue
                    # professor_arr = []
                    # for k in range(len(under_data_sort_list[j])):
                        # 과목 일치하는게 있으면 과목 일치하는 것으로만 random
                        # if professor_sorted_assign_list[i][1] == under_data_sort_list[j][k][1]:
                        #     professor_arr.append(under_data_sort_list[j][k])
                    # 과목 일치하는 게 있으면
                    # if len(professor_arr) != 0:
                    #     idx = random.randrange(0, len(professor_arr))
                    #     class_arr = professor_arr[idx]
                    # # 과목 일치하는 게 없으면
                    # else:
                    idx = random.randrange(0, len(under_data_sort_list[j]))
                    class_arr = under_data_sort_list[j][idx]
                    # print("class_arr")
                    # print(class_arr)
                    # for k in range(0, 10):
                    #     if class_arr[4]
                    diff_arr = []
                    if class_arr[1] != professor_sorted_assign_list[i][1] and class_arr[1] == '수학적프로그래밍':
                        overlap_stack = 1
                        break
                    diff_arr = [class_arr[0], class_arr[4], lesson_dictionary[professor_sorted_assign_list[i][1]]]
                    for k in class_arr[3].split(','):
                        if "월" in class_arr[2]:
                            for l in range(len(lesson_assign_arr[int(k)][0])):
                                for m in range(len(diff_arr)):
                                    if lesson_assign_arr[int(k)][0][l][m] == diff_arr[m]:
                                        overlap_stack = 1
                                    if overlap_stack == 1:
                                        break
                                if overlap_stack == 1:
                                    break
                            lesson_assign_arr[int(k)][0].append(diff_arr)
                        if "화" in class_arr[2]:
                            for l in range(len(lesson_assign_arr[int(k)][1])):
                                for m in range(len(diff_arr)):
                                    if lesson_assign_arr[int(k)][1][l][m] == diff_arr[m]:
                                        overlap_stack = 1
                                    if overlap_stack == 1:
                                        break
                                if overlap_stack == 1:
                                    break
                            lesson_assign_arr[int(k)][1].append(diff_arr)
                        if "수" in class_arr[2]:
                            for l in range(len(lesson_assign_arr[int(k)][2])):
                                for m in range(len(diff_arr)):
                                    if lesson_assign_arr[int(k)][2][l][m] == diff_arr[m]:
                                        overlap_stack = 1
                                    if overlap_stack == 1:
                                        break
                                if overlap_stack == 1:
                                    break
                            lesson_assign_arr[int(k)][2].append(diff_arr)
                        if "목" in class_arr[2]:
                            for l in range(len(lesson_assign_arr[int(k)][3])):
                                for m in range(len(diff_arr)):
                                    if lesson_assign_arr[int(k)][3][l][m] == diff_arr[m]:
                                        overlap_stack = 1
                                    if overlap_stack == 1:
                                        break
                                if overlap_stack == 1:
                                    break
                            lesson_assign_arr[int(k)][3].append(diff_arr)
                        if "금" in class_arr[2]:
                            for l in range(len(lesson_assign_arr[int(k)][4])):
                                for m in range(len(diff_arr)):
                                    if lesson_assign_arr[int(k)][4][l][m] == diff_arr[m]:
                                        overlap_stack = 1
                                    if overlap_stack == 1:
                                        break
                                if overlap_stack == 1:
                                    break
                            if overlap_stack == 1:
                                break
                            lesson_assign_arr[int(k)][4].append(diff_arr)
                        if overlap_stack == 1:
                            break
                    if overlap_stack == 1:
                        break
                if overlap_stack == 1:
                    random_denied_list.append(professor_sorted_assign_list[i])
                else:
                    professor_sorted_assign_list[i][4] = class_arr[2]
                    professor_sorted_assign_list[i][5] = class_arr[3]
                    professor_sorted_assign_list[i][6] = diff_arr[1]
            print('lesson_assign_arr')
            for i in range(len(lesson_assign_arr)):
                print(lesson_assign_arr[i])
            # print('random_denied_list')
            # print(random_denied_list)
            print('professor_sorted_assign_list')
            print(professor_sorted_assign_list)
            lesson_assign_under_list = professor_sorted_assign_list
            print('lesson_assign_under_list')
            print(lesson_assign_under_list)

            # 학부 랜덤 배정
        else:
            # 교수님 순번별로 다시 sort
            professor_sorted_assign_list = []
            random_denied_list = []
            for i in range(len(professor_list)):
                for j in range(len(lesson_assign_list_dae)):
                    if professor_dictionary[i] == lesson_assign_list_dae[j][0]:
                        professor_sorted_assign_list.append(lesson_assign_list_dae[j])
            print(professor_sorted_assign_list)

            # print(lesson_assign_under_list)
            for i in range(len(professor_sorted_assign_list)):
                check_arr = []
                if professor_sorted_assign_list[i][4] == '':
                    continue
                for j in professor_sorted_assign_list[i][5].split(","):  # 12,13,14,15,16
                    check_arr = [professor_sorted_assign_list[i][0], professor_sorted_assign_list[i][6],
                                 lesson_dictionary[professor_sorted_assign_list[i][1]]]
                    print(check_arr)
                    if "월" in professor_sorted_assign_list[i][4]:
                        lesson_assign_arr[int(j)][0].append(check_arr)
                    if "화" in professor_sorted_assign_list[i][4]:
                        lesson_assign_arr[int(j)][1].append(check_arr)
                    if "수" in professor_sorted_assign_list[i][4]:
                        lesson_assign_arr[int(j)][2].append(check_arr)
                    if "목" in professor_sorted_assign_list[i][4]:
                        lesson_assign_arr[int(j)][3].append(check_arr)
                    if "금" in professor_sorted_assign_list[i][4]:
                        lesson_assign_arr[int(j)][4].append(check_arr)
                print(lesson_assign_arr)

            # 랜덤 배정 start
            for i in range(len(professor_sorted_assign_list)):
                idx = 0
                overlap_stack = 0
                # 요일 비지 않았으면 랜덤 배정 x
                if professor_sorted_assign_list[i][4] != '':
                    continue

                # 랜덤
                for j in range(len(under_data_sort_list)):
                    # 새로오신 교수님은 데이터셋에 없음... 그래서 아쉽지만 continue....
                    if len(under_data_sort_list[j]) == 0:
                        continue
                    if professor_sorted_assign_list[i][0] != under_data_sort_list[j][0][0]:
                        continue
                    professor_arr = []
                    for k in range(len(under_data_sort_list[j])):
                        # 과목 일치하는게 있으면 과목 일치하는 것으로만 random
                        if professor_sorted_assign_list[i][1] == under_data_sort_list[j][k][1]:
                            professor_arr.append(under_data_sort_list[j][k])
                    class_arr = []
                    # 과목 일치하는 게 있으면
                    if len(professor_arr) != 0:
                        idx = random.randrange(0, len(professor_arr))
                        class_arr = professor_arr[idx]
                    # 과목 일치하는 게 없으면
                    else:
                        idx = random.randrange(0, len(under_data_sort_list[j]))
                        class_arr = under_data_sort_list[j][idx]
                    print("class_arr")
                    print(class_arr)
                    # for k in range(0, 10):
                    #     if class_arr[4]
                    diff_arr = []
                    diff_arr = [class_arr[0], class_arr[4], lesson_dictionary[professor_sorted_assign_list[i][1]]]
                    for k in class_arr[3].split(','):
                        if "월" in class_arr[2]:
                            for l in range(len(lesson_assign_arr[int(k)][0])):
                                for m in range(len(diff_arr)):
                                    if lesson_assign_arr[int(k)][0][l][m] == diff_arr[m]:
                                        overlap_stack = 1
                                    if overlap_stack == 1:
                                        break
                                if overlap_stack == 1:
                                    break
                            lesson_assign_arr[int(k)][0].append(diff_arr)
                        if "화" in class_arr[2]:
                            for l in range(len(lesson_assign_arr[int(k)][1])):
                                for m in range(len(diff_arr)):
                                    if lesson_assign_arr[int(k)][1][l][m] == diff_arr[m]:
                                        overlap_stack = 1
                                    if overlap_stack == 1:
                                        break
                                if overlap_stack == 1:
                                    break
                            lesson_assign_arr[int(k)][1].append(diff_arr)
                        if "수" in class_arr[2]:
                            for l in range(len(lesson_assign_arr[int(k)][2])):
                                for m in range(len(diff_arr)):
                                    if lesson_assign_arr[int(k)][2][l][m] == diff_arr[m]:
                                        overlap_stack = 1
                                    if overlap_stack == 1:
                                        break
                                if overlap_stack == 1:
                                    break
                            lesson_assign_arr[int(k)][2].append(diff_arr)
                        if "목" in class_arr[2]:
                            for l in range(len(lesson_assign_arr[int(k)][3])):
                                for m in range(len(diff_arr)):
                                    if lesson_assign_arr[int(k)][3][l][m] == diff_arr[m]:
                                        overlap_stack = 1
                                    if overlap_stack == 1:
                                        break
                                if overlap_stack == 1:
                                    break
                            lesson_assign_arr[int(k)][3].append(diff_arr)
                        if "금" in class_arr[2]:
                            for l in range(len(lesson_assign_arr[int(k)][4])):
                                for m in range(len(diff_arr)):
                                    if lesson_assign_arr[int(k)][4][l][m] == diff_arr[m]:
                                        overlap_stack = 1
                                    if overlap_stack == 1:
                                        break
                                if overlap_stack == 1:
                                    break
                            if overlap_stack == 1:
                                break
                            lesson_assign_arr[int(k)][4].append(diff_arr)
                        if overlap_stack == 1:
                            break
                    if overlap_stack == 1:
                        break
                if overlap_stack == 1:
                    continue
                    # random_denied_list.append(professor_sorted_assign_list[i])
                else:
                    professor_sorted_assign_list[i][4] = class_arr[2]
                    professor_sorted_assign_list[i][5] = class_arr[3]
                    professor_sorted_assign_list[i][6] = diff_arr[1]


            print('lesson_assign_arr')
            print(lesson_assign_arr)
            print('random_denied_list')
            print(random_denied_list)
            lesson_assign_under_list = professor_sorted_assign_list

        self.tableData()
        count -= 1
        self.randomAssign()


    # 저장 메소드
    def saveInfo(self):
        global lesson_assign_under_df, lesson_assign_df_dae
        global_funtion().message_box_2(QMessageBox.Question, "확인", "작성내용을 저장하시겠습니까?", "예", "아니오")
        self.jsonLoad()
        if configData['message'] == 'Y':
            if radioBtn2.isChecked():  # 학부 라디오 버튼이 체크 되어있을 때, 학부 파일 lesson_assign_under_list 를 데이터프레임으로 저장
                lesson_assign_under_df = pd.DataFrame(lesson_assign_under_list, columns=lesson_assign_under_list_col)
                lesson_assign_under_df.to_excel('data/lesson_assign_under.xlsx', index=False)
                print("lesson_assign_under_df", lesson_assign_under_df)
                lesson_assign_under_df.to_excel('data/lesson_assign_under_tableview.xlsx',
                                  index=False)  # dataframe excel 저장
                global_funtion().message_box_1(QMessageBox.Information, "정보", "저장되었습니다", "확인")
            else:  # 대학원 라디오 버튼 체크시, 대학원 파일 lesson_assign_list_dae 를 데이터프레임으로 저장
                lesson_assign_df_dae = pd.DataFrame(lesson_assign_list_dae, columns=lesson_assign_list_col_dae)
                lesson_assign_df_dae.to_excel('data/lesson_assign_dae.xlsx', index=False)
                print("lesson_assign_df_dae", lesson_assign_df_dae)
                lesson_assign_df_dae.to_excel('data/lesson_assign_grad_tableview.xlsx',
                                                index=False)  # dataframe excel 저장
                global_funtion().message_box_1(QMessageBox.Information, "정보", "저장되었습니다", "확인")

    # 시간표 미리보기
    def showTimetable(self):
        global radioBtn, radioBtn2, under_timetable_list, grad_timetable_list
        if radioBtn2.isChecked():   # 학부 라디오버튼 체크시
            Ui_ShowUnderTimetable().exec_()
        elif radioBtn.isChecked():  # 대학원 라디오버튼 체크시
            grad_timetable_list = lesson_assign_list_dae
            Ui_ShowGradTimetable().exec_()

    # 추가,수정, 삭제된 사항을 table에 새로 띄우기
    def tableData(self):
        global df, df2
        self.tableWidget.clear()        # 테이블위젯 초기화
        for i in range(0,8):            # 데이터 7개: 교수명 강의명 분반 분류 요일 시작시간 종료시간 강의실명
            item = QTableWidgetItem()   # 교수
            item.setText(header_arr[i])
            self.tableWidget.setHorizontalHeaderItem(i, item)
            self.tableWidget.horizontalHeader().setSectionResizeMode(i, QHeaderView.Stretch)
        print('a') #확인용

        if self.radioButton.isChecked():    # 대학원 라디오버튼 체크시
            self.comboBox_2.clear()         # 대학원 수업명 콤보박스 초기화
            grad_lesson_arr = []            # 대학원 수업명 담을 빈 array
            for i in range(len(lesson_list)):
                if str(lesson_list[i][2]) != str(semester_str):     # 현재 학기와 lesson_list 학기와 다르면 continue -> 같은 학기 수업만
                    continue
                if str(lesson_list[i][3]) != '대학원':               # 대상이 대학원이 아니면 continue -> 대학원 수업만
                    continue
                grad_lesson_arr.append(lesson_list[i][1])           # 해당 학기의 대학원 수업명을 grad_lesson_arr에 append
            self.comboBox_2.addItems(grad_lesson_arr)               # 수업명 콤보박스에 추가
            self.tableWidget.setRowCount(0)

            # 대학원 파일을 불러온다
            temp_lesson_assign_df_dae = pd.DataFrame(lesson_assign_list_dae, columns=lesson_assign_list_col_dae)
            df = temp_lesson_assign_df_dae
            df.replace(np.NaN, '', inplace=True)
            df = df.reset_index()[['교수명', '강좌명', '분반', '분류', '요일', '시간ID', '강의실명']]
            df['분반'] = df['분반'].astype(str).apply(lambda x: x.replace('.0', ''))
            df['시간ID'] = df['시간ID'].astype(str)
            # 시간 id 중 가장 작은 숫자에 해당하는 time 시작시간으로 불러오기
            start = time_df.iloc[df['시간ID'].str.split(',').str[0]]['시작시간']
            start = start.reset_index()['시작시간']
            df = pd.concat([df, start], axis=1)
            # 시간 id 중 가장 큰 숫자에 해당하는 time 종료시간으로 불러오기
            finish = time_df.iloc[df['시간ID'].str.split(',').str[-1]]['종료시간']
            finish = finish.reset_index()['종료시간']
            df = pd.concat([df, finish], axis=1)
            df = df[header_arr]
            # print('df')
            # print(df)
            self.tableWidget.setRowCount(len(df))
            # 테이블 위젯에 데이터 집어넣기
            for i in range(len(df)):
                # row = self.tableWidget.rowCount()
                # self.tableWidget.insertRow(row)
                for j in range(len(df.columns)):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(df.iloc[i, j])))

        elif self.radioButton_2.isChecked():    # 학부 라디오버튼 체크시
                self.comboBox_2.clear()         # 학부 수업명 콤보박스 초기화
                under_lesson_arr = []           # 학부 수업명 담을 빈 array
                for i in range(len(lesson_list)):
                    if str(lesson_list[i][2]) != str(semester_str):     # 해당 학기가 아니면 continue -> 해당 학기만
                        continue
                    if str(lesson_list[i][3]) != '학부':                 # 학부 수업이 아니면 continue -> 학부 수업만
                        continue
                    under_lesson_arr.append(lesson_list[i][1])          # 해당 학기의 학부 수업 이름을 under_lesson_arr에 append
                self.comboBox_2.addItems(under_lesson_arr)              # 강의명 콤보박스에 추가
                self.tableWidget.setRowCount(0)

                # 학부 파일을 불러온다
                lesson_assign_under_df = pd.DataFrame(lesson_assign_under_list, columns=lesson_assign_under_list_col)
                df2 = lesson_assign_under_df
                df2.replace(np.NaN, '', inplace=True)
                df2 = df2.reset_index()[['교수명', '강좌명', '분반', '분류', '요일', '시간ID', '강의실명']]
                df2['분반'] = df2['분반'].astype(str).apply(lambda x: x.replace('.0', ''))
                df2['시간ID'] = df2['시간ID'].astype(str)
                # 시간 id 중 가장 작은 숫자에 해당하는 time 시작시간으로 불러오기
                start2 = time_df.iloc[df2['시간ID'].str.split(',').str[0]]['시작시간']
                start2 = start2.reset_index()['시작시간']
                df2 = pd.concat([df2, start2], axis=1)
                # 종료 id 중 가장 큰 숫자에 해당하는 time 종료시간으로 불러오기
                finish2 = time_df.iloc[df2['시간ID'].str.split(',').str[-1]]['종료시간']
                finish2 = finish2.reset_index()['종료시간']
                df2 = pd.concat([df2, finish2], axis=1)
                df2 = df2[header_arr]
                # print('df2')
                # print(df2)
                # 테이블 위젯에 데이터 집어넣기
                self.tableWidget.setRowCount(len(df2))
                for i in range(len(df2)):
                    # row = self.tableWidget.rowCount()
                    # self.tableWidget.insertRow(row)
                    for j in range(len(df2.columns)):
                        self.tableWidget.setItem(i, j, QTableWidgetItem(str(df2.iloc[i, j])))








if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Dialog = QDialog()
    ui = Ui_Dialog()
    ui.setupUi()
    ui.show()
    app.exec_()
