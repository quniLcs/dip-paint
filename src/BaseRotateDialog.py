# coding =utf-8

import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.Qt import *
from src.view.BaseRotateDialog import  Ui_baseRotateDialog
from functools import partial


class BaseRotateDialog(QDialog,Ui_baseRotateDialog):

    rotateClockWiseBtnClicked = pyqtSignal()
    rotateAntiClockWiseBtnClicked = pyqtSignal()
    rotateVerFlipBtnClicked = pyqtSignal()
    rotateHorFlipBtnClicked = pyqtSignal()

    def __init__(self,*args,**kwargs):
        super(BaseRotateDialog, self).__init__(*args,**kwargs)
        self.setupUi(self)
        self._establishConnections()

    def _establishConnections(self):
        self.rotateClockWiseBtn.clicked.connect(self._rotateClockWise)
        self.rotateAntiClockWiseBtn.clicked.connect(self._rotateAntiClockWise)
        self.rotateVerFlipBtn.clicked.connect(self._rotateVerFlip)
        self.rotateHorFlipBtn.clicked.connect(self._rotateHorFlip)

    def _rotateClockWise(self):
        self.rotateClockWiseBtnClicked.emit()

    def _rotateAntiClockWise(self):
        self.rotateAntiClockWiseBtnClicked.emit()

    def _rotateVerFlip(self):
        self.rotateVerFlipBtnClicked.emit()

    def _rotateHorFlip(self):
        self.rotateHorFlipBtnClicked.emit()


def main():
    app = QApplication(sys.argv)
    application = BaseRotateDialog()
    application.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
