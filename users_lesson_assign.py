from global_py import *
from data_load import *

class Ui_Lesson_Assign(QDialog):
    def __init__(self):
        super().__init__()
        self.get_init_data()
        self.setupUi()

    # 기본 데이터 설정
    def get_init_data(self):
        global tool_button_arr, configData

        # 버튼 관련 설정
        tool_button_arr = [
            ["입력", "img/add_person.png", 40, 40, self.addInfo],
            ["수정", "img/eraser.png", 40, 40, self.changeInfo],
            ["삭제", "img/delete.png", 40, 40, self.deleteInfo],
            ["배정", "img/shuffle.png", 40, 40, self.AssignInfo],
            ["저장", "img/floppy-disk.png", 40, 40, self.saveInfo]
        ]

        # json load
        with open("info_type.json", "r") as info:
            configData = json.load(info)

    # 화면 출력
    def setupUi(self):
        self.setObjectName("Dialog")
        self.setFixedSize(600, 600)
        self.setStyleSheet("background-color: white;")  # 배경화면 색깔(흰색)

        # 제목 label
        self.label_6 = QLabel(self)
        self.label_6.setGeometry(QRect(200, 30, 151, 16))
        self.label_6.setObjectName("label_6")


        # gridLayoutWidget
        self.gridLayoutWidget = QWidget(self)
        self.gridLayoutWidget.setGeometry(QRect(40, 80, 450, 80))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        # label
        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)

        self.label_5 = QLabel(self.gridLayoutWidget)
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 4, 1, 1)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 3, 1, 1)

        # lineEdit
        self.lineEdit = QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)

        self.lineEdit_3 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 1, 2, 1, 1)

        self.lineEdit_4 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 1, 3, 1, 1)

        self.lineEdit_5 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_5, 1, 4, 1, 1)

        # tableWidget
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setGeometry(QRect(30, 210, 371, 271))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)

        # 우측 버튼 verticalLayoutWidget
        self.verticalLayoutWidget = QWidget(self)
        self.verticalLayoutWidget.setGeometry(QRect(430, 250, 95, 201))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        #self.pushButton_1 = QPushButton(self.verticalLayoutWidget)
        #self.pushButton_1.setObjectName("pushButton_1")
        #self.verticalLayout.addWidget(self.pushButton_1)
        #
        #self.pushButton_5 = QPushButton(self.verticalLayoutWidget)
        #self.pushButton_5.setObjectName("pushButton_5")
        #self.verticalLayout.addWidget(self.pushButton_5)
        #
        #self.pushButton_2 = QPushButton(self.verticalLayoutWidget)
        #self.pushButton_2.setObjectName("pushButton_2")
        #self.verticalLayout.addWidget(self.pushButton_2)
        #
        #self.pushButton_3 = QPushButton(self.verticalLayoutWidget)
        #self.pushButton_3.setObjectName("pushButton_3")
        #self.verticalLayout.addWidget(self.pushButton_3)
        #
        #self.pushButton_4 = QPushButton(self.verticalLayoutWidget)
        #self.pushButton_4.setObjectName("pushButton_4")
        #self.verticalLayout.addWidget(self.pushButton_4)

        # 버튼 생성 (verticalLayoutWidget 으로 변경)
        for i in range(len(tool_button_arr)):
            self.toolButton = QToolButton(self.verticalLayoutWidget)
            global_funtion.tool_button_setting_widget(self, self.toolButton, self.verticalLayout, tool_button_arr[i])

        self.retranslateUi()
        QMetaObject.connectSlotsByName(self)

    # 텍스트 출력
    def retranslateUi(self):
        _translate = QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "사용자 지정 배정"))
        self.label.setText(_translate("Dialog", "교수"))
        self.label_2.setText(_translate("Dialog", "강의"))
        self.label_3.setText(_translate("Dialog", "시간"))
        self.label_4.setText(_translate("Dialog", "요일"))
        self.label_5.setText(_translate("Dialog", "강의실"))
        self.label_6.setText(_translate("Dialog", "사용자 지정 배정"))

    # 입력 메소드
    def addInfo(self):
        print("입력")

    # 수정 메소드
    def changeInfo(self):
        print("수정")

    # 삭제 메소드
    def deleteInfo(self):
        print("삭제")

    # 배정 메소드
    def AssignInfo(self):
        print("배정")

    # 저장 메소드
    def saveInfo(self):
        print("저장")


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Dialog = QDialog()
    ui = Ui_Dialog()
    ui.setupUi()
    ui.show()
    app.exec_()