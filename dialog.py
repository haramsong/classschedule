from data_load import *
from global_py import *
import json

# 마스터데이터 정보 창
class Ui_Dialog(QDialog):
    # 마스터데이터 정보 창 출력
    def __init__(self):
        super().__init__()
        self.get_init_data()
        self.setupUi()


    # 기본 데이터 설정
    def get_init_data(self):
        global tool_button_arr, label_arr, line_arr, configData
        # 버튼 관련 설정
        tool_button_arr = [
            ["새로고침", "img/refresh.png", 40, 40, self.refreshInfo],
            ["저장", "img/floppy-disk.png", 40, 40, self.saveInfo],
            ["수정", "img/shuffle.png", 40, 40, self.changeInfo],
            ["삭제", "img/delete.png", 40, 40, self.deleteInfo]
        ]
        
        # label 정보
        label_arr = ["self.label_2","self.label_3","self.label_4","self.label_5","self.label_6","self.label_7"]
        # 입력창 정보
        line_arr = ["self.nameLine", "self.etc1Line", "self.etc2Line", "self.etc3Line", "self.etc4Line", "self.etc5Line"]

        # json load
        with open("info_type.json", "r") as info:
            configData = json.load(info)


    # 화면 출력
    def setupUi(self):
        self.setFixedSize(700, 500)                         # 출력 사이즈
        self.setStyleSheet("background-color: white;")      # 배경화면 색깔(흰색)

        # 제목
        self.titleLabel = QLabel(self)
        self.titleLabel.setGeometry(QRect(0, 0, 700, 70))
        global_funtion.fontSetting(self, self.titleLabel, "8H", 24, " ")
        self.titleLabel.setAlignment(Qt.AlignCenter)

        # List Widget
        self.listWidget = QListWidget(self)
        self.listWidget.setGeometry(QRect(20, 90, 150, 350))

        # 버튼 Layout
        self.verticalLayoutWidget = QWidget(self)
        self.verticalLayoutWidget.setGeometry(QRect(220, 110, 60, 300))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        
        # 버튼 생성
        for i in range(len(tool_button_arr)):
            self.toolButton = QToolButton(self.verticalLayoutWidget)
            global_funtion.tool_button_setting_widget(self, self.toolButton, self.verticalLayout, tool_button_arr[i])

        # 입력 Form Layout
        self.gridLayoutWidget = QWidget(self)
        self.gridLayoutWidget.setGeometry(QRect(310, 90, 360, 300))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
    
        # 입력 Form 생성
        for i in range(len(label_arr)):
            label_arr[i] = QLabel(self.gridLayoutWidget)
            self.gridLayout.addWidget(label_arr[i], i, 0, 1, 1)     # (i,0) 번째 Label
            line_arr[i] = QLineEdit(self.gridLayoutWidget)
            self.gridLayout.addWidget(line_arr[i], i, 1, 1, 1)      # (i,1) 번째 LineEdit

        self.page_data()            # 데이터 불러오기
        self.retranslateUi()        # 텍스트 출력
        global_funtion.buttonBox(self, self, 330, 450, 311, 30, self.accept)


    # json에서 가져온 값에 따라 Dialog 모습이 바뀜
    def page_data(self):
        global data, label_col, dialog_type
        data = []           # 마스터 데이터의 전체 데이터 row
        label_col = []      # 마스터 데이터 column
        dialog_type = ""    # Dialog 타입
        if configData['info_type'] == "lesson":         # 강의 정보
            data = lesson_list
            label_col = lesson_list_col
            dialog_type = "강의"
        elif configData['info_type'] == "professor":    # 교수 정보
            data = professor_list
            label_col = professor_list_col
            dialog_type = "교수"
        elif configData['info_type'] == "classroom":    # 강의실 정보
            data = classroom_list
            label_col = classroom_list_col
            dialog_type = "강의실"
            
        # 잘 모르시겠으면 print 주석 제거한 후 확인해보세요!
        # print(data)
        # print(label_col)
        
        # List Widget에 등록된 데이터 등록
        for i in data:
            self.listWidget.addItem(i[1])


    # 텍스트 출력
    def retranslateUi(self):
        _translate = QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", dialog_type + " 정보"))
        self.titleLabel.setText(_translate("Dialog", dialog_type + " 정보"))
        for i in range(len(label_arr)):
            label_arr[i].setText(_translate("Dialog", label_col[i+1]))


    # 새로고침 메소드
    def refreshInfo(self):
        print("")


    # 데이터 저장 메소드
    def saveInfo(self):
        # 코드를 한번 짜보세요!
        # Tip 1. 우측 입력한 form들의 데이터를 임의의 array에 담는다.
        # Tip 2. array를 data 안에 append한다.(이때 각각 마스터ID는 data의 length에서 +1 해주면 Auto-Increment 형태가 되겠죠?)
        # Tip 3. configData에 따라서 저장해야하는 excel의 위치가 다르겠죠? if/else문을 사용하여 to_excel을 해주세요!
        #       잘 모르시겠으면 page_data의 if/else문을 참고하세요.

        # 여기에 코드를 입력해주세요!
        new_data = []  # 여기에 등록하려는 정보를 담아주세요!

        list.sort(data, key=lambda k: (k[0]))               # data array의 0번째 index를 기준으로 sort
        df = pd.DataFrame(data, columns=label_col)          # data array, column은 label_col로 하는 dataframe 생성
        df.to_excel('', index=False)                        # dataframe excel 저장
        global_funtion().message_box_1(QMessageBox.Information, "정보", "등록되었습니다", "확인")      # 저장완료 메세지 출력


    # 데이터 수정 메소드
    def changeInfo(self):
        print("")


    # 데이터 삭제 메소드
    def deleteInfo(self):
        print("")

