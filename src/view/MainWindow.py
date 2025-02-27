# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(971, 631)
        MainWindow.setMouseTracking(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/img/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMouseTracking(True)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.toolBox = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBox.sizePolicy().hasHeightForWidth())
        self.toolBox.setSizePolicy(sizePolicy)
        self.toolBox.setObjectName("toolBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.toolBox)
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout_2.setContentsMargins(10, -1, -1, -1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.baseAdjustBtn = QtWidgets.QPushButton(self.toolBox)
        self.baseAdjustBtn.setObjectName("baseAdjustBtn")
        self.gridLayout_2.addWidget(self.baseAdjustBtn, 8, 0, 1, 2)
        self.baseRotateBtn = QtWidgets.QPushButton(self.toolBox)
        self.baseRotateBtn.setObjectName("baseRotateBtn")
        self.gridLayout_2.addWidget(self.baseRotateBtn, 5, 0, 1, 2)
        self.preColorBtn = QtWidgets.QPushButton(self.toolBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.preColorBtn.sizePolicy().hasHeightForWidth())
        self.preColorBtn.setSizePolicy(sizePolicy)
        self.preColorBtn.setStyleSheet("background-color: #000000")
        self.preColorBtn.setText("")
        self.preColorBtn.setIconSize(QtCore.QSize(32, 32))
        self.preColorBtn.setObjectName("preColorBtn")
        self.gridLayout_2.addWidget(self.preColorBtn, 4, 0, 1, 1)
        self.backColorBtn = QtWidgets.QPushButton(self.toolBox)
        self.backColorBtn.setStyleSheet("background-color:#FFFFFF")
        self.backColorBtn.setText("")
        self.backColorBtn.setObjectName("backColorBtn")
        self.gridLayout_2.addWidget(self.backColorBtn, 4, 1, 1, 1)
        self.eraseButton = QtWidgets.QToolButton(self.toolBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.eraseButton.sizePolicy().hasHeightForWidth())
        self.eraseButton.setSizePolicy(sizePolicy)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/img/img/erase.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.eraseButton.setIcon(icon1)
        self.eraseButton.setIconSize(QtCore.QSize(32, 32))
        self.eraseButton.setCheckable(True)
        self.eraseButton.setObjectName("eraseButton")
        self.gridLayout_2.addWidget(self.eraseButton, 2, 1, 1, 1)
        self.baseResizeBtn = QtWidgets.QPushButton(self.toolBox)
        self.baseResizeBtn.setObjectName("baseResizeBtn")
        self.gridLayout_2.addWidget(self.baseResizeBtn, 7, 0, 1, 2)
        self.rectBtn = QtWidgets.QToolButton(self.toolBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rectBtn.sizePolicy().hasHeightForWidth())
        self.rectBtn.setSizePolicy(sizePolicy)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/img/img/rect.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rectBtn.setIcon(icon2)
        self.rectBtn.setIconSize(QtCore.QSize(32, 32))
        self.rectBtn.setCheckable(True)
        self.rectBtn.setObjectName("rectBtn")
        self.gridLayout_2.addWidget(self.rectBtn, 1, 1, 1, 1)
        self.lineBtn = QtWidgets.QToolButton(self.toolBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineBtn.sizePolicy().hasHeightForWidth())
        self.lineBtn.setSizePolicy(sizePolicy)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/img/img/line.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.lineBtn.setIcon(icon3)
        self.lineBtn.setIconSize(QtCore.QSize(32, 32))
        self.lineBtn.setCheckable(True)
        self.lineBtn.setObjectName("lineBtn")
        self.gridLayout_2.addWidget(self.lineBtn, 1, 0, 1, 1)
        self.penSizeBtn = QtWidgets.QComboBox(self.toolBox)
        self.penSizeBtn.setEditable(True)
        self.penSizeBtn.setObjectName("penSizeBtn")
        self.penSizeBtn.addItem("")
        self.penSizeBtn.addItem("")
        self.penSizeBtn.addItem("")
        self.penSizeBtn.addItem("")
        self.penSizeBtn.addItem("")
        self.penSizeBtn.addItem("")
        self.penSizeBtn.addItem("")
        self.gridLayout_2.addWidget(self.penSizeBtn, 3, 0, 1, 1)
        self.sharpenBtn = QtWidgets.QPushButton(self.toolBox)
        self.sharpenBtn.setObjectName("sharpenBtn")
        self.gridLayout_2.addWidget(self.sharpenBtn, 15, 0, 1, 2)
        self.invertBtn = QtWidgets.QPushButton(self.toolBox)
        self.invertBtn.setObjectName("invertBtn")
        self.gridLayout_2.addWidget(self.invertBtn, 11, 0, 1, 2)
        self.cannyBtn = QtWidgets.QPushButton(self.toolBox)
        self.cannyBtn.setObjectName("cannyBtn")
        self.gridLayout_2.addWidget(self.cannyBtn, 13, 0, 1, 2)
        self.grayBtn = QtWidgets.QPushButton(self.toolBox)
        self.grayBtn.setObjectName("grayBtn")
        self.gridLayout_2.addWidget(self.grayBtn, 9, 0, 1, 2)
        self.penBtn = QtWidgets.QToolButton(self.toolBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.penBtn.sizePolicy().hasHeightForWidth())
        self.penBtn.setSizePolicy(sizePolicy)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/img/img/pen.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.penBtn.setIcon(icon4)
        self.penBtn.setIconSize(QtCore.QSize(32, 32))
        self.penBtn.setCheckable(True)
        self.penBtn.setObjectName("penBtn")
        self.gridLayout_2.addWidget(self.penBtn, 0, 0, 1, 1)
        self.bucketBtn = QtWidgets.QToolButton(self.toolBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bucketBtn.sizePolicy().hasHeightForWidth())
        self.bucketBtn.setSizePolicy(sizePolicy)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/img/img/bucket.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bucketBtn.setIcon(icon5)
        self.bucketBtn.setIconSize(QtCore.QSize(32, 32))
        self.bucketBtn.setCheckable(True)
        self.bucketBtn.setObjectName("bucketBtn")
        self.gridLayout_2.addWidget(self.bucketBtn, 0, 1, 1, 1)
        self.embossBtn = QtWidgets.QPushButton(self.toolBox)
        self.embossBtn.setObjectName("embossBtn")
        self.gridLayout_2.addWidget(self.embossBtn, 12, 0, 1, 2)
        self.pxLabel = QtWidgets.QLabel(self.toolBox)
        self.pxLabel.setObjectName("pxLabel")
        self.gridLayout_2.addWidget(self.pxLabel, 3, 1, 1, 1)
        self.binaryBtn = QtWidgets.QPushButton(self.toolBox)
        self.binaryBtn.setObjectName("binaryBtn")
        self.gridLayout_2.addWidget(self.binaryBtn, 10, 0, 1, 2)
        self.blurBtn = QtWidgets.QPushButton(self.toolBox)
        self.blurBtn.setObjectName("blurBtn")
        self.gridLayout_2.addWidget(self.blurBtn, 14, 0, 1, 2)
        self.ellipseBtn = QtWidgets.QToolButton(self.toolBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ellipseBtn.sizePolicy().hasHeightForWidth())
        self.ellipseBtn.setSizePolicy(sizePolicy)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/img/img/ellipse.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ellipseBtn.setIcon(icon6)
        self.ellipseBtn.setIconSize(QtCore.QSize(32, 32))
        self.ellipseBtn.setCheckable(True)
        self.ellipseBtn.setObjectName("ellipseBtn")
        self.gridLayout_2.addWidget(self.ellipseBtn, 2, 0, 1, 1)
        self.baseCropBtn = QtWidgets.QPushButton(self.toolBox)
        self.baseCropBtn.setObjectName("baseCropBtn")
        self.gridLayout_2.addWidget(self.baseCropBtn, 6, 0, 1, 2)
        self.horizontalLayout_3.addWidget(self.toolBox)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_3.addWidget(self.line)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setMouseTracking(True)
        self.widget.setObjectName("widget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.imgRatioBtn = QtWidgets.QComboBox(self.widget)
        self.imgRatioBtn.setObjectName("imgRatioBtn")
        self.imgRatioBtn.addItem("")
        self.imgRatioBtn.addItem("")
        self.imgRatioBtn.addItem("")
        self.imgRatioBtn.addItem("")
        self.imgRatioBtn.addItem("")
        self.imgRatioBtn.addItem("")
        self.imgRatioBtn.addItem("")
        self.gridLayout_3.addWidget(self.imgRatioBtn, 1, 2, 1, 1)
        self.mousePosLabel = QtWidgets.QLabel(self.widget)
        self.mousePosLabel.setObjectName("mousePosLabel")
        self.gridLayout_3.addWidget(self.mousePosLabel, 1, 0, 1, 1)
        self.imgSizeLabel = QtWidgets.QLabel(self.widget)
        self.imgSizeLabel.setObjectName("imgSizeLabel")
        self.gridLayout_3.addWidget(self.imgSizeLabel, 1, 1, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(self.widget)
        self.scrollArea.setMouseTracking(True)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setWidgetResizable(False)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 600, 400))
        self.scrollAreaWidgetContents.setMouseTracking(True)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setContentsMargins(0, 0, -1, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.board = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.board.sizePolicy().hasHeightForWidth())
        self.board.setSizePolicy(sizePolicy)
        self.board.setMouseTracking(True)
        self.board.setLineWidth(0)
        self.board.setText("")
        self.board.setScaledContents(True)
        self.board.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.board.setIndent(0)
        self.board.setObjectName("board")
        self.gridLayout.addWidget(self.board, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_3.addWidget(self.scrollArea, 0, 0, 1, 3)
        self.horizontalLayout_3.addWidget(self.widget)
        self.horizontalLayout_3.setStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 971, 22))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/img/img/new.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew.setIcon(icon7)
        self.actionNew.setObjectName("actionNew")
        self.actionOpenImg = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/img/img/open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpenImg.setIcon(icon8)
        self.actionOpenImg.setObjectName("actionOpenImg")
        self.actionSave = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/img/img/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon9)
        self.actionSave.setObjectName("actionSave")
        self.actionClear = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/img/img/clear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClear.setIcon(icon10)
        self.actionClear.setObjectName("actionClear")
        self.actionClearDraw = QtWidgets.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/img/img/clearImg.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClearDraw.setIcon(icon11)
        self.actionClearDraw.setObjectName("actionClearDraw")
        self.actionClockWise = QtWidgets.QAction(MainWindow)
        self.actionClockWise.setObjectName("actionClockWise")
        self.actionAntiClockWise = QtWidgets.QAction(MainWindow)
        self.actionAntiClockWise.setObjectName("actionAntiClockWise")
        self.actionVerFilp = QtWidgets.QAction(MainWindow)
        self.actionVerFilp.setObjectName("actionVerFilp")
        self.actionHorFilp = QtWidgets.QAction(MainWindow)
        self.actionHorFilp.setObjectName("actionHorFilp")
        self.menu.addAction(self.actionNew)
        self.menu.addAction(self.actionOpenImg)
        self.menu.addAction(self.actionSave)
        self.menu_2.addAction(self.actionClear)
        self.menu_2.addAction(self.actionClearDraw)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        self.imgRatioBtn.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Paint"))
        self.baseAdjustBtn.setText(_translate("MainWindow", "图像调节"))
        self.baseRotateBtn.setText(_translate("MainWindow", "图像旋转"))
        self.eraseButton.setText(_translate("MainWindow", "橡皮擦"))
        self.baseResizeBtn.setText(_translate("MainWindow", "图像缩放"))
        self.rectBtn.setText(_translate("MainWindow", "矩形"))
        self.lineBtn.setText(_translate("MainWindow", "直线"))
        self.penSizeBtn.setItemText(0, _translate("MainWindow", "2"))
        self.penSizeBtn.setItemText(1, _translate("MainWindow", "4"))
        self.penSizeBtn.setItemText(2, _translate("MainWindow", "6"))
        self.penSizeBtn.setItemText(3, _translate("MainWindow", "8"))
        self.penSizeBtn.setItemText(4, _translate("MainWindow", "10"))
        self.penSizeBtn.setItemText(5, _translate("MainWindow", "12"))
        self.penSizeBtn.setItemText(6, _translate("MainWindow", "14"))
        self.sharpenBtn.setText(_translate("MainWindow", "锐化"))
        self.invertBtn.setText(_translate("MainWindow", "反相"))
        self.cannyBtn.setText(_translate("MainWindow", "边缘检测"))
        self.grayBtn.setText(_translate("MainWindow", "灰度化"))
        self.penBtn.setText(_translate("MainWindow", "画笔"))
        self.bucketBtn.setText(_translate("MainWindow", "喷桶"))
        self.embossBtn.setText(_translate("MainWindow", "浮雕"))
        self.pxLabel.setText(_translate("MainWindow", "px"))
        self.binaryBtn.setText(_translate("MainWindow", "二值化"))
        self.blurBtn.setText(_translate("MainWindow", "模糊"))
        self.ellipseBtn.setText(_translate("MainWindow", "椭圆"))
        self.baseCropBtn.setText(_translate("MainWindow", "图像裁剪"))
        self.imgRatioBtn.setItemText(0, _translate("MainWindow", "25%"))
        self.imgRatioBtn.setItemText(1, _translate("MainWindow", "50%"))
        self.imgRatioBtn.setItemText(2, _translate("MainWindow", "75%"))
        self.imgRatioBtn.setItemText(3, _translate("MainWindow", "100%"))
        self.imgRatioBtn.setItemText(4, _translate("MainWindow", "200%"))
        self.imgRatioBtn.setItemText(5, _translate("MainWindow", "300%"))
        self.imgRatioBtn.setItemText(6, _translate("MainWindow", "400%"))
        self.mousePosLabel.setText(_translate("MainWindow", "(0,0)"))
        self.imgSizeLabel.setText(_translate("MainWindow", "(0,0)"))
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.menu_2.setTitle(_translate("MainWindow", "编辑"))
        self.actionNew.setText(_translate("MainWindow", "新建"))
        self.actionOpenImg.setText(_translate("MainWindow", "打开"))
        self.actionSave.setText(_translate("MainWindow", "保存"))
        self.actionClear.setText(_translate("MainWindow", "清空"))
        self.actionClearDraw.setText(_translate("MainWindow", "还原"))
        self.actionClockWise.setText(_translate("MainWindow", "顺时针"))
        self.actionAntiClockWise.setText(_translate("MainWindow", "逆时针"))
        self.actionVerFilp.setText(_translate("MainWindow", "垂直"))
        self.actionHorFilp.setText(_translate("MainWindow", "水平"))
import img
