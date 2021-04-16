import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Table(QWidget):
    def __init__(self, ) -> None:
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("Table Image Viewer")
        self.resize(850, 450);   # width, height 
        conLayout = QHBoxLayout()

        table = QTableWidget()
        table.setColumnCount(2)
        table.setRowCount(1)
        table.setHorizontalHeaderLabels(['Origin', 'Converted'])
        table.setEditTriggers(QAbstractItemView.NoEditTriggers)

        table.setIconSize(QSize(400, 400));

        for i in range(2):  # 让列宽和图片相同
            table.setColumnWidth(i, 400)
        for i in range(1):  # 让行高和图片相同
            table.setRowHeight(i, 400)

        conLayout.addWidget(table)
        self.setLayout(conLayout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = Table()
    example.show()
    sys.exit(app.exec_())