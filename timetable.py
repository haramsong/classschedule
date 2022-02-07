# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '1.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


#from PyQt5 import QtCore, QtGui, QtWidgets

from dialog import *
from data_load import *
import json
from users_lesson_assign import *

# 시간표 창 만들기
class Ui_Timetable(QDialog):
    def __init__(self):
        super().__init__()
        self.get_init_data()
        self.setupUi()

    # 데이터 불러오기
    def get_init_data(self):
        global tool_button_arr, configData
        # 버튼 관련 설정
        tool_button_arr = [
            ["사용자 지정", "img/edit.png", 50, 50, self.lesson_assign],
            ["삭제", "img/delete.png", 50, 50, self.delete]
        ]

        # json load
        with open("info_type.json", "r") as info:
            configData = json.load(info)

    # 화면 출력
    def setupUi(self):
        self.setObjectName("Dialog")
        self.resize(548, 599)

        # 테이블 위젯 설정( 시간표)
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setGeometry(QRect(160, 50, 381, 526))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(21)

        # 시간대 표시
        item = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, item)
        item = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, item)
        item = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, item)
        item = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, item)
        item = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, item)
        item = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(15, item)
        item = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(16, item)
        item = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(17, item)
        item = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(18, item)
        item = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(19, item)
        item = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(20, item)

        # 요일 입력
        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)

        # 테이블 위젯 행렬 사이즈 조절
        self.tableWidget.horizontalHeader().setDefaultSectionSize(60)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(15)
        self.tableWidget.verticalHeader().setDefaultSectionSize(5)

        # 제목 설정
        self.horizontalLayoutWidget = QWidget(self)
        self.horizontalLayoutWidget.setGeometry(QRect(0, -10, 551, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(80, 10, 80, 20)
        self.horizontalLayout.setObjectName("horizontalLayout")

        # 라벨 설정
        self.label_4 = QLabel(self.horizontalLayoutWidget)  # 2022
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        global_funtion.fontSetting(self, self.label_4, "8H", 24, " ")

        self.label = QLabel(self.horizontalLayoutWidget) # 학년도
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        global_funtion.fontSetting(self, self.label, "8H", 24, " ")

        self.label_5 = QLabel(self.horizontalLayoutWidget) # 1
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        global_funtion.fontSetting(self, self.label_5, "8H", 24, " ")

        self.label_2 = QLabel(self.horizontalLayoutWidget) # 학기
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        global_funtion.fontSetting(self, self.label_2, "8H", 24, " ")

        self.label_3 = QLabel(self.horizontalLayoutWidget)  # 시간표
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        global_funtion.fontSetting(self, self.label_3, "8H", 24, " ")

        # 버튼 설정
        self.verticalLayoutWidget = QWidget(self)
        self.verticalLayoutWidget.setGeometry(QRect(60, 80, 160, 420))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        # self.pushButton = QPushButton(self.verticalLayoutWidget)
        # self.pushButton.setObjectName("pushButton")
        # self.verticalLayout.addWidget(self.pushButton)
        # self.pushButton_2 = QPushButton(self.verticalLayoutWidget)
        # self.pushButton_2.setObjectName("pushButton_2")
        # self.verticalLayout.addWidget(self.pushButton_2)
        # 버튼 생성
        for i in range(len(tool_button_arr)):
            self.toolButton = QToolButton(self.verticalLayoutWidget)
            global_funtion.tool_button_setting_widget(self, self.toolButton, self.verticalLayout, tool_button_arr[i])

        # 텍스트 출력
        self.retranslateUi()
        QMetaObject.connectSlotsByName(self)

        self.page_data()
        self.jsonload()

    def retranslateUi(self):
        _translate = QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Dialog"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "9:00-9:30"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Dialog", "10:00-10:30"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("Dialog", "10:30-11:00"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("Dialog", "11:00-11:30"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("Dialog", "9:30-10:00"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("Dialog", "10:00-10:30"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("Dialog", "10:30-11:00"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("Dialog", "11:00-11:30"))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("Dialog", "11:30-12:00"))
        item = self.tableWidget.verticalHeaderItem(9)
        item.setText(_translate("Dialog", "12:00-12:30"))
        item = self.tableWidget.verticalHeaderItem(10)
        item.setText(_translate("Dialog", "12:30-13:00"))
        item = self.tableWidget.verticalHeaderItem(11)
        item.setText(_translate("Dialog", "13:00-13:30"))
        item = self.tableWidget.verticalHeaderItem(12)
        item.setText(_translate("Dialog", "13:30-14:00"))
        item = self.tableWidget.verticalHeaderItem(13)
        item.setText(_translate("Dialog", "14:00-14:30"))
        item = self.tableWidget.verticalHeaderItem(14)
        item.setText(_translate("Dialog", "14:30-15:00"))
        item = self.tableWidget.verticalHeaderItem(15)
        item.setText(_translate("Dialog", "15:00-15:30"))
        item = self.tableWidget.verticalHeaderItem(16)
        item.setText(_translate("Dialog", "15:30-16:00"))
        item = self.tableWidget.verticalHeaderItem(17)
        item.setText(_translate("Dialog", "16:00-16:30"))
        item = self.tableWidget.verticalHeaderItem(18)
        item.setText(_translate("Dialog", "16:30-17:00"))
        item = self.tableWidget.verticalHeaderItem(19)
        item.setText(_translate("Dialog", "17:00-17:30"))
        item = self.tableWidget.verticalHeaderItem(20)
        item.setText(_translate("Dialog", "17:30-18:00"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "월"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "화"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "수"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "목"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "금"))
        self.label_4.setText(_translate("Dialog", "2022"))
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label.setText(_translate("Dialog", "학년도"))
        self.label_5.setText(_translate("Dialog", "1"))
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_2.setText(_translate("Dialog", "학기"))
        self.label_3.setText(_translate("Dialog", "시간표"))
        # self.pushButton.setText(_translate("Dialog", "배정"))
        # self.pushButton_2.setText(_translate("Dialog", "저장"))

    def page_data(self):
        global data, label_col
        data=[]
        if configData['info_type'] == "lesson_assign":
            data=lesson_assign_list
            label_col = lesson_assign_list_col

    def jsonload(self):
        global configData
        with open("info_type.json", "r") as info:
            configData = json.load(info)


    def lesson_assign(self):
        a = Ui_Lesson_Assign()
        a.show()
        exec
        #print('사용자 지정')

    def delete(self):
        print('삭제')

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Dialog = QDialog()
    ui = Ui_Dialog()
    ui.setupUi()
    ui.show()
    app.exec_()
