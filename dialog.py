from data_load import *
from global_py import *
import json

# pull request
# 마스터데이터 정보 창
class Ui_Dialog(QDialog):
    # 마스터데이터 정보 창 출력
    def __init__(self):
        super().__init__()
        self.get_init_data()
        self.setupUi()


    # 기본 데이터 설정
    def get_init_data(self):
        global tool_button_arr, label_arr, line_arr, configData, row
        row = 999
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
    
        # 입력 Form 생성 - label 생성
        for i in range(len(label_arr)):
            label_arr[i] = QLabel(self.gridLayoutWidget)
            self.gridLayout.addWidget(label_arr[i], i, 0, 1, 1)  # (i,0) 번째 Label

        # 입력 Form 생성 - lineedit, combobox 생성
        if configData['info_type'] == "lesson":  # 강의 정보
            # lineedit
            for i in [0, 5]:
                line_arr[i] = QLineEdit(self.gridLayoutWidget)
                self.gridLayout.addWidget(line_arr[i], i, 1, 1, 1)  # (i,1) 번째 LineEdit

            # combobox
            line_arr[1] = QComboBox(self.gridLayoutWidget)
            line_arr[1].addItems(['1', '2'])
            line_arr[1].setStyleSheet("QComboBox { padding-left : 2px; }")
            self.gridLayout.addWidget(line_arr[1], 1, 1, 1, 1)  # (2,1) 번째 QComboBox

            line_arr[2] = QComboBox(self.gridLayoutWidget)
            line_arr[2].addItems(['학부', '대학원'])
            line_arr[2].setStyleSheet("QComboBox { padding-left : 2px; }")
            self.gridLayout.addWidget(line_arr[2], 2, 1, 1, 1)  # (2,1) 번째 QComboBox

            line_arr[3] = QComboBox(self.gridLayoutWidget)
            line_arr[3].addItems(['', '1', '2', '3', '4'])
            line_arr[3].setStyleSheet("QComboBox { padding-left : 2px; }")
            self.gridLayout.addWidget(line_arr[3], 3, 1, 1, 1)  # (2,1) 번째 QComboBox

            line_arr[4] = QComboBox(self.gridLayoutWidget)
            line_arr[4].addItems(['3', '2', '1'])
            line_arr[4].setStyleSheet("QComboBox { padding-left : 2px; }")
            self.gridLayout.addWidget(line_arr[4], 4, 1, 1, 1)  # (4,1) 번째 QComboBox

        elif configData['info_type'] == "professor":    # 교수 정보
            # lineedit
            for i in [0, 2, 3, 4, 5]:
                line_arr[i] = QLineEdit(self.gridLayoutWidget)
                self.gridLayout.addWidget(line_arr[i], i, 1, 1, 1)  # (i,1) 번째 LineEdit

            # combobox
            line_arr[1] = QComboBox(self.gridLayoutWidget)
            line_arr[1].addItems(['교수', '부교수', '조교수'])
            line_arr[1].setStyleSheet("QComboBox { padding-left : 2px; }")
            self.gridLayout.addWidget(line_arr[1], 1, 1, 1, 1)  # (1,1) 번째 QComboBox

        elif configData['info_type'] == 'classroom':    # 강의실 정보
            for i in range(len(label_arr)):
                line_arr[i] = QLineEdit(self.gridLayoutWidget)
                self.gridLayout.addWidget(line_arr[i], i, 1, 1, 1)  # (i,1) 번째 LineEdit
            
        # List Widget 클릭 메소드 연결
        self.listWidget.itemClicked.connect(self.listClick)

        self.page_data()            # 데이터 불러오기
        self.retranslateUi()        # 텍스트 출력

        
    # List Click Event
    def listClick(self):
        global row
        row = self.listWidget.currentRow()
        item = ""
        if configData['info_type'] == "lesson":  # 강의 정보
            for i in [0, 5]:               # lineedit에 해당
                line_arr[i].setText(str(data[row][i+1]))

            for i in [1, 2, 3, 4]:                     # combobox에 해당
                item = str(data[row][i+1])
                print(item)
                line_arr[i].setCurrentText(item)    # setting current item

        elif configData['info_type'] == "professor":  # 교수 정보
            # lineedit에 해당
            for i in [0, 2, 3, 4, 5]:
                line_arr[i].setText(str(data[row][i+1]))

            # combobox에 해당
            item = str(data[row][2])
            line_arr[1].setCurrentText(item)

        elif configData['info_type'] == 'classroom':  # 강의실 정보
            for i in range(len(line_arr)):
                line_arr[i].setText(str(data[row][i+1]))

    def jsonLoad(self):
        global configData
        with open("info_type.json", "r") as info:
            configData = json.load(info)


    # json에서 가져온 값에 따라 Dialog 모습이 바뀜
    def page_data(self):
        global data, label_col, dialog_type, masterID_code, next_index
        data = []           # 마스터 데이터의 전체 데이터 row
        label_col = []      # 마스터 데이터 column
        dialog_type = ""    # Dialog 타입
        if configData['info_type'] == "lesson":         # 강의 정보
            data = lesson_list
            label_col = lesson_list_col
            dialog_type = "강의"
            masterID_code = global_list[0][1]   # A
            next_index = int(global_list[0][3])
        elif configData['info_type'] == "professor":    # 교수 정보
            data = professor_list
            label_col = professor_list_col
            dialog_type = "교수"
            masterID_code = global_list[1][1]   # B
            next_index = int(global_list[1][3])
        elif configData['info_type'] == "classroom":    # 강의실 정보
            data = classroom_list
            label_col = classroom_list_col
            dialog_type = "강의실"
            masterID_code = global_list[2][1]   # R
            next_index = int(global_list[2][3])

        # 잘 모르시겠으면 print 주석 제거한 후 확인해보세요!
        #print(data)         #excel 파일에 저장된 데이터 값을 pandas dataframe으로 읽어온 후 python의 array로 넘긴 것
        #print(label_col)    #excel 파일의 column명
        
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
        self.close()
        self.__init__()
        self.exec_()

    # 데이터 저장 메소드
    def saveInfo(self):
        # listclick 시 임력폼에 데이터가 담긴 상태의 내용을 다시 저장하지 못하도록하는 코드
        # 입력하고 수정을 눌러야하는데 저장버튼을 잘못 눌렀을 경우를 대비한 코드
        if row != 999:      # 새 창이 열릴 때 row의 default = 999
            global_funtion().message_box_1(QMessageBox.Information, "정보", "이미 입력된 내용입니다", "확인")  # 알림 메세지 출력
            return

        # Step1 우측 입력한 form들의 데이터를 new_data에 담는다
        new_data = []
        if configData['info_type'] == "lesson":  # 강의 정보
            new_data.append(line_arr[0].text())
            new_data.append(line_arr[1].currentText())
            new_data.append(line_arr[2].currentText())
            new_data.append(line_arr[3].currentText())
            new_data.append(line_arr[4].currentText())
            new_data.append(line_arr[5].text())

        elif configData['info_type'] == "professor":  # 교수 정보
            new_data.append(line_arr[0].text())
            new_data.append(line_arr[1].currentText())
            new_data.append(line_arr[2].text())
            new_data.append(line_arr[3].text())
            new_data.append(line_arr[4].text())
            new_data.append(line_arr[5].text())

        elif configData['info_type'] == 'classroom':  # 강의실 정보
            for i in range(len(line_arr)):
                new_data.append(line_arr[i].text())
        #print(new_data)

        # Step2 array를 data 안에 append한다.
        masterID = masterID_code + str(next_index).zfill(3)  #문자 A, B, R 표현을 위해 masterID_code라는 global 변수를 추가함
        new_data.insert(0, masterID)
        data.append(new_data)

        print(data)
        #list.sort(data, key=lambda k: (k[0]))               # data array의 0번째 index를 기준으로 sort
        #df = pd.DataFrame(data, columns=label_col)          # data array, column은 label_col로 하는 dataframe 생성

        # Step3 configData에 따라서 저장해야하는 excel의 위치 바꿔서 저장
        if configData['info_type'] == "lesson":                     # 강의 정보
            list.sort(data, key=lambda k: (k[0]))                   # data array의 0번째 index를 기준으로 sort
            df = pd.DataFrame(data, columns=label_col)              # data array, column은 label_col로 하는 dataframe 생성
            df.to_excel('data/lesson_info.xlsx', index=False)       # dataframe excel 저장
            global_list[0][3] = next_index + 1                      # 다음 ID 수정

        elif configData['info_type'] == "professor":                # 교수 정보
            list.sort(data, key=lambda k: int(k[3]))                # data array의 3번째 index(교수임용순서)를 기준으로 sort
            df = pd.DataFrame(data, columns=label_col)              # data array, column은 label_col로 하는 dataframe 생성
            df.to_excel('data/professor_info.xlsx', index=False)    # dataframe excel 저장
            global_list[1][3] = next_index + 1                      # 다음 ID 수정

        elif configData['info_type'] == "classroom":                # 강의실 정보
            list.sort(data, key=lambda k: (k[0]))                   # data array의 0번째 index를 기준으로 sort
            df = pd.DataFrame(data, columns=label_col)              # data array, column은 label_col로 하는 dataframe 생성
            df.to_excel('data/classroom_info.xlsx', index=False)    # dataframe excel 저장
            global_list[2][3] = next_index + 1                      # 다음 ID 수정
        print(df)

        df = pd.DataFrame(global_list, columns=global_list_col)     # global_list array, column은 global_list_col로 하는 dataframe 생성
        df.to_excel('data/global_master.xlsx', index=False)         # global list df를 excel 저장

        global_funtion().message_box_1(QMessageBox.Information, "정보", "등록되었습니다", "확인")      # 저장완료 메세지 출력
        print("저장완료")   #확인용
        print(df)   #확인용

        self.close()
        self.__init__()
        self.exec_()


    # 데이터 수정 메소드
    def changeInfo(self):
        global_funtion().message_box_2(QMessageBox.Question, "확인", "작성내용을 수정하시겠습니까?", "예", "아니오")
        self.jsonLoad()
        selected_row = row
        if configData['message'] == 'Y':
            for i in range(len(data)):      # data 개수만큼 for문
                if i == selected_row:       # 위젯list에서 선택한 row와 i번째 data가 일치하면
                    changed_data = []
                    if configData['info_type'] == "lesson":  # 강의 정보
                        # 입력폼으로 수정한 내용을 changed_data에 담는다
                        changed_data.append(line_arr[0].text())
                        changed_data.append(line_arr[1].currentText())
                        changed_data.append(line_arr[2].currentText())
                        changed_data.append(line_arr[3].curentText())
                        changed_data.append(line_arr[4].currentText())
                        changed_data.append(line_arr[5].text())

                    elif configData['info_type'] == "professor":  # 교수 정보
                        # 입력폼으로 수정한 내용을 changed_data에 담는다
                        changed_data.append(line_arr[0].text())
                        changed_data.append(line_arr[1].currentText())
                        changed_data.append(line_arr[2].text())
                        changed_data.append(line_arr[3].text())
                        changed_data.append(line_arr[4].text())
                        changed_data.append(line_arr[5].text())

                    elif configData['info_type'] == 'classroom':  # 강의실 정보
                        # 입력폼으로 수정한 내용을 changed_data에 담는다
                        for i in range(len(line_arr)):
                            changed_data.append(line_arr[i].text())

                    changed_data.insert(0, data[selected_row][0])  # masterID 추가 : 입력폼에서 선택했던 row에 해당하는 masterID를 가져옴
                    data[selected_row] = changed_data              # 수정한 내용인 changed_data를 selected_row의 data에 담기

                    #list.sort(data, key=lambda k: (k[0]))          # data array의 0번째 index를 기준으로 sort
                    #df = pd.DataFrame(data, columns=label_col)     # data array, column은 label_col로 하는 dataframe 생성

                    # configData에 따라서 저장해야하는 excel의 위치 바꿔서 저장
                    if configData['info_type'] == "lesson":                   # 강의 정보
                        list.sort(data, key=lambda k: (k[0]))                 # data array의 0번째 index를 기준으로 sort
                        df = pd.DataFrame(data, columns=label_col)            # data array, column은 label_col로 하는 dataframe 생성
                        df.to_excel('data/lesson_info.xlsx', index=False)     # dataframe excel 저장

                    elif configData['info_type'] == "professor":              # 교수 정보
                        list.sort(data, key=lambda k: int(k[3]))              # data array의 3번째 index를 기준으로 sort
                        df = pd.DataFrame(data, columns=label_col)            # data array, column은 label_col로 하는 dataframe 생성
                        df.to_excel('data/professor_info.xlsx', index=False)  # dataframe excel 저장

                    elif configData['info_type'] == "classroom":              # 강의실 정보
                        list.sort(data, key=lambda k: k[0])                   # data array의 0번째 index를 기준으로 sort
                        df = pd.DataFrame(data, columns=label_col)            # data array, column은 label_col로 하는 dataframe 생성
                        df.to_excel('data/classroom_info.xlsx', index=False)  # dataframe excel 저장

                    break    #수정 완료했으므로 break

            print("수정완료")
            global_funtion().message_box_1(QMessageBox.Information, "정보", "등록되었습니다", "확인")  # 수정완료 메세지 출력

        elif configData['message'] == 'N':
            print("no")
            return

        print(df)   #확인용
        self.close()
        self.__init__()
        self.exec_()

    # 데이터 삭제 메소드
    def deleteInfo(self):
        global_funtion().message_box_2(QMessageBox.Question, "확인", "작성내용을 삭제하시겠습니까?", "예", "아니오")
        self.jsonLoad()
        selected_row = row          # 위젯 list에서 선택한 row
        if configData['message'] == 'Y':
            for i in range(len(data)):      # data 개수만큼 for문
                if i == selected_row:       # i번째 data와 위젯 list에서 선택한 row가 일치할 때
                    data.pop(i)             # i번째 data를 삭제한다 -> i번째 이후에 있던 값들이 한칸씩 앞으로 자동으로 이동한다 -> 중간에서 data가 삭제되었다면 masterID 안맞음
                    break       # 삭제 및 masterID 업데이트 완료했으므로 break

            #list.sort(data, key=lambda k: (k[0]))           # data array의 0번째 index를 기준으로 sort
            #df = pd.DataFrame(data, columns=label_col)      # data array, column은 label_col로 하는 dataframe 생성

            # configData에 따라서 저장해야하는 excel의 위치 바꿔서 저장
            if configData['info_type'] == "lesson":                     # 강의 정보
                list.sort(data, key=lambda k: (k[0]))                   # data array의 0번째 index를 기준으로 sort
                df = pd.DataFrame(data, columns=label_col)              # data array, column은 label_col로 하는 dataframe 생성
                df.to_excel('data/lesson_info.xlsx', index=False)       # dataframe excel 저장

            elif configData['info_type'] == "professor":                # 교수 정보
                list.sort(data, key=lambda k: int(k[3]))                # data array의 3번째 index를 기준으로 sort
                df = pd.DataFrame(data, columns=label_col)              # data array, column은 label_col로 하는 dataframe 생성
                df.to_excel('data/professor_info.xlsx', index=False)    # dataframe excel 저장

            elif configData['info_type'] == "classroom":                # 강의실 정보
                list.sort(data, key=lambda k: (k[0]))  # data array의 0번째 index를 기준으로 sort
                df = pd.DataFrame(data, columns=label_col)  # data array, column은 label_col로 하는 dataframe 생성
                df.to_excel('data/classroom_info.xlsx', index=False)    # dataframe excel 저장

            print("삭제완료")
            global_funtion().message_box_1(QMessageBox.Information, "정보", "삭제되었습니다", "확인")  # 삭제완료 메세지 출력

        elif configData['message'] == 'N':
            print("no")
            return

        print(df)      #확인용
        self.close()
        self.__init__()
        self.exec_()