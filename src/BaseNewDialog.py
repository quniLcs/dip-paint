# coding =utf-8

import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.Qt import *
from src.view.BaseNewDialog import  Ui_baseNewDialog
from functools import partial


class BaseNewDialog(QDialog,Ui_baseNewDialog):
    def __init__(self,*args,**kwargs):
        super(BaseNewDialog, self).__init__(*args,**kwargs)
        self.setupUi(self)


def main():
    app = QApplication(sys.argv)
    application = BaseNewDialog()
    application.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
