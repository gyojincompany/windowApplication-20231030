import sys

from PyQt5.QtWidgets import QApplication, QWidget
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
        self.show() # 윈도우창을 스크린에 보여줌


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWin()
    sys.exit(app.exec_())