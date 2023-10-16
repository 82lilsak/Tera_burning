
import sys

from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import *
from PyQt5 import uic




# UI파일 연결
# 단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType('./tera_ui.ui')[0]


# 화면을 띄우는데 사용되는 Class 선언
class WindowClass(QWidget, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.btn_tera.clicked.connect(self.btn_clicked_slot)

        # values
        self.my_lev = 0
        self.read_text = 0
        self.tera = 0
        self.to_tera = 0
        self.idiot_flag = 0
        self.maxlev_flag = 0

        self.tera2 = 0
        self.list_idiot = []
        # 10, 13 에서 시작.. 199 마무리
        self.list_end200 = []
        # 11, 14 에서 시작.. 200 마무리
        self.need1lev = self.my_lev + 1
        self.list_198 = []
        self.nu = []
        self.need = 0
        # 아랫줄 text lbl 이름
        # lbl_text_info

    def btn_clicked_slot(self):
        btn = self.sender() # 누가 보냈는지 확인 할수 있다.
        # btn signal을 누가 보냈는지 확인 하기 위해 사용.
        # 시그널을 보낸 버튼 오브젝트의 이름이 다음과 같으면 구문 실행.
        if btn.objectName() == 'btn_tera':
        # 시그널을 보낸 버튼 오브젝트의 이름이 btn_tera 이면 이후 구문 실행.
            self.my_lev = int(self.lbl_line.text())
            print(self.my_lev)
            print(type(self.my_lev))
            self.need = (200 - self.my_lev) // 3
            self.lbl_text_write.setText('입력하신 캐릭터의 레벨은 {} 입니다.\n{}번 더 레벨업 해야 합니다.'.format(self.my_lev, self.need))












            for i in range(0, 189, 3):
                p = 198 - i
                self.list_198.append(p)
            self.list_198.sort()

            if self.my_lev in self.list_198:
                if self.my_lev == 198:
                    self.lbl_text_info.setText('캐릭터의 레벨이 198레벨이라 테라버닝 부스터를 사용하면 200 달성이 가능합니다. \n테라버닝 부스터 사용을 추천드리지 않고 199까지 레벨업을 하고 멍청이 퀘스트 클리어시 200이 됩니다.')

                else:
                    self.lbl_text_info.setText('해당 레벨에 테라버닝 사용시 198 레벨에 멍청이 퀘스트를 클리어 하면 200레벨 입니다.')

            for i in range(1, 201, 3):
                self.tera = 200 - i  # 반복 중에 199~ 3씩 뺀 값
                self.list_idiot.append(self.tera)
            self.list_idiot.sort()

            if self.my_lev in self.list_idiot:  # 입력한 레벨이 list_idiot에 있는경우
                if self.my_lev == 199:

                    self.lbl_text_info.setText('199 레벨이라 테라버닝 부스터를 사용하지 않고 멍청이 퀘스트만 클리어 하면 200레벨 입니다.')
                else:

                    self.lbl_text_info.setText('해당 레벨에 테라버닝 사용시 199 레벨에 종료됩니다.')
            #

            for ii in range(0, 200, 3):
                self.tera2 = 200 - ii  # 반복 중에 200~ 3씩 뺀 값
                self.list_end200.append(self.tera2)
            self.list_end200.sort()
            if self.my_lev in self.list_end200:  # 나머지 가 1 이고 내 래밸과 같은 경우
                if self.my_lev == 200:

                    self.lbl_text_info.setText('이미 200레벨 이어서 테라버닝 사용이 불가능 합니다.')
                else:

                    self.lbl_text_info.setText('해당 레벨에 테라버닝 사용시 200 레벨에 마무리 됩니다.')

            self.nu = self.list_198 + self.list_idiot + self.list_end200
            self.nu.sort()






if __name__ == "__main__" :
    # QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    # WindowClass의 인스턴스 생성
    myWindow = WindowClass()

    # 프로그램 화면을 보여주는 코드
    myWindow.show()

    # 프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()

