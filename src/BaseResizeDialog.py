# coding =utf-8

import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.Qt import *
from src.view.BaseResizeDialog import  Ui_baseResizeDialog
from functools import partial


class BaseResizeDialog(QDialog, Ui_baseResizeDialog):

    dialogRejected = pyqtSignal()
    dialogAccepted = pyqtSignal(object, object)

    def __init__(self, *args, **kwargs):
        super(BaseResizeDialog, self).__init__(*args,**kwargs)
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
    application = BaseResizeDialog()
    application.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
