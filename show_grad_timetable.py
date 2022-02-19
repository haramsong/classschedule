#from PyQt5 import QtCore, QtGui, QtWidgets

from dialog import *
from data_load import *
import json
from users_lesson_assign import *
from PyQt5 import QtGui

# 시간표 창 만들기
class Ui_ShowGradTimetable(QDialog):
    def __init__(self):
        super().__init__()
        self.get_init_data()
        self.setupUi()

    # 데이터 불러오기
    def get_init_data(self):
        global tool_button_arr, configData, horizontal_header_arr
        # 버튼 관련 설정
        tool_button_arr = [
            ["시간표 저장", "img/floppy-disk.png", 50, 50, self.saveTimetable],
            ["시간표 삭제", "img/delete.png", 50, 50, self.delete]
        ]

        # json load
        with open("info_type.json", "r") as info:
            configData = json.load(info)

        horizontal_header_arr = ['월', '화', '수', '목', '금']

    # 화면 출력
    def setupUi(self):
        self.setObjectName("Dialog")
        self.setFixedSize(1050, 700)

        # 테이블 위젯 설정(시간표)
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setGeometry(QRect(50, 100, 950, 530))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)

        # 시간대 표시
        for i in range(len(time_list)):
            row = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row)
            item = QTableWidgetItem()
            self.tableWidget.setVerticalHeaderItem(i, item)
            item = self.tableWidget.verticalHeaderItem(i)
            # print(time_list[i])
            time_text = time_list[i][1]+ '-' + time_list[i][2]
            item.setText(time_text)

        # 요일 입력
        for i in range(len(horizontal_header_arr)):
            item = QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(i, item)
            item = self.tableWidget.horizontalHeaderItem(i)
            item.setText(horizontal_header_arr[i])
            self.tableWidget.horizontalHeader().setSectionResizeMode(i, QHeaderView.Stretch)

        # 데이터 배치
        # 교수명 강좌명 분반 분류 요일 시간ID 강의실명
        # 월 수 -> [][0], [][2]
        # 화 목 -> [][1], [][3]
        # 금 -> [][4]
        # 9:00 -> [1][]

        # lesson_assign_list.append(['MA15642', 2, '최영준', '복소변수', '월, 수', '0,1,2', '607-208', '수학과2', 2022, 1])
        # print(lesson_assign_list)

        for i in range(5):
            for j in range(18):
                self.tableWidget.setItem(j, i, QTableWidgetItem(""))

## lesson_assign_list_dae 바꾸기
        lesson_assign_list_dae = lesson_assign_df_dae.values.tolist()

        pre = ""
        for i in range(len(lesson_assign_list_dae)):
            txt = ""
            for j in lesson_assign_list_dae[i][5].split(","): #12,13,14,15,16
                if self.tableWidget.item(int(j),0).text() != "":
                    pre = self.tableWidget.item(int(j),0).text() + "\n"
                txt = pre + lesson_assign_list_dae[i][0] + "(" + lesson_assign_list_dae[i][1] + ")"
                if "월" in lesson_assign_list_dae[i][4]:
                    self.tableWidget.setItem(int(j),0,QTableWidgetItem(txt))
                if "화" in lesson_assign_list_dae[i][4]:
                    self.tableWidget.setItem(int(j),1,QTableWidgetItem(txt))
                if "수" in lesson_assign_list_dae[i][4]:
                    self.tableWidget.setItem(int(j),2,QTableWidgetItem(txt))
                if "목" in lesson_assign_list_dae[i][4]:
                    self.tableWidget.setItem(int(j),3,QTableWidgetItem(txt))
                if "금" in lesson_assign_list_dae[i][4]:
                    self.tableWidget.setItem(int(j),4,QTableWidgetItem(txt))



        # 테이블 위젯 행렬 사이즈 조절
        self.tableWidget.verticalHeader().setDefaultSectionSize(60)

        # 라벨 설정
        self.label = QLabel(self) # 학년도
        self.label.setObjectName("label")
        self.label.setGeometry(QRect(0, 10, 1050, 80))
        self.label.setAlignment(Qt.AlignCenter)
        global_funtion.fontSetting(self, self.label, "8H", 24, " ")
        # label_text = str(year_str) + '학년도 ' + str(semester_str) + '학기'


        # 버튼 설정
        self.horizontalLayoutWidget = QWidget(self)
        self.horizontalLayoutWidget.setGeometry(QRect(70, 0, 100, 100))

        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        # 버튼 생성
        for i in range(len(tool_button_arr)):
            self.toolButton = QToolButton(self.horizontalLayoutWidget)
            global_funtion.tool_button_setting_widget(self, self.toolButton, self.horizontalLayout, tool_button_arr[i])


        ############################ 수정
        # Combobox
        self.yearSelect = QComboBox(self)
        self.yearSelect.setGeometry(QRect(800, 60, 200, 30))

        font = QtGui.QFont('Arial', 10, QtGui.QFont.Bold)

        self.yearSelect.setFont(font)
        self.yearSelect.addItems(['2020학년도 1학기', '2020학년도 2학기'])  # 데이터를 불러와서 year 정보 수정하기

        # self.yearSelect.setStyleSheet("QComboBox { padding-left : 2px; }")
        self.yearSelect.currentIndexChanged.connect(self.comboboxClicked)

        # 텍스트 출력
        self.retranslateUi()

        self.page_data()
        self.jsonload()

    def retranslateUi(self):
        label_text = self.yearSelect.currentText()
        self.label.setText(label_text)
        _translate = QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "강의 배정"))


    def page_data(self):
        global data, label_col
        data=[]

        if configData['info_type'] == "lesson_assign":
            data=lesson_assign_list_dae
            label_col = lesson_assign_list_col_dae

        # if configData['info_type'] == 'under':#학부 라디오 버튼 체크시
        #     data= lesson_assign_under_list
        #     label_col = lesson_assign_under_list_col
        #
        # elif configData['info_type'] == 'grad':#대학원 라디오 버튼 체크시
        #     data = lesson_assign_list_dae
        #     label_col = lesson_assign_list_col_dae


    def jsonload(self):
        global configData
        with open("info_type.json", "r") as info:
            configData = json.load(info)


    def comboboxClicked(self, i):# 시간표 미리보기에서도 이 기능이 쓰이는지 모르겠음
        label_text = self.yearSelect.currentText()
        self.label.setText(label_text)


    def saveTimetable(self):# 시간표 미리보기 결과 마음에 들면 lesson_assign에 저장 -> 시간표 확정
        print("")

    def delete(self):# 시간표 미리보기 결과 마음에 안들어서 삭제
        print('삭제')
        for i in range(5):
            for j in range(18):
                self.tableWidget.setItem(j, i, QTableWidgetItem(""))


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Dialog = QDialog()
    ui = Ui_Dialog()
    ui.setupUi()
    ui.show()
    app.exec_()
