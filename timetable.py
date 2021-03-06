#from PyQt5 import QtCore, QtGui, QtWidgets

from dialog import *
from data_load import *
import json
from users_lesson_assign import *
from PyQt5 import QtGui
import os
import pandas as pd

# 시간표 창 만들기
class Ui_Timetable(QDialog):
    def __init__(self):
        super().__init__()
        self.get_init_data()
        self.setupUi()

    # 데이터 불러오기
    def get_init_data(self):
        global tool_button_arr, configData, horizontal_header_arr
        # 버튼 관련 설정
        tool_button_arr = [
            ["사용자 지정", "img/edit.png", 50, 50, self.lesson_assign],
            ["삭제", "img/delete.png", 50, 50, self.delete]
        ]
        # json load
        self.jsonLoad()

        horizontal_header_arr = ['월', '화', '수', '목', '금']

    def jsonLoad(self):
        global configData
        with open("info_type.json", "r") as info:
            configData = json.load(info)

    # 화면 출력
    def setupUi(self):
        self.setObjectName("Dialog")
        self.setFixedSize(1250, 900)

        # 테이블 위젯 설정(시간표)
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setGeometry(QRect(25, 100, 1200, 730))
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)


        # 테이블 위젯 행렬 사이즈 조절
        self.tableWidget.verticalHeader().setDefaultSectionSize(90)

        # 라벨 설정
        self.label = QLabel(self) # 학년도
        self.label.setObjectName("label")
        self.label.setGeometry(QRect(0, 10, 1250, 80))
        self.label.setAlignment(Qt.AlignCenter)
        global_funtion.fontSetting(self, self.label, "8H", 24, " ")
        # label_text = str(year_str) + '학년도 ' + str(semester_str) + '학기'


        # 버튼 설정
        self.verticalLayoutWidget = QWidget(self)
        self.verticalLayoutWidget.setGeometry(QRect(30, 30, 200, 60))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QHBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        # Combobox
        self.yearSelect = QComboBox(self)
        self.yearSelect.setGeometry(QRect(1000, 60, 200, 30))


        subdir_names = os.listdir('data/class_dataset')
        print(subdir_names)
        font = QtGui.QFont('Arial', 10, QtGui.QFont.Bold)

        self.yearSelect.setFont(font)

        self.yearSelect.addItem(str(year_str)+"학년도 "+str(semester_str)+"학기")
        year_arr = []
        for i in list(subdir_names):
            ar = []
            y = i[0:4]
            s = i[5]
            ar.append(y)
            ar.append(s)
            year_arr.append(ar)
        print(year_arr)
        list.sort(year_arr, key=lambda k: (k[0], k[1]))
        print(year_arr)
        for i in list(reversed(year_arr)):
            n = i[0]+"학년도 " + i[1] + "학기"
            self.yearSelect.addItem(n)
        # self.yearSelect.addItems(['2020학년도 1학기', '2020학년도 2학기'])  # 데이터를 불러와서 year 정보 수정하기

        # self.yearSelect.setStyleSheet("QComboBox { padding-left : 2px; }")
        self.yearSelect.currentIndexChanged.connect(self.comboboxClicked)

        # 데이터 배치
        #강의ID	분반	교수명	강좌명	요일	시간ID	강의실명	대상학과	년도	학기
        # 월 수 -> [][0], [][2]
        # 화 목 -> [][1], [][3]
        # 금 -> [][4]
        # 9:00 -> [1][]

        # lesson_assign_list.append(['MA15642', 2, '최영준', '복소변수', '월, 수', '0,1,2', '607-208', '수학과2', 2022, 1])
        print(lesson_assign_list)


        self.table_fill()

        # 버튼 생성
        for i in range(len(tool_button_arr)):
            self.toolButton = QToolButton(self.verticalLayoutWidget)
            global_funtion.tool_button_setting_widget(self, self.toolButton, self.verticalLayout, tool_button_arr[i])

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
            data=lesson_assign_list
            label_col = lesson_assign_list_col

    def jsonload(self):
        global configData
        with open("info_type.json", "r") as info:
            configData = json.load(info)

    def comboboxClicked(self, i):
        label_text = self.yearSelect.currentText()
        self.label.setText(label_text)
        self.table_fill()

    def lesson_assign(self):
        a = Ui_Lesson_Assign()
        a.exec_()
        self.table_fill()

    def table_fill(self):
        global lesson_assign_df, lesson_assign_list
        lesson_assign_df = pd.read_excel('data/lesson_assign.xlsx')
        lesson_assign_df.replace(np.NaN, '', inplace=True)
        lesson_assign_list = lesson_assign_df.values.tolist()

        self.tableWidget.clear()
        self.tableWidget.setRowCount(0)

        # 시간대 표시
        for i in range(len(time_list) - 1):
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

        for i in range(5):
            for j in range(len(time_list)-1):
                self.tableWidget.setItem(j, i, QTableWidgetItem(""))

        pre = ""
        for i in range(len(lesson_assign_list)):
            if (str(lesson_assign_list[i][9]) == self.yearSelect.currentText()[0:4]) and (str(lesson_assign_list[i][10]) == self.yearSelect.currentText()[8]):
                for j in lesson_assign_list[i][6].split(","): #12,13,14,15,16
                    txt = ""
                    print(self.tableWidget.item(int(j), 0).text())
                    if "월" in lesson_assign_list[i][5]:
                        if self.tableWidget.item(int(j), 0).text() != "":
                            pre = self.tableWidget.item(int(j), 0).text() + "\n"
                        txt = pre + lesson_assign_list[i][1] + "(" + lesson_assign_list[i][2] + ")"
                        self.tableWidget.setItem(int(j),0,QTableWidgetItem(txt))
                    if "화" in lesson_assign_list[i][5]:
                        if self.tableWidget.item(int(j), 1).text() != "":
                            pre = self.tableWidget.item(int(j), 1).text() + "\n"
                        txt = pre + lesson_assign_list[i][1] + "(" + lesson_assign_list[i][2] + ")"
                        self.tableWidget.setItem(int(j),1,QTableWidgetItem(txt))
                    if "수" in lesson_assign_list[i][5]:
                        if self.tableWidget.item(int(j), 2).text() != "":
                            pre = self.tableWidget.item(int(j), 2).text() + "\n"
                        txt = pre + lesson_assign_list[i][1] + "(" + lesson_assign_list[i][2] + ")"
                        self.tableWidget.setItem(int(j),2,QTableWidgetItem(txt))
                    if "목" in lesson_assign_list[i][5]:
                        if self.tableWidget.item(int(j), 3).text() != "":
                            pre = self.tableWidget.item(int(j), 3).text() + "\n"
                        txt = pre + lesson_assign_list[i][1] + "(" + lesson_assign_list[i][2] + ")"
                        self.tableWidget.setItem(int(j),3,QTableWidgetItem(txt))
                    if "금" in lesson_assign_list[i][5]:
                        if self.tableWidget.item(int(j), 4).text() != "":
                            pre = self.tableWidget.item(int(j), 4).text() + "\n"
                        txt = pre + lesson_assign_list[i][1] + "(" + lesson_assign_list[i][2] + ")"
                        self.tableWidget.setItem(int(j),4,QTableWidgetItem(txt))
                    pre = ''

    def delete(self):
        global_funtion().message_box_2(QMessageBox.Question, "경고", "저장되어 있던 학부, 대학원 사용자 배정 정보가 삭제됩니다. 정말 삭제하시겠습니까? (새학기 강의 배정할 때만 사용)", "예",
                                       "아니오")
        self.jsonLoad()
        if configData['message'] == 'Y':
            df_del = pd.DataFrame([], columns=lesson_assign_under_list_col)  # data array, column은 label_col로 하는 dataframe 생성
            df_del2 = pd.DataFrame([], columns=lesson_assign_list_col_dae)  # data array, column은 label_col로 하는 dataframe 생성
            df_del.to_excel('data/lesson_assign_under.xlsx', index=False)  # dataframe excel 저장
            df_del2.to_excel('data/lesson_assign_dae.xlsx', index=False)
            global_funtion().message_box_1(QMessageBox.Information, "확인", "삭제되었습니다. ", "확인")

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Dialog = QDialog()
    ui = Ui_Dialog()
    ui.setupUi()
    ui.show()
    app.exec_()
