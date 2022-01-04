from imports import *

# 사용자 정의 함수
class global_funtion():
    # 폰트 설정
    def fontSetting(self, tgt_widget, type, size, widget_index):
        font_type = {"4R":"에스코어 드림 4 Regular", "5M":"에스코어 드림 5 Medium",
                     "6B": "에스코어 드림 6 Bold", "8H": "에스코어 드림 8 Heavy"}
        font = QFont()
        font.setFamily(font_type[type])
        font.setPointSize(size)
        if widget_index == " ":
           tgt_widget.setFont(font)
        else:
           tgt_widget.setFont(int(widget_index), font)

    # 버튼 세팅
    def tool_button_setting(self, qwidget, tool_button_arr):
        qwidget.setToolTip(tool_button_arr[0])
        qwidget.setGeometry(QRect(tool_button_arr[1], tool_button_arr[2], tool_button_arr[3], tool_button_arr[4]))
        icon = QIcon()
        icon.addPixmap(QPixmap(tool_button_arr[5]), QIcon.Normal, QIcon.Off)
        qwidget.setCursor(QCursor(Qt.PointingHandCursor))  # Point Cursor가 손가락 Cursor로 변경
        qwidget.setIcon(icon)
        qwidget.setIconSize(QSize(tool_button_arr[6], tool_button_arr[7]))
        qwidget.setStyleSheet("border : 0")
        qwidget.clicked.connect(tool_button_arr[8])

    # 위젯 안 버튼 세팅
    def tool_button_setting_widget(self, qwidget, inheritWidget, tool_button_arr):
        inheritWidget.addWidget(qwidget)
        qwidget.setToolTip(tool_button_arr[0])
        icon = QIcon()
        icon.addPixmap(QPixmap(tool_button_arr[1]), QIcon.Normal, QIcon.Off)
        qwidget.setCursor(QCursor(Qt.PointingHandCursor))  # Point Cursor가 손가락 Cursor로 변경
        qwidget.setIcon(icon)
        qwidget.setIconSize(QSize(tool_button_arr[2], tool_button_arr[3]))
        qwidget.setStyleSheet("border : 0")
        qwidget.clicked.connect(tool_button_arr[4])

    # 예, 아니오 출력
    def final_decision_button_box(self, qwidget, v, w, x, y, Ok_txt, Cancel_txt, Ok_evt, Canc_evt):
        qwidget.setGeometry(QRect(v, w, x, y))
        qwidget.setOrientation(Qt.Horizontal)
        qwidget.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        qwidget.button(QDialogButtonBox.Ok).setText(Ok_txt)           # Ok -> 등록, 저장
        qwidget.button(QDialogButtonBox.Cancel).setText(Cancel_txt)   # Cancel -> 취소
        qwidget.accepted.connect(Ok_evt)
        qwidget.rejected.connect(Canc_evt)

    # Message Icon Option : QMessageBox.[NoIcon, Question, Information, Warning, Critical]
    # 범용 Message Box(Single Buttons)
    def message_box_1(self, MsgOption, title, MsgText, YesText):
        msgBox1 = QMessageBox()
        msgBox1.setIcon(MsgOption)
        msgBox1.setWindowTitle(title)
        msgBox1.setText(MsgText)
        msgBox1.setStandardButtons(QMessageBox.Yes)
        buttonY = msgBox1.button(QMessageBox.Yes)
        buttonY.setText(YesText)
        msgBox1.exec_()

    # 범용 Message Box(2 Buttons)
    def message_box_2(self, MsgOption, title, MsgText, YesText, NoText):
         with open("info_type.json", "r") as info:
            configData = json.load(info)

        msgBox2 = QMessageBox()
        msgBox2.setIcon(MsgOption)
        msgBox2.setWindowTitle(title)
        msgBox2.setText(MsgText)
        msgBox2.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        buttonY = msgBox2.button(QMessageBox.Yes)
        buttonY.setText(YesText)
        buttonN = msgBox2.button(QMessageBox.No)
        buttonN.setText(NoText)
        msgBox2.exec_()

        if msgBox2.clickedButton() == buttonY:
           configData['message'] = "Y"
        elif msgBox2.clickedButton() == buttonN:
           configData['message'] = "N"

        json.dumps(configData, indent="\t")

        with open('info_type.json', 'w', encoding='utf-8') as make_file:
            json.dump(configData, make_file, indent="\t")

    def buttonBox(self, qwidget, x, y, w, h, slot):
        self.buttonBox = QDialogButtonBox(qwidget)
        self.buttonBox.setGeometry(QRect(x, y, w, h))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        self.buttonBox.accepted.connect(slot)
        self.buttonBox.rejected.connect(self.reject)

