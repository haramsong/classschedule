from dialog import *
from timetable import timetable


# 메인 화면
class Ui_MainWindow(QMainWindow):
    # 메인 화면 출력
    def __init__(self):
        super().__init__()          # PyQt5의 QMainWindow의 속성을 가져옴
        self.get_init_data()
        self.setupUi()

    # 기본 데이터 설정
    def get_init_data(self):
        global tool_button_arr, configData
        # 버튼 관련 설정
        tool_button_arr = [
            ["강좌 정보", "img/lesson.png", 60, 60, self.classInfo],
            ["교수 정보", "img/professor.png", 60, 60, self.professorInfo],
            ["강의실 정보", "img/classroom.png", 60, 60, self.classroomInfo],
            ["강의 배정", "img/lesson_schedule.png", 60, 60, self.lessonSchedule]
        ]

        # json load
        with open("info_type.json", "r") as info:
            configData = json.load(info)

    # 화면 출력
    def setupUi(self):
        self.setFixedSize(550, 250)                         # 출력 사이즈
        self.setStyleSheet("background-color: white;")      # 배경화면 색깔(흰색)

        # 메인 위젯
        self.centralwidget = QWidget(self)

        # 제목
        self.titleLabel = QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QRect(0, 10, 550, 90))
        global_funtion.fontSetting(self, self.titleLabel, "8H", 36, " ")
        self.titleLabel.setAlignment(Qt.AlignCenter)

        # 버튼의 Layout
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QRect(0, 100, 550, 120))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)

        # 버튼 생성
        for i in range(len(tool_button_arr)):
            self.toolButton = QToolButton(self.horizontalLayoutWidget)
            global_funtion.tool_button_setting_widget(self, self.toolButton, self.horizontalLayout, tool_button_arr[i])


        # 위젯 설정
        self.setCentralWidget(self.centralwidget)

        # 텍스트 출력
        self.retranslateUi()

    # 텍스트 출력
    def retranslateUi(self):
        _translate = QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "교과 배정 프로그램"))
        self.titleLabel.setText(_translate("MainWindow", "교과 배정 프로그램"))

    # 강의 정보 창 이동
    def classInfo(self):
        configData['info_type'] = "lesson"
        self.page_move()

    # 교수 정보 창 이동
    def professorInfo(self):
        configData['info_type'] = "professor"
        self.page_move()


    # 강의실 정보 창 이동
    def classroomInfo(self):
        configData['info_type'] = "classroom"
        self.page_move()

    # 강의 배정 창 이동(아직 UI 작성 안됨)
    def lessonSchedule(self):
        page=timetable()
        page.show()
        exec
        #print("")

    # 창 이동 메소드
    def page_move(self):
        json.dumps(configData, indent="\t")

        with open('info_type.json', 'w', encoding='utf-8') as make_file:
            json.dump(configData, make_file, indent="\t")

        Ui_Dialog().exec_()



if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = Ui_MainWindow()
    ui.show()
    app.exec_()

