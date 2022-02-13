# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import pandas as pd
# merge 왜 안댕~~~
from imports import *
from dialog import *
from data_load import *
import json
import os

# 사용자 지정 창 만들기
class Ui_Lesson_Assign(QDialog):
    def __init__(self):
        super().__init__()
        self.get_init_data()
        self.setupUi()

    # 데이터 불러오기
    def get_init_data(self):
        global tool_button_arr, configData
            # 버튼 관련 설정
        tool_button_arr = [
            ["입력", "img/add_person.png",40, 40, self.writeInfo],
            ["수정", "img/shuffle.png", 40, 40, self.changeInfo],
            ["배정", "img/floppy-disk.png", 40, 40, self.saveInfo],
            ["삭제", "img/delete.png", 40, 40, self.deleteInfo]
        ]

        # 시작, 종료시간 combobox 정보
        global time_start_arr, time_end_arr
        time_start_arr = [""]
        time_end_arr = [""]
        for i in range(len(time_list)):
            time_start_arr.append(time_list[i][1])
            time_end_arr.append(time_list[i][2])

        # with open("info_type.json", "r") as info:
        #     configData = json.load(info)

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

        # 교수
        self.label_8 = QLabel(self.gridLayoutWidget)
        self.label_8.setAlignment(Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 0, 0, 1, 1)
        # 강의
        self.label_9 = QLabel(self.gridLayoutWidget)
        self.label_9.setAlignment(Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 0, 1, 1, 1)
        # 분반
        self.label_6 = QLabel(self.gridLayoutWidget)
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 0, 2, 1, 1)
        # 분류
        self.label_16 = QLabel(self.gridLayoutWidget)
        self.label_16.setAlignment(Qt.AlignCenter)
        self.label_16.setObjectName("label_6")
        self.label_16.setText("분류")
        self.gridLayout_2.addWidget(self.label_16, 0, 3, 1, 1)
        # 요일
        self.label_10 = QLabel(self.gridLayoutWidget)
        self.label_10.setAlignment(Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 2, 0, 1, 1)
        # 시작시간
        self.label_7 = QLabel(self.gridLayoutWidget)
        self.label_7.setAlignment(Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 2, 1, 1, 1)
        # 종료시간
        self.label_12 = QLabel(self.gridLayoutWidget)
        self.label_12.setAlignment(Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 2, 2, 1, 1)
        # 강의실
        self.label_13 = QLabel(self.gridLayoutWidget)
        self.label_13.setAlignment(Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_13, 2, 3, 1, 1)

        # 교수 콤보박스
        self.comboBox = QComboBox(self.gridLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout_2.addWidget(self.comboBox, 1, 0, 1, 1)
        self.comboBox.addItems(professor_df['성명'])
        # 강의 콤보박스
        self.comboBox_2 = QComboBox(self.gridLayoutWidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.gridLayout_2.addWidget(self.comboBox_2, 1, 1, 1, 1)
        # 분반
        self.lineEdit_8 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout_2.addWidget(self.lineEdit_8, 1, 2, 1, 1)
        # 분류 콤보박스
        self.comboBox_5 = QComboBox(self.gridLayoutWidget)
        self.comboBox_5.setObjectName("comboBox_3")
        self.gridLayout_2.addWidget(self.comboBox_5, 1, 3, 1, 1)
        self.comboBox_5.addItems(["전공기초", "전공선택", "전공필수", "전공", "교양선택"])
        # 요일
        self.lineEdit_9 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.gridLayout_2.addWidget(self.lineEdit_9, 3, 0, 1, 1)
        # 시작 콤보박스
        self.comboBox_3 = QComboBox(self.gridLayoutWidget)
        self.comboBox_3.setObjectName("comboBox_3")
        self.gridLayout_2.addWidget(self.comboBox_3, 3, 1, 1, 1)
        self.comboBox_3.addItems(time_start_arr)
        # 종료 콤보박스
        self.comboBox_4 = QComboBox(self.gridLayoutWidget)
        self.comboBox_4.setObjectName("comboBox_4")
        self.gridLayout_2.addWidget(self.comboBox_4, 3, 2, 1, 1)
        self.comboBox_4.addItems(time_end_arr)
        # 강의실
        self.lineEdit_11 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.gridLayout_2.addWidget(self.lineEdit_11, 3, 3, 1, 1)




        # 테이블 위젯 만들기( 목록 띄우기 위함 )
        self.tableWidget =QTableWidget(self.groupBox_2)
        self.tableWidget.setGeometry(QRect(30, 150, 571, 440))
        self.tableWidget.setObjectName("tableWidget")
        # 행과 열 만들기
        self.tableWidget.setColumnCount(8)
        # 테이블위젯 이름 넣으려고 만듬
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
        self.verticalLayoutWidget.setGeometry(QRect(640, 105, 111, 451))
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

    # 대학원 라디오 버튼 연결 ( 대학원 데이터 불러오기 )
    def onClicked(self):
        global df, radioBtn
        radioBtn=self.sender()
        if radioBtn.isChecked():
            self.comboBox_2.clear()
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
            df = lesson_assign_df[lesson_assign_df['대상학과'].str.contains('대학원')]
            df = df.reset_index()[['교수명','강좌명','분반','분류','요일','시간ID','강의실명']]
            # 시간 id 중 가장 작은 숫자에 해당하는 time 시작시간으로 불러오기
            start=time_df.iloc[df['시간ID'].str.split(',').str[0]]['시작시간']
            start=start.reset_index()['시작시간']
            df=pd.concat([df, start], axis=1)
            # 시간 id 중 가장 큰 숫자에 해당하는 time 종료시간으로 불러오기
            finish = time_df.iloc[df['시간ID'].str.split(',').str[-1]]['종료시간']
            finish = finish.reset_index()['종료시간']
            df = pd.concat([df, finish], axis=1)
            df=df[header_arr]
            print(df)
            print(len(df))
            print(len(df.columns))
            # 테이블 위젯에 데이터 집어넣기
            for i in range(len(df)):
                row = self.tableWidget.rowCount()
                self.tableWidget.insertRow(row)
                for j in range(len(df.columns)):
                     self.tableWidget.setItem(i,j,QTableWidgetItem(str(df.iloc[i,j])))

    # 학부 라디오 버튼 연결 ( 학부 데이터 불러오기 )
    def onClicked2(self):
        global df2, radioBtn2
        radioBtn2=self.sender()
        if radioBtn2.isChecked():

            # under_lesson_arr = []
            # for i in range(len(lesson_list)):
            #     if lesson_list[i][]
            self.comboBox_2.clear()
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
            df2 = lesson_assign_df[~lesson_assign_df['대상학과'].str.contains('대학원')]
            df2 = df2.reset_index()[['교수명', '강좌명','분반', '분류', '요일', '시간ID', '강의실명']]
            # 시간 id 중 가장 작은 숫자에 해당하는 time 시작시간으로 불러오기
            start2 = time_df.iloc[df2['시간ID'].str.split(',').str[0]]['시작시간']
            start2 = start2.reset_index()['시작시간']
            df2 = pd.concat([df2, start2], axis=1)
            # 종료 id 중 가장 큰 숫자에 해당하는 time 종료시간으로 불러오기
            finish2 = time_df.iloc[df2['시간ID'].str.split(',').str[-1]]['종료시간']
            finish2 = finish2.reset_index()['종료시간']
            df2 = pd.concat([df2, finish2], axis=1)
            df2 = df2[header_arr]
            # print(df2)
            # 테이블 위젯에 데이터 집어넣기
            for i in range(len(df2)):
                row = self.tableWidget.rowCount()
                self.tableWidget.insertRow(row)
                for j in range(len(df2.columns)):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(df2.iloc[i, j])))

    # tableClick Event ( 테이블 위젯 클릭시 창에 정보 띄우기 )
    def tableClick(self):
        global curr_row, curr_col
        curr_row = self.tableWidget.currentRow()  # 테이블 위젯에서 선택한 행 인덱스
        curr_col = self.tableWidget.currentColumn()  # 테이블 위젯에서 선택한 열 인덱스

        if radioBtn2.isChecked():  # 학부 라디오 버튼 체크시
            df2_list = df2.values.tolist()
            item = df2_list[curr_row]
        else:  # 대학원 라디오 버튼 체크시
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


    def saveInfo(self):     # 배정 메소드
        print("랜덤배정")


    def deleteInfo(self):   # 삭제 메소드
        global_funtion().message_box_2(QMessageBox.Question, "확인", "작성내용을 삭제하시겠습니까?", "예", "아니오")
        self.jsonLoad()
        if configData['message'] == 'Y':
            # 테이블 위젯에서 클릭한 셀 내용 삭제
            self.tableWidget.takeItem(curr_row, curr_col)
            count = 0
            # lesson_assign.xlsx 에도 내용 삭제 --- 학부와 대학원 정보를 나눠서 불러온 다음 삭제해야함
            if radioBtn2.isChecked():               # 학부 라디오 버튼 체크시
                df2.iloc[curr_row, curr_col] = ""   # 학부 파일 df2 에서 해당 내용 삭제
                # 아이디어 : lesson_assign_list 에서 학부 수업 찾아서 count 세어서 curr_row으로 처리
                for i in range(len(lesson_assign_list)):
                    if '대학원' not in lesson_assign_list[i][8]:
                        count = count + 1           # count 값은 lesson_assign_list 중 학부 몇 번째임을 나타냄
                        if count == curr_row + 1:
                            lesson_assign_list[i][curr_col + 1] = ""
                            break
                print("학부 삭제")

            else:  # 대학원 라디오 버튼 체크시
                df.iloc[curr_row, curr_col] = ""  # 대학원 파일 df 에서 해당 내용 삭제
                for i in range(len(lesson_assign_list)):
                    if '대학원' in lesson_assign_list[i][8]:
                        count = count + 1           # count 값은 lesson_assign_list 중 대학원 몇 번째임을 나타냄
                        if count == curr_row + 1:
                            lesson_assign_list[i][curr_col + 1] = ""
                            break
                print("대학원 삭제")

            lesson_assign_df = pd.DataFrame(lesson_assign_list, columns=lesson_assign_list_col)
            lesson_assign_df.to_excel('data/lesson_assign.xlsx', index=False)  # dataframe excel 저장

        elif configData['message'] == 'N':
            print("삭제 안함")
            return

        #self.close()
        #self.__init__()
        #self.exec_()

    # 입력하기
    def writeInfo(self):
        global write_data , lesson_assign_df
        # array에 현재 해당하는 교수, 강의명 입력
        write_data=[]
        write_data.append(self.comboBox.currentText())
        write_data.append(self.comboBox_2.currentText())
        # 종료 index에서 시작 Index까지의 값 담기
        time = []
        start = self.comboBox_3.currentIndex()
        end = self.comboBox_4.currentIndex()
        for i in range(start+1,end+2):
            time.append(i)
        write_data.append(str(time)[1:-1])
        # print(write_data)
        write_data = pd.DataFrame([write_data], columns=['교수명', '강좌명','시간ID'])

        lesson_assign_df=pd.concat([lesson_assign_df,write_data] , axis=0)
        lesson_assign_df.to_excel('data/lesson_assign.xlsx', index=False)
        global_funtion().message_box_1(QMessageBox.Information, "정보", "입력되었습니다", "확인")

        # print(time)
        # #print(write_data)
        # #print(lesson_assign_df)


    def changeInfo(self):
        print("")

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Dialog = QDialog()
    ui = Ui_Dialog()
    ui.setupUi()
    ui.show()
    app.exec_()
