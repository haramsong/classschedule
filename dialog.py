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
        global tool_button_arr, label_arr, line_arr, configData , row
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

        row=999
        #print(row)


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
            
        # List Widget 클릭 메소드 연결
        self.listWidget.itemClicked.connect(self.listClick)

        self.page_data()            # 데이터 불러오기
        self.retranslateUi()        # 텍스트 출력
        global_funtion.buttonBox(self, self, 330, 450, 311, 30, self.accept)
        
        
    # List Click Event
    def listClick(self):
        global row
        row = self.listWidget.currentRow()
        for i in range(len(line_arr)):
            line_arr[i].setText(str(data[row][i+1]))
        print(row)

    def jsonLoad(self):
        global configData
        with open("info_type.json", "r") as info:
            configData = json.load(info)


    # json에서 가져온 값에 따라 Dialog 모습이 바뀜
    def page_data(self):
        global data, label_col, dialog_type, masterID_code , next_index
        data = []           # 마스터 데이터의 전체 데이터 row
        label_col = []      # 마스터 데이터 column
        dialog_type = ""    # Dialog 타입
        if configData['info_type'] == "lesson":         # 강의 정보
            data = lesson_list
            label_col = lesson_list_col
            dialog_type = "강의"
            masterID_code = global_list[0][1]   # A
            next_index = global_list[0][3]
        elif configData['info_type'] == "professor":    # 교수 정보
            data = professor_list
            label_col = professor_list_col
            dialog_type = "교수"
            masterID_code = global_list[1][1]   # B
            next_index = global_list[1][3]
        elif configData['info_type'] == "classroom":    # 강의실 정보
            data = classroom_list
            label_col = classroom_list_col
            dialog_type = "강의실"
            masterID_code = global_list[2][1]  # R
            next_index = global_list[2][3]

            
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
        # for i in range(len(line_arr)):
        #     line_arr[i].setText("")
        self.close()
        self.__init__()
        self.exec_()


    # 데이터 저장 메소드
    def saveInfo(self):
        new_data=[]
        # 데이터 입력 list 만들기
        for i in range(len(line_arr)):
            new_data.append(line_arr[i].text())
        # 라인에 작성된 text 가져오기
        masterID=masterID_code + str(next_index).zfill(3)
        # 마스터id = 마스터 코드 + ((데이터 길이+1) + 앞에 0 넣어서 자릿수 채우기)
        new_data.insert(0,masterID)
        # 마스터id를 new_data 맨 앞에다 붙이자
        if row != 999:
            global_funtion().message_box_1(QMessageBox.Information, "정보", "이미 입력된 값입니다", "확인")
            return
        data.append(new_data)
        # row가 999가 아니면 저장이 되지 않게 설정
        # data에 new_data 붙여넣자

        #print(data)
        list.sort(data,key=lambda k: (k[0]))
        # list를 index 기준으로 정렬하자
        df=pd.DataFrame(data, columns=label_col)
        # 데이터 프레임으로 저장하자

        if configData['info_type'] == "lesson":
            df.to_excel('data/lesson_info.xlsx', index=False)
            global_list[0][3] = next_index + 1
        elif configData['info_type'] == "professor":
            df.to_excel('data/professor_info.xlsx', index=False)
            global_list[1][3] = next_index + 1
        elif configData['info_type'] == "classroom":
            df.to_excel('data/classroom_info.xlsx', index=False)
            global_list[2][3] = next_index + 1

        df = pd.DataFrame(global_list, columns = global_list_col)  # global_list_array, column은 global_list_col 로 하는 dataframe 생성
        df.to_excel('data/global_master.xlsx', index=False)    # global list df 를 excel 저장

        global_funtion().message_box_1(QMessageBox.Information, "정보", "등록되었습니다", "확인")
        self.close()
        self.__init__()
        self.exec_()


    # 데이터 수정 메소드
    def changeInfo(self):
        global_funtion().message_box_2(QMessageBox.Question, "확인", "작성내용을 수정하시겠습니까?", "예", "아니오")
        self.jsonLoad()
        if configData['message'] == 'Y':
            # 수정하시겠습니까? => 예
            selected_row = []
            # 데이터 입력 list 만들기
            for i in range(len(line_arr)):
                selected_row.append(line_arr[i].text())
            # 라인에 작성된 text 가져오기 ( 내가 수정한 값 )
            masterID = data[row][0]
            # 마스터 id = 내가 클릭한 데이터에 해당하는 인덱스 뽑아오자  ( 수정 전 데이터의 idx)
            selected_row.insert(0, masterID)
            # 라인에 작성된 text 앞에 마스터 id 넣자 ( 수정 전 index와 수정 후 index가 같게 설정 -> idx는 같지만 안에 내용은 수정되었음 )
            for i in range(len(data)):
                if selected_row[0] == data[i][0]:
                    data[i]=selected_row
            # 기존 데이터랑 비교해서 수정 전 idx와 수정 후 idx가 같으면 수정한 값들로 변경하자

            list.sort(data, key=lambda k: (k[0]))
            # list를 index 기준으로 정렬하자
            df = pd.DataFrame(data, columns=label_col)
            # 데이터 프레임으로 저장하자
            print(df)

            if configData['info_type'] == "lesson":  # 강의 정보
                df.to_excel('data/lesson_info.xlsx', index=False)  # dataframe excel 저장
            elif configData['info_type'] == "professor":  # 교수 정보
                df.to_excel('data/professor_info.xlsx', index=False)  # dataframe excel 저장
            elif configData['info_type'] == "classroom":  # 강의실 정보
                df.to_excel('data/classroom_info.xlsx', index=False)  # dataframe excel 저장

            print("yes")
            global_funtion().message_box_1(QMessageBox.Information, "정보", "수정되었습니다", "확인")
        elif configData['message'] == 'N':
            print("no")
            return
        self.close()
        self.__init__()
        self.exec_()

    # 데이터 삭제 메소드
    def deleteInfo(self):
        global_funtion().message_box_2(QMessageBox.Question, "확인", "작성내용을 삭제하시겠습니까?", "예", "아니오")
        self.jsonLoad()
        if configData['message'] == 'Y':
            for i in range(len(data)):
                selected_row = line_arr[0].text()
                # 라인에 작성된 첫번째 값 즉, 과목 명만 selected_row로 뽑아오자
                if selected_row == data[i][1]:
                    data.pop(i)
                    break
                # selected_row가 기존 데이터와 비교했을 때 같으면 그 데이터는 삭제하자
            # print(selected_row)
            # print("yes")
            # print(data)

            list.sort(data, key=lambda k: (k[0]))
            # list를 index 기준으로 정렬하자
            df = pd.DataFrame(data, columns=label_col)
            # 데이터 프레임으로 저장하자
            # print(df)

            if configData['info_type'] == "lesson":  # 강의 정보
                df.to_excel('data/lesson_info.xlsx', index=False)  # dataframe excel 저장
            elif configData['info_type'] == "professor":  # 교수 정보
                df.to_excel('data/professor_info.xlsx', index=False)  # dataframe excel 저장
            elif configData['info_type'] == "classroom":  # 강의실 정보
                df.to_excel('data/classroom_info.xlsx', index=False)  # dataframe excel 저장

            global_funtion().message_box_1(QMessageBox.Information, "정보", "삭제되었습니다", "확인")  # 저장완료 메세지 출력

        elif configData['message'] == 'N':
            print("no")
            return


        self.close()
        self.__init__()
        self.exec_()


