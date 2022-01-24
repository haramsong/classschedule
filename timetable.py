from users_lesson_assign import *
from data_load import *

class Ui_Timetable(QDialog):
    def __init__(self):
        super().__init__()
        self.get_init_data()
        self.setupUi()

    # 기본 데이터 설정
    def get_init_data(self):
        global tool_button_arr, configData
        # 버튼 관련 설정
        tool_button_arr = [
            ["사용자 지정", "img/edit.png", 80, 80, self.users_lesson_assign],
            ["삭제", "img/delete.png", 80, 80, self.deleteInfo]
        ]

        # json load
        with open("info_type.json", "r") as info:
            configData = json.load(info)

    # 화면 출력
    def setupUi(self):
        self.setObjectName("Dialog")
        self.setFixedSize(800, 800)                          # 출력 사이즈
        self.setStyleSheet("background-color: white;")       # 배경화면 색깔(흰색)

        # horizontalLayoutWidget 제목
        self.horizontalLayoutWidget = QWidget(self)
        self.horizontalLayoutWidget.setGeometry(QRect(60, 30, 500, 50))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.label = QLabel(self.horizontalLayoutWidget)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)

        # tableWidget 표시
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setGeometry(QRect(150, 100, 600, 600))         # 시작x, 시작y, 가로, 세로
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(18)
        item = QTableWidgetItem()

        # tableWidget에 시간대 표시
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
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QTableWidgetItem()

        # 요일 입력
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)

        self.tableWidget.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget.verticalHeader().setDefaultSectionSize(31)
        self.tableWidget.verticalHeader().setMinimumSectionSize(20)

        # verticalLayoutWidget
        self.verticalLayoutWidget = QWidget(self)
        self.verticalLayoutWidget.setGeometry(QRect(40, 120, 60, 500))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        # 버튼 생성 ( verticalLayoutWidget으로 수정)
        for i in range(len(tool_button_arr)):
            self.toolButton = QToolButton(self.verticalLayoutWidget)
            global_funtion.tool_button_setting_widget(self, self.toolButton, self.verticalLayout, tool_button_arr[i])

        #self.pushButton = QPushButton(self.verticalLayoutWidget)
        # self.pushButton.setObjectName("pushButton")
        # self.verticalLayout.addWidget(self.pushButton)
        # self.pushButton_2 = QPushButton(self.verticalLayoutWidget)
        # self.pushButton_2.setObjectName("pushButton_2")
        # self.verticalLayout.addWidget(self.pushButton_2)

        # 텍스트 출력
        self.retranslateUi()

        QMetaObject.connectSlotsByName(self)

    # 텍스트 출력
    def retranslateUi(self):
        _translate = QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "강의 배정"))
        self.label.setText(_translate("Dialog", "시간표 배정"))      # ㅇㅇㅇㅇ학년도 ㅇ학기 시간표 배정

        # 시간대
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "9:00-9:30"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Dialog", "9:30-10:00"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("Dialog", "10:00-10:30"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("Dialog", "10:30-11:00"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("Dialog", "11:00-11:30"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("Dialog", "11:30-12:00"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("Dialog", "12:00-12:30"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("Dialog", "12:30-13:00"))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("Dialog", "13:00-13:30"))
        item = self.tableWidget.verticalHeaderItem(9)
        item.setText(_translate("Dialog", "13:30-14:00"))
        item = self.tableWidget.verticalHeaderItem(10)
        item.setText(_translate("Dialog", "14:00-14:30"))
        item = self.tableWidget.verticalHeaderItem(11)
        item.setText(_translate("Dialog", "14:30-15:00"))
        item = self.tableWidget.verticalHeaderItem(12)
        item.setText(_translate("Dialog", "15:00-15:30"))
        item = self.tableWidget.verticalHeaderItem(13)
        item.setText(_translate("Dialog", "15:30-16:00"))
        item = self.tableWidget.verticalHeaderItem(14)
        item.setText(_translate("Dialog", "16:00-16:30"))
        item = self.tableWidget.verticalHeaderItem(15)
        item.setText(_translate("Dialog", "16:30-17:00"))
        item = self.tableWidget.verticalHeaderItem(16)
        item.setText(_translate("Dialog", "17:00-17:30"))
        item = self.tableWidget.verticalHeaderItem(17)
        item.setText(_translate("Dialog", "17:30-18:00"))

        # 요일
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

    # 사용자 지정 입력 창 이동
    def users_lesson_assign(self):
        Ui_Lesson_Assign().exec_()
        print("사용자 지정")

    # 삭제
    def deleteInfo(self):
        print("삭제")


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = Ui_Dialog()
    ui.setupUi()
    ui.show()
    app.exec_()
