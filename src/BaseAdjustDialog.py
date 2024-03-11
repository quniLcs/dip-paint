# coding =utf-8

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.Qt import *
from src.view.BaseAdjustDialog import  Ui_baseAdjustDialog
from functools import partial


class BaseAdjustDialog(QDialog,Ui_baseAdjustDialog):

    dialogRejected = pyqtSignal()
    dialogAccepted = pyqtSignal()

    brightSliderReleased = pyqtSignal(object)
    warmSliderReleased = pyqtSignal(object)
    saturabilitySliderReleased = pyqtSignal(object)
    contrastSliderReleased = pyqtSignal(object)

    def __init__(self,*args,**kwargs):
        super(BaseAdjustDialog, self).__init__(*args,**kwargs)
        self.setupUi(self)
        self._initParam()
        self._establishConnections()

    def _initParam(self):
        self.sliders = [self.brightSlider, self.saturabilitySlider, self.contrastSlider, self.warmSlider]
        self.sliderLabels = [self.brightLabel, self.saturabilityLabel, self.contrastLabel, self.warmLabel]

    def _establishConnections(self):
        self.dialogBtnBox.accepted.connect(self._dialogAccepted)
        self.dialogBtnBox.rejected.connect(self._dialogRejected)
        [slider.valueChanged.connect(partial(self._sliderValueChanged,slider)) for slider in self.sliders]
        self.brightSlider.sliderReleased.connect(self._brightSliderReleased)
        self.warmSlider.sliderReleased.connect(self._warmSliderReleased)
        self.saturabilitySlider.sliderReleased.connect(self._saturabilitySliderReleased)
        self.contrastSlider.sliderReleased.connect(self._contrastSliderReleased)

    def _sliderValueChanged(self,slider):
        self.sliderLabels[self.sliders.index(slider)].setNum(slider.value())

    def _brightSliderReleased(self):
        brightValue = self.brightSlider.value()
        self.brightLabel.setNum(brightValue)
        self.brightSliderReleased.emit(brightValue)
    def _contrastSliderReleased(self):
        contrastValue = self.contrastSlider.value()
        self.contrastLabel.setNum(contrastValue)
        self.contrastSliderReleased.emit(contrastValue)

    def _warmSliderReleased(self):
        warmValue = self.warmSlider.value()
        self.warmLabel.setNum(warmValue)
        self.warmSliderReleased.emit(warmValue)

    def _saturabilitySliderReleased(self):
        saturationValue = self.saturabilitySlider.value()
        self.saturabilityLabel.setNum(saturationValue)
        self.saturabilitySliderReleased.emit(saturationValue)

    def _dialogAccepted(self):
        self.dialogAccepted.emit()

    def _dialogRejected(self):
        self.dialogRejected.emit()








