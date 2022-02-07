# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

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
            ["입력", "img/add_person.png",30, 30, self.writeInfo],
            ["수정", "img/shuffle.png", 30, 30, self.changeInfo],
            ["저장", "img/floppy-disk.png", 30, 30, self.saveInfo],
            ["삭제", "img/delete.png", 30, 30, self.deleteInfo]
        ]

        with open("info_type.json", "r") as info:
            configData = json.load(info)

    # 화면 출력
    def setupUi(self):
        self.setObjectName("Dialog")
        self.resize(618, 476)

        # 그룹박스 만들기
        self.groupBox = QGroupBox(self)
        self.groupBox.setGeometry(QRect(50, 40, 521, 61))

        # 그룹박스 내 layout -> 라디오 버튼 넣으려고
        self.horizontalLayoutWidget = QWidget(self.groupBox)
        self.horizontalLayoutWidget.setGeometry(QRect(20, 30, 491, 22))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        # 라디오 버튼 2개 만들기
        self.radioButton = QRadioButton(self.horizontalLayoutWidget)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout.addWidget(self.radioButton, 0, Qt.AlignHCenter)
        self.radioButton_2 = QRadioButton(self.horizontalLayoutWidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout.addWidget(self.radioButton_2, 0, Qt.AlignHCenter)

        # 두번째 그룹박스 만들기
        self.groupBox_2 = QGroupBox(self)
        self.groupBox_2.setGeometry(QRect(50, 110, 521, 351))

        # 입력창 만드려고 그룹박스 내 그리드위젯 만들기
        self.gridLayoutWidget = QWidget(self.groupBox_2)
        self.gridLayoutWidget.setGeometry(QRect(20, 30, 491, 51))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        # 교수
        self.label_8 = QLabel(self.gridLayoutWidget)
        self.label_8.setAlignment(Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 0, 0, 1, 1)
        # 요일
        self.label_10 = QLabel(self.gridLayoutWidget)
        self.label_10.setAlignment(Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 0, 3, 1, 1)

        # 강의
        self.label_9 = QLabel(self.gridLayoutWidget)
        self.label_9.setAlignment(Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 0, 1, 1, 1)
        # 강의실
        self.label_7 = QLabel(self.gridLayoutWidget)
        self.label_7.setAlignment(Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 0, 4, 1, 1)
        # 시간
        self.label_6 = QLabel(self.gridLayoutWidget)
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 0, 2, 1, 1)

        self.lineEdit_9 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.gridLayout_2.addWidget(self.lineEdit_9, 1, 3, 1, 1)

        self.lineEdit_7 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout_2.addWidget(self.lineEdit_7, 1, 1, 1, 1)

        self.lineEdit_10 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.gridLayout_2.addWidget(self.lineEdit_10, 1, 4, 1, 1)

        self.lineEdit_8 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout_2.addWidget(self.lineEdit_8, 1, 2, 1, 1)

        self.lineEdit_6 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout_2.addWidget(self.lineEdit_6, 1, 0, 1, 1, Qt.AlignHCenter)

        # 테이블 위젯 만들기
        self.tableWidget =QTableWidget(self.groupBox_2)
        self.tableWidget.setGeometry(QRect(20, 90, 401, 251))
        self.tableWidget.setObjectName("tableWidget")
        # 행과 열 만들기
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(50)
        # 테이블위젯 이름 넣으려고 만듬
        item = QTableWidgetItem() # 교수
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QTableWidgetItem() # 강의
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QTableWidgetItem() # 시간
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QTableWidgetItem() # 요일
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item =QTableWidgetItem() # 강의실
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(77)

        # 사용자 지정 배정 라벨
        self.label_11 = QLabel()
        self.label_11.setGeometry(QRect(260, 20, 151, 16))
        self.label_11.setObjectName("label_11")

        self.verticalLayoutWidget = QWidget(self.groupBox_2)
        self.verticalLayoutWidget.setGeometry(QRect(455, 90, 81, 251))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        for i in range(len(tool_button_arr)):
            self.toolButton = QToolButton(self.verticalLayoutWidget)
            global_funtion.tool_button_setting_widget(self, self.toolButton, self.verticalLayout, tool_button_arr[i])


        # 텍스트 출력
        self.retranslateUi()
        QMetaObject.connectSlotsByName(self)

        # 라디오 버튼 연결시키기
        self.radioButton.toggled.connect(self.onClicked)
        self.radioButton_2.toggled.connect(self.onClicked2)

    # 첫번째 라디오 버튼 연결 ( 대학원 데이터 불러오기 )
    def onClicked(self):
        global df
        radioBtn=self.sender()
        if radioBtn.isChecked():
            self.tableWidget.clear()
            df=[]
            df = pd.read_excel('/Users/seojung/Desktop/시간표 정리/2021_2.xlsx')
            df = df[df['대상학과'].str.contains('대학원')]
            df['요일'] = df['강의시간'].str.findall('[ㄱ-ㅣ가-힣]+')
            df = df[['성명', '교과목명','강의시간','강의실','교과구분']]
            #df = df.drop('Unnamed: 0',axis=1)
            print(df)
            print(len(df))
            print(len(df.columns))
            #df.to_csv("tlqkf.csv")
            for i in range(len(df)):
                for j in range(len(df.columns)):
                     self.tableWidget.setItem(i,j,QTableWidgetItem(df.iloc[i,j]))

    # 두번째 라디오 버튼 연결 ( 학부 데이터 불러오기 )
    def onClicked2(self):
        global df2
        radioBtn2=self.sender()
        if radioBtn2.isChecked():
            self.tableWidget.clear()
            df2 = []
            df2 = pd.read_excel('/Users/seojung/Desktop/시간표 정리/2021_2.xlsx')
            df2 = df2[~df2['대상학과'].str.contains('대학원')]
            df2['요일'] = df2['강의시간'].str.findall('[ㄱ-ㅣ가-힣]+')
            df2 = df2[['성명', '교과목명', '강의시간', '강의실', '교과구분']]
            #print(data2)
            for i in range(len(df2)):
                for j in range(len(df2.columns)):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(df2.iloc[i, j]))

    # 텍스트 출력
    def retranslateUi(self):
        _translate = QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Dialog"))
        self.radioButton.setText(_translate("Dialog", "대학원"))
        self.radioButton_2.setText(_translate("Dialog", "학부"))
        self.label_6.setText(_translate("Dialog", "시간"))
        self.label_7.setText(_translate("Dialog", "강의실"))
        self.label_8.setText(_translate("Dialog", "교수"))
        self.label_9.setText(_translate("Dialog", "강의"))
        self.label_10.setText(_translate("Dialog", "요일"))
        self.label_11.setText(_translate("Dialog", "사용자지정 배정"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "교수"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "강의"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "시간"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "요일"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "강의실"))
        # self.pushButton_5.setText(_translate("Dialog", "입력"))
        # self.pushButton_2.setText(_translate("Dialog", "수정"))
        # self.pushButton_3.setText(_translate("Dialog", "삭제"))
        # self.pushButton_4.setText(_translate("Dialog", "저장"))

    def saveInfo(self):
        print("")

    def deleteInfo(self):
        print("")

    def writeInfo(self):
        print("")

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
