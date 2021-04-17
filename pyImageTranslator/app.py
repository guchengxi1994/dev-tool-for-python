'''
Descripttion: 
version: 
Author: xiaoshuyui
email: guchengxi1994@qq.com
Date: 2021-04-16 19:00:08
LastEditors: xiaoshuyui
LastEditTime: 2021-04-17 11:36:21
'''

import copy
import sys

from PIL import Image, ImageDraw, ImageFont
import numpy as np
sys.path.append("..")
import threading
import time

import cv2
from PyQt5 import QtCore, QtGui, QtWidgets

from pyImageTranslator.PaddleOCR.ppocr.utils.utility import (
    check_and_read_gif, get_image_file_list)

from PyQt5.QtCore import QSize, Qt, pyqtSignal
from PyQt5.QtGui import QIcon, QPainter
from PyQt5.QtWidgets import (QAbstractItemView, QApplication, QComboBox,
                             QDialog, QHBoxLayout, QLabel, QPushButton,
                             QTableWidget, QTableWidgetItem, QVBoxLayout,
                             QWidget)

from pyImageTranslator.paddleOCRWrapper import TextSystem, getFontSize, polygon2rect
from pyImageTranslator.utils.preparation import changeImgPath, fakeArgs
from pyImageTranslator.utils.translator import google

__finishState__ = "start"  # ["start","ocr","end"]


def renderImage(args):
    image_file_list = get_image_file_list(args.image_dir)
    image_file_list = image_file_list[args.process_id::args.total_process_num]
    text_sys = TextSystem(args)
    res = []
    for image_file in image_file_list:
        img, flag = check_and_read_gif(image_file)
        if not flag:
            img = cv2.imread(image_file)
        if img is None:
            print("error in loading image:{}".format(image_file))
            continue
        starttime = time.time()
        dt_boxes, rec_res = text_sys(img)
        elapse = time.time() - starttime
        print("Predict time of %s: %.3fs" % (image_file, elapse))

        for text, score in rec_res:
            print("{}, {:.3f}".format(text, score))

        txts = [rec_res[i][0] for i in range(len(rec_res))]
        res.append([dt_boxes, txts])
    # return res
    global __finishState__
    __finishState__ = 'ocr'
    g = google()
    img = cv2.imread(fakeArgs.image_dir)
    backImg = copy.deepcopy(img)
    print("............{}".format(len(res[0])))
    # print(res[0][1])
    if len(res) == 0:
        __finishState__ = 'end'
    else:
        for i in range(0, len(res[0][1])):
            txt = res[0][1][i]
            print("............" + txt)
            mi, ma = polygon2rect(res[0][0][i])
            try:
                englishTxt = g.translate(txt)[0]
                if len(englishTxt) == 0:
                    englishTxt = "Can't explain"
            except:
                englishTxt = "WENT ERROR"

            print(englishTxt)

            imgHeight = abs(mi[1] - ma[1])
            imgWidth = abs(mi[0] - ma[0])
            im = Image.new("RGB", (imgWidth, imgHeight), (255, 255, 255))
            dr = ImageDraw.Draw(im)
            fontSize = getFontSize(imgWidth / len(englishTxt))
            font = ImageFont.truetype(fakeArgs.vis_font_path,
                                      size=max(int(fontSize * 1.5), 10),
                                      encoding="utf-8")
            print(fontSize)
            dr.text((0, 0), englishTxt, fill=(0, 0, 0), font=font)
            im = np.array(im)
            backImg[mi[1]:ma[1], mi[0]:ma[0]] = im
        cv2.imwrite("t.png", backImg)
        __finishState__ = 'end'


class Table(QWidget):
    def __init__(self, ) -> None:
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Image Translator")
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
        self.btn.setFixedSize(100, 30)

        self.btn_convert = QPushButton('Convert', self)
        self.btn_convert.setFixedSize(100, 30)
        self.btn_convert.clicked.connect(self.convertBtnClick)

        self.cb = QComboBox()
        self.cb.addItem("Smooth")
        self.cb.addItem("None")
        self.cb.setFixedSize(100, 30)

        mainLayout.addWidget(self.table)
        conLayout.addWidget(self.btn)
        conLayout.addWidget(self.cb)
        conLayout.addWidget(self.btn_convert)
        mainLayout.addLayout(conLayout)
        self.setLayout(mainLayout)

    def click_btn(self):
        self.showMinimized()
        self.screenshot = ScreenShotsWin()
        self.screenshot.showFullScreen()
        self.screenshot.exec_()
        # print(type(self.screenshot.cropperedImg))
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

        t = Worker(func=renderImage, args=(fakeArgs, ))
        t.start()

        self._loading()

    def _loading(self):
        global __finishState__
        l = Loading(self)
        l.show()

        self.thread = RunThread()
        self.thread.update_pb.connect(l.update_progressbar)  # 关联
        self.thread.start()

        self.t2 = ShowImage()
        self.t2.start()
        self.t2.state.connect(self._show)

    def _show(self,s:str):
        print(":::::::::::::{}".format(s))
        if s == 'end':
            item = QTableWidgetItem()
            icon = QIcon("t.png")
            item.setIcon(QIcon(icon))
            self.table.setItem(0, 1, item)
        # __finishState__ = "start"


class ShowImage(QtCore.QThread):
    state = pyqtSignal(str)

    def __init__(self, parent=None) -> None:
        super().__init__(parent=parent)
        self.running = True

    def run(self):
        while self.running:
            global __finishState__
            self.state.emit(__finishState__)
            time.sleep(0.2)
            if __finishState__ == 'end':
                self.state.emit(__finishState__)
                self.running = False


class Worker(threading.Thread):
    def __init__(self, func, args=()):
        super(Worker, self).__init__()
        self.func = func
        self.args = args

    def run(self):
        global __finishState__
        __finishState__ = "start"
        self.result = self.func(*self.args)
        __finishState__ = "end"

    def get_result(self):
        try:
            return self.result
        except:
            return None


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

    def update_progressbar(self, p_int):
        self.progressBar.setValue(p_int)
        if p_int == 100:
            self.close()

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        global __finishState__
        if __finishState__ != "end":
            __finishState__ = "canceled"


class RunThread(QtCore.QThread):
    update_pb = QtCore.pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.running = True

    def run(self):
        while self.running:
            global __finishState__
            if __finishState__ == "start":
                self.update_pb.emit(20)
            elif __finishState__ == "ocr":
                self.update_pb.emit(80)
            elif __finishState__ == "canceled":
                print("CANCELED BY USER!")
                self.update_pb.emit(100)
                self.running = False
            else:
                self.update_pb.emit(100)
                self.running = False
            time.sleep(0.2)
        pass


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
