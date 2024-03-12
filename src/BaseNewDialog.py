# coding =utf-8

import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.Qt import *
from src.view.BaseNewDialog import  Ui_baseNewDialog
from functools import partial


class BaseNewDialog(QDialog,Ui_baseNewDialog):

    dialogRejected = pyqtSignal()
    dialogAccepted = pyqtSignal(object, object)

    def __init__(self,*args,**kwargs):
        super(BaseNewDialog, self).__init__(*args,**kwargs)
        self.setupUi(self)
        self._establishConnections()

    def _establishConnections(self):
        self.dialogBtnBox.accepted.connect(self._dialogAccepted)
        self.dialogBtnBox.rejected.connect(self._dialogRejected)

    def _dialogAccepted(self):
        width = self.spinBoxWidth.value()
        height = self.spinBoxHeight.value()
        self.dialogAccepted.emit(width, height)

    def _dialogRejected(self):
        self.dialogRejected.emit()


def main():
    app = QApplication(sys.argv)
    application = BaseNewDialog()
    application.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
