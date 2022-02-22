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
        global configData, horizontal_header_arr, grad_timetable_list

        # json load
        with open("info_type.json", "r") as info:
            configData = json.load(info)

        horizontal_header_arr = ['월', '화', '수', '목', '금']
        

        grad_timetable_df = pd.read_excel('data/lesson_assign_dae_tableview.xlsx')
        grad_timetable_df.replace(np.NaN, '', inplace=True)
        grad_timetable_list = grad_timetable_df.values.tolist()

    # 화면 출력
    def setupUi(self):
        self.setObjectName("Dialog")
        self.setFixedSize(1250, 800)

        # 테이블 위젯 설정(시간표)
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setGeometry(QRect(50, 100, 1150, 630))
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        self.tableWidget.clear()

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

        # 데이터 배치
        # 교수명 강좌명 분반 분류 요일 시간ID 강의실명
        # 월 수 -> [][0], [][2]
        # 화 목 -> [][1], [][3]
        # 금 -> [][4]
        # 9:00 -> [1][]

        for i in range(5):
            for j in range(len(time_list)-1):
                self.tableWidget.setItem(j, i, QTableWidgetItem(""))

        pre = ""
        for i in range(len(grad_timetable_list)):
            if grad_timetable_list[i][4] == '' or grad_timetable_list[i][5] == '':
                continue
            for j in grad_timetable_list[i][5].split(","): #12,13,14,15,16
                txt = ""
                if "월" in grad_timetable_list[i][4]:
                    if self.tableWidget.item(int(j), 0).text() != "":
                        pre = self.tableWidget.item(int(j), 0).text() + "\n"
                    txt = pre + grad_timetable_list[i][0] + "(" + grad_timetable_list[i][1] + ")"
                    self.tableWidget.setItem(int(j),0,QTableWidgetItem(txt))
                if "화" in grad_timetable_list[i][4]:
                    if self.tableWidget.item(int(j), 1).text() != "":
                        pre = self.tableWidget.item(int(j), 1).text() + "\n"
                    txt = pre + grad_timetable_list[i][0] + "(" + grad_timetable_list[i][1] + ")"
                    self.tableWidget.setItem(int(j),1,QTableWidgetItem(txt))
                if "수" in grad_timetable_list[i][4]:
                    if self.tableWidget.item(int(j), 2).text() != "":
                        pre = self.tableWidget.item(int(j), 2).text() + "\n"
                    txt = pre + grad_timetable_list[i][0] + "(" + grad_timetable_list[i][1] + ")"
                    self.tableWidget.setItem(int(j),2,QTableWidgetItem(txt))
                if "목" in grad_timetable_list[i][4]:
                    if self.tableWidget.item(int(j), 3).text() != "":
                        pre = self.tableWidget.item(int(j), 3).text() + "\n"
                    txt = pre + grad_timetable_list[i][0] + "(" + grad_timetable_list[i][1] + ")"
                    self.tableWidget.setItem(int(j),3,QTableWidgetItem(txt))
                if "금" in grad_timetable_list[i][4]:
                    if self.tableWidget.item(int(j), 4).text() != "":
                        pre = self.tableWidget.item(int(j), 4).text() + "\n"
                    txt = pre + grad_timetable_list[i][0] + "(" + grad_timetable_list[i][1] + ")"
                    self.tableWidget.setItem(int(j),4,QTableWidgetItem(txt))
                pre = ''


        # 테이블 위젯 행렬 사이즈 조절
        self.tableWidget.verticalHeader().setDefaultSectionSize(70)

        # 라벨 설정
        self.label = QLabel(self) # 학년도
        self.label.setObjectName("label")
        self.label.setGeometry(QRect(0, 10, 1250, 80))
        self.label.setAlignment(Qt.AlignCenter)
        global_funtion.fontSetting(self, self.label, "8H", 24, " ")

        # 텍스트 출력
        self.retranslateUi()

        #self.page_data()
        self.jsonload()

    def retranslateUi(self):
        self.label.setText('대학원 시간표 미리보기')
        _translate = QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "강의 배정"))


    # def page_data(self):
    #     global data, label_col
    #     data=[]
    #
    #     if configData['info_type'] == "lesson_assign":
    #         data=grad_timetable_list
    #         label_col = lesson_assign_list_col_dae

    def jsonload(self):
        global configData
        with open("info_type.json", "r") as info:
            configData = json.load(info)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Dialog = QDialog()
    ui = Ui_Dialog()
    ui.setupUi()
    ui.show()
    app.exec_()
