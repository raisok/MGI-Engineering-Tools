# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FOVMetricsFunction.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FovMetricsForm(object):
    def setupUi(self, FovMetricsForm):
        FovMetricsForm.setObjectName("FovMetricsForm")
        FovMetricsForm.resize(640, 480)
        self.widget = QtWidgets.QWidget(FovMetricsForm)
        self.widget.setGeometry(QtCore.QRect(110, 90, 401, 271))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.FovOpenButton = QtWidgets.QPushButton(self.widget)
        self.FovOpenButton.setObjectName("FovOpenButton")
        self.horizontalLayout.addWidget(self.FovOpenButton)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.FOVImportButton = QtWidgets.QPushButton(self.widget)
        self.FOVImportButton.setObjectName("FOVImportButton")
        self.horizontalLayout.addWidget(self.FOVImportButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.FOVAnalysisButton = QtWidgets.QPushButton(self.widget)
        self.FOVAnalysisButton.setObjectName("FOVAnalysisButton")
        self.horizontalLayout_2.addWidget(self.FOVAnalysisButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(FovMetricsForm)
        QtCore.QMetaObject.connectSlotsByName(FovMetricsForm)

    def retranslateUi(self, FovMetricsForm):
        _translate = QtCore.QCoreApplication.translate
        FovMetricsForm.setWindowTitle(_translate("FovMetricsForm", "FOV Metrics"))
        self.FovOpenButton.setText(_translate("FovMetricsForm", "Open"))
        self.FOVImportButton.setText(_translate("FovMetricsForm", "Import"))
        self.label.setText(_translate("FovMetricsForm", "导入成功/失败提示"))
        self.label_2.setText(_translate("FovMetricsForm", "Category:"))
        self.FOVAnalysisButton.setText(_translate("FovMetricsForm", "Analysis"))
