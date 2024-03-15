# coding =utf-8

import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.Qt import *
from src.view.BaseCropDialog import  Ui_baseCropDialog
from functools import partial


class BaseCropDialog(QDialog, Ui_baseCropDialog):

    dialogRejected = pyqtSignal()
    dialogAccepted = pyqtSignal(object, object, object, object)

    def __init__(self, *args, **kwargs):
        super(BaseCropDialog, self).__init__(*args,**kwargs)
        self.setupUi(self)
        self._establishConnections()

    def _establishConnections(self):
        self.dialogBtnBox.accepted.connect(self._dialogAccepted)
        self.dialogBtnBox.rejected.connect(self._dialogRejected)

    def _dialogAccepted(self):
        x1 = self.spinBoxX1.value()
        y1 = self.spinBoxY1.value()
        x2 = self.spinBoxX2.value()
        y2 = self.spinBoxY2.value()
        self.dialogAccepted.emit(x1, y1, x2, y2)

    def _dialogRejected(self):
        self.dialogRejected.emit()


def main():
    app = QApplication(sys.argv)
    application = BaseCropDialog()
    application.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
