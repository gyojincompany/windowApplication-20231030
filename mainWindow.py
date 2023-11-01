import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon

class MyWin(QWidget): # QWidget 클래스를 상속받는 자식클래스를 선언
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("나의 첫 프로그램") # 윈도우 타이틀 입력
        self.setWindowIcon(QIcon("google.png")) # 아이콘 불러오기
        self.move(300, 300) # 윈도우창이 시작되는 위치 x, y
        self.resize(400, 400) # 윈도우의 크기
        self.btn1 = QPushButton('버튼1번', self) # 버튼1 생성
        self.btn1.move(50, 50) # 버튼1의 위치
        self.btn1.resize(100, 50) # 버튼1의 크기
        self.btn1.clicked.connect(self.btn1_click) # 버튼1이 클릭되었을 때 실행될 함수를 연결
        self.btn2 = QPushButton('버튼2번', self) # 버튼2 생성
        self.btn2.move(150, 50)  # 버튼2의 위치
        self.btn2.resize(100, 50)  # 버튼2의 크기
        self.btn2.clicked.connect(self.btn2_click)  # 버튼2이 클릭되었을 때 실행될 함수를 연결

        self.label1 = QLabel('버튼1과 버튼2를 클릭하세요!!', self)
        self.label1.move(80, 20)


        self.show() # 윈도우창을 스크린에 보여줌

    def btn1_click(self): # 버튼1번이 클릭되면 실행되는 메서드
        print("버튼1번이 클릭됨!!!!")

    def btn2_click(self): # 버튼1번이 클릭되면 실행되는 메서드
        print("버튼2번이 클릭됨!!!!")




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWin()
    sys.exit(app.exec_())