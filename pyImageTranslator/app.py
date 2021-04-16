import sys
import time

from PyQt5 import QtCore
from PyQt5 import QtWidgets
sys.path.append("..")
import threading

from PyQt5.QtCore import QSize, QThread, pyqtSignal, Qt
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import (QAbstractItemView, QApplication, QDialog,
                             QHBoxLayout, QLabel, QPushButton, QTableWidget,
                             QVBoxLayout, QWidget)
from pyImageTranslator.paddleOCRWrapper import process as pprocess
from pyImageTranslator.utils.preparation import fakeArgs, changeImgPath

__finishState__ = False


class Table(QWidget):
    def __init__(self, ) -> None:
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Table Image Viewer")
        # self.resize(1000, 800)
        self.setFixedSize(900, 500)
        # width, height
        conLayout = QHBoxLayout()
        mainLayout = QVBoxLayout()

        self.table = QTableWidget()
        self.table.setColumnCount(2)
        self.table.setRowCount(1)
        self.table.setHorizontalHeaderLabels(['Origin', 'Converted'])
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.table.setIconSize(QSize(400, 400))

        for i in range(2):  # 让列宽和图片相同
            self.table.setColumnWidth(i, 400)
        for i in range(1):  # 让行高和图片相同
            self.table.setRowHeight(i, 400)

        self.btn = QPushButton('Crop', self)
        self.btn.clicked.connect(self.click_btn)
        self.btn.setFixedSize(100, 50)

        self.btn_convert = QPushButton('Convert', self)
        self.btn_convert.setFixedSize(100, 50)
        self.btn_convert.clicked.connect(self.convertBtnClick)

        mainLayout.addWidget(self.table)
        conLayout.addWidget(self.btn)
        conLayout.addWidget(self.btn_convert)
        mainLayout.addLayout(conLayout)
        self.setLayout(mainLayout)

    def click_btn(self):
        self.showMinimized()
        self.screenshot = ScreenShotsWin()
        self.screenshot.showFullScreen()
        self.screenshot.exec_()
        print(type(self.screenshot.cropperedImg))
        item = QLabel()
        item.resize(400, 400)
        item.setPixmap(self.screenshot.cropperedImg)
        self.table.setCellWidget(0, 0, item)
        self.showMaximized()

    def convertBtnClick(self):
        global __finishState__
        path = "./cache/cache.jpg"
        self.screenshot.cropperedImg.save(path)
        changeImgPath(path)

        t = Worker(func=pprocess, args=(fakeArgs, ))
        t.start()

        self._loading()

    def _loading(self):
        global __finishState__
        l = Loading(self)
        l.show()
        while __finishState__ != True:
            time.sleep(1.5)
        else:
            print(True)
            l.close()


class Worker(threading.Thread):
    def __init__(self, func, args=()):
        super(Worker, self).__init__()
        self.func = func
        self.args = args

    def run(self):
        self.func(*self.args)
        global __finishState__
        __finishState__ = True


class Ui_Dialog(object):
    """https://www.jb51.net/article/176361.htm
    """
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(369, 128)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel
                                          | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))


class Loading(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(Loading, self).__init__(parent)
        self.setupUi(self)


class ScreenShotsWin(QDialog):
    # 定义一个信号
    oksignal = pyqtSignal()

    def __init__(self):
        super(ScreenShotsWin, self).__init__()
        self.initUI()
        self.start = (0, 0)  # 开始坐标点
        self.end = (0, 0)  # 结束坐标点
        self.cropperedImg = None

    def initUI(self):
        # self.showFullScreen()
        self.setWindowOpacity(0.4)
        # self.btn_ok = QPushButton('保存', self)

        self.oksignal.connect(lambda: self.screenshots(self.start, self.end))

    def screenshots(self, start, end):
        '''
        截图功能
        :param start:截图开始点
        :param end:截图结束点
        :return:
        '''

        x = min(start[0], end[0])
        y = min(start[1], end[1])
        width = abs(end[0] - start[0])
        height = abs(end[1] - start[1])

        des = QApplication.desktop()
        screen = QApplication.primaryScreen()
        if screen:
            self.setWindowOpacity(0.0)
            pix = screen.grabWindow(des.winId(), x, y, width, height)
            self.cropperedImg = pix

        self.close()

    def paintEvent(self, event):
        '''
        给出截图的辅助线
        :param event:
        :return:
        '''
        x = self.start[0]
        y = self.start[1]
        w = self.end[0] - x
        h = self.end[1] - y

        pp = QPainter(self)
        pp.drawRect(x, y, w, h)

    def mousePressEvent(self, event):

        # 点击左键开始选取截图区域
        if event.button() == Qt.LeftButton:
            self.start = (event.pos().x(), event.pos().y())

    def mouseReleaseEvent(self, event):

        # 鼠标左键释放开始截图操作
        if event.button() == Qt.LeftButton:
            self.end = (event.pos().x(), event.pos().y())

            self.oksignal.emit()
            # 进行重新绘制
            self.update()

    def mouseMoveEvent(self, event):

        # 鼠标左键按下的同时移动鼠标绘制截图辅助线
        if event.buttons() and Qt.LeftButton:
            self.end = (event.pos().x(), event.pos().y())
            # 进行重新绘制
            self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = Table()
    example.show()
    sys.exit(app.exec_())
    # from pyImageTranslator.utils.translator import google
    # g = google()
    # print(g.translate("你是猪"))
